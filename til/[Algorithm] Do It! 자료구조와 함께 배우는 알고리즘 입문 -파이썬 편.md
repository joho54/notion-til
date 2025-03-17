# [Algorithm] Do It! 자료구조와 함께 배우는 알고리즘 입문 -파이썬 편



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> #: 주제, 그림, 스텝(중요)

>  정렬 부분은 다 한번 해봤지만 기억이 안 남. → 그럼 그냥 해. 알면 빨리 될 것이고, 그렇지 않으면 느리겠지. 코드는 타이핑하고 그림은 따라 그리기.

> 💡 추천 학습법:

# 버블정렬

## 단순 버블 정렬

### 그림: 버블정렬 pass 

pass: 일련의 비교 교환 과정. 버블 정렬에서는 첫 번째 패스로 가장 작은 원소를 구할 수 있음.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/db2cb1a5-5d4c-4ea7-933e-5797c5871104/IMG_9884.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=359483b3ba466989bb87a6abc46d2f71ffbbc8621335bf9b7b2588c835753553&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


```

## 버블정렬 개선 1

### 코드: 교환 횟수 감지해서 성능 올리기

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    for i in range(n-1):
		    exchng = 0 # exchange time in a pass
        for j in range(n-1, i, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
    if exchng == 0:
			break
```

## 버블정렬 개선 2

아래와 같은 상태일 때 스캔 범위(비교 범위)를 좁히는 부분 추가.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/4bb85350-4f4a-4c1c-8c0a-0f24ba97063b/IMG_9885.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=7f0fdf82c4d1628a159cb857be47a452445e5bb03b0f74980a1f5ac9918e69e8&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 스캔 범위 제한

```python
from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    """bubble sort"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1    
        for j in range(n-1, k, -1): # from the end
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j # update last. we can mark maximum area that should be scanned.
        k = last



```

## 셰이커 정렬

밀크 셰이크 먹고 싶다.

위와 같은 경우 거의 정렬이 다 됐지만 빠르게 마칠 수 없음. 9가 맨 끝에 있어서. 아이디어: 9를 맨 뒤로 이동시키면 정렬이 훨씬 빠르겠지?

### 코드: 셰이커 정렬

```python
from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
```

### 그림: 셰이커 정렬 패스

일단 스킵

# 단순 선택 정렬

# 단순 삽입 정렬

# 셸 정렬

# 퀵 정렬

## 기본 개념

### 그림: 퀵 정렬의 예

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/daac6dc7-7587-4378-a249-39ce32d19c09/IMG_9899.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=4d5513a0d511ac8bc276e4e690791114800562bfd868510fe869c934075215e9&X-Amz-SignedHeaders=host&x-id=GetObject)

### 개구코 1.

개념

재귀를 사용하지 않는 퀵정렬 구현은 pl, pr 포인터를 이용해야 한다. 아래는 이 아이디어만으로 직접 작성해본 퀵정렬 수도코드.

구현

```python
# 1. 일단 배열을 본다
# 2. 배열의 중간 값을 피벗으로 삼는다.
# 3. 양 끝에 pl, pr 포인터를 초기화한다.
# 4. '피벗 기준'을 충족하는 동안 포인터를 감소시킨다.
# 5. '피벗 기준'에 벗어나는 요소를 교환한다. 
# 6. 포인터들이 배열의 중간에 오기 전까지? 이 기준을 어떻게 잡아야 하지? 
# 7. 피벗을 다시 잡고 pl, pr을 초기화해서 진행한다. 
```

6번이 잘 모르겠다. 책을 다시 참고해서 정리해보자. 책에서는 이 기준을 pl ≤ pr로 잡았다. 즉, ‘배열의 중간’으로 픽스하면 안 되고, “pl, pr이 피벗 기준으로 배열을 모두 정리하기까지”가 이것을 의미한다. 

그리고 이 책의 구현에서도 퀵정렬은 재귀를 사용한다. 대신 in-place한 정렬이다. 재귀를 사용하는 inplace 정렬인데, 그럼 이걸 직접 구현해보도록 하자

