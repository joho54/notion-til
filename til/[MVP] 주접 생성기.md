# [MVP] 주접 생성기



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

# Links

진자 실습용 레포: 

# MVP Goals: 클라이언트 작업

1. 목표: index.html 에서 MVP-프로필 사진과 주접 생성 버튼
1. 목표: joojeop.html에서 mvp-주접 프로필 하나와 주접 키워드.  
1. 목표: 타이틀 작업
1. 목표: 그리드 작업-소네트랑 진행
1. 목표: jinja에 자바 스크립트 연동하고 jquery 사용하기
  1. 일단 따로 프로젝트 파서 간단한 예재로 해보는게 나을듯. → 완료
1. 목표: 버튼을 누르면 /joojeop으로 GET 리퀘스트 보내기
1. 다음 MVP는 뭐지? 일단 GPT 랑 병합해야지. 
1. 정렬 기능 구현
1. 내주접, 모든주접 필터링
1. likes
1. 링크 누르면 홈으로 라우팅하는 기능
# 추가 아이디어

1. 싫어요 기능: 아재 개그 컨셉으로 주접을 생성한다면, 주접은 야유하는 재미도 있는 거니까
1. 관리자페이지. 
1. 직접 입력 기능
# 이슈: 할당된 버튼을 눌러도 /joojeop으로 GET 리퀘스트 보내지지 않음

## Phase1.

### 환경: macOS, arm, flak, jinja2, jquery, 

### 로그: 없음

### 최근 변경사항

```javascript
$('#myButton').on('click', function () {
        $.ajax({
            type: "GET",
            url: "/joojeop",
            success: function (response) {
                alert("success");
            }
        });
    });
```

alert는 정상적으로 뜸. 

## Phase2-1: 성공

### 확인

개발자 도구(NETWORK 탭)에서 요청이 실제로 발생하는지 확인

아래 내용이 정상적으로 network inspector에 뜸.

http://127.0.0.1:5000/joojeop

응답까지 제대로 다 전달되는 것을 확인. 그렇다면 페이지를 새로고치고 띄워주는 작업이 안 되고 있는 건가?

### 시도

```javascript
$('#myButton').on('click', function () {
        $.ajax({
            type: "GET",
            url: "/joojeop",
            success: function (response) {
                window.location.href = "/joojeop";  
            }
        });
    });
```

### 결과분석: 잘 이동 됨.

# MVPs

1. 드랍다운 메뉴 구현하기(main.js, index.html)
1. 주접 컬랙션을 가져와서 클라이언트에 뿌려주기.  
1. static 코치 이미지 저장
1. static 이미지를 서버에서 넘겨주는게 낫지 않을까? 
1. 코치별 버튼 생성 할 때 id도 넘겨주기→ 이벤트 리스너를 추가해야 하는데, 어떻게 추가해야 잘 추가한 거지? 그냥 모든 코치 버튼에 아이디를 추가해서 쿼리스트링 링크를 추가해서 처리.
# 목표: 쿼리 스트링으로 필터링 및 정렬 정보 넘기기

## Phase1. 공부

### JavaScript로 동적으로 쿼리 스트링 만들기

버튼에 클릭 이벤트를 직접 자바스크립트로 달아서, 쿼리 스트링을 구성해 이동하거나 요청을 보낼 수도 있어요.

```c

<button id="myButton" data-id="123">Click me</button>
<script>
document.addEventListener('DOMContentLoaded', function() {
var btn = document.getElementById("myButton");
btn.addEventListener('click', function() {
var buttonId = this.getAttribute("data-id");
// 쿼리 스트링 붙여서 이동
window.location.href = "/some_route?button_id=" + buttonId;
});
});
</script>
```

### 템플릿에서 바로 처리

가장 단순 예시는 템플릿에서 URL을 직접 만들어 <button onclick="location.href='...'"> 형태로 사용하는 거예요.

```c
<button onclick="location.href='{{ url_for('some_route') }}?button_id={{ item.id }}'">
버튼 클릭!
</button>
```

