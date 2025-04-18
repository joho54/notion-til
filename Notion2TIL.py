import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
import pyheif
from PIL import Image
import subprocess

def heic_to_png_cli(src_path, dst_path):
    """
    ImageMagick CLI를 사용해 HEIC 이미지를 PNG로 변환합니다.
    ImageMagick이 설치되어 있어야 하며,
    'magick convert <src> <dst>' 명령이 유효해야 합니다.
    """
    cmd = ["magick", "convert", src_path, dst_path]
    subprocess.run(cmd, check=True)

load_dotenv()

def process_notion_image_block(block, image_save_path: str) -> str:
    """
    Notion 'image' 블록:
    1) 이미지 URL을 구해 다운로드
    2) .heic 확장자라면 ImageMagick을 통해 PNG 변환
    3) 변환 후에는 원본 heic 삭제
    4) 마크다운 링크(`![caption](./images/xxx)`)를 리턴
    """

    image_data = block["image"]

    # 1) 이미지 URL 결정
    if image_data["type"] == "external":
        image_url = image_data["external"]["url"]
    else:
        image_url = image_data["file"]["url"]

    # 2) 파일명 추출(쿼리 파라미터 제거, 한글/공백 디코딩)
    parsed_url = urlparse(image_url)
    filename = unquote(os.path.basename(parsed_url.path))  # 예: "myphoto.heic"

    # 저장될 전체 경로
    image_filename = os.path.join(image_save_path, filename)

    # 3) 이미지 다운로드
    response = requests.get(image_url, stream=True)
    if response.status_code != 200:
        print(f"이미지 다운로드 실패: {image_url} [status code: {response.status_code}]")
        return ""  # 원하는 에러 처리 방식을 선택

    with open(image_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    # 4) 확장자가 .heic이면 ImageMagick으로 PNG 변환
    ext = os.path.splitext(filename)[1].lower()  # ".heic", ".jpg", ...
    if ext == ".heic":
        # 최종 PNG 파일명
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(image_save_path, png_filename)
        try:
            # CLI 기반 변환
            heic_to_png_cli(image_filename, png_path)
            # 변환 완료 후 원본 .heic 제거
            os.remove(image_filename)
            # 마크다운에서 사용할 파일명 교체
            filename = png_filename
        except subprocess.CalledProcessError as e:
            print(f"HEIC → PNG 변환 실패: {e}")
            return ""  # 실패 시 원하는 처리

    # 5) 캡션 처리
    caption_texts = image_data.get("caption", [])
    caption = "".join(text["plain_text"] for text in caption_texts) if caption_texts else ""

    # 6) 최종 마크다운 링크 리턴
    md_line = f"![{caption}](./images/{filename})\n\n"
    return md_line



# 이미지 저장 폴더 설정
image_save_path = "./til/images"
os.makedirs(image_save_path, exist_ok=True)

# Notion API 설정
NOTION_API_KEY = os.getenv('NOTION_API_KEY')
PAGE_ID = os.getenv('PAGE_ID') 
EXPORT_DIR = "/Users/johyeonho/notion-til/til" 

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def fetch_page_blocks(page_id, start_cursor=None):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    if start_cursor:
        url += f"&start_cursor={start_cursor}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", []), data.get("next_cursor", None)
    else:
        print(f"Failed to fetch blocks for page {page_id}: {response.text}")
        return [], None


def fetch_all_blocks(page_id):
    blocks = []
    next_cursor = None
    while True:
        current_blocks, next_cursor = fetch_page_blocks(page_id, next_cursor)
        blocks.extend(current_blocks)
        if not next_cursor:
            break
    return blocks