```python
def q_sort(A, left, right):
    if left >= right: # 종료조건: 더 정렬할 영역이 없거나 요소가 하나일 때
        return
    pl, pr = left, right # 양 끝을 포인터로 설정
    pivot = A[(left + right)//2] # 피벗을 중간 값으로 설정
    while pl <= pr: # 포인터가 겹치지 않는 동안
        while A[pl] < pivot:  # 교환할 필요가 없을 때까지 포인터 움직여주기
            pl += 1 
        while A[pr] > pivot:
            pr -= 1
        # 다 움직인 다음에 교환. 이때 불필요한 교환이 최대 한 번 발생할 수 있음
        A[pl], A[pr] = A[pr], A[pl]
        pl += 1
        pr -= 1
    # 최종적으로 저장된 pr, pl 값의 의미
    # pl: 피벗 바로 왼쪽
    # pr: 그 반대
    q_sort(A, left, pl) # 피멋을 기준으로 왼쪽 영역 재귀
    q_sort(A, pr, right) # 피벗을 기준으로 오른쪽 영역 재귀



arr = [3, 2, 5, 234, 14, 5,234]
q_sort(arr, 0, 6)
    
```

위에가 내가 작성한 엉터리 정렬이고, 아래가 제대로된 정렬이다.

```python
def q_sort(A, left, right):
    if left >= right: # 종료조건: 더 정렬할 영역이 없거나 요소가 하나일 때
        return
    pl, pr = left, right # 양 끝을 포인터로 설정
    pivot = A[(left + right)//2] # 피벗을 중간 값으로 설정
    while pl <= pr: # 포인터가 겹치지 않는 동안
        while A[pl] < pivot and pl <= right:  # 교환할 필요가 없을 때까지 포인터 움직여주기
            pl += 1 
        while A[pr] > pivot and pr >= left:
            pr -= 1
        # 다 움직인 다음에 교환. 이때 불필요한 교환이 최대 한 번 발생할 수 있음
        if pl <= pr: 
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
    # 최종적으로 저장된 pr, pl 값의 의미
    # pl: 피벗 바로 왼쪽
    # pr: 그 반대
    q_sort(A, left, pr) # 피멋을 기준으로 왼쪽 영역 재귀
    q_sort(A, pl, right) # 피벗을 기준으로 오른쪽 영역 재귀



arr = [3, 2, 5, 234, 14, 5,234]
q_sort(arr, 0, 6)
print(arr)
```

코멘트

아무리 생각해도 제대로 된 인덱스 설정이 어렵다. 어떻게 하면 이 능력을 기를 수 있을까?

> 🔍 올바른 인덱스 설정 능력을 기르는 방법

위 내용에 따라 연습하면 되기도 하겠지만, 여기서 헤맸던 건 그냥 퀵 정렬의 포인터 이동을 제대로 이해하지 못했던 것 때문인거 같다.

→ 이 정렬의 스탭을 쉐도잉 해보자.

### 개구코 2

개념

피벗을 중심으로 배열을 두 부분으로 나누는 코드 작성해보기. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/df47a3d5-dd47-4d92-97fb-03da13dadd98/IMG_9908.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=68b4f18663157bb510244e13fd0380cb2775082894c5c74c2a12d078ddd36036&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/1df4cf6d-3df4-4f6a-a610-db02190c5291/IMG_9909.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=acea61e260f9f00407d538d8b6a2b14de27097c3a112ce49995a182d6913f4c8&X-Amz-SignedHeaders=host&x-id=GetObject)

위 그림을 그대로 해주면 될 거 같다.

구현

```python
def q_sort(A: list):
    # A를 피벗을 기준으로 '피벗보다 작은 영역'과 '큰 영역'으로 나누는 함수
    left, right = 0, len(A)-1
    # 배열의 양 끝에 포인터를 잡아줍니다.
    pl, pr = left, right
    # 피벗을 구해줍니다.
    p = A[(left+right)//2]
    # 두 포인터가 겹치지 않는 동안 포인터를 가운데로 스캔합니다.
    while pl <= pr:
        while A[pl] < p:
            pl += 1
        while A[pr] > p:
            pr -= 1
        # 만약에 포인터가 멈췄고, 두 값을 비교했을 때 대소관계가 다르면 교환해줍니다
        if A[pl] > A[pr]:
            print(f'before: {A}')
            print(f'pivot: {p}, exchange: {A[pl]}, {A[pr]}')
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
            print(f'after: {A}')
        
    # 작업이 끝났다면 결과를 출력해줍니다.
    print(A)

q_sort([5, 4, 3, 2 ,1])

```

코멘트

> 현재 코드에서 피벗을 기준으로 배열을 나누는 동작은 부분적으로 수행되지만, 완전히 올바르게 동작하지 않습니다.