이렇게 하면 클릭 시 GET /some_route?button_id=123가 날아가고, Flask에서 request.args.get('button_id')로 123을 처리할 수 있습니다. 

## Phase2-1. 구현

```html
<button class="bg-white border border-blue-300 text-blue-400 hover:bg-blue-50 p-2 block mx-auto"
                    id="btn-{{coach.name}}" onclick="location.href='joojeop?coach_name={{ coach.name }}'">주접떨기</button>
```

# 목표: 기존 url에 쿼리 스트링을 추가하여 정렬 기능 구현 

## Phase1. 공부

1) 기존 쿼리스트링을 유지하면서 order=newest만 추가하고 싶다면?

(A) 서버에서 Jinja2로 “병합”해서 링크 생성하기

1.	현재 쿼리 파라미터를 request.args로 가져옵니다.

2.	이를 사전 형태로 변환 후, order 값을 덮어씌우거나 새로 추가합니다.

3.	url_for로 해당 파라미터들을 다시 붙여서 링크를 생성합니다.

```c
{% set current_args = request.args.to_dict() %}
{% set current_args['order'] = 'newest' %}
<a href="{{ url_for('index', **current_args) }}" class="...">
최신순
</a>
```



•	이렇게 하면, 예를 들어 현재 URL이 /items?page=2&category=apple라면,
•	current_args = {'page': '2', 'category': 'apple'}
•	current_args['order'] = 'newest'
•	결과 링크: /items?page=2&category=apple&order=newest
•	기존 파라미터들은 그대로 유지되고, order=newest만 추가(또는 덮어쓰기)합니다.


### 궁금한 점: jinja가 서버 사이드 렌더링이라서 리퀘스트 객체를 템플릿에 가져올 수 있는 건가?

Flask(또는 Django 등)에서 사용하는 Jinja2는 서버 사이드 렌더링 방식이므로, 서버에서 실행되는 파이썬 코드와 템플릿이 같은 프로세스 내에 있어요. 이 때문에 Flask가 템플릿을 렌더링할 때 request(요청 객체)나 session(세션 객체) 같은 전역 컨텍스트(플라스크 내부적으로 context_processor 같은 기능)에 접근할 수 있게 해 줍니다.

즉, “jinja 템플릿 내부에서 request 객체를 직접 가져와 사용하는” 것이 가능한 이유는,

•	Jinja 템플릿이 서버 쪽에서 렌더링될 때,

•	Flask가 템플릿에 필요한 전역 객체(request, session, g, 등)를 주입해 주기 때문입니다.

1) Flask에서 템플릿 안에서 request 사용 예시

```plain text
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head><title>Example</title></head>
<body>

<p>현재 URL의 쿼리: {{ request.args }}</p>
<p>특정 파라미터: {{ request.args.get('order') }}</p>

</body>
</html>
```

Flask 코드:

