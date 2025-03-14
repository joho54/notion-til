# [MVP] 워드 임베딩 기반 메모앱



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> MVP, 이슈 이 두가지만 있으면 프로젝트는 뚝딱이다.



# Quick Demo

```python
from sentence_transformers import SentenceTransformer

# SBERT 모델 로드
model = SentenceTransformer("all-MiniLM-L6-v2")

# 예제 메모
memos = [
    "Python is a great programming language.",
    "Machine learning is powerful.",
    "Deep learning is a subset of machine learning.",
    "I love coding in Python.",
    "So if i buy some snacks here, it could be a disaster for both of us.",
    "The people without the knowledge of hebrew made christianity worse",
    "The bible is written of hebrew, not the language you use.",
]

# 벡터 변환
vectors = model.encode(memos)
print(vectors.shape)  # (4, 384)  -> 4개 문서, 384차원 벡터

#### search test

import faiss
import numpy as np

# 벡터 차원 설정
dim = vectors.shape[1]

# FAISS 인덱스 생성
index = faiss.IndexFlatL2(dim)  # L2 거리 기반 검색
index.add(np.array(vectors))  # 벡터 추가

# 검색 예제 (첫 번째 문서와 가장 가까운 메모 찾기)
D, I = index.search(np.array([vectors[0]]), k=2)  # k=2 (자기 자신 포함)
print("closest document with the first document:", I)  # 가장 가까운 문서 인덱스 출력

#### dimension reduction
import umap

# UMAP으로 2D로 축소
umap_model = umap.UMAP(n_components=2, random_state=42)
vectors_2d = umap_model.fit_transform(vectors)

print(vectors_2d)  # 2차원 좌표값 출력

### visualization
import networkx as nx
import matplotlib.pyplot as plt

# 그래프 생성
G = nx.Graph()

# 노드 추가
for i, (x, y) in enumerate(vectors_2d):
    G.add_node(i, pos=(x, y), label=memos[i])

# 거리 기반으로 간선 추가
threshold = 1.5  # 거리 임계값 설정
for i in range(len(vectors_2d)):
    for j in range(i + 1, len(vectors_2d)):
        dist = np.linalg.norm(vectors_2d[i] - vectors_2d[j])
        if dist < threshold:
            G.add_edge(i, j, weight=dist)

# 노드 위치 설정
pos = nx.get_node_attributes(G, "pos")

# 그래프 시각화
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    pos,
    with_labels=True,
    labels=nx.get_node_attributes(G, "label"),
    node_size=3000,
    font_size=10,
    edge_color="gray",
)
plt.show()

```

# Q. SBERT가 토크나이징과 임베딩을 같이 해 주는 건가?

A. 

네, SBERT (Sentence-BERT) 는 토크나이징(tokenization)과 임베딩(embedding) 을 동시에 수행합니다. 즉, 텍스트를 입력하면 자동으로 토큰화한 후 임베딩 벡터를 생성합니다.

✅ SBERT의 내부 처리 과정

SBERT 모델을 사용할 때, model.encode(text) 함수가 내부적으로 하는 작업은 다음과 같습니다:

1.	토크나이징 (Tokenization)

•	입력된 문장을 WordPiece 토크나이저를 사용해 토큰으로 변환.

•	예시:

```plain text
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

text = "I love natural language processing."
tokens = model.tokenizer.tokenize(text)
print(tokens)
```

출력 예시:

```plain text
['i', 'love', 'natural', 'language', 'processing', '.']
```

2.	입력 인덱스 변환 (Token ID 변환)

•	토큰을 사전에서 ID (정수형 인덱스) 로 변환.

```plain text
input_ids = model.tokenizer.encode(text)
print(input_ids)
```

출력 예시:

```plain text
[101, 1045, 2293, 3019, 2653, 6845, 1012, 102]
```

(여기서 101은 [CLS], 102는 [SEP] 토큰)

3.	SBERT 모델을 통해 임베딩 벡터 생성

•	Transformer 기반 모델(BERT, MiniLM 등)을 사용해 토큰을 벡터로 변환.

•	[CLS] 토큰의 벡터를 사용하거나, 전체 토큰의 평균 풀링을 적용하여 문장 벡터 생성.

```plain text
embedding = model.encode(text)
print(embedding.shape)  # (384,)  -> 384차원 벡터 출력
```

🚀 결론

✅ SBERT는 토크나이징과 임베딩을 자동으로 수행

✅ 사용자가 따로 토큰화할 필요 없이 model.encode(text) 호출만 하면 됨

✅ 내부적으로 WordPiece 토크나이저를 사용하여 BERT 스타일의 입력을 만듦

✅ 최종적으로 384차원 또는 768차원 벡터를 반환 (모델 종류에 따라 다름)

혹시 더 궁금한 점 있으면 알려주세요! 😊



# Q. D3.js가 뭐지?

# MVP 후보

1. 한 메모 문서를 다차원 벡터로 임베딩해서 데이터베이스에 저장하는 앱 프로젝트 구축
1. 임베딩된 다차원 벡터를 기준으로 화면 상에 x, y 값을 가지는 노드로 메모를 표현
1. 각 메모 문서의 벡터 값을 기준으로 서로간의 거리를 결정하여 노드를 배치. 이때 모든 메모 노드 중 하나를 기준점으로 삼는다.
1. 이제 빠르게 UI 입혀 보고 후속 작업으로 넘어갈 것
  1. 메모 추가 버튼을 생성하자.
  1. 메모 좌표 로직에 임베딩기반 좌표 업데이트 로직을 추가 → vector2coord.py 모듈을 만들어서 해결.
  1. 이 모듈의 사용 방법. 메모 리스트를 입력 → 각 메모의 좌표 리스트를 리턴
  1. argument: [{”text”: “memo contents”, “x”: 1.2, “y”: -0.5}, {”text”: “memo contents”, “x”: 1.2, “y”: -0.5}….]
  1. return: fix initial values using logis