제대로 수정한 코드는 다음과 같음

```python
def q_sort(A: list):
    # A를 피벗을 기준으로 '피벗보다 작은 영역'과 '큰 영역'으로 나누는 함수
    left, right = 0, len(A)-1
    # 배열의 양 끝에 포인터를 잡아줍니다.
    pl, pr = left, right
    # 피벗을 구해줍니다.
    p = A[(left+right)//2]
    # 두 포인터가 겹치지 않는 동안 포인터를 가운데로 스캔합니다.
    while pl <= pr:
        while A[pl] < p:
            pl += 1
        while A[pr] > p:
            pr -= 1
        # 만약에 포인터가 멈췄고, 포인터 위치가 엇갈리지 않았다면 교환
        if pl <= pr:
            print(f'before: {A}')
            print(f'pivot: {p}, exchange: {A[pl]}, {A[pr]}')
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
            print(f'after: {A}')
        
    # 작업이 끝났다면 결과를 출력해줍니다.
    print(A)

q_sort([5, 4, 3, 2 ,1])

```

### 개구코 3.

개념: 구현한 파티셔닝을 토대로 퀵 정렬 만들기

구현: 그냥 해 봅시다

```python
def paritioning(A: list, left, right):
    if left >= right:
        return
    # A를 피벗을 기준으로 '피벗보다 작은 영역'과 '큰 영역'으로 나누는 함수
    # 파티션 배열의 양 끝에 포인터를 잡아줍니다.
    pl, pr = left, right
    # 피벗을 구해줍니다.
    p = A[(left+right)//2]
    # 두 포인터가 겹치지 않는 동안 포인터를 가운데로 스캔합니다.
    while pl <= pr:
        while A[pl] < p and pl < right: # 파티션을 벗어나지 않게 조건을 추가합니다!
            pl += 1
        while A[pr] > p and pr > left: # 이하 동일
            pr -= 1
        # 만약에 포인터가 멈췄고, 포인터 위치가 엇갈리지 않았다면 교환
        if pl <= pr:
            print(f'before: {A}')
            print(f'pivot: {p}, exchange: {A[pl]}, {A[pr]}')
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
            print(f'after: {A}')
    paritioning(A, left, pr) # 파티셔닝이 끝난 후 pr은 작은 그룹의 끝단에 위치하게 됨
    paritioning(A, pl, right)
    # 작업이 끝났다면 결과를 출력해줍니다.s

def quick_sort(A: list):
    paritioning(A, 0, len(A) - 1) # 배열 전체를 범위로 하는 파티셔닝 호출

A = [5, 4, 3, 2, 1, 4, 3, 6, 4]
quick_sort(A)
print(A)


```

코멘트

성공~ 퀵 정렬은 ‘파티셔닝’과정과 ‘정렬’ 과정을 차례로 구현하면 잘 되네요.


### 개구코 4.

개념: 비재귀적인 퀵 정렬 만들기

> 비재귀적인 퀵 정렬은 이미 배운 재귀 함수 recur()를 비재귀적으로 구현하는 방법과 같이 만들 수 있습니다. 