```plain text
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

•	이렇게 하면, 브라우저에서 http://127.0.0.1:5000/?order=newest로 접속 시 템플릿에서 request.args.get('order')가 newest로 표시됩니다.

2) “서버 사이드”라 가능한 이유

•	서버 사이드 렌더링: 사용자가 URL을 요청하면, 서버에서 템플릿을 실행(변수 치환, 로직 수행)한 뒤 HTML을 완성해서 브라우저로 보냅니다.

•	이 과정에서 Flask는 request 객체(HTTP 요청 정보)를 템플릿 렌더링에 포함시킬 수 있어요.

•	따라서 템플릿 안에서 request.args.get(...) 같은 함수를 호출해도 이미 서버에 있는 request를 참조하므로 정상 동작합니다.

3) 클라이언트 사이드 JS(React, Vue 등)와 비교

•	React, Vue 같은 클라이언트 사이드 SPA 프레임워크에서 “템플릿”을 작성할 땐, **브라우저(클라이언트)**가 그 코드를 실행합니다.

•	그 환경에선 브라우저에서 바로 request 객체(Flask의 request)는 당연히 없고, AJAX를 통해 서버에 요청해야만 서버 정보를 받을 수 있어요.

•	즉, 서버 사이드에서는 Flask의 request를 템플릿에 곧바로 넘길 수 있지만, 클라이언트 사이드에서는 직접 API 호출(ajax, fetch) 등을 해야 합니다.

4) “템플릿에 request가 꼭 필요한가?”

•	많은 경우, 뷰 함수에서 직접 파라미터를 추출하고, 필요한 데이터를 “결과값”으로 템플릿에 넘기는 게 더 명확합니다.

•	템플릿에서 “이 로직”을 처리해야 하나, “컨트롤러(뷰 함수)”에서 처리해야 하나는 개발자가 판단하면 됩니다.

•	예) “request.args.get('page')를 int로 변환하고, 범위를 벗어나면 1로 세팅한다” 같은 로직은 보통 뷰 함수 안에서 하고, 템플릿에는 최종 값만 넘겨 주는 식으로 구현.

요약

•	Flask + Jinja2가 “서버 사이드 렌더링”을 수행하기 때문에, Flask가 미리 만들어 둔 request 객체를 템플릿에서 직접 참조 가능.

•	이는 브라우저 쪽이 아니라, 서버 쪽에서 HTML을 완성하는 구조라 가능한 것이며, Flask가 템플릿 렌더링 컨텍스트에 기본적으로 request를 포함시켜 주기 때문입니다.

### 내 생각

그럼, 그냥 기본값을 날짜순 정렬로 넘겨줘서 쿼리 스트링에서 항상 정렬 기준을 유지하고, 드랍다운 메뉴를 클릭했을 때 이 기준을 변경해주는 방향이 맞을 거 같다.

```python
@app.route('/', methods=['GET'])
def home():
    coaches = [
        {"name":"김정민", "path":"images/김정민.png"},
        {"name":"김현수", "path":"images/김현수.png"},
        {"name":"방효식", "path":"images/방효식.png"},
        {"name":"백승현", "path":"images/백승현.png"},
        {"name":"안예인", "path":"images/안예인.png"},
        {"name":"유윤선", "path":"images/유윤선.png"},
        {"name":"이동석", "path":"images/이동석.png"},
        {"name":"이승민", "path":"images/이승민.png"},
    ]
    return render_template("index.html", coaches=coaches, joojeops=joojeops)
```

→ 여기로 라우팅 됐을 때 url에 기본 정렬 쿼리 스트링(?order=newest)를 추가하여 이걸 별도로 정렬 함수에 전달해주고, 그 함수가 올바르게 정렬한 데이터를 리턴해주면 되지 않나? 다른 쿼리 스트링이 없는 인덱스 페이지에서는 문제가 없는데 기존 쿼리 스트링이 있을 경우 다 날려버리는 문제가 있음

## Phase2. 구현 내용

결국 쿼리 스트링을 처리하는 함수를 스크립트에 적용하여 구현하였음.

```javascript
// 기존 URL에 query string 파라미터를 추가하거나 업데이트하는 함수
function updateQueryStringParameter(uri, key, value) {
    var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
    var separator = uri.indexOf('?') !== -1 ? "&" : "?";
    if (uri.match(re)) {
        return uri.replace(re, '$1' + key + "=" + value + '$2');
    } else {
        return uri + separator + key + "=" + value;
    }
}
// 사용 예
$('.sort-btn.oldest').on('click', function () {
    var newUrl = updateQueryStringParameter(window.location.href, 'sort_order', 'oldest');
    window.location.href = newUrl;
});
```

원래 이렇게 한다고 함.

# 이슈: 앵커 태그에서 href에 지정된 쿼리 스트링을 눌렀을 때 기존 쿼리 스트링이 날아가버리는 문제

## Phase1.

### 환경: macOS, arm, flak, jinja2, jquery, 

### 로그: 없음

### 최근 변경사항

```html
<!-- 드롭다운 메뉴 (초기에는 hidden 클래스 적용) -->
                <div id="dropdownMenu"
                    class="absolute mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg hidden">
                    <!-- 메뉴 항목들 -->
                    <a href="?order=newest" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">최신순</a>
                    <a href="?order=like" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">좋아요순</a>
                    <a href="?order=oldest" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">오래된순</a>
                </div>
