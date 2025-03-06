import os
import requests

# Notion API 설정
NOTION_API_KEY = "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"  # Notion integration에서 발급 받은 API 키
PAGE_ID = "1a04047c5d6d808b8017f3c55c3a6ad7"  # 위에서 추출한 페이지 ID (하이픈 없이)
EXPORT_DIR = "/Users/johyeonho/notion-til/til"  # Markdown 파일을 저장할 디렉토리 경로

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


# Notion 페이지의 블록을 가져오는 함수
def fetch_page_blocks(page_id, start_cursor=None):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    if start_cursor:
        url += f"&start_cursor={start_cursor}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data.get("results", []), data.get("next_cursor", None)
    else:
        print("Failed to fetch blocks:", response.text)
        return [], None


# 전체 블록을 가져오는 함수 (페이지네이션 처리)
def fetch_all_blocks(page_id):
    blocks = []
    next_cursor = None
    while True:
        current_blocks, next_cursor = fetch_page_blocks(page_id, next_cursor)
        blocks.extend(current_blocks)
        if not next_cursor:
            break
    return blocks


# 블록을 Markdown으로 변환하는 함수
def convert_to_markdown(blocks):
    md_text = ""
    for block in blocks:
        block_type = block.get("type")
        if block_type == "paragraph":
            texts = block["paragraph"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += content + "\n\n"
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
            md_text += "- " + content + "\n"
        elif block_type == "numbered_list_item":
            texts = block["numbered_list_item"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += "1. " + content + "\n"
        elif block_type == "code":
            texts = block["code"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            language = block["code"].get("language", "")
            md_text += f"```{language}\n{content}\n```\n\n"
        elif block_type == "image":
            image_data = block["image"]
            # image 파일의 URL은 type에 따라 다를 수 있음 (external/internal)
            if image_data["type"] == "external":
                image_url = image_data["external"]["url"]
            else:
                image_url = image_data["file"]["url"]
            # 캡션은 리스트 형태로 제공됨
            caption_texts = image_data.get("caption", [])
            caption = (
                "".join([text["plain_text"] for text in caption_texts])
                if caption_texts
                else ""
            )
            md_text += f"![{caption}]({image_url})\n\n"
        elif block_type == "quote":
            texts = block["quote"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"> {content}\n\n"
        elif block_type == "callout":
            texts = block["callout"].get("rich_text", [])
            content = "".join([text["plain_text"] for text in texts])
            md_text += f"> **Note:** {content}\n\n"
        elif block_type == "equation":  # 독립적인 수식 블록
            latex = block["equation"]["expression"]
            md_text += f"$$\n{latex}\n$$\n\n"

        elif block_type == "paragraph":  # 문장 내 인라인 수식이 있는 경우
            for item in block["paragraph"]["rich_text"]:
                if item["type"] == "equation":  # 인라인 수식 탐색
                    latex = item["equation"]["expression"]
                    md_text += f"${latex}$"
                elif item["type"] == "text":  # 일반 텍스트 처리
                    md_text += item["text"]["content"]
            md_text += "\n\n"  # 문장 끝
    return md_text


# Markdown 파일로 저장하는 함수
def save_markdown(title, content):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    filename = os.path.join(EXPORT_DIR, f"{title}.md")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Saved: {filename}")


# 단일 페이지 변환 실행 함수
def main():
    # 페이지 제목(여기서는 단순히 PAGE_ID를 제목으로 사용하지만,
    # Notion API의 페이지 조회로 제목을 가져올 수도 있음)
    title = PAGE_ID
    blocks = fetch_all_blocks(PAGE_ID)
    if not blocks:
        print("No blocks found or error occurred.")
        return
    markdown_content = convert_to_markdown(blocks)
    save_markdown(title, markdown_content)


if __name__ == "__main__":
    main()