(그렇다면 이 작업을 하기 전에 복습 차원에서 recur()를 다시 비재귀적으로 구현해보는 것도 좋을 거 같다. 전혀 기억이 안 난다. 이걸 그 사이에 까먹네. 

코드 자체를 기억하려 하지 말고 제발 방법론을 떠올려봐라.

1. 상향식 재귀 분석
1. 스택 동작 그림
```python
def recur(n):
    if n <= 0: 
        return # n이 0보다 작으면 아무 작업하지 않는다.
    
    recur(n-1) # 이 세 줄의 코드가 트리형으로 갑니다.
    print(n)
    recur(n-2) #n-2로 업데이트하고 함수의 처음으로 돌아갑니다.

```

이 코드의 상향식 재귀 분석 및 스택 동작 예측

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/23adf9a4-59f4-46ce-9a31-dff30aad8c8b/IMG_9910.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBKHQKMB%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIzi7rM2EV273KIv8BiBQKcv2inYU03F%2Bt5uLrtWXlqgIgBN8yX7tJ7Ks7tj0zK3U%2BWCG0i4XOmEkm%2BVTFcpCAcEgq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJTUwKYFo4iquB8ClCrcA%2B%2B0CUavwXhR9Orj%2BGGduqkS6qLMQBJL0ptfnfrBHfA%2FicCm7GLnIDf0Pbj30EZrtq4iQGzMsfml5XSU80lqzUILUC6sbuuMlerV60eq56aYmyttUNrNp1DGS5R5jIIN5qGbtViq2ylXOL%2FXWGJrFFpH6eZ5sNDEbcYF7KFQHMJwmaj7JJafPMaRiyq7pHOOitXyXjKZXBV9jztrLgt8hyLvX9Wkw9KDMHGHlONv3s%2FXcSqA29L7V9J7xHRR6UBofmqG6CDskzjT4mw5mdqCZL6eM6HQFTF%2FDJeYJVQhCBNhmsneslV0MJEWDtPFMtjFQQTQg6ECREzzNHuFS74b%2Fsv3ld7UNeugkaj7r5ORsZw7UDg3u62sTnLrnbKkGnN%2F7ApNswVlsC8MaaLg5U6camAbziL3gCcr5xSNsPmMnq7S7PpQMJRJy0ZWsHj49OVyaCrhKPjV4th1TGGuMuyqbsRWbrnm9uwYL216q4gsLW0Ae6d1UpoDiNSScue6TJPTl14PQUZO%2FscbQbNWXu664Z1CykJM89vdKBmVOcZ21TZkKPDV%2Becu8YlqFK9XXaMtbLqP88CmQSCPKRTWF8tZwWiLWxmupGkSx3kqVnVbLVo8xASsUy5K4kWqmYOzMPHs374GOqUBet4r0g6hN4Iv%2BGhO%2FW1P28blOF9Jzfwcz3d4AjPZJkOpI3Iv1usJ8Uy4tflkfmLi%2F%2FM9XVP1l0FIAyIdMyVNHdXr6tBx2Rnp2WCPFTfahCe0zBKlMnePADAgunBseMMiftSfORs4vrs98nyD0BmeT8jMR1MyEQLKA8oain4eUa6dszcdT73tLLr7KmezchHi86KEJ7jIScjal5Ub4s1fRT3qJhBo&X-Amz-Signature=bfcb431f5b84ee8086e44b032fb3da662f7004d4a774ea5cc5553880e30a6d37&X-Amz-SignedHeaders=host&x-id=GetObject)

따라서 제대로 된 구현은 아래와 같을 것

```plain text
1. 초기 n을 스택에 푸시
2. 만약 n 값이 0보다 크면(n>0)이면 
	1. 푸시된 n을 n-1로 업데이트
4. 만약 n 값이 0 이하면(n <= 0)이면 
	1. n = pop()
	2. print(n)
	2. (그림에서 까먹음. 만약 n-2가 0보다 크면) n-2를 스택에 푸시
	3. n = n -1
```

진짜..이래도 기억이 안 난다. 다시 참조

> 복습지시: 아래 코드를 비재귀적으로 표현하기

```python
# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
	"""순수한 재귀 함수 recur의 구현"""
	if n > 0:
		recur(n-1)
		print(n)
		recur(n-2)

x = int(input())
recur(x)
```

1. 꼬리 재귀를 제거하기: 꼬리 재귀는 recur(n-2)인데, 이것의 역할은 n을 n-2로 업데이트하고 함수를 처음부터 실행하는 것임.
```python
def recur(n: int) -> int:
	while True:
		if n > 0:
			recur(n-1)
			print(n)
			n = n - 2
```

1. 중간재귀를 제거하기: 중간 재귀는 recur(n-1)인데, 이것을 제거하고 처음으로 돌아가버리면 발생하는 가장 큰 두 가지 문제는 print할 n을 저장할 수 없고, 꼬리 재귀에서 사용할 n값 역시 날아간다는 것임. 스택을 사용하여 해결. 그리고 결국 n = n -1로 업데이트 후 함수의 처음으로 돌아가기는 해야 함.
```python
from stack import Stack

def recur(n: int) -> int:
	s = Stack(n)
	while True:
		if n > 0:
			s.push(n) # 일단 스택에 저장을 했다면!
			n = n - 1 # n = n -1로 업데이트하고 처음으로 돌아가면 되긴 함. 그러니까 이것도, 
			continue
		if not s.is_empty():
			n = s.pop()
			print(n)
			n = n - 2
			continue
		break
```

위 코드에서도 보다시피, 재귀를 스택으로 구현하는 과정을 순서대로 생각할 필요가 있다.

```plain text
1. 꼬리 재귀 제거
2. 중간 재귀 제거 및 스택 저장 과정을 추가.
```