```

이와 같이 드랍다운 메뉴 요소들에 쿼리 스트링을 추가하였고, 클릭하면 기존 쿼리 스트링이 없어져버리는 문제가 있음.

## Phase2-1.

### 확인: 서버사이드에서 그냥 기존 쿼리들 가져와서 병합하는 방식이 있음. 아래가 핵심 부분

```plain text
{% set params_newest = request.args.to_dict() %}
{% set params_like   = request.args.to_dict() %}
{% set params_oldest = request.args.to_dict() %}

{% set params_newest['order'] = 'newest' %}
{% set params_like['order']   = 'like' %}
{% set params_oldest['order'] = 'oldest' %}

<a href="{{ url_for('your_route', **params_newest) }}"
   class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
   최신순
</a>

<a href="{{ url_for('your_route', **params_like) }}"
   class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
   좋아요순
</a>

<a href="{{ url_for('your_route', **params_oldest) }}"
   class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
   오래된순
</a>

```



### 시도

위 코드를 그대로 병합하여 시도.

### 결과분석

{% set params_newest['order'] = 'newest' %}  부분에서 에러 발생. GPT의 코드가 잘못된 것으로 보인다. 최선의 방식은 for_url을 사용해 서버 사이드에서 쿼리를 기존 url과 쿼리 스트링에 추가하는 간단한 예재로 공부하는게 최선일듯.

## Phase2-2. Path variable로 전환

### 확인: 생략

### 시도

```html
 <div id="dropdownMenu"
              class="absolute mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg hidden">
              <a href="/joojeop/{{coach.name}}/newest" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">최신순</a>
              <a href="/joojeop/{{coach.name}}/like" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">좋아요순</a>
              <a href="/joojeop/{{coach.name}}/oldest" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">오래된순</a>
          </div>
      </div>
```

### 결과분석: 잘 됨. 앞에 슬래쉬를 안 붙여주면 기존 url에 링크가 추가가 됨.

(추후 작업 중 이 부분은 다 변경되었음.)

# 이슈: 소셜 로그인 실패

## Phase1.

### 환경: macOS, arm, flak, jinja2, jquery, 

### 로그: 

액세스 차단됨: 이 앱의 요청이 잘못되었습니다

이 앱에서 잘못된 요청을 전송했으므로 로그인할 수 없습니다. 나중에 다시 시도하거나 개발자에게 이 문제를 문의하세요. 이 오류에 관해 자세히 알아보기이 앱의 개발자인 경우 오류 세부정보를 참고하세요.

400 오류: redirect_uri_mismatch

### 오류 400: redirect_uri_mismatch

앱이 Google의 OAuth 2.0 정책을 준수하지 않기 때문에 앱에 로그인할 수 없습니다.앱 개발자라면 Google Cloud Console에서 리디렉션 URI를 등록하세요.

요청 세부정보: redirect_uri=http://127.0.0.1:5000/login/google/authorized flowName=GeneralOAuthFlow

### 최근 변경 사항

window os에서 구현된 소셜 로그인 기능 병합

## Phase2-1

### 확인 

1. 구글 개발자 콘솔에서 redirect_uri 등록 상태 확인
  1. Authorized redirect URIs(승인된 리디렉션 URI) 항목 확인: 비어 있음.
1. 앱에서 로그인할 때 리다이렉트 되는 url이 등록된 redirect URIs중 하나와 일치해야 함
### 시도

Oauth2.0 인증서버에 클라이언트를 등록해야되는데 맥북 환경에서는 기존에 등록된 localhost:5000/….가 먹히지 않았음. 127.0.0.1로 변경하니 해결됨.

### 결과 분석: 해결. 개발 환경에서는 맥 환경을 위해 Oauth2.0 인증 서버에 로컬 호스트 대신 127.0.0.1을 사용해야 함.

# 목표: 토글 버튼의 값을 폼의 포스트 액션에 추가

자바 스크립트로 동적으로 관리해야겠다.

# 이슈: 저장 후 갱신된 데이터베이스가 클라이언트에 뿌려지지 않음

## Phase1.

### 환경: macOS, arm, flak, jinja2, jquery, mongoDB

### 로그: 없음

### 최근 변경사항

save 함수 및 joojeop 함수 구현

```python
@app.route("/joojeop/<coach_name>/<sort_order>/save", methods=["POST"])
def save_joojeop(coach_name, sort_order):
    print("save_joojeop 함수 호출")
    user_id = decode_jwt_from_cookie()
    content = request.form.get("content")
    save_joojeop(user_id, user_id, coach_name, content)
    return redirect(url_for("joojeop", coach_name=coach_name, sort_order=sort_order))
