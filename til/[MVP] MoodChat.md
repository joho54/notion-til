# [MVP] MoodChat

> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 5회까지 반복하고 해결 안 되면 도움 요청.)

> 실습은 천천히, 하지만 robust하게 하세요. 



> 디자인은 최대한 나중에. 핵심 기능부터 빠르게. 

# 작은 목표: 웹 버전은 디스코드하고 비슷한 UI로 만들고 싶다.

# 작은 목표: 채팅방 만들기



# 작은 목표: 보낸 메시지 옆에 감정 점수 달기

# 작은 목표: 보낸 메시지의 감정점수에 따라 그 채팅 줄의 배경 색을 긍정이면 붉은 색, 부정이면 푸른 색으로 설정







# 이슈: get message error

## Phase1

환경: macOS, Flask, MongoDB, 

로그: 127.0.0.1 - - [21/Feb/2025 21:26:15] "GET /get_messages HTTP/1.1" 404 -

최근 변경 사항: 없음. 잘 작동하던 프로젝트를 오랜만에 실행했더니 발생

## Phase2

확인: get message 중간중간에 로그 찍어서 확인하기. 404면은, 인터널 서버 에러가 아니라 그냥 클라이언트가 서버에 접속을 못하는 문제 아닌가. 

라우팅 경로에 s가 빠져 있었다. get_message로 돼 있었음.

시도: 오타 수정

결과 분석: 성공