구현

```python
from collections import deque

def recur(n):
    if n <= 0: 
        return # n이 0보다 작으면 아무 작업하지 않는다.
    
    recur(n-1) # 이 세 줄의 코드가 트리형으로 갑니다.
    print(n)
    recur(n-2) #n-2로 업데이트하고 함수의 처음으로 돌아갑니다.


# 1. 꼬리 재귀 제거
# 2. 중간 재귀 제거 및 스택 저장 과정을 추가.

def recur2(n):
    s = deque()
    s.append(n)
    while True:
        if n > 0:
            s.append(n)
            n = n - 1
            continue
        if s:
            n = s.popleft()
            print(n)
            n = n - 2
            continue
        break


recur(4)
print('='*8)
recur2(4)
```

코멘트

아 어려워. 왜 이 둘의 구현이 다른 거지?

# 이슈: 퀵 정렬 구현중 index out of range 에러 발생

## Phase1.

환경: 파이썬

로그

```python
while pl <= pr:
        while A[pl] <= pivot: # list index out of range
```

최근 변경 사항

아래 코드 구현

```python


def q_sort(A, pl, pr):
    pivot = A[(pl + pr) // 2]
    while pl <= pr:
        while A[pl] <= pivot:
            pl += 1
        while A[pr] > pivot:
            pr -= 1
        # now pl, pr are pointing elems must be exchanged
        A[pl], A[pr] = A[pr], A[pl]
        print(f'exchanged {A[pl]}, {A[pr]}, pivot: {pivot}')
        print(A)
        pl += 1
        pr -= 1
        # and repeat?
    
    # then what? now we have half area array
    if pl <= pr//2 - 1: q_sort(A, pl, pr//2 -1)
    if pr//2 <= pr: q_sort(A, pr//2, pr)


def quick_sort(A):
    return q_sort(A, 0, len(A)-1)

A = [3, 32, 3, 5, 1]
A = quick_sort(A)
print(A)
```

## Phase2-1

### 확인

에러 발생 당시 인덱스 값들

pl: 5

pr: -1

while pl ≤ pr: 조건 반복을 거치지 않고 아래 부분에서 각 포인터를 움직여서 그런거 같다. 

저 부분은 교환이 필요할 때만 실행돼야 하는데, 지금 그렇게 되고 있는가?  그냥 별도의 배열 업데이트 필요가 없어도, 이 부분이 무조건 실행되기 때문에 조건문을 달아줄 필요가 있어 보인다.

### 시도

```python
if pl <= pr:
            A[pl], A[pr] = A[pr], A[pl]
            print(f'exchanged {A[pl]}, {A[pr]}, pivot: {pivot}')
            print(A)
            pl += 1
            pr -= 1
        # and repeat?
```

이와 같이 while문과 동일한 조건을 안에 네스트 시켜줬다.

### 결과 분석

인덱스 에러는 해결 됨. 대신 다음 에러가 발생

# 이슈: 퀵 정렬 재귀 호출 과정에 재귀 깊이 오류 발생

## Phase1.

환경: 파이썬

로그: RecursionError: maximum recursion depth exceeded

```python
    if pr//2 <= pr: q_sort(A, pr//2, pr)
```

최근 변경 사항: 없음

## Phase2-1

### 확인

재귀문을 실행하는 조건이 잘못돼서 무한 재귀 호출 되는 것으로 보인다. 그럼 어떻게 해결할 수 있지? 등호를 빼 볼까?

질문: 이 조건에서 확인하고 싶은 것이 뭐지?

우리가 정렬해야 하는 배열의 넓이.

그렇게 생각하면 아래 두 조건은 완전히 합리적이지 않나?

```python
if pl < (pr//2 - 1): q_sort(A, pl, pr//2 -1)
if (pr//2) < pr: q_sort(A, pr//2, pr)
```

아니! pr//2-1이 완전히 틀렸지. (pl+pr)//2 -1로 해야지!

이렇게 수정 후 다음 문제를 발견: pl이 이미 증가하고, pr이 감소한 시점이라서 재귀해야 하는 배열 영역이 잘못 정의됨. 그러면 어떻게 배열 영역을 결정지어야 하는가? 그냥 따로 저장해두면 안 되나

### 시도

```python
if pl < ((pl+pr)//2) - 1: 
        print('recursion call 1')
        q_sort(A, pl, (pl+pr)//2 -1)
    # 피벗 앞 부분을 먼저 처리해주고
    if ((pl+pr)//2) < pr: 
        print('recursion call 1')
        q_sort(A, (pl+pr)//2, pr)
```