```

joojeop 함수 호출되면 갱신된 데이터가 뿌려져야 하는데, 그게 안 됨

```python
@app.route('/joojeop/<coach_name>/<sort_order>', methods=['GET'])
def joojeop(coach_name, sort_order):
    print("joojeop 함수 호출")
    # 클라이언트에서 선택한 코치 이름 path variable로 받아오기
    # 코치 딕셔너리 생성
    coach = {"name": coach_name, "path": f"images/{coach_name}.png"}
    # 해당 코치의 주접 리스트만 표현하도록 업데이트
    joojeops = get_joojeops_by_coach_name(coach_name, sort_order)
    print("주접 데이터베이스!!!\n", joojeops)
    # get content from query string if exists
    content = request.args.get('content', '')

    # 코치 데이터 템플릿에 넘겨주기
    return render_template("joojeop.html", coach=coach, joojeops=joojeops, sort_order=sort_order, content=content)

```

## Phase2-1

### 확인: 

1. DB에 레코드가 실제로 들어가는지 → 커밋 여부, DB에 확인.
  1. 잘 들어가고 있음
1. get_joojeops_by_coach_name(coach_name, sort_order)가 최신 데이터를 반환하는지
  1. 정상 작동함
1. return redirect(url_for("joojeop", coach_name=coach_name, sort_order=sort_order)) 실행 후 리다이렉트된 joojeop 핸들러 함수 출력 시 처음에는 주접 데이터베이스가 갱신된 값을 안 불러옴
  1. 이게 문제인듯
  1. print("collection.write_concern =", collection.write_concern.document)
    1. 이 코드로 일단 확인해보기
    1. 결과: collection.write_concern = {} , 즉 즉각적인 저장이 이루어지고 있음.
1. Ajax 포스트가 문제였다!
Ajax로 폼을 제출하는 경우

•	Ajax 요청의 경우, 브라우저는 302 리다이렉트를 자동으로 따라가지 않습니다. 즉, Ajax 콜백 내에서 리다이렉트 URL을 받아서 직접 window.location.href를 설정해 주어야 합니다.

•	만약 Ajax를 사용 중이라면, 예를 들어 jQuery의 $.ajax()나 $.post()를 사용하고 있다면, 서버에서 받은 302 응답의 Location 헤더를 이용해 페이지를 강제로 리로드해 주어야 합니다.

### 시도

```html

            $('.save-btn').on('click', function (e) {
                e.preventDefault();
                let content = $('.result').text();
                $.post(`/joojeop/${encodeURIComponent(coachName)}/${sortOrder}/save`, {
                    content: content
                }, function (data) {
                    location.reload();
                });
            });