def convert_to_markdown(blocks, indent=0):
    md_text = ""
    indent_str = "  " * indent  # 두 칸씩 들여쓰기

    for block in blocks:
        block_type = block.get("type")
        if block_type == "paragraph":
            for item in block["paragraph"]["rich_text"]:
                if item["type"] == "equation":  # 인라인 수식 탐색
                    latex = item["equation"]["expression"]
                    md_text += f"${latex}$"
                elif item["type"] == "text":  # 일반 텍스트 처리
                    md_text += item["text"]["content"]
            md_text += "\n\n"  # 문장 끝
        elif block_type == "heading_1":
            texts = block["heading_1"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += "# " + content + "\n\n"
        elif block_type == "heading_2":
            texts = block["heading_2"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += "## " + content + "\n\n"
        elif block_type == "heading_3":
            texts = block["heading_3"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += "### " + content + "\n\n"
        elif block_type == "bulleted_list_item":
            texts = block["bulleted_list_item"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"{indent_str}- {content}\n"
            # 하위 리스트가 있으면 재귀 호출로 처리
            if block.get("has_children"):
                child_blocks = fetch_all_blocks(block["id"])
                md_text += convert_to_markdown(child_blocks, indent=indent + 1)
        elif block_type == "numbered_list_item":
            texts = block["numbered_list_item"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"{indent_str}1. {content}\n"
            # 하위 리스트가 있으면 재귀 호출로 처리
            if block.get("has_children"):
                child_blocks = fetch_all_blocks(block["id"])
                md_text += convert_to_markdown(child_blocks, indent=indent + 1)
        elif block_type == "code":
            texts = block["code"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            language = block["code"].get("language", "")
            md_text += f"```{language}\n{content}\n```\n\n"
                    
        elif block_type == "image":
            md_line = process_notion_image_block(block, image_save_path)
            md_text += md_line
            
        elif block_type == "quote":
            texts = block["quote"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"> {content}\n\n"
        elif block_type == "callout":
            texts = block["callout"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"> **Note:** {content}\n\n"
        # 기타 블록 유형 추가 가능
        elif block_type == "equation":  # 독립적인 수식 블록
            latex = block["equation"]["expression"]
            md_text += f"$$\n{latex}\n$$\n\n"
    return md_text


def save_markdown(title, content):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    # 파일명에 특수문자가 있으면 문제가 생길 수 있으므로 간단하게 처리
    filename = os.path.join(EXPORT_DIR, f"{title}.md")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Saved: {filename}")


def fetch_page_title(page_id):
    """
    페이지 조회 API를 통해 페이지 제목을 가져옵니다.
    페이지가 데이터베이스가 아닌 일반 페이지인 경우,
    'child_page' 객체 내 title 필드 또는 properties에서 title을 추출할 수 있습니다.
    """
    url = f"https://api.notion.com/v1/pages/{page_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        # 일반 페이지는 properties에 title이 없는 경우도 있으므로, child_page 속성을 확인
        if "child_page" in data:
            return data["child_page"].get("title", page_id)
        # properties에서 title 추출 (데이터베이스 페이지의 경우)
        for prop in data.get("properties", {}).values():
            if prop.get("type") == "title":
                title_arr = prop.get("title", [])
                if title_arr:
                    return "".join([t.get("plain_text", "") for t in title_arr])
    else:
        print(f"Failed to fetch title for page {page_id}: {response.text}")
    return page_id


def get_nested_page_ids(page_id):
    """
    주어진 페이지 내의 블록들 중 'child_page' 타입인 블록을 찾아
    재귀적으로 자식 페이지들의 ID를 수집합니다.
    """
    nested_ids = []
    blocks = fetch_all_blocks(page_id)
    for block in blocks:
        if block.get("type") == "child_page":
            child_page_id = block["id"]
            nested_ids.append(child_page_id)
            # 재귀 호출: 자식 페이지 내의 추가 child_page가 있을 경우 처리
            nested_ids.extend(get_nested_page_ids(child_page_id))
    return nested_ids


def main():
    root_page_id = PAGE_ID
    # 최상위 페이지와 그 안의 모든 자식 페이지들의 ID를 수집
    all_page_ids = [root_page_id] + get_nested_page_ids(root_page_id)

    for pid in all_page_ids:
        title = fetch_page_title(pid)
        blocks = fetch_all_blocks(pid)
        if not blocks:
            print(f"No blocks found or error occurred for page: {pid}")
            continue
        # 제목을 md 파일 상단에 포함 (헤더 형태)
        markdown_content = f"# {title}\n\n" + convert_to_markdown(blocks)
        save_markdown(title, markdown_content)


if __name__ == "__main__":
    main()