### 결과 분석: 실패

최종 코드

```python
# 1. 일단 배열을 본다
# 2. 배열의 중간 값을 피벗으로 삼는다.
# 3. 양 끝에 pl, pr 포인터를 초기화한다.
# 4. '피벗 기준'을 충족하는 동안 포인터를 감소시킨다.
# 5. '피벗 기준'에 벗어나는 요소를 교환한다. 
# 6. 포인터들이 겹치기 전까지 이 과정을 반복한다.
# 7. 피벗을 다시 잡고 pl, pr을 초기화해서 진행한다. 

def q_sort(A, pl, pr):
    pl_b, pr_b = pl, pr
    pivot = A[(pl + pr) // 2]
    while pl <= pr:
        while A[pl] <= pivot:
            pl += 1
        while A[pr] > pivot:
            pr -= 1
        # now pl, pr are pointing elems must be exchanged
        if pl <= pr:
            A[pl], A[pr] = A[pr], A[pl]
            print(f'exchanged {A[pl]}, {A[pr]}, pivot: {pivot}')
            print(A)
            pl += 1
            pr -= 1
        # and repeat?
    
    # then what? now we have half area array
    if pl_b < ((pl_b+pr_b)//2) - 1: 
        print('recursion call 1')
        q_sort(A, pl_b, (pl_b+pr_b)//2 -1)
    # 피벗 앞 부분을 먼저 처리해주고
    if ((pl_b+pr_b)//2) < pr_b: 
        print('recursion call 1')
        q_sort(A, (pl_b+pr_b)//2, pr_b)
    # 피벗 뒷 부분을 처리.


def quick_sort(A):
    return q_sort(A, 0, len(A)-1)

A = [3, 32, 3, 5, 1]
A = quick_sort(A)
print(A)
```

실패. 그냥 무한 반복을 하게 된다. 이유가 뭐지? 

> 🔍 현재 코드의 문제점 분석

일단 백업을 한다는 아이디어 자체는 잘못된게 아니었다. 문제점은 재귀할 때 파라메터를 잘못 넘겨줬고(이미 정렬이 끝난 부분까지 포함하거나 혹은 의미적으로 불분명한 파라메터를 넘겨줬음) 중요한 건 각 코드의 의미와 인덱스의 의미인데, 이런 것들을 최대한 쓰면서 구현하는게 옳다.

그렇다면 마지막으로 다시 한 번 안 보고 인플레이스한 퀵 정렬을 구현해봅시다.

# 병합 정렬

## 기본 개념

### 그림: 정렬을 마친 배열의 병합

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/57d32329-254c-46b7-85eb-6c7905b86749/IMG_9897.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=bac352b3040fff4fe380cb428c90f5e06e8d8826e761a38ddf20c209b6810264&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 해당 그림을 구현한 코드

```python
from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence):
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 원소 수

    while pa < na and pb < nb: # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pa]:
            c[pc] = a[pa]
            pa += 1
        else:
            pb += 1
    # 떨이요~ 떨이
    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    # 떨이요~ 떨이
    while pb < na:
        c[pc] = a[pb]
        pb += 1
        pc += 1


   
```

이 내용은 사실 쉬워서 더 볼 필요 없을 거 같다.

### 그림: 병합 정렬하는 방법

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/6b5838ad-1623-41fc-93d6-ddd0d95255a5/IMG_9898.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=d38e43524257a75328d38bfa0c7eda3fc0d744fcca6147d8c0e5d0a46a3f953a&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 병합정렬

```python
from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합정렬
            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:
                if buff[i] <= a[i]
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1) # 배열 전체를 병합 정렬.
    del buff

```

# 힙 정렬

## 기본 개념

### 그림: 힙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/00b0f9c1-8f4e-4d1b-9d3f-b94d9a18d4bc/IMG_9890.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=21cff80a0323ca2791c95a8725477c6684a950f1ee24febe15f7a2969bd40da9&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 루트노드 삭제하고 힙 업데이트 하는 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/fc323225-8952-40bd-af97-788fef3539bb/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=b562d6ab6998437605c3d667e7e1aa40eb60c517e1c719b0311792ecf5603e4a&X-Amz-SignedHeaders=host&x-id=GetObject)

큰 값을 가진 자식과 위치를 교환. (이하 생략)