```

포스트 후 location.reload();를 추가

### 결과분석: 정상적으로 작동함. 아래는 이에 관한 중요한 내용

Ajax 요청으로 폼을 제출할 경우, 브라우저는 서버가 보낸 302 리다이렉트 응답을 자동으로 따르지 않습니다. 대신 Ajax 호출은 백그라운드에서 요청을 보내고 응답을 받아오게 되는데, 이 때 리다이렉트 URL은 브라우저 주소창에 반영되지 않고 Ajax 콜백 함수 내부로 전달됩니다.

따라서 서버에서는 저장 후 302 리다이렉트 응답을 보내더라도, Ajax 요청에서는 해당 리다이렉트가 자동으로 수행되지 않아 새 페이지로 이동하지 않습니다. 이 때문에 클라이언트는 여전히 이전 페이지를 보여주고, 새로 갱신된 데이터가 보이지 않게 됩니다.

이를 해결하기 위해 Ajax 요청의 콜백 함수에서 location.reload();를 호출하면, 브라우저가 전체 페이지를 새로고침하여 최신 데이터를 다시 로드하게 됩니다. 이렇게 하면 서버에서 저장한 데이터가 새로 반영된 페이지를 볼 수 있게 됩니다.

요약하자면:

•	일반 폼 제출에서는 브라우저가 302 응답을 자동으로 따라 새 URL로 이동하지만,

•	Ajax 요청에서는 리다이렉트가 내부적으로 처리되어 브라우저 주소창에는 반영되지 않습니다.

•	그래서 Ajax 콜백에서 location.reload();를 명시적으로 호출해 페이지를 갱신해야 합니다.

이 방식으로 문제를 해결하면, 저장 후 새 데이터를 클라이언트에서 정상적으로 확인할 수 있습니다.

# 목표: 좋아요 구현

## Phase1. 스텝바이스텝

1. 좋아요 클릭 했을 때 알러트 띄우기
1. 알러트에 주접 아이디 담기
1. 주접 아이디 like 함수에 넘기기
1. jinja에서 플래그 변수에 따라 클래스 태그를 추가 하는 방법 조사
1. 클라이언트 구현 완료. 백에서 각 주접당 플래그를 제대로 넘겨주면 됨


여기서 like-btn 뒤에 liked 클래스 추가하면 빨갛게 칠해짐

```html
                    <span class="joojeop-likes flex items-center">
                        <!-- like-btn에 cursor-pointer를 추가해 클릭 가능함을 표시 -->
                        <span class="like-btn cursor-pointer">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24"
                                stroke="currentColor" stroke-width="2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                            </svg>
                        </span>
                        {{ joojeop.like }} likes
                    </span>
```



# 목표: 정렬과 필터링 동시 구현

## Phase1. 스텝바이스텝

1. 일단 쿼리스트링을 추가. 
  1. href가 앵커에 있는 이상 쿼리스트링도 덮어 써버린다. 그러면 어떻게 해야 하는데? 그냥 지워. newest가 화석처럼 남아버리긴 하는데 천천히 수정이 가능하지 이러면 일단.
1. 스텝 바이 스텝으로 정렬 순서 경로 변수를 어트리뷰트로 대체
  1. 생성 후 리다이렉트 되는 과정 확인
    1. 제미니로 generate 할 떄 경로변수 삭제. 그리고 백엔드 함수에서 쿼리 스트링 받아오기
      1. 정상 작동 확인 오케이
    1. GPT 생성에서도 똑같이 경로변수 삭제, 글고 백엔드 함수에서 쿼리 스트링 받아 오기
  1. joojeop.html 접속할 때 라우팅 해결
    1. 템플릿 측: url에서 경로변수 삭제
    1. 백엔드 측: 라우팅 설정에서 경로변수 삭제. 
      1. 리다이렉트 될 때 이 경로변수를 쓰는 것들이 있는지 확인해야 함.
      1. 세 군데서 /joojeop/coach_name 으로 라우팅 되는데, 모든 코드는 아래와 같음
        1. return redirect(url_for("joojeop", coach_name=coach_name, sort_order=sort_order))
    1. 신기하게 아무 문제 없는 것으로 보임.
    1. 병합하고 변경 사항이 날아가긴 했는데 다시 살려냄. 역시 브렌치가 조아.
1. 저장 과정에서 정렬순서를 경로변수로 쓰는 것도 제거 → 완료
1. 생성 과정에서 정렬 순서를 경로변수로 쓰는 것도 제거
# 목표: 저장 하고 나면 .result 태그의 텍스트 비워버리기

## Phase1. 스텝바이스텝

1. 저장 클릭하고 호출된 다음 일단 태그를 비워주기도 해야 한다. 왜? 템플릿에서 태그를 비우는 것과 서버에서 템플릿에 내용 던져주는 건 별도다.
1. 근데도 안 돼네. 이럴 때는 순서대로 정리하는게 직빵. 
1. 저장 과정은 별도로 놔 두고, 저장 이후 동작을 그냥 하드코딩해야 할 듯하다. 그럴려면 저장하고 나서 특정 url로 이동하도록 해야 하는데 → 결국 이 부분도 Ajax 동작 방식 때문에 문제가 된듯 하다.
아래 동작 후에 reload 하는 대신 다른 url로 이동하는 방법은? 아래 코드를 다음과 같이 수정

```javascript

            $(".save-btn").on("click", function (e) {
                e.preventDefault();
                let content = $(".result").text();
                $.post(
                    `/joojeop/${encodeURIComponent(coachName)}/${sortOrder}/save`,
                    {
                        content: content,
                    },
                    function (data) {
                        location.reload();
                    }
                );
            });

