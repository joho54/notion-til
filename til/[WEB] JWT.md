# [WEB] JWT



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



> 학습 순서: 학습 자료 읽고, Q&A 작성, 실습 하면서 트러블슈팅 해보기

# 학습 자료

JWT(Json Web Token)을 간단하게 공부하는 방법을 정리해보겠습니다.

1️⃣ JWT 개념 이해 (10분)

JWT는 클라이언트와 서버 간에 정보를 안전하게 전달하는 토큰 기반 인증 방식입니다.

주요 특징:

•	Header, Payload, Signature 세 부분으로 구성

•	Base64 인코딩된 JSON 데이터

•	HMAC, RSA 등의 서명(Signature) 을 포함해 위변조 방지

🔹 JWT의 기본 구조:

```plain text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvbiBEb2UiLCJpYXQiOjE1MTYyMzkwMjJ9
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

각 부분의 역할:

•	Header: 사용 알고리즘 (예: HS256)

•	Payload: 사용자 정보 (예: id, role, exp 등)

•	Signature: 토큰 무결성 검증을 위한 서명

✅ 공식 사이트에서 디코딩 연습:

👉 https://jwt.io/

2️⃣ JWT 동작 방식 이해 (10분)

JWT는 인증 과정에서 다음과 같이 사용됩니다.

1.	사용자가 로그인하면 서버가 JWT를 생성하여 클라이언트에게 전달

2.	클라이언트는 JWT를 저장 (예: localStorage, sessionStorage)

3.	클라이언트가 서버에 요청할 때 JWT를 포함하여 전송 (보통 Authorization: Bearer <JWT>)

4.	서버는 JWT를 검증하여 사용자 요청을 처리

5.	만료 시간이 지난 경우, 토큰 재발급 필요 (refresh token 활용 가능)

✅ 한눈에 보는 흐름:

```plain text
1. [로그인 요청] → 서버에서 JWT 생성 후 반환
2. [API 요청] → Authorization 헤더에 JWT 포함
3. [서버 검증] → JWT가 유효하면 응답, 아니면 401 에러 반환
```

3️⃣ 실습: JWT 직접 생성 & 검증 (15분)

🛠 JWT 발급하기 (Python 예제)

```python
import jwt # pip install pyjwt
import datetime

SECRET_KEY = "your_secret_key"

# JWT 생성
payload = {
    "user_id": 123,
    "role": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 만료 시간 1시간
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("JWT:", token)
```

🔑 JWT 검증하기

```python
try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("Decoded JWT:", decoded)
except jwt.ExpiredSignatureError:
    print("토큰 만료!")
except jwt.InvalidTokenError:
    print("유효하지 않은 토큰!")
```

4️⃣ JWT 보안 주의사항 (5분)

✅ JWT를 안전하게 사용하려면?

1.	민감한 정보(PW, 카드번호 등) 포함 X → JWT는 노출될 수 있음

2.	HTTPS 사용 → 토큰이 가로채지지 않도록 암호화

3.	Access Token은 짧게, Refresh Token 활용 → 짧은 만료 시간 설정 후 재발급 정책 사용

4.	JWT는 서버에서 블랙리스트 관리 X → 만료 전까지 유효, 로그아웃 관리 어려움

# 실습: JWT를 활용한 웹 페이지 구현

## Phase1. 목표 정리

1. 기본 페이지 템플릿 만들기
1. jwt 생성 로직 작성
1. 간단한 로그인 시스템 카피 라이팅
## Phase2-1. 실습코드 리뷰

```python
from flask import Flask, request, jsonify
import datetime
import jwt

SECRETE_KEY  = "your_secret_key"

app = Flask(__name__)

USERS = {
    "admin": "password123",
    "user": "test1234"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # user identification
    if USERS.get(username) == password:
        payload  = {
            "username": username,
            "role": "admin" if username == "admin" else "user", 
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRETE_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"message": "login failed"}), 401

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

1. JWT
  1. JWT 서명 키로 사용됨
  1. 실제 환경에서는 보안을 위해 .env 파일 등에 저장하는게 좋음
  1. JWT 생성과정
    1. 사용자가 로그인 요청(POST /login)
    1. 서버가 사용자 확인 후 JWT 생성
      1. payload 설정
      1. jwt.encode 해서 토큰 생성
      1. 토큰을 제이슨으로 클라이언트에 반환.
      1. 실패할 경우 메시지 전달
1. USERS : 사용자 정보. 간단한 사용자 정보 저장(admin, user 두 계정만 존재). 실제 시스템에서는 데이터베이스에서 사용자 정보를 조회해야 함.
1. 로그인 API 엔드포인트(/login)
## Phase3. 실습 코드 테스트

```java
curl -X POST http://127.0.0.1:5001/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "password123"}'
```