### 순서: 힙 정렬 알고리즘

1. 힙의 루트 a[0]에 위치한 최댓값 10을 꺼내 배열의 맨 끝 원소인 a[9]와 교환합니다.
1. 최댓값을 a[9]로 이동하면 a[9]는 정렬을 마칩니다. 앞에서 살펴본 순서대로 a[0] ~ a[8]의 원소를 힙으로 만듭니다. 그 결과 두 번째로 큰 값인  9가 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값 9를 꺼내 아직 정렬하지 않은 부분의 맨 끝 원소인 a[8]과 교환합니다.
1. 두 번째로 큰 값을 a[8]로 이동한 결과 a[8]~a[9]가 정렬을 마칩니다. 앞의 단계와 마찬가지로 a[0]~a[7]의 원소를 힙으로 만듭니다. 그 결과 세 번째로 큰 값인 8이 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값을 꺼내 아직 정렬하지 않은 맨 끝 원소인 a[7]과 교환합니다.
1. 이 과정을 반복하면 배열의 맨 끝에 최댓값부터 순서대로 하나씩 저장됩니다.
### 그림: 힙 정렬 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/45579a74-22f3-44cc-9040-cfe92f1e407b/IMG_9892.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=7ef88df84b7990085047b476f33018d90171be743af067248b7a7d417796e01a&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/9d650163-c6f4-4f18-9b53-13a425a25ccc/IMG_9893.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=8d8956ca9cf4274b47486ef3a172e1f2b11310b5d9622ad9cade32454bbfa8ce&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: A는 힙이 아니고 B, C는 힙이다

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/472ae03c-8298-4ea1-8357-fecc60bf247c/IMG_9894.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=5589777705c5849427097256a9b4f55cff5757f0e7ee7f3cacf430870482a1bb&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 정렬되지 않은 서브트리를 힙으로 만드는 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/f318a344-9231-4017-a950-59930627a59d/IMG_9895.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=90ce6e693c1b44bd3635392788f838230591cc68ed3515c1ebcc8996ad5b8f9d&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/0c24fd7b-146e-486d-826a-a3479c2988eb/IMG_9896.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=33c383d87513d4f67618a6fe9e568b5333378329c297d830bc6b1edbb6978a80&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 힙 정렬

> 힙은 사실 그렇게 복잡하지 않다. 솔루션에 모듈이 많아서 복잡해 보이는 거지.

```python
from typing import MutableSequence

def heap_sort(a: MutableSequence):

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        temp = a[left] # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl # choose larger child
            if temp >= a[child]:
                break 
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)
    
    
    for i in range((n - 1) // 2, -1, -1): # a[i] ~ a[n-1]을 힙으로 만들기 
        down_heap(a, i, n - 1) # 밑에서부터 차례대로 올라가며 힙으로 만드는 과정.


    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0] # 최댓값인 a[0]과 마지막 원소를 교환
        down_heap(a, 0, i - 1) # a[0] ~ a[i-1]을 힙으로 만들기
```

> 머리가~ 안 돌아~ 가서~ 주석을~ 포함한~ 코드를~ 필사하세요! 

### 코드설명

- down_heap(): 배열 a에서 a[left] ~ a[right] 원소를 힙으로 만듭니다. a[left] 이외에는 모두 힙 상태라고 가정하고 a[left]를 아랫부분의 알맞은 위치로 옮겨 힙 상태를 만듭니다.
- 궁금증: 그럼 a[right]는 어떻게 힙 정렬을 하나요?
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/fc323225-8952-40bd-af97-788fef3539bb/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=b562d6ab6998437605c3d667e7e1aa40eb60c517e1c719b0311792ecf5603e4a&X-Amz-SignedHeaders=host&x-id=GetObject)

- heap_sort()함수
  - 원소 수가 n인 배열 a를 힙 정렬하는 함수입니다. 다음과 같이 2단계로 구성됩니다.
  - 1단계: down_heap() 함수를 호출하여 배열 a를 힙으로 만듭니다.
  - 2단계: 최댓값인 루트 a[0]을 꺼내 배열의 마지막 원소와 교환하고, 배열의 남은 부분을 다시 힙으로 만드는 과정을 반복하여 정렬을 수행합니다.
## 힙 정렬의 시간 복잡도

이 부분 내용은 좀 부실함. 다른 교재를 참고하여 정리할 것.

# 도수 정렬

## 기본 개념