```

# 이슈: EC2 서버의 앱 접속 시 속성 없음 에러(encode)

## Phase1.

### 환경: Ubuntu, amd, EC2, Python, flask, 

### 로그

```shell
AttributeError: module 'jwt' has no attribute 'encode'

1.238.129.195 - - [12/Mar/2025 15:01:33] "

**GET /github HTTP/1.1**

" 500 -

JWT 토큰이 쿠키에 존재하지 않습니다.

1.238.129.195 - - [12/Mar/2025 15:02:05] "GET / HTTP/1.1" 200 -

1.238.129.195 - - [12/Mar/2025 15:02:05] "GET /static/js/main.js HTTP/1.1" 304 -

JWT 토큰이 쿠키에 존재하지 않습니다.

1.238.129.195 - - [12/Mar/2025 15:02:39] "GET / HTTP/1.1" 200 -

1.238.129.195 - - [12/Mar/2025 15:02:39] "GET /static/js/main.js HTTP/1.1" 304 -

JWT 토큰이 쿠키에 존재하지 않습니다.

1.238.129.195 - - [12/Mar/2025 15:02:42] "GET / HTTP/1.1" 200 -

1.238.129.195 - - [12/Mar/2025 15:02:42] "GET /static/js/main.js HTTP/1.1" 304 -

JWT 토큰이 쿠키에 존재하지 않습니다.

1.238.129.195 - - [12/Mar/2025 15:02:43] "GET / HTTP/1.1" 200 -

1.238.129.195 - - [12/Mar/2025 15:02:43] "GET /static/js/main.js HTTP/1.1" 304 -

google_login 함수 호출

1.238.129.195 - - [12/Mar/2025 15:02:52] "GET /google HTTP/1.1" 302 -

1.238.129.195 - - [12/Mar/2025 15:02:52] "GET /login/google HTTP/1.1" 302 -

google_login 함수 호출

1.238.129.195 - - [12/Mar/2025 15:03:03] "GET /google HTTP/1.1" 302 -

1.238.129.195 - - [12/Mar/2025 15:03:03] "GET /login/google HTTP/1.1" 302 -

JWT 토큰이 쿠키에 존재하지 않습니다.

1.238.129.195 - - [12/Mar/2025 15:03:13] "GET / HTTP/1.1" 200 -

1.238.129.195 - - [12/Mar/2025 15:03:13] "GET /static/js/main.js HTTP/1.1" 304 -