1. DBMS 연동 아니아니


# 이슈: faiss 라이브러리 설치 안 됨

## Phase1.

환경: macOS, m1, python 3.10.7, 

로그

 pip install faiss
ERROR: Could not find a version that satisfies the requirement faiss (from versions: none)
ERROR: No matching distribution found for faiss

최근변경사항: 개발 환경 구축 중. 

## Phase2-1: 해결(GPT의 잘못된 라이브러리 명 추천이 문제였음)

확인: pip install faiss는 PyPI에서 공식 지원 안 되고 대신 faiss-cpu 혹은 faiss-gpu를 써야 함.

시도: pip install faiss-cpu

결과 분석: 성공

# 이슈: UMAP 작동 안 함

## Phase1.

환경: macOS, m1, python 3.10.7

로그

Exception has occurred: AttributeError

module 'umap' has no attribute 'UMAP'

File "/Users/johyeonho/memo-embedding/main.py", line 38, in <module>
    umap_model = umap.UMAP(n_components=2, random_state=42)
AttributeError: module 'umap' has no attribute 'UMAP'

최근 변겅 사항: umap_model = umap.UMAP(n_components=2, random_state=42) 실행

## Phase2-1

확인: umap이 아니라 umap-learn이 올바른 라이브러리 이름.

시도: umap 삭제 후 pip install umap-learn 설치

결과 분석: 성공


# 이슈: vscode 코파일럿 활성화 안 됨

## Phase1.

환경: macOS, m1

로그

아무 로그 없음

최근변경사항: sign in to github copilot 버튼 클릭 후 무반응. 

## Phase2-1

확인: VS Code에서 GitHub 인증 확인 및 재로그인

시도:	GitHub 로그아웃 후 다시 로그인

결과 분석: 아무 변화 없음.

## Phase2-2

확인: 확장 삭제 후 다시 시도

시도: 그대로

결과분석: 아무 변화 없음

## Phase2-3

확인: VS Code 설정에서 GitHub Enterprise (GHE) 연결 확인

시도: Preferences: Open Settings (JSON)에 아래 설정이 있는지 확인

"github.copilot.advancedSettings": {
"serverUrl": "https://github.com"
}

(user) settings.json 에 해당 설정 추가.

결과분석: 아무 변화 없음

## Phase2-4

확인: curl https://api.github.com을 통해 서버와 통신 가능한지 확인

시도: 그대로 실시

결과 분석: json 형식의 출력이 정상적으로 돌아옴. 아무 변화 없음.

## Phase2-5

확인: 인증 캐시 삭제

시도: rm -rf ~/.config/github-copilot

결과 분석: 아무 변화 없음

## Phase3. 재설치, 해결



# 이슈: umap_model.fit_transform(vectors) 실패

## Phase1. 

환경: macOS, m1, python 3.10.7

로그

Exception has occurred: ValueError

zero-size array to reduction operation maximum which has no identity

File "/Users/johyeonho/memo-embedding/vector2coord.py", line 21, in convert
    vectors_2d = umap_model.fit_transform(vectors)
  File "/Users/johyeonho/memo-embedding/vector2coord.py", line 30, in <module>
    memos = Vector2Coord.convert([
ValueError: zero-size array to reduction operation maximum which has no identity
변경사항

문제가 되는 부분

```python

class Vector2Coord:
    @staticmethod
    def convert(memos):
        if not memos:
            return memos
        
        # Load SBERT model
        model = SentenceTransformer("all-MiniLM-L6-v2")
        
        # Extract texts from memos
        texts = [memo["text"] for memo in memos]
        
        # Convert texts to vectors
        vectors = model.encode(texts)
        
        # Reduce dimensions to 2D using UMAP
        umap_model = umap.UMAP(n_components=2, random_state=42)
        vectors_2d = umap_model.fit_transform(vectors)
        
        # Update memos with new coordinates
        for i, memo in enumerate(memos):
            memo["x"], memo["y"] = vectors_2d[i].tolist()
        
        return memos
```

아래의 경우 에러 없음(요소가 하나)

```markdown
    memos = Vector2Coord.convert([
        {"text": "Finish AI project", "x": 0.3, "y": -1.2}
    ])
```

아래와 같을 경우 에러 발생

```javascript
    memos = Vector2Coord.convert([
        {"text": "Meeting at 3PM", "x": 1.2, "y": -0.5},
        {"text": "Finish AI project", "x": 0.3, "y": -1.2}
    ])
```

## Phase2-1: 해결

확인: 코드 작동방식 확인

vectors = model.encode(texts) 동작의 결과가 무엇인가?

texts 리스트의 모든 문장을 한 번에 벡터로 변환

출력: vectors.shape = (N, 384) (N개의 문장, 384차원 벡터) 

즉 주어지는 texts가 몇개든 상관이 없다.

```python
print(vectors.shape)  # (2, 384)
# 첫 번째 문장의 벡터 일부 출력
print(vectors[0][:5])  # [ 0.0213 -0.1154  0.3072 -0.0847  0.2913]


```

vectors_2d = umap_model.fit_transform(vectors)의 동작 결과는 무엇인가?

그냥 별거 없음

→ 어떨결에 해결

시도: 그냥 초기 입력 데이터를 많이 줬음. 한 7개. 그랬더니 작동함. 임베딩이 기본적으로 전체 문서의 집합이 필요한 작업이라 그런듯. AI 잘못은 아님.

결과분석: 성공

→ 그렇다면 초기 주어지는 문서를 어떻게 초기화해야 균형있게 문서를 임베딩할 수 있을까?