### 그림: 도수분포표 작성

그냥 간단함. 주어진 값의 최대값을 크기로 하는 배열을 만들고 각 값을 인덱스로 해당 칸을 1 더하면 됨.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/5b251fbd-b065-4d1d-b407-40139302c8f6/IMG_9886.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=8db1739b62474699c0789dd0b6ccaf2b15faea2b59d0dcc5c32baf34e3258ce7&X-Amz-SignedHeaders=host&x-id=GetObject)

이에 대한 Prefix Sum 배열을 구하면 누적 도수 분포표를 구할 수 있음. 이를 통해 작업용 배열을 만들면 되는데, 아래와 같음

### 그림: 작업용 배열 만들기

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/80e796a5-1525-403e-a91f-6acd21d88998/IMG_9887.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=16295cc2a80250d48f9162eb8138876ad5cce2ed8dfcac23bc202f44c717db0e&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 위 그림을 수행하는 코드

```python
for i in range(n - 1, -1 ,-1):
	f[a[i]] -= 1
	b[f[a[i]]] = a[i]
```

### 그림: 작업용 배열 만들기 2

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/c8614daa-8dc9-4387-89eb-14e313f8a985/IMG_9888.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=758467c0ffcc0807997dc0177b877ad79f7126540df2b9a4669fa8084134b02a&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 작업용 배열 만들기 3

f 테이블의 요소 값을 줄여주는 덕분에 중복 값이 알아서 잘 처리되는 모습을 볼 수 있다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b158ccf2-c130-4f6e-a389-4c06d1997a13/_.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H3VDQRH%2F20250317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250317T110447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGnOYdfoK%2Fd%2BnTvjKDWmK%2B%2BAZCNRJeZQuKpqqA5%2B2UVIAiBV27agVEksb9ObESE%2Fg9QZRNSHABbdkLR444zrKAEAnSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMuYhxmmvCow2kApSNKtwDbD93Yc0oPlndTgIAganiZSTNv%2B0aYYW5L7pKPn6BuNyRuKzHTOpk3pNw8IhGWXz7WTmNfSbILutQiE6ub2xvT%2BbwyRaRysNWifl1k52ijb4xlyR1BgogONcxhS8ExkIq0AueTTC6%2Bpy8OJoXEdcoDKdYZ9i%2BXBKUG%2F9YuhG6f90ku52DNSCTdoqOk5MA%2FWxX7cM8wJeoGtryDKEWGyjfRL%2F65voEDl2kLBGAo4Att4CoOCfKuF91iMCWHDo9bPyeX2BATCX5nXLiJDP7pn%2BO4LeDyqacAsILqKL7zTMCZsA7YfGx3pXu%2BhmhEyGPjyCitkk4tFxU4riVifiCb2XWRoYuiiv6kOZc9stVqEjpyjOV5kwSwJjK8W7lIpfCVH3HL6zz51hRqbiEdVLd5koKEd8Bf%2Bg%2FR3Z0JoXSewOKmTTr0KRbYNlxi7UAIWa0d3GWzRPIHt2qRRTA%2BKreupYJuw%2BDk1z6rb9HPOB2SYqJjwfzW1JqQMSJnLscVfL8QDFMcUdZIOp1SgQ%2FNSjfqEqvZPwLJVaDvJC%2FY8M%2FW9SmmmNY%2BVg0JFnGoWQNIIZLWDURpjp2WEFkOl6iJUHZf10euxWXykx5dCABdX727OdSgFS%2FwkEgSB26VQGAJmgw9uzfvgY6pgE6mUEQ9%2BGALc6rZUQwCACNt132GqJUOqptI3uZ6M2Sv6LH6BEoYnVB78IsdrgYcJQPsKuCj0aEQUlZBRspcipUFIJVIpsNeXEGo1ZWyjXAZKmzwkM2Qk3%2ByJkqnHb5gQflf%2FBwghJdPAYgYhHqJaLp2csNblrhV%2Fa1yFhHN%2Fb9clsyKZHaShACW6rD4%2Fc0qMb8yGbweAVPJqOuxymSWHz6m1B%2BLLae&X-Amz-Signature=607420ff54a586700b2b45b03fc670a6940793709b9544f49f54da30ce6978cb&X-Amz-SignedHeaders=host&x-id=GetObject)

거꾸로 하자. 너무 지루하고 그러니까.

그리고 일단 이 내용 정리한 다음 정렬은 마무리하자.