43.129.169.161 - - [12/Mar/2025 15:03:47] "HEAD /Core/Skin/Login.aspx HTTP/1.1" 404 -
```

### 최근 변경 사항

EC2에 플라스크 앱 업로드하고 도메인 연결 함. 

PyJWT 설치 

flask-jwt-extended 삭제

## Phase2-1.

### 확인: PyJWT 최신 버전의 JWT 모듈에는 encode 속성이 없음. 그냥 사라짐

### 시도: PyJWT 다운그레이드(무슨 버전으로?)

### 결과 분석: 해결.

# 이슈: 인덱스 페이지에서 정렬 안 됨

## Phase1.

### 환경

1. MacOS, arm, flask, mongoDB, 
1. Linux, Ubuntu, amd, flask, mongoDB
### 로그: 없음. 그냥 정렬이 안 됨

### 최근 변경 사항: 확인 불가

## Phase2-1.

### 확인

joojeop.html에서는 정렬이 잘 되니까, 두 코드를 비교하여 확인할 것. 일단 서버 코드 보고 모르겠으면 템플릿 보자. 

joojeop의 서버 코드

```python
def get_joojeops_by_coach_id(coach_id, order='newest', limit=None, filter_option='all'):
    """
    주어진 coach_id의 모든 주접을 가져와서 정렬하여 반환하는 함수
    """
    query = {}
    if coach_id:
        query["coach_id"] = coach_id
    query = {}
    if coach_id:
        query["coach_id"] = coach_id

    joojeops = list(db.joojeops.find(query))

    if order == 'newest':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['date'], reverse=True)
    elif order == 'like':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['like'], reverse=True)
    elif order == 'dislike':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['dislike'], reverse=True)
    elif order == 'oldest':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['date'], reverse=False)
    else:
        sorted_joojeops = joojeops

    # 필터링
    if filter_option == 'all':
        pass
    elif filter_option == 'mine':
        sorted_joojeops = [
            joojeop for joojeop in sorted_joojeops if joojeop['author_id'] == decode_jwt_from_cookie()]

    if limit:
        sorted_joojeops = sorted_joojeops[:limit]

    # _id를 string으로 변환
    for joojeop in sorted_joojeops:
        joojeop['_id'] = str(joojeop['_id'])
        joojeop['isAuthor'] = False if joojeop['author_id'] != decode_jwt_from_cookie(
        ) else True
        joojeop['isLiked'] = True if decode_jwt_from_cookie(
        ) in joojeop.get('liked_by', []) else False
        joojeop['isDisLiked'] = True if decode_jwt_from_cookie(
        ) in joojeop.get('disliked_by', []) else False

    return sorted_joojeops
```

index의 서버 코드

```javascript
def get_joojeops(order='newest', limit=None, filter_option='all'):
    """
    모든 주접을 가져와서 정렬하여 반환하는 함수
    :param order: 정렬 기준 ('newest', 'like' 또는 'oldest')
    :param limit: 반환할 주접의 최대 개수 (None이면 제한 없음)
    :return: 정렬된 주접 리스트
    """
    joojeops = list(db.joojeops.find())

    if order == 'newest':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['date'], reverse=True)
    elif order == 'like':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['like'], reverse=True)
    elif order == 'dislike':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['dislike'], reverse=True)
    elif order == 'oldest':
        sorted_joojeops = sorted(
            joojeops, key=lambda x: x['date'], reverse=False)
    else:
        sorted_joojeops = joojeops

    # 필터링
    if filter_option == 'all':
        pass
    elif filter_option == 'mine':
        sorted_joojeops = [
            joojeop for joojeop in sorted_joojeops if joojeop['author_id'] == decode_jwt_from_cookie()]

    if limit:
        sorted_joojeops = sorted_joojeops[:limit]

    # id를 string으로 변환
    for joojeop in sorted_joojeops:
        joojeop['_id'] = str(joojeop['_id'])
        joojeop['isAuthor'] = False if joojeop['author_id'] != decode_jwt_from_cookie(
        ) else True
        joojeop['isLiked'] = True if decode_jwt_from_cookie(
        ) in joojeop.get('liked_by', []) else False
        joojeop['isDisLiked'] = True if decode_jwt_from_cookie(
        ) in joojeop.get('disliked_by', []) else False

    return sorted_joojeops
```

get_joojeops 에 인수로 넘어온 order 값이 항상 newest인 것을 확인. 인수 넘겨줄 때 문제가 있는게 확실함.

문제 발견

sort_order = request.args.get('order', 'newest')  # 기본값 newest 

키 값이 쿼리 스트링에는 sort_order로 넘어가는 상황에서 order로 조회하고 있었음. 이건 함수가 다 흩어져 있어서 생긴 문제다. 유지 보수가 극악인 코드가 완성됨.

### 시도

수정



