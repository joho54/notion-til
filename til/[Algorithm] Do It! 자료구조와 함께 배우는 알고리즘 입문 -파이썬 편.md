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

![](./images/IMG_9884.heic)

![](./images/IMG_9884.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=ce2ebd77584a1a7e4a74b78fbcaa089231e95684b240e50286f4bd1ed5a7a708&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9885.heic)

![](./images/IMG_9885.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=fa4c9bb0ea5d28f339fe362dc9b8807af0edd3269ef9b70c3ccee096cc0c09cb&X-Amz-SignedHeaders=host&x-id=GetObject)

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

# 퀵 정렬: 학습 종료

> 안 보고 구현한 다음, 재귀를 스택 형태로 바꾸는 연습을 반복해봅시다.

### 그림: 퀵 정렬의 예

![](./images/IMG_9899.heic)

![](./images/IMG_9899.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=4053637e94e8b7f88f9996cfd635edb9e3ee438a855212442f9708ee0e3cdbb0&X-Amz-SignedHeaders=host&x-id=GetObject)

## 개구코 1.

### 개념

재귀를 사용하지 않는 퀵정렬 구현은 pl, pr 포인터를 이용해야 한다. 아래는 이 아이디어만으로 직접 작성해본 퀵정렬 수도코드.

### 구현

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

### 코멘트

아무리 생각해도 제대로 된 인덱스 설정이 어렵다. 어떻게 하면 이 능력을 기를 수 있을까?

> 🔍 올바른 인덱스 설정 능력을 기르는 방법

위 내용에 따라 연습하면 되기도 하겠지만, 여기서 헤맸던 건 그냥 퀵 정렬의 포인터 이동을 제대로 이해하지 못했던 것 때문인거 같다.

→ 이 정렬의 스탭을 쉐도잉 해보자.

## 개구코 2

### 개념

피벗을 중심으로 배열을 두 부분으로 나누는 코드 작성해보기. 

![](./images/IMG_9908.heic)

![](./images/IMG_9908.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=c98f276b740acd2d6ab84b530a5656d6007d726b245751ff5ab8cf75c43122ab&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9909.heic)

![](./images/IMG_9909.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=368cbcd7a6bb651d7f7eaa0a467fd472cb49e67987c95d64f8786a0c39d9e768&X-Amz-SignedHeaders=host&x-id=GetObject)

위 그림을 그대로 해주면 될 거 같다.

### 구현

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

### 코멘트

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

## 개구코 3.

### 개념: 구현한 파티셔닝을 토대로 퀵 정렬 만들기

### 구현: 그냥 해 봅시다

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

### 코멘트

성공~ 퀵 정렬은 ‘파티셔닝’과정과 ‘정렬’ 과정을 차례로 구현하면 잘 되네요.


## 개구코 4. 비재귀적 퀵 정렬로 바꾸기

### 개념: 비재귀적인 퀵 정렬 만들기

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

![](./images/IMG_9910.heic)

![](./images/IMG_9910.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=cb5126ae8dc4d26b59dbbc66aa544afd308a9a95f3a2d64efac0380ded088b40&X-Amz-SignedHeaders=host&x-id=GetObject)

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

## 개구코 5. 퀵 정렬에서 피벗과 겹치는 부분.

### 개념

퀵 정렬에서 pl, pr을 계속 스캔하며 포인터를 옮겨주면 피벗과 일치하는 그룹이 생길 수 있다. 이때는 배열 나누기가 완료되어 pl > pr + 1일 때 뿐이다.

### 구현

그림 참조

![](./images/IMG_9927.heic)

![](./images/IMG_9927.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UR744HK%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDM5nAGlNkm5ATrnGHc0SJNPrx906lxRGMmsED1bZZMKgIhAOArLqsF6%2BGS%2BuhtMvh7ddQwC5fWCmyRVDzOWhO96cHWKv8DCGYQABoMNjM3NDIzMTgzODA1IgzEe9UcAiP5xFpqTAMq3AN%2BW%2B8%2B7lVtrcNaEJPq0XrSzDYhFd7bn%2BxCR7K7eq52SAT3RCG52%2Bk2L3DBOAzPUSAGaeP1ZkURqn6LW8WtQmBB1dAdfkJorWq1QgnQiSkkn6HL0H6EdugkjRA9mrik%2BGOHzDdx0HCZcDiwWqJ7phsoubb28QF9M1rPPLu3yAA9mUL6VlxMavXcVCj%2B2XJtBdv%2BrDaUKk3n5dJcP%2FND%2FjbIgyarB3KfeSrTLLmLD9yoQTG3BvFvFF5dITAbQhvKHe8xbCmezOgP2PIcLGT2sewGYSD9HFue1fEzOcPnD7g9jF6EShytNajT5Iqk%2B8tyYdJWK95EXs0bOarnu5uWzl2NwfaXPi%2FGenz%2FmeoV11Fw%2B6oW5JBpPYA59%2BuIOKPbHV7XuClAu%2B%2ByGxHKHxEjSMVrHhtBwbB2TGsn43FRiYa7ljbBFJH0i3Q2IKMGh6oHlJgCi3KqlBCCIU1td2JyKKRn6vo4fq67GsvOw6iYK3Afz%2BmwpTaP3q%2BClWvjZOLzjllTjzo%2FLUk3YkbKzlTIDLEeHVSdJ%2Bre%2BiuTeI7AicmdL0ejMk6CrB6rZyoE33d0IVmAQimR2hZ%2FgC2A1zqhz3A1DmJ2e79hPpTDms3t3DyQeUFS5PABD5CbHis1YTDSsee%2BBjqkAXMgVnZSicP930FErnMvcmWnGbeUxwV1BKV6Rok3wk69T%2F3Mn9EbmcVuJuWXIG%2FrTG6QJK4MIjXHNEXOb60AMtssrnR7zmV4EYPrYRizqPv4662hK%2FOSzvrGyYhXAyL6y6Wml2qI7wh%2FVTftEbE%2Byc1zYhS3ay1d9tw04NNKTKI92XF3bikQTAEu%2B4waaXv6jhl%2Fe6w0B3U685VDsoWcQZK8eBNg&X-Amz-Signature=762e171fe976978cafba4e9c828ee165a2e8da0e0b44b9f0a25798f065607c87&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코멘트

아마 피벗과 같은 값이 더 있어도, 피벗과 일치하는 그룹이라는 건 하나밖에 없을 거 같다. 그니까 이게 이렇게 표현하면 안 될 거 같은데. ‘그룹’이 아니라 그냥 피벗 값 하나만 들어올 수 있는 거 아닌가.

## 개구코 6. 퀵 정렬을 스택으로 구현할 때 적절한 크기

### 개념: 퀵 정렬 규칙에 의해 배열에서 원소 수가 n이면 스택에 쌓이는 데이터의 최대 개수는 log n보다 적다.

따라서 원소 수 n이 100만 개라도, 스태의 최대 크기는 20이면 충분하다

$log_2 1000000$

이를 계산하면,

$log_2 1000000 = \frac{\log_{10} 1000000}{\log_{10} 2}$

상용로그 값을 이용하면,

$\log_{10} 1000000 = 6$

$log_{10} 2 \approx 0.3010$

따라서,

$log_2 1000000 = \frac{6}{0.3010} \approx 19.9$

즉, 최대값은 약 19.9입니다.

### 구현

이건 어렵게 보면 어렵긴 한데, 그냥 트리로 그려보면 바로 이해 됨. 재귀 결정 트리에서 스택에 저장되어야 하는 값은 어차피 루트-리프까지의 한 경로밖에 없음. 다른 경로들은 형제 노드를 처리한 다음 처리하게 됨. 이전에 화이트보드에 그렸던 것을 참조

![](./images/70f72466-8719-4e8b-b781-3b6bb71da2d6.png)

![](./images/70f72466-8719-4e8b-b781-3b6bb71da2d6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VCMDYZZ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIGSmm6T014tu%2BGlGWbaXK%2BdTQkNq5dOfRmIhkS79PnDcAiEAjQCF7EpNZXGte6SMDgjM9BTYmviz6%2Bc3hiWeoCIDs6gq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHWcWgYXTDteQ1m7hSrcAz3L2kCMgjogta1uk8eWEMAXuXIRuwkm4pYIvOmuIH0ckmTuN3WAUL9YhJZk2bbb%2BGcG4FA8EjcfRkq3N%2F4JBtVy0rs6Qtr%2BvJsRuTzkNRGok8rpckIrm3r9Jn8Rp0EkuaKTH0GdJPbXokozEdpZQJ5%2Bsq3UdXxszQCm88O5JdRdHPUcIcr%2Fw7MgNXEM38YW2rMXTzCAfK%2FnRGULSt0%2FmOtuO1AZVsfjkYE0mRT1ull2iJDnb0AnC%2FMjcN6LCSMklq3Xs%2BO9aVCmZHioXDF9eah81xSAptnAzacUFkW%2Fd5kgHE4626ygc7oP0s1ZQEG%2FJF3PXrfKKQxT38GrUAfrA%2B0dn4OScYoCHpZQgXft5lh1cF7rcSpumBI0ysdUv98iI2MVXfNtKi1eYhe0eUbaUBZBPE1EwcZg31O%2F9pljrAqJXQBNYXDnVAsfQXNsm92Q5Pp00bHnPHAgfxHZ0nHgOkYvZj7zmh9pe2J4hT%2Fx9mvgIGphah1Mn%2Fdg7GqFIGmi%2FXkn2Duk1sKxruuEF8dq654NWNOT9MdHQGtKpYQA9vzSDFWJ8NzdFdWnIxLH9L8cMJyVL2xoje587Tn1OMNCAugkqQAh6IQeihgzkFMW24v3sZ5tFbDNP29w9TjiMOiw574GOqUBLnhg3AcbP1yhslv9tk1fSCv1s369WVEpEMU3ASkIl8Vmrv%2FSfu%2FUUP9M6xjkRzrwYxiZmVjWgL5YFuTJoU%2FnVF0wivXl5rbKzgO6M%2FaW%2BvXOIuVP2d2AdQfKYKICzwegBA0rzr3VIsynsp6lHCNbm%2FT92gKMkAtHdRZeqFKs9lVKJZaZjwn%2BH%2FJ%2B%2F6FS0t7vPyW4e0XXjpInUJuZZFIkDPs2PH0Y&X-Amz-Signature=41140831d48bc9cce562518bf9afb38c07ddfe9245fff255328b3155982168cc&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코멘트: 없음.

## 복습: 재귀를 스택으로

### 개념: 재귀를 스택으로 변경하는 Robust한 방법론

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

### 구현

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

### 코멘트

아 어려워. 왜 이 둘의 구현이 다른 거지? 정리한 다음 다시 구현. 아래와 같이 방법론을 수정하며 구현해 보았다.

```python
def recur(n: int) -> int:
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

# 1. 그대로 while 문에 넣는다.

from collections import deque

def recur2(n: int) -> int:
    s = deque()
    while True:
        if n > 0: 
            # 중요한 사실: n은 이미 업데이트 된 상태다.
            # recur(n-1) # 스택에 저장을 해줄 부분과 안 해줄 부분을 구별해야 함
            s.append(n) #n을 저장하고
            n = n - 1 # 네. 이렇게 해서 n이 0보다 크면 다 1씩 줄여서 처음으로 돌아가는 겁니다. 
            continue
        if s: # 이 부분은 n이 0 보다 작을때만 출력되지 않나? 
            n = s.pop() #그러니까 n이 충분히 작아졌으면 이제 저장됐던 n을 팝해서 프린트 해주고 
            #디크레멘트해서 다시 콜 해주는 겁니다. 만약에 n이 1보다 크면 알아서 조건문에 걸릴 거고요.
            print(n)
            # recur(n-2) # 
            n = n - 2
            continue
        break
recur(4)
print("="*8)
recur2(4)
```

이를 다시 robust 한 방법론으로 정리해보자.

1. 재귀를 스택으로 만드는 기본: 함수의 첫 머리에 while True: 문을 삽입. 
1. 꼬리재귀: 함수의 파라메터 값을 재귀와 동일한 방식으로 수정하여 continue
1. 중간재귀(함수의 주요 구현 윗 부분): 이 부분도 꼬리 재귀와 똑같이 파라메터를 업데이트하여 함수의 처음으로 플로우를 보내야 함. 
1. 3에서 주의할 점: 그대로 뒤로 보내면 5의 내용 때문에 파라메터값이 덮어씌워진다. 
1. 스택은 실행 부분을 포함한다: 스택은 함수의 주요 실행 부분을 포함한다. 기본적으로 실행할 타이밍의 데이터를 스택에서 꺼내 와야 하고, 그것으로 작업을 한 다음, 꼬리 재귀를 실시해준다. 그 다음 중간 재귀에 걸리고 말고는 알 바 아님.
제대로 이해한 거 맞나? 찝찝하지만 일단 또 넘어가자. 반복만이 답이다.

## 복습: 재귀적 퀵 정렬 구현하기

### Phase1. 단계 구별하기

1. 파티셔닝
1. quick_sort 함수 구현하기
### Phase2. 코딩하기

```python
def partitioning(A: list, left, right):
    if left >= right: # 만약 봐야 하는 파티션이 유효하지 않은 값(파티셔닝 할요소가 하나거나 없다면)이라면 패스
        return
    pivot = A[(left+right)//2]
    pl, pr = left, right
    while pl <= pr: # 파티션이 엇갈리지 않는 동안
        while A[pl] < pivot and pl < right: # 첫 번째 조건: 파티셔닝의 기본 원리. # 두 번째 조건: 영역 유지
            pl += 1
        while A[pr] > pivot and pr > left: 
            pr -= 1
        if pl <= pr: # 포인터 값이 유효하다면
            A[pl], A[pr] = A[pr], A[pl]
            pl += 1
            pr -= 1
    partitioning(A, left, pr)
    partitioning(A, pl, right)

def quick_sort(A):
    partitioning(A, 0, len(A)-1)
        
A = [4, 2, 5, 3, 243, 5534, 21, 3]
quick_sort(A)
print(A)
```

일단 단기기억 덕분인지는 모르겠으나, 정상적으로 작동하는 정렬 구현에 성공했다.

## 연습: 위에서 구현한 재귀적 정렬을 스택으로 구현하기

### Phase1. 구현 단계

자, robust한 재귀 제거 방법을 떠올려보자

1. 기본적으로 while True:로 코드를 감싸기
1. 꼬리 재귀: 그냥 업데이트 해서 밀어버리면 됨. 밀어버리기 전에 두 재귀 중간에 있는 코드를 실행해야 함.
1. 중간 재귀: 스택에 저장하고, 파라메터 업데이트해서 밀어야 함.
### Phase2. 구현

```python
from collections import deque

def partitioning(A: list, left, right):
    s = deque()
    while True:
        # if left >= right: # 만약 봐야 하는 파티션이 유효하지 않은 값(파티셔닝 할요소가 하나거나 없다면)이라면 패스
        #     return
        pivot = A[(left+right)//2]
        pl, pr = left, right
        while pl <= pr: # 파티션이 엇갈리지 않는 동안
            while A[pl] < pivot and pl < right: # 첫 번째 조건: 파티셔닝의 기본 원리. # 두 번째 조건: 영역 유지
                pl += 1
            while A[pr] > pivot and pr > left: 
                pr -= 1
            if pl <= pr: # 포인터 값이 유효하다면
                A[pl], A[pr] = A[pr], A[pl]
                pl += 1
                pr -= 1
        
        if left < right:
            # partitioning(A, left, pr)
            s.append((left, pr)) # 저장해주고
            left = left# 파라메터 업데이트 해 줍니다.
            right = pr
            continue
        if s:
            # partitioning(A, pl, right)
            pl, right = s.pop()
            left = pl
            right = right
            continue
        break

def quick_sort(A):
    partitioning(A, 0, len(A)-1)
        
A = [4, 2, 5, 3, 243, 5534, 21, 3]
quick_sort(A)
print(A)

################결과################
[2, 3, 3, 5, 243, 5534, 21, 4]

```

이거는 이슈로 넘겨서 해결해볼까.

# 이슈: 퀵 정렬 스택 표현 결과 뒷 부분 정렬 안 되는 문제.

## Phase1.

환경: 파이썬

로그(이상 결과)

```plain text
A = [4, 2, 5, 3, 243, 5534, 21, 3]
quick_sort(A)
print(A)

################결과################
[2, 3, 3, 5, 243, 5534, 21, 4]
```

최근 변경사항: 재귀로 표현된 퀵 정렬의 파티셔닝 과정을 스택으로 바꿈.

## Phase2-1

### 확인

문제는 당연히 스택에 있겠지? 앞 부분이 어느 정도 정렬되는 거 보면 완전 틀린 구현은 아닌 거 같은데, 어떤 걸 봐야할지 잘 모르겠음. 당연히 파티셔닝에 문제가 있을 거 같은데.

```plain text
        if left < right:
            # partitioning(A, left, pr)
            s.append((left, pr)) # 저장해주고
            left = left# 파라메터 업데이트 해 줍니다.
            right = pr
            continue
```

파티션 뒷 부분을 스택에 저장해줘야 되나? 앞 부분은 어차피 다음 루프에서 보게 되잖아. 

### 시도

```python
from collections import deque

def partitioning(A: list, left, right):
    s = deque()
    while True:
        # if left >= right: # 만약 봐야 하는 파티션이 유효하지 않은 값(파티셔닝 할요소가 하나거나 없다면)이라면 패스
        #     return
        pivot = A[(left+right)//2]
        pl, pr = left, right
        while pl <= pr: # 파티션이 엇갈리지 않는 동안
            while A[pl] < pivot and pl < right: # 첫 번째 조건: 파티셔닝의 기본 원리. # 두 번째 조건: 영역 유지
                pl += 1
            while A[pr] > pivot and pr > left: 
                pr -= 1
            if pl <= pr: # 포인터 값이 유효하다면
                A[pl], A[pr] = A[pr], A[pl]
                pl += 1
                pr -= 1
        
        if left < right:
            # partitioning(A, left, pr)
            s.append((pl, right)) # 저장해주고
            left = left# 파라메터 업데이트 해 줍니다.
            right = pr
            continue
        if s:
            # partitioning(A, pl, right)
            left, right = s.pop()
            # left = pl
            # right = right
            continue
        break

def quick_sort(A):
    partitioning(A, 0, len(A)-1)
        
A = [4, 2, 5, 3, 243, 5534, 21, 3]
quick_sort(A)
print(A)
```

### 결과분석: 성공!!

스택에 저장하지 않으면 다음 루프에서 소실될 정보가 무엇인지 생각하니 해결됐다! 이 경우, (pl, right), 즉 파티션의 뒷 부분을 스택에 저장하고, 파티션의 앞 부분을 left, right 매개변수에 전달해주면 된다. 

그럼 여기서 응용해서, 파티션의 뒷 부분부터 정렬할 수도 있을 거 같긴 하다.

```python
	
if left < right:
	s.append((left, pr))
	left, right = pl,right
	continue
```

이렇게 해도 정확히 똑같이 작동한다! 이렇게 하면 파티션의 뒷 부분부터 정렬하게 된다. (정렬 작업 순서가 바뀌는 것이지, 정렬 순서가 바뀌는 것은 아님)

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

### 결과 분석: 다른 에러 발생

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

![](./images/IMG_9897.heic)

![](./images/IMG_9897.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=09ced2aa1401435454a2bdef18e4eb449a2c212b0c2340a0d76fe64202405046&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9898.heic)

![](./images/IMG_9898.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=4d2b914818a7b050617850ca243f88c920bfbd1d7058add803c198f326aee1a4&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 병합정렬

```python
from typing import MutableSequence

def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합정렬"""
        if left < right: # 파티션이 유효한 동안 
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합정렬
            p = j = 0
            i = k = left

            while i <= center: # 복사
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p: # 병합
                if buff[i] <= a[i]
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            
            while j < p: # 떨이
                a[k] = buff[j]
                k += 1
                j += 1
    n = len(a)
    buff = [None] * n # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1) # 배열 전체를 병합 정렬.
    del buff

```

## 구현: 병합정렬

### Phase1. 병합 정렬의 최소 요구 파악

배열을 이해할 때는 수도코드를 이해하는 것보다, 정렬의 메커니즘을 코드와 연결시켜서 1차적인 암기와 개념화 작업을 동시에 해야 한다.

1. 일단 이것도 파티션이 있다. 파티션을 잡고, 파티션이 유효할 때만 정렬 프로세스를 실행한다
1. 센터를 잡는다
1. 앞 파티션을 병합정렬 한다
1. 뒤 파티션을 병합정렬 한다.
1. 네 개 포인터를 초기화 한다. 어떤 기준으로 초기화하는 건지는 잘 모르겠다.
1. 앞 파티션을 이터레이션 하면서(i ≤ center)
1. 버퍼에다가 배열 값을 저장한다. 왜? 버퍼에 앞 부분을 따로 저장해놔야, 작은 파티션을 새로 덮어 씌워도 데이터가 안 날아가니까. 즉 이 과정은 not in place 한 병합 정렬이 필연적으로 해야 하는 백업이다.
1. 아직 이해가 안 되는 조건이 유효한 동안(i ≤ right and j > p)
1. buff[i] = 앞 파티션의 값과, a[i] =  뒤 파티션의 값을 비교해서
1. 작은 쪽을 a[k](정렬 포인터)에 집어 넣어준다. 
1. p, j, i, k 포인터가 너무 많아서 헷갈린다.
1. 비교해서 집어넣어준 후에, while j < p 인 동안 a[k] = buff[j], k += 1, j += 1을 하며 a[k]에 버퍼 값을 저장해준다. 이건 떨이 데이터를 저장하는 과정으로 보인다.
### 중요: p, j, i, k의 의미를 이해할 필요가 있다. 

> 병합 과정을 그림으로 그려 보면서 이해.

그림: 병합 정렬의 전체적인 흐름

![](./images/IMG_9913.heic)

![](./images/IMG_9913.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=844c32e5097a1ec0920bb66d270204bfce4e396c1ffa512939c32ba386ab9528&X-Amz-SignedHeaders=host&x-id=GetObject)

그림: 배열 a의 앞 부분을 배열 buff로 복사.

![](./images/IMG_9914.heic)

![](./images/IMG_9914.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=bd867e6ddd3645489852cd97ff7806bab2b082a27e571b28bf9286344c393ccb&X-Amz-SignedHeaders=host&x-id=GetObject)

```python
while i <= center: # i는 처음에 left(파티션의 첫 값)으로, p는 0으로(buff의 첫 값으로) 초기화.
	buff[p] = a[i] # 이 루프가 끝나고 나면 p는 버퍼의 center+1 인덱스를 가리키게 됨.
	p += 1
	i += 1
```

그림: 배열 a의 뒷 부분과 배열 buff를 a에 병합

![](./images/IMG_9914_2.heic)

![](./images/IMG_9914_2.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=50697b61ad907e7545512d4d10a6c874ac278a04faef3a6c9550aca596c493e4&X-Amz-SignedHeaders=host&x-id=GetObject)

```python
# 첫 번째 조건: a의 파티션을 가리키는 i가 유효한 동안, j < p는 버퍼에서 포인터가 center 앞에 있는 동안.
while i <= right and j < p: 
	if buff[j]<= a[i]: # 알잘딱깔센으로 병합. a[k]는 그냥 포인터. 어떤 방식으로 병합됐든 k++
		a[k] = buff[j]
		j += 1
	else:
		a[k] = a[i]
		i += 1
	k += 1
```

그림: 배열 buff의 나머지 원소를 배열 a에 복사합니다.

![](./images/IMG_9915.heic)

![](./images/IMG_9915.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QYYSDKR%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDgL%2FxXawN8yEQoDE3aTJ%2B9%2B5wZ24E8%2FY9Jpvys80D3zgIgd0nloIhsKWhoPPRdZEsVq0H6Z%2FN6G%2Fai9rCc0wINbyUq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDMJKaTrXvaSt28fgvyrcA1EdOR47N1xeEO91XZo3shrr5gM%2BKyjIf8atHtJuprznUf%2Bq6fPFPo0vlF9NXvixE5ot%2F3azcl7UcpAtYM4BLyxEZguPkv3YIIS5iIV7OgFQawcD1TIoYwuRYUqSMkC3K%2BHTWDRpovF7mAKY1BVSECV%2BxUQuuLcptoXQdJ1g4MDXIl2EIZARKHvUafTIZ2EqahcC98ZkVb%2BY8zE2K1PJFoXLH54oP7bRrZ2xNckEV8h2KH6wZHE0jOH2kzEr13uhCvpcnXkoJa6WU2SLPLgqq0lks6HmrxhdoK8%2B5N1o0F%2BtIfinS4xKZFpDB%2BBxrbS1fkJQYAGJw%2FKl3fhQ%2FryFbsunHs2tayrek6oAik3Se8cq6vt3EU2CHNUBxG4kvuqnVTTHMT%2BkaAdjIkfnjHNjSGTxSuh0belRZtxUd1hXEuzAL%2Bp9GqKnuyuwsii5cmb3DW%2FCtrdpFScjVUu5Gr4LutH7KyDtpdXdsbxD33Zr3hA3qWecEH9An6nGue8qHcFZVy%2BYicLPdLJ0h09%2BrUK1gRhBiIxev9aGJCb41YeIYcP%2FTNJBugAyGsIZv9Mfmg9vG3eEJwSxJ0xPTISCj4FCZ0PoDOIdje24dtUYOBxnx61Q89iJ5aDmRidKFFGQMOaw574GOqUBTWm1OknOmEeZW0aPgtFVhuwM%2FOjw9uujAOs%2Fo968wCcsFJSZBRu%2FPG4kfQjVhXq0yjKHoOyKH2ZQ1iTsOExxad0SeaHByOSd5r0wOkQy9EjVBE9jDAj%2BfBmOlm9b69eY17kTPJAFkteZOKJ4lQP75fG4MUYoeBVihpLSKZnCA%2F%2FiVXVASvsHpA0ueRq%2By7xeSBMl2h7%2BNSB8Tw7O4WnRiSTzleHQ&X-Amz-Signature=41d0cb94ad569b49fc50b0b07a9c4df4c4cc1f51c90b756f2915ed66d73c228c&X-Amz-SignedHeaders=host&x-id=GetObject)

```python
while j < p: # 궁금한 점. a의 나머지 원소는 왜 a의 적절한 위치로 복사하지 않아도 되는 거지?
	a[k] = buff[j]
	k += 1
	j += 1
```

궁금한 점: buff의 나머지 원소를 a로 복사하는 과정은 있는데, 왜 a의 나머지 뒷부분 파티션을 복사하는 과정은 없어?

> ✅ 오른쪽 부분 배열을 복사하는 과정이 필요 없는 이유

### Phase2. 직접 구현해보기

구현요소 정리

1. 파티션 유효성 검사
1. 앞 파티션 재귀
1. 뒤 파티션 재귀
1. 버퍼에 복사
1. 병합
1. 떨이 처리
완성 코드

```python
def partitioning(A: list, left, right):
    # 파티션 유효성 검사
    if left <= right:
        partitioning(A, left, (left+right)//2-1)
        partitioning(A, (left+right)//2, right)
        # 인덱스 설정
        p, k, i, j = 0, 0, 0, 0 # 헷갈리는 것들
        p = 0
        i = left
        j = 0
        center = (left+right)//2
        # 배열의 앞 부분을 버퍼에복사 
        while i < center: 
            buff[p] = A[i] # p는 버퍼의 시작 지점(0), i는 파티션의 시작지점 = left
            p += 1
            i += 1
        # 버퍼와 파티션을 병합
        # k는 버퍼의 두 번째 포인터?
        # j는 배열의 정렬용 포인터
        while k < p:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
            else:
                A[j] = A[i]
            j += 1
            i += 1
            k += 1
        # 버퍼 떨이 처리
        while k < p:
            A[j] = buff[k]
            k += 1



A = [34, 4, 5, 2, 5, 1]
buff = [None for _ in range(len(A))]
partitioning(A, 0, len(A)-1)
print(A)
```

최대 재귀 에러 발생. 이슈로 넘겨서 해결

## 구현: 병합정렬, 복기해보기

### Phase1. 병합정렬 요구사항 정리

1. 파티션이 유효한 동안 루프
1. 앞 부분, 뒷 부분 재귀
1. 포인터 적절히 초기화
1. 버퍼에 앞 부분 복사
1. 버퍼와 뒷 부분 병합
1. 버퍼 떨이 처리.
center 인덱스에 유의할 것

### Phase2. 코드 구현

```python
# ### Phase1. 병합정렬 요구사항 정리

# 1. 파티션이 유효한 동안 루프
# 2. 앞 부분, 뒷 부분 재귀
# 3. 포인터 적절히 초기화
# 4. 버퍼에 앞 부분 복사
# 5. 버퍼와 뒷 부분 병합
# 6. 버퍼 떨이 처리.

# center 인덱스에 유의할 것

def merge_sort(A: list, left, right):
    if left < right:
        center = (left+right)//2
        merge_sort(A, left, center)
        merge_sort(A, center+1, right)

        # set pointers
        sorting_idx = left
        a_pointer = left
        b_pointer1 = 0
        b_pointer2 = 0

        # copy to buffer
        while a_pointer <= center:
            buff[b_pointer1] = A[a_pointer]
            b_pointer1 += 1
            a_pointer += 1

        # merge two array A
        while b_pointer2 < b_pointer1 and a_pointer <= right:
            # compare
            if buff[b_pointer2] < A[a_pointer]:
                A[sorting_idx] = buff[b_pointer2]
                b_pointer2 += 1
            else:
                A[sorting_idx] = A[a_pointer]
                a_pointer += 1
            sorting_idx += 1

        # 떨이 처리
        while b_pointer2 < b_pointer1:
            A[sorting_idx] = buff[b_pointer2]
            sorting_idx += 1
            b_pointer2 += 1 


arr = [4, 4, 2, 5, 4342, -324, 5324]
buff = [None for _ in range(len(arr))]

merge_sort(arr, 0, len(arr)-1)
print(arr)
```

구현 성공!

## 병합 정렬 스택으로 표현하기

### Phase1. Robust하게 스택으로 바꾸는 방법

1. 루프 씌우기
1. 꼬리재귀 처리하기
1. 중간 재귀 처리하기
### Phase2. 코드로 구현해보기

```python
# ### Phase1. 병합정렬 요구사항 정리

# 1. 파티션이 유효한 동안 루프
# 2. 앞 부분, 뒷 부분 재귀
# 3. 포인터 적절히 초기화
# 4. 버퍼에 앞 부분 복사
# 5. 버퍼와 뒷 부분 병합
# 6. 버퍼 떨이 처리.

# center 인덱스에 유의할 것

from collections import deque

def merge_sort(A: list, left, right):
    s = deque()
    s.append((left,right)) # 초기 스택을 입력 해 줌.
    while True:
        if left < right:
            center = (left+right)//2
            # merge_sort(A, left, center) # 이 코드가 먼저 실행돼야 하긴 함.
            s.append((center+1, right)) # 두 번째 파티션을 미리 저장하고, 나중에 다람쥐가 저장해둔 도토리를 꺼내 까먹듯 pop해서 매개변수 설정하면 됨.
						# 매개변수를 중간 재귀 함수와 동일하게 설정하고 병합 정렬 구현부로 넘어간다.
            left = left
            right = center
        elif s: # 이 코드의 경우 continue문으로 앞으로 갈 수 없기 때문에 그냥 if를 쓰면 중간재귀로 맞춰 파라메터를 설정하고도 여기서 다음 스택을 까먹게 된다. 따라서 없어진 continue문에 대한 trade-off로 else 조건이 붙은 것으로 생각하면 된다.
            # merge_sort(A, center+1, right)
            left, right = s.pop()
            # continue를 넣으면 안 된다: 원래 코드가 매개변수를 업데이트하고 처음으로 가는게 아니라, 함수의 뒷 부분으로 가야 해서.
        # set pointers
        center = (left+right)//2
        sorting_idx = left
        a_pointer = left
        b_pointer1 = 0
        b_pointer2 = 0

        # copy to buffer
        while a_pointer <= center:
            buff[b_pointer1] = A[a_pointer]
            b_pointer1 += 1
            a_pointer += 1

        # merge two array A
        while b_pointer2 < b_pointer1 and a_pointer <= right:
            # compare
            if buff[b_pointer2] < A[a_pointer]:
                A[sorting_idx] = buff[b_pointer2]
                b_pointer2 += 1
            else:
                A[sorting_idx] = A[a_pointer]
                a_pointer += 1
            sorting_idx += 1

        # 떨이 처리
        while b_pointer2 < b_pointer1:
            A[sorting_idx] = buff[b_pointer2]
            sorting_idx += 1
            b_pointer2 += 1 
				# 종료조건이 이것 말고는 잘 모르겠음. 
        if not s:
            break



arr = [4, 4, 2, 5, 4342, -324, 5324]
buff = [None for _ in range(len(arr))]

merge_sort(arr, 0, len(arr)-1)
print(arr)
```

전반적으로 잘 구현된 줄 알았으나 아래와 같은 테스트케이스 오류를 발견했다.

```python
[-324, 2, 4, 4, 5, 24, 123, 234, 234, 243, 2435, 132, 243, 435, 3452, 4342, 5324]
```

이거 딱 봐도 마지막 단계에 병합이 안 된 거 같다. 이슈로 넘겨서 처리.

## 개구코: sorted() 함수로 병합정렬하기

### 개념: 파이썬에서 제공하는 sorted함수로 병합 정렬을 할 수 있다.

### 구현

```python
c = list(sorted(a + b))이 
```

이 방법은 a와 b가 정렬을 마친 상태가 아니어도 적용할 수 있다는 장점이 있지만, 속도가 빠르지 않다는 단점도 있습니다. 빠르게 병합하려면 다음과 같이 heapq 모듈의 merge() 함수를 사용하면 됩니다.

```python
import heapq

a = [2, 4, 6, 8, 11, 13]
b = [1, 2, 3, 4, 9, 16, 21]
c = list(heapq.merge(a, b))
```

### 코멘트

기본 정렬 메서드로 병합정렬을 할 수 있다는 걸 처음 알아서 신박했다.

# 이슈: 병합 정렬 구현 중 재귀 에러 발생

## Phase1.

### 환경: 파이썬

### 로그: maximum recursion depth exceed

### 최근 변경 사항: 병합 정렬 구현

## Phase2-1

### 확인

당연히 아래 부분에 문제가 있을 것임.

```python
    if left <= right:
        partitioning(A, left, (left+right)//2-1)
        partitioning(A, (left+right)//2, right)
```

두 번째 재귀에서 left, right가 0이면 계속 0, 0으로 재귀 되는게 문제임. left < right로 조건을 바꿔야할 거 같은데

### 시도

실패. 여전히 left, right가 2, 3인 상태에서 partitioning(A, 2, 3)이 무한히 호출됨.

```python
    if left < right:
        partitioning(A, left, (left+right)//2-1)
        partitioning(A, (left+right)//2, right)
```

### 결과 분석

정답 코드 참조.

```python
        if left < right: # 파티션이 유효한 동안 
            center = (left + right) // 2

            _merge_sort(a, left, center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right) # 배열 뒷부분을 병합정렬
```

아니 이게 내 시도랑 뭐가 다른거지? 

> 🔍 문제 분석: maximum recursion depth exceeded (재귀 깊이 초과 오류)

# 이슈: 병합 정렬 결과 이상

## Phase1.

### 환경: 파이썬

### 로그: 정렬 결과 이상

[4, 6, 6, 5, 2, 34, 534, -123]

### 최근 변경 사항: 아래 코드 작성

```python
def partitioning(A: list, left, right):
    # 파티션 유효성 검사
    if left < right:
        partitioning(A, left, (left+right)//2)
        partitioning(A, (left+right)//2+1, right)
        # 인덱스 설정
        p, k, i, j = 0, 0, 0, 0 # 헷갈리는 것들
        p = 0
        i = left
        j = 0
        center = (left+right)//2
        
        # 배열의 앞 부분을 버퍼에복사 
        while i < center: 
            buff[p] = A[i] # p는 버퍼의 시작 지점(0), i는 파티션의 시작지점 = left
            p += 1
            i += 1
        
        # 버퍼와 파티션을 병합
        # k는 버퍼의 두 번째 포인터?
        # j는 배열의 정렬용 포인터
        while k < p:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
                k += 1 # 버퍼 포인터 늘리고
                j += 1 #  정렬용포인터 늘리고
            else:
                A[j] = A[i]
                i += 1 # 배열의 뒷 부분 포인터 늘리고
                j += 1 # 정렬용 포인터 늘리고
        # 버퍼 떨이 처리
        while k < p:
            A[j] = buff[k]
            k += 1



A = [34, 4, 5, 2, 4, 6, 534, -123]
buff = [None for _ in range(len(A))]
partitioning(A, 0, len(A)-1)
print(A)
```

## Phase2-1. 성공!

### 확인

각 과정을 나눠서 로그를 찍어보기.

1. 버퍼에 저장하는 과정은 잘 이루어지는가? 그래 보인다.
```plain text
copy to buffer [] from [34, 4, 5, 2, 4, 6, 534, -123]
copy complete. buff: [None, None, None, None, None, None, None, None]
copy to buffer [] from [34, 4, 5, 2, 4, 6, 534, -123]
copy complete. buff: [None, None, None, None, None, None, None, None]
copy to buffer [34] from [34, 4, 5, 2, 4, 6, 534, -123]
copy complete. buff: [34, None, None, None, None, None, None, None]
copy to buffer [] from [4, 5, 2, 4, 6, 34, 534, -123]
copy complete. buff: [34, None, None, None, None, None, None, None]
copy to buffer [] from [4, 5, 2, 4, 6, 34, 534, -123]
copy complete. buff: [34, None, None, None, None, None, None, None]
copy to buffer [6] from [4, 5, 2, 4, 6, 34, 534, -123]
copy complete. buff: [6, None, None, None, None, None, None, None]
copy to buffer [6, 5, 2] from [6, 5, 2, 4, 6, 34, 534, -123]
copy complete. buff: [6, 5, 2, None, None, None, None, None]
```

1. 병합 과정은 잘 이루어지는가? 못 그래 보인다. 다시 그림을 참조해보자.
```python
        
        print(f'merge {A[left:center+1]} with {A[center+1:right+1]}')
        while k < p:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
                k += 1 # 버퍼 포인터 늘리고
            else:
                A[j] = A[i]
                i += 1 # 배열의 뒷 부분 포인터 늘리고
            j += 1 # 정렬용 포인터 늘리고
        print(f'merge complete {A[left:right+1]}')
        
####################################
merge [34] with [4]
merge complete [34, 4]
merge [5] with [2]
merge complete [5, 2]
merge [34, 4] with [5, 2]
merge complete [4, 5, 2, 4]
merge [6] with [34]
merge complete [6, 34]
merge [534] with [-123]
merge complete [534, -123]
merge [6, 34] with [534, -123]
merge complete [6, 34, 534, -123]
merge [4, 5, 2, 4] with [6, 34, 534, -123]
merge complete [4, 4, 5, 2, 6, 34, 534, -12]
[4, 6, 6, 5, 2, 34, 534, -123]
```

![](./images/IMG_9914_2.heic)

![](./images/IMG_9914_2.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=ca1f2a6f223fdd16ea8dedc5a36aebd9f981e1b677ca8b521522a6c950c30381&X-Amz-SignedHeaders=host&x-id=GetObject)

그림을 보면 포인터 의미를 더 잘 정리할 수 있긴 하다.

- a의 뒷 파티션을 가리키는 포인터 = i
- a정렬할 때 값을 삽입할 위치를 가리키는 포인터 = j
- 버퍼(a의 앞 파티션)을 가리키는 포인터. = k
### 시도

```javascript
    
        print(f'merge {A[left:center]} with {A[center+1:right+1]}')
        while k < p:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
                k += 1 # 버퍼 포인터 늘리고
            else:
                A[j] = A[i]
                i += 1 # 배열의 뒷 부분 포인터 늘리고
            j += 1 # 정렬용 포인터 늘리고
        print(f'merge complete {A[left:right+1]}')
```

이렇게 수정을 해주니 어느정도 정렬이 일어나고 있다. 그런데 i인덱스가 A의 범위를 초과하게 된다.

```python
  p = k = 0
        j = i = left
        center = (left+right)//2
        
        print(f'copy to buffer {A[left:center]} from {A}')
        print(f'{i} <= {center} ?')
        while i <= center: 
            buff[p] = A[i]
            p += 1
            i += 1
        print(f'copy complete. buff: {buff}')
        
        print(f'merge {A[left:center+1]} with {A[center+1:right+1]}')
        print(f'{k} < {p} ?')
        while k < p:
            print(f'comparing {buff[k]} v {A[i]}')
            if buff[k] < A[i]: # A[i] 인덱스 초과 발생!!!
                A[j] = buff[k]
                k += 1 
            else:
                A[j] = A[i]
                i += 1 
            j += 1 
        print(f'merge complete {A[left:right+1]}')
        
################################################################
copy to buffer [] from [34, 4, 5, 2, 4, 6, 534, -123]
0 <= 0 ?
copy complete. buff: [34, None, None, None, None, None, None, None]
merge [34] with [4]
0 < 1 ?
comparing 34 v 4 #여기서 문제가 발생하는데, 
comparing 34 v 5 #버퍼에 있는 내용을 4하고만 비교해야하는데 
comparing 34 v 2 # 자신보다 큰 A의 모든 값을 만날때까지 비교를 한다.
comparing 34 v 4
comparing 34 v 6
comparing 34 v 534
merge complete [4, 5]
copy to buffer [] from [4, 5, 2, 4, 6, 34, 534, -123]
2 <= 2 ?
copy complete. buff: [2, None, None, None, None, None, None, None]
merge [2] with [4]
0 < 1 ?
comparing 2 v 4
merge complete [2, 4]
copy to buffer [4] from [4, 5, 2, 4, 6, 34, 534, -123]
0 <= 1 ?
copy complete. buff: [4, 5, None, None, None, None, None, None]
merge [4, 5] with [2, 4]
0 < 2 ?
comparing 4 v 2
comparing 4 v 4
comparing 4 v 6
comparing 5 v 6
merge complete [2, 4, 4, 5]
copy to buffer [] from [2, 4, 4, 5, 6, 34, 534, -123]
4 <= 4 ?
copy complete. buff: [6, 5, None, None, None, None, None, None]
merge [6] with [34]
0 < 1 ?
comparing 6 v 34
merge complete [6, 34]
copy to buffer [] from [2, 4, 4, 5, 6, 34, 534, -123]
6 <= 6 ?
copy complete. buff: [534, 5, None, None, None, None, None, None]
merge [534] with [-123]
0 < 1 ?
comparing 534 v -123
```

루프 조건을 아래와 같이 추가해주니 해결!

```python
        while k < p and i <= right:

```

### 결과분석: 수정한 것들

1. while 루프 조건에서 A배열의 포인터가 파티션을 넘어가지 않도록 제한
1. 버퍼에 앞 파티션을 복사할 때도 center까지 복사하도록 수정. 앞 파티션은 left~center로 정의되고, 뒤 파티션은 center+1 ~ right로 정의된다.
1. 각 정의에 알맞게 포인터 초기화
최종코드

```python
def partitioning(A: list, left, right):
    # 파티션 유효성 검사
    if left < right:
        partitioning(A, left, (left+right)//2)
        partitioning(A, (left+right)//2+1, right)
        # 인덱스 설정
        p = k = 0
        i = j = left
        center = (left+right)//2
        
        # 배열의 앞 부분을 버퍼에복사 
        while i <= center: 
            buff[p] = A[i] # p는 버퍼의 시작 지점(0), i는 파티션의 시작지점 = left
            p += 1
            i += 1
        
        # 버퍼와 파티션을 병합
        # k는 버퍼의 두 번째 포인터?
        # j는 배열의 정렬용 포인터
        while k < p and i <= right:
            if buff[k] < A[i]: # 버퍼에 있는 친구가 작으면
                A[j] = buff[k]
                k += 1 # 버퍼 포인터 늘리고
            else:
                A[j] = A[i]
                i += 1 # 배열의 뒷 부분 포인터 늘리고
            j += 1 # 정렬용 포인터 늘리고
        # 버퍼 떨이 처리
        while k < p:
            A[j] = buff[k]
            k += 1



A = [34, 4, 5, 2, 4, 6, 534, -123]
buff = [None for _ in range(len(A))]
partitioning(A, 0, len(A)-1)
print(A)
```

# 이슈: 병합정렬 스택 표현 중 병합이 제대로 이루어지지 않는 문제

## Phase1.

환경: 파이썬

로그: 

```python
[-324, 2, 4, 4, 5, 24, 123, 234, 234, 243, 2435, 132, 243, 435, 3452, 4342, 5324]
```

최근 변경 사항:

```python

from collections import deque

def merge_sort(A: list, left, right):
    s = deque()
    s.append((left,right))
    while True:
        if left < right:
            center = (left+right)//2
            # merge_sort(A, left, center) # 이 코드가 먼저 실행돼야 하긴 함.
            s.append((center+1, right)) # 두 번째 파티션을 집어넣고 후반의 코드를 실행
            # 바닥 조건을 쳤다면 저장해 둔 거 꺼내서 다람쥐가 도토리 까먹듯 하면 됨
            left = left
            right = center
        elif s:
            # merge_sort(A, center+1, right)
            left, right = s.pop()
            # continue를 넣으면 안 된다: 원래 코드가 매개변수를 업데이트하고 처음으로 가는게 아니라서.
        # set pointers
        center = (left+right)//2
        sorting_idx = left
        a_pointer = left
        b_pointer1 = 0
        b_pointer2 = 0

        # copy to buffer
        while a_pointer <= center:
            buff[b_pointer1] = A[a_pointer]
            b_pointer1 += 1
            a_pointer += 1

        # merge two array A
        while b_pointer2 < b_pointer1 and a_pointer <= right:
            # compare
            if buff[b_pointer2] < A[a_pointer]:
                A[sorting_idx] = buff[b_pointer2]
                b_pointer2 += 1
            else:
                A[sorting_idx] = A[a_pointer]
                a_pointer += 1
            sorting_idx += 1

        # 떨이 처리
        while b_pointer2 < b_pointer1:
            A[sorting_idx] = buff[b_pointer2]
            sorting_idx += 1
            b_pointer2 += 1 

        if not s:
            break



arr = [4, 4, 2, 5, 4342, -324, 5324, 24, 234, 234, 2435, 123,243, 3452, 435, 132, 243]
buff = [None for _ in range(len(arr))]

merge_sort(arr, 0, len(arr)-1)
print(arr)
```

## Phase2-1

### 확인

루프 바로 밑에 조건이 무조건 잘못된 거 같다. left, right 값을 갱신해준 다음 베이스 컨디션을 보게 해야하지 않나? 아니다. 

정렬 과정을 수행하기 전에 문제가 있으면 continue시켜야 하지 않나? 

if not (left < right): continue

이거 있어야 하지 않나? 추가해도 의미 없음.

전혀 모르겠네. 10분만 더 고민.

종료 조건이 좀 문제인 거 같기도 하고. 아닌데, 문제 없는 거 같은데.

마지막 병합이 안 일어나는게 아니라, 중간 병합이 문제인가. 로그를 다 찍어봐? 아이구…

```python
merging [4, 4, 2, 5, 4342] [-324, 5324, 24, 234]
merge complete [-324, 4, 4, 2, 5, 4342, 5324, 24, 234]
merging [-324, 4, 4] [2, 5]
merge complete [-324, 2, 4, 4, 5]
merging [-324, 2] [4]
merge complete [-324, 2, 4]
merging [-324] [2]
merge complete [-324, 2]
merging [-324] []
merge complete [-324]
merging [2] []
merge complete [2]
merging [4] []
merge complete [4]
merging [4] [5]
merge complete [4, 5]
merging [4] []
merge complete [4]
merging [5] []
merge complete [5]
merging [4342, 5324] [24, 234]
merge complete [24, 234, 24, 234]
merging [24] [234]
merge complete [24, 234]
merging [24] []
merge complete [24]
merging [234] []
merge complete [234]
merging [4342] [5324]
merge complete [4342, 5324]
merging [4342] []
merge complete [4342]
merging [5324] []
merge complete [5324]
merging [234, 2435, 123, 243] [3452, 435, 132, 243]
merge complete [234, 2435, 123, 243, 3452, 435, 132, 243]
merging [234, 2435] [123, 243]
merge complete [123, 234, 243, 243]
merging [123] [234]
merge complete [123, 234]
merging [123] []
merge complete [123]
merging [234] []
merge complete [234]
merging [243] [2435]
merge complete [243, 2435]
merging [243] []
merge complete [243]
merging [2435] []
merge complete [2435]
merging [3452, 435] [132, 243]
merge complete [132, 243, 132, 243]
merging [132] [243]
merge complete [132, 243]
merging [132] []
merge complete [132]
merging [243] []
merge complete [243]
merging [3452] [435]
merge complete [435, 435]
merging [435] []
merge complete [435]
merging [3452] []
merge complete [3452]
merging [-324, 2, 4, 4, 5, 24, 234, 4342, 5324] [123, 234, 243, 2435, 132, 243, 435, 3452]
merge complete [-324, 2, 4, 4, 5, 24, 123, 234, 234, 243, 2435, 132, 243, 435, 3452, 435, 3452]
[-324, 2, 4, 4, 5, 24, 123, 234, 234, 243, 2435, 132, 243, 435, 3452, 4342, 5324]
```

병합 순서가 아주 이상하다. 문제를 알겠다. 원래 작은 부분부터 병합해야 하는데, 전체 배열의 절반 영역부터 병합하는게 문제다.

> 현재 병합 정렬 코드의 가장 큰 문제점은 스택을 활용하여 병합정렬을 반복적으로 구현할 때 올바른 병합 순서를 유지하지 못하는 것입니다. 특히, 배열의 병합 순서가 큰 구간부터 작은 구간 순서로 거꾸로 진행되는 것이 문제입니다.

이거 어렵네…핵심은 merged라는 플래그를 파티션과 함께 주어서 해결하는 것임. not merged인 파티션을 꺼냈을 때만 병합을 시작? merged가 True면 아무 작업 안 하는게 중요함. 아…어려워.

### 시도 

실패. 뇌 과부화.

### 결과분석: 실패

실패

# 힙 정렬

## 기본 개념

### 그림: 힙

![](./images/IMG_9890.heic)

![](./images/IMG_9890.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=8533c52e5be357b722d79aba79e5046ceac7cda925241ed8d506712959f74457&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 루트노드 삭제하고 힙 업데이트 하는 과정

![](./images/IMG_9891.heic)

![](./images/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=93005803f5d03965c0050f151bb43a573c17d585a0342fe245a74ae3224c699c&X-Amz-SignedHeaders=host&x-id=GetObject)

큰 값을 가진 자식과 위치를 교환. (이하 생략)

### 순서: 힙 정렬 알고리즘

1. 힙의 루트 a[0]에 위치한 최댓값 10을 꺼내 배열의 맨 끝 원소인 a[9]와 교환합니다.
1. 최댓값을 a[9]로 이동하면 a[9]는 정렬을 마칩니다. 앞에서 살펴본 순서대로 a[0] ~ a[8]의 원소를 힙으로 만듭니다. 그 결과 두 번째로 큰 값인  9가 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값 9를 꺼내 아직 정렬하지 않은 부분의 맨 끝 원소인 a[8]과 교환합니다.
1. 두 번째로 큰 값을 a[8]로 이동한 결과 a[8]~a[9]가 정렬을 마칩니다. 앞의 단계와 마찬가지로 a[0]~a[7]의 원소를 힙으로 만듭니다. 그 결과 세 번째로 큰 값인 8이 루트에 위치합니다. 힙의 루트 a[0]에 위치한 최댓값을 꺼내 아직 정렬하지 않은 맨 끝 원소인 a[7]과 교환합니다.
1. 이 과정을 반복하면 배열의 맨 끝에 최댓값부터 순서대로 하나씩 저장됩니다.
### 그림: 힙 정렬 과정

![](./images/IMG_9892.heic)

![](./images/IMG_9892.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=08ddcd97ef15b9369ac2c4729b88b619fc6b20c2792ffde0a3f91ada050d0fa2&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9893.heic)

![](./images/IMG_9893.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=d3041e099b0b0ea8824c6426c0728572a00f9625a74fab495c2e4241736d63d7&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: A는 힙이 아니고 B, C는 힙이다

![](./images/IMG_9894.heic)

![](./images/IMG_9894.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=4638df9ec2a865fc2e939795c8b93e55c68d0a7adda1e8171a55e7d921bfdd8a&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 정렬되지 않은 서브트리를 힙으로 만드는 과정

![](./images/IMG_9895.heic)

![](./images/IMG_9895.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=fe2b9b6802a138ab08913284404efbfb3093b74b3f4f2aaa9e5ad0f804f4cc41&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9896.heic)

![](./images/IMG_9896.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=c90bf5defd12236569a52d83de28797dba71f66af1ba2e2283e8c3daf8d78c27&X-Amz-SignedHeaders=host&x-id=GetObject)

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
            if temp >= a[child]: # 이게 무슨 뜻이지? 최대 자식이 이미 부모보다 작음 따라서 더 볼 필요 없음.
                break 
            # 더 아래로 다운힙을 전개.
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
![](./images/IMG_9891.heic)

![](./images/IMG_9891.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=93005803f5d03965c0050f151bb43a573c17d585a0342fe245a74ae3224c699c&X-Amz-SignedHeaders=host&x-id=GetObject)

- heap_sort()함수
  - 원소 수가 n인 배열 a를 힙 정렬하는 함수입니다. 다음과 같이 2단계로 구성됩니다.
  - 1단계: down_heap() 함수를 호출하여 배열 a를 힙으로 만듭니다.
  - 2단계: 최댓값인 루트 a[0]을 꺼내 배열의 마지막 원소와 교환하고, 배열의 남은 부분을 다시 힙으로 만드는 과정을 반복하여 정렬을 수행합니다.
## 힙 정렬의 시간 복잡도

이 부분 내용은 좀 부실함. 다른 교재를 참고하여 정리할 것.

## 연습: 힙 정렬 구현하기 

### Phase1.

1. down_heap(a: MutableSequence, left: int, right: int) → None: 함수 작성
1. 1단계: a[i] ~ a[n-1]을 힙으로 만들기
1. 2단계: a[0] ~ a[n-1]을 힙으로 만들기.
### Phase2. 안 보고 구현하기 전에 공부하기.

일단 힙 정렬의 순서를 이해할 필요가 있다. 메커니즘은 대강 알고 있으니 화이트보드에 힙정렬 과정을 그리고 사진을 업로드 할 것.

![](./images/IMG_9932.heic)

![](./images/IMG_9932.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN5ISDDW%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCICXu8XpIOWBjByUnHiUFWzICqjQ6pY2RDtfmeo1svrPdAiAXsU9lHBhBl7fGKvkzzwMI8EK1bxktb42UZQ1SKc8MECr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMildV8qIyFpvcdJfeKtwD9jbc8dOm%2F8YISDeDTs%2BwSL%2BtQ8uPRHLArpqPzm2XO41zmqwRghhnNWVkqLR0pfbgpwpXNyc%2Flk6wBsRFhGu6c6BrDj2UsYn%2FXZVUfvDQHBVzsyFrZk5ZnHL705BZ0kv4bTeEoBcT6axSkMd3GSLHZ1G%2BAPtuw2Hbr%2FshqNRXg3MhSHmHblymCeIWimKD1Imq4VNIFkr2ufZFN0FGL98M9rjKOwBXhG0SkUqS0UJR00wrUZVUcFCOau3ns1VzCKpWKb1PhSFAxOoONKfrz4SaRHk9Xc3b3MAwgR5OLLOHOyOF8eB59DeWk6ldbFmXfG6yg%2FD8xLkp8ams6eGg1mXY11BTT%2FfogrvsZBFdWD9UXQVQ3ruTeTUzXDgZ%2BO%2FPsTz5HJQDV7FOonrSlGV1GmmY5ftVHDZANAwxA%2BxrcdWc7SVWmsmjCU1TljFsxh8j%2BvFbuNUzvx7LZgiweKvJyruWqsSylALlh2qA4YR8xVjkHIDLfFmag0rI8N3%2BZvuPbIxInQdWkJwWgr%2FI4urHLE8PSVjnpe5fzhioC0haqOJzNkUcAK6ymg6z5zliJkCSWNUhwbYnCSiiFFyek4UknGNm0RYL1wFBo20EOPxoBDf9GC8qKD7cNCrx4F65y9swvLHnvgY6pgFE8Nx7c07mJ6VHo6bTT3e0ksjICE2sFKROyDbrDDvkgAIukZOjMwRPyWeF%2FhogYDukWiLabL3J2goW0z%2FWjmTey%2BbdgLyUKDAyc2xJA%2FB4ef7sQ9CLYNcq1xa%2Fb1TBkwf4E3txKam%2Bwnf8jhXI73APQt2C%2B60gJE5Ae7gOyyreT9Gmmcg3E5%2FEazrbK6AAUYnHI8MRIi%2FuZlrVSTLWQ6q9QOZMaUts&X-Amz-Signature=9750ddc3d496f68b7144f6c311baaca7085150afb0d54f8d12f2d38e08d4b4f3&X-Amz-SignedHeaders=host&x-id=GetObject)

알게된 점: 난 다운힙을 모른다. 다시 그림을 보고 이해.

![](./images/IMG_9895.heic)

![](./images/IMG_9895.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=59cdf430516d0f0ccf2f5837a29580d2e1afd29b1a9b19bf16c47f777c183b6f&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9896.heic)

![](./images/IMG_9896.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=5045ab00952b047ee2b5b52c5137ba96856a1a1c08e05817b575c483644f6f75&X-Amz-SignedHeaders=host&x-id=GetObject)

### Phase3. 이제 좀 이해가 되시면 구현을 해 봅시다.

최소 요구사항 정리

1. 다운 힙을 구현하니다.
1. 다운힙 함수를 범위를 줄여가며 호출합니다.
```python
# ### Phase3. 이제 좀 이해가 되시면 구현을 해 봅시다.

# 최소 요구사항 정리

# 1. 다운 힙을 구현하니다.
# 2. 다운힙 함수를 범위를 줄여가며 호출합니다.

from typing import MutableSequence

def heap_sort(A):
    def down_heap(A: MutableSequence, left, right):
        root = A[left]
        while left * 2 + 1 < right: # while root has child
            # 힙 성질을 구현
            lchild = left * 2
            rchild = lchild + 1
            gt_child = lchild if A[lchild] > A[rchild] else rchild #큰아들 구하기
            if root >= gt_child:
                break
            # 교환?
            A[left], A[gt_child] = A[gt_child], A[left]
            # 아래 요소에 대해 다운힙. 근데 이제 변경된 자식에 대해서만
            left = gt_child
            root = A[gt_child]

    # 이제? 아래서부터 다운힙 하면 됨
    n = len(A)-1
    for i in range(n//2, -1, -1): # 이때 올라가는 범위가 이런 느낌이었는데. 아 이거였나.
        down_heap(A, i, n) 
        # 힙으로 초기화
    # 이제 루트 하나씩 빼서 저장하고 전체에 대해 다운힙 진행.
    # 이때 해야 되는게 그... 루트 빼서 저장하고 다운힙하기 인데,
    # 첫 반복문은 뭘 해야되냐? 범위를 줄여가면서 다운힙을 실시해야지. right가 줄어듦.
    complete = []
    for i in range(n, -1, -1):
        # 루트를 빼서 완성 정렬에 추가해주고
        complete.append(A[0])
        # 끝 값을 복사해서 올려준다.
        A[n], A[0] = A[0], A[n]
        down_heap(A, 0, i)
    return A

print(heap_sort([4,3, 4,2,4,5,2,3]))
################결과########################
[4, 3, 5, 2, 4, 4, 2, 3]
        
```

위와 같이 최초 구현을 했으나,  정렬 실패. 이제 로그를 찍으면서 교환 과정을 확인해보자. 이건 따로 이슈 파도록

# 이슈: 힙 정렬 결과 이상

## Phase1.

### 환경: 파이썬

### 로그

```python
[4, 3, 5, 2, 4, 4, 2, 3]
```

### 최근 변경 사항

힙 정렬 구현

## Phase2-1

### 확인

일단 교환 과정이 예상대로 일어나고 있는지 확인

```python
sort start: [4, 3, 4, 2, 4, 5, 2, 3]
down heap called: [4, 2, 4, 5, 2, 3]
heap down. root: 4, left: 4, right: 5
compared 4 v 5, choose 5
exchanging family: (4, 4, 5)
exchanged gt-child with parent: [4, 3, 5, 2, 4, 4, 2, 3]
next child: 4, index: 5
down heap called: [3, 5, 2, 4, 4, 2, 3]
heap down. root: 3, left: 5, right: 2
compared 5 v 2, choose 5
root is already greatest value
down heap called: [4, 3, 5, 2, 4, 4, 2, 3]
heap down. root: 4, left: 4, right: 3
compared 4 v 3, choose 4
root is already greatest value

initial down heap complete: [4, 3, 5, 2, 4, 4, 2, 3]
```

일단 자식을 제대로 구하지 못하고 있음. 인덱스가 1씩 작다.

```python
...앞에선 잘 가다가
exchanging family: (3, 2, 4)
exchanged gt-child with parent: [4, 4, 5, 2, 3, 4, 2, 3]
next child: 3, index: 4
down heap called: [4, 4, 5, 2, 3, 4, 2, 3]
heap down. root: 4, left: 4, right: 5
compared 4 v 5, choose 5 <= 여기서 문제
root is already greatest value
initial down heap complete: [4, 4, 5, 2, 3, 4, 2, 3]

```

잘 가다가 마지막에 교환이 안 일어난다. compared 한 다음 루트가 이미 최대값이라며 넘어간다. 더 자세한 로그 보기

```python
sort start: [4, 3, 4, 2, 4, 5, 2, 3]
down heap called: [4, 2, 4, 5, 2, 3]
heap down. root: 4, left: 5, right: 2
compared 5 v 2, choose 5
exchanging family: (4, 5, 2)
exchanged gt-child with parent: [4, 3, 5, 2, 4, 4, 2, 3]
next child: 4, index: 5
down heap called: [3, 5, 2, 4, 4, 2, 3]
heap down. root: 3, left: 2, right: 4
compared 2 v 4, choose 4
exchanging family: (3, 2, 4)
exchanged gt-child with parent: [4, 4, 5, 2, 3, 4, 2, 3]
next child: 3, index: 4
down heap called: [4, 4, 5, 2, 3, 4, 2, 3]
heap down. root: 4, left: 4, right: 5
compared 4 v 5, choose 5
exchanging family: (4, 4, 5)
exchanged gt-child with parent: [5, 4, 4, 2, 3, 4, 2, 3]
next child: 4, index: 2
heap down. root: 4, left: 4, right: 2
compared 4 v 2, choose 4
root is already greatest value. root: 4, gt-child:4

initial down heap complete: [5, 4, 4, 2, 3, 4, 2, 3]

```

인덱스를 값과 잘못 비교하고 있었다. 

```python
            if root >= A[gt_child]: # gt_child를 직접 비교하고 있었음.

```

일단 다운힙은 성공.

```python
initial down heap complete: [5, 4, 4, 2, 3, 4, 2, 3]

complete: [5]
down heap called: [3, 4, 4, 2, 3, 4, 2, 5]
heap down. root: 3, left: 4, right: 4
compared 4 v 4, choose 4
exchanging family: (3, 4, 4)
exchanged gt-child with parent: [4, 4, 3, 2, 3, 4, 2, 5]
next child: 3, index: 2
heap down. root: 3, left: 4, right: 2
compared 4 v 2, choose 4
exchanging family: (3, 4, 2)
exchanged gt-child with parent: [4, 4, 4, 2, 3, 3, 2, 5]
next child: 3, index: 5
down heap complete: [4, 4, 4, 2, 3, 3, 2, 5]

complete: [5, 4]
down heap called: [5, 4, 4, 2, 3, 3, 2]
heap down. root: 5, left: 4, right: 4
compared 4 v 4, choose 4
root is already greatest value. root: 5, gt-child:4
down heap complete: [5, 4, 4, 2, 3, 3, 2, 4]

complete: [5, 4, 5]
down heap called: [4, 4, 4, 2, 3, 3]
heap down. root: 4, left: 4, right: 4
compared 4 v 4, choose 4
root is already greatest value. root: 4, gt-child:4
down heap complete: [4, 4, 4, 2, 3, 3, 2, 5]

```

지금은 딱 봐도 다운 힙 범위가 제대로 정해지지 않았다. 어펜드는 무조건 루트를 하기 때문에 틀릴 여지가 없고, 다운 힙 할 때 처리된 값까지 처리해서 중복으로 complete가 들어온다.

```python
   complete = []
    for i in range(n, -1, -1):
        # 루트를 빼서 완성 정렬에 추가해주고
        complete.append(A[0])
        print(f'complete: {complete}')
        # 끝 값을 복사해서 올려준다.
        A[n], A[0] = A[0], A[n]
        down_heap(A, 0, i)
        print(f'down heap complete: {A}\n')
```

아! 아래가 문제였다.

```python
					
				# 끝 값을 복사해서 올려준다.
        A[n], A[0] = A[0], A[n]
```

n이 아니라, i를 교환해주면 되나? 어떻게 교환해줘야지?

### 시도

```python
# ### Phase3. 이제 좀 이해가 되시면 구현을 해 봅시다.

# 최소 요구사항 정리

# 1. 다운 힙을 구현하니다.
# 2. 다운힙 함수를 범위를 줄여가며 호출합니다.

from typing import MutableSequence

def heap_sort(A):
    def down_heap(A: MutableSequence, left, right):
        print(f'down heap called: {A[left:right+1]}')
        root = A[left]
        while left * 2 + 1 < right: # while root has child
            # 힙 성질을 구현
            lchild = left * 2 + 1 
            rchild = lchild + 1
            print(f'heap down. root: {root}, left: {A[lchild]}, right: {A[rchild]}')
            gt_child = lchild if A[lchild] > A[rchild] else rchild #큰아들 구하기
            print(f'compared {A[lchild]} v {A[rchild]}, choose {A[gt_child]}')
            if root >= A[gt_child]:
                print(f'root is already greatest value. root: {root}, gt-child:{A[gt_child]}')
                break
            print(f'exchanging family: {A[left], A[lchild], A[rchild]}')
            # 교환?
            A[left], A[gt_child] = A[gt_child], A[left]
            print(f'exchanged gt-child with parent: {A[:right+1]}')
            # 아래 요소에 대해 다운힙. 근데 이제 변경된 자식에 대해서만
            left = gt_child
            root = A[gt_child]
            print(f'next child: {A[left]}, index: {left}')
        

    # 이제? 아래서부터 다운힙 하면 됨
    n = len(A)-1
    print(f'sort start: {A}')
    for i in range(n//2-1, -1, -1): # 이때 올라가는 범위가 이런 느낌이었는데. 아 이거였나.
        down_heap(A, i, n) 
    # print(f'\ninitial down heap complete: {A}\n')
        # 힙으로 초기화
    # 이제 루트 하나씩 빼서 저장하고 전체에 대해 다운힙 진행.
    # 이때 해야 되는게 그... 루트 빼서 저장하고 다운힙하기 인데,
    # 첫 반복문은 뭘 해야되냐? 범위를 줄여가면서 다운힙을 실시해야지. right가 줄어듦.
    # complete = []
    for i in range(n, -1, -1):
        # 루트를 빼서 완성 정렬에 추가해주고
        # complete.append(A[0])
        # print(f'complete: {complete}')
        # 끝 값을 복사해서 올려준다.
        print(f'before exchange: {A}')
        A[i], A[0] = A[0], A[i]
        print(f'exchanging: {A[0]} <-> {A[i]} ')
        print(f'after exchange: {A}')

        print(f'\ni: {i}====================\n')
        # print(f'down heap complete: {A}\n')
        down_heap(A, 0, i-1)
    return A
    # return complete


print(heap_sort([4, 3, 4, 2, 4, 5, 2, 234, 3245, 5234, 4325, 3]))
        
```

### 결과 분석: 성공!

아래는 결과 예시. 최초 다운힙을 실시한 다음 인덱스를 줄여가며 힙을 구현해줘야 한다.

```python
sort start: [4, 3, 4, 2, 4, 5, 2, 3]
down heap called: [4, 2, 4, 5, 2, 3]
heap down. root: 4, left: 5, right: 2
compared 5 v 2, choose 5
exchanging family: (4, 5, 2)
exchanged gt-child with parent: [4, 3, 5, 2, 4, 4, 2, 3]
next child: 4, index: 5
down heap called: [3, 5, 2, 4, 4, 2, 3]
heap down. root: 3, left: 2, right: 4
compared 2 v 4, choose 4
exchanging family: (3, 2, 4)
exchanged gt-child with parent: [4, 4, 5, 2, 3, 4, 2, 3]
next child: 3, index: 4
down heap called: [4, 4, 5, 2, 3, 4, 2, 3]
heap down. root: 4, left: 4, right: 5
compared 4 v 5, choose 5
exchanging family: (4, 4, 5)
exchanged gt-child with parent: [5, 4, 4, 2, 3, 4, 2, 3]
next child: 4, index: 2
heap down. root: 4, left: 4, right: 2
compared 4 v 2, choose 4
root is already greatest value. root: 4, gt-child:4
before exchange: [5, 4, 4, 2, 3, 4, 2, 3]
exchanging: 3 <-> 5
after exchange: [3, 4, 4, 2, 3, 4, 2, 5]
```

```python
i: 7====================
```

```python
down heap called: [3, 4, 4, 2, 3, 4, 2]
heap down. root: 3, left: 4, right: 4
compared 4 v 4, choose 4
exchanging family: (3, 4, 4)
exchanged gt-child with parent: [4, 4, 3, 2, 3, 4, 2]
next child: 3, index: 2
heap down. root: 3, left: 4, right: 2
compared 4 v 2, choose 4
exchanging family: (3, 4, 2)
exchanged gt-child with parent: [4, 4, 4, 2, 3, 3, 2]
next child: 3, index: 5
before exchange: [4, 4, 4, 2, 3, 3, 2, 5]
exchanging: 2 <-> 4
after exchange: [2, 4, 4, 2, 3, 3, 4, 5]
```

```python
i: 6====================
```

```python
down heap called: [2, 4, 4, 2, 3, 3]
heap down. root: 2, left: 4, right: 4
compared 4 v 4, choose 4
exchanging family: (2, 4, 4)
exchanged gt-child with parent: [4, 4, 2, 2, 3, 3]
next child: 2, index: 2
before exchange: [4, 4, 2, 2, 3, 3, 4, 5]
exchanging: 3 <-> 4
after exchange: [3, 4, 2, 2, 3, 4, 4, 5]
```

```python
i: 5====================
```

```python
down heap called: [3, 4, 2, 2, 3]
heap down. root: 3, left: 4, right: 2
compared 4 v 2, choose 4
exchanging family: (3, 4, 2)
exchanged gt-child with parent: [4, 3, 2, 2, 3]
next child: 3, index: 1
heap down. root: 3, left: 2, right: 3
compared 2 v 3, choose 3
root is already greatest value. root: 3, gt-child:3
before exchange: [4, 3, 2, 2, 3, 4, 4, 5]
exchanging: 3 <-> 4
after exchange: [3, 3, 2, 2, 4, 4, 4, 5]
```

```python
i: 4====================
```

```python
down heap called: [3, 3, 2, 2]
heap down. root: 3, left: 3, right: 2
compared 3 v 2, choose 3
root is already greatest value. root: 3, gt-child:3
before exchange: [3, 3, 2, 2, 4, 4, 4, 5]
exchanging: 2 <-> 3
after exchange: [2, 3, 2, 3, 4, 4, 4, 5]
```

```python
i: 3====================
```

```python
down heap called: [2, 3, 2]
heap down. root: 2, left: 3, right: 2
compared 3 v 2, choose 3
exchanging family: (2, 3, 2)
exchanged gt-child with parent: [3, 2, 2]
next child: 2, index: 1
before exchange: [3, 2, 2, 3, 4, 4, 4, 5]
exchanging: 2 <-> 3
after exchange: [2, 2, 3, 3, 4, 4, 4, 5]
```

```python
i: 2====================
```

```python
down heap called: [2, 2]
before exchange: [2, 2, 3, 3, 4, 4, 4, 5]
exchanging: 2 <-> 2
after exchange: [2, 2, 3, 3, 4, 4, 4, 5]
```

```python
i: 1====================
```

```python
down heap called: [2]
before exchange: [2, 2, 3, 3, 4, 4, 4, 5]
exchanging: 2 <-> 2
after exchange: [2, 2, 3, 3, 4, 4, 4, 5]
```

```python
i: 0====================
```

```python
down heap called: []
[2, 2, 3, 3, 4, 4, 4, 5]
```



# 도수 정렬

## 기본 개념

### 그림: 도수분포표 작성

그냥 간단함. 주어진 값의 최대값을 크기로 하는 배열을 만들고 각 값을 인덱스로 해당 칸을 1 더하면 됨.

![](./images/IMG_9886.heic)

![](./images/IMG_9886.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=27c315c59ad634c9e1dfb4ac8b92b56cd1a9194cb5dc835f6989c01ba1b4d488&X-Amz-SignedHeaders=host&x-id=GetObject)

이에 대한 Prefix Sum 배열을 구하면 누적 도수 분포표를 구할 수 있음. 이를 통해 작업용 배열을 만들면 되는데, 아래와 같음

### 그림: 작업용 배열 만들기

![](./images/IMG_9887.heic)

![](./images/IMG_9887.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=c4c243f0773d661d1bfb87769694f2eea890ed5454f0cc33923d815c96817da1&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드: 위 그림을 수행하는 코드

```python
for i in range(n - 1, -1 ,-1):
	f[a[i]] -= 1
	b[f[a[i]]] = a[i]
```

### 그림: 작업용 배열 만들기 2

![](./images/IMG_9888.heic)

![](./images/IMG_9888.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=aec5792d3aaef69e5852a04ad6cb17ab2503a5f9e46fbdbc077ed1c9be1a773a&X-Amz-SignedHeaders=host&x-id=GetObject)

### 그림: 작업용 배열 만들기 3

f 테이블의 요소 값을 줄여주는 덕분에 중복 값이 알아서 잘 처리되는 모습을 볼 수 있다. 

![](./images/_.heic)

![](./images/_.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W462LHG2%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDVo7slpapgeGmAL2bTvRDz3Tq9RkTXBQY%2BkCe3ccC1vQIhANvdkeB6hCIZ4DFi%2Bb6loZXE4jrE5PvLmUmRqvRDSJSiKv8DCGYQABoMNjM3NDIzMTgzODA1IgzmpZjOdOReoqUTa4sq3AP6W7wYbTef3elifZzFAY%2BmmcxVimom3dSdnLyScUrJSch%2BCqQHiNAezXXpKpfu6MtjxJlpkPsv77rAj%2FfknaCQUbqLof0PLiuPlVr9tAfa%2FuP%2BPIDRU5kJ9UB6hP5lqtx8PTg%2BJ2E%2F2HafIIS82WtT%2Boj7y85TsnWqY2n4jqXlF2DJs3D5avUhwWolCfYTNbEJvWYJWFMnS%2FDTtAwKMD0gFX%2FFOj%2FN6UowBUgG4cYWgqyf65QjRKmPaxqSFGcSCBKs0Jdd4fTJvUYJlAjFEIgdUEM2LwLlLxX8Q3dilF%2FNcKxa8oQlNXruFNhit8MG44lHXlEgnEmBhMG8iaF9kvxx5WUftzhyGTmpCwDTLqykiEGuWYPVHJdLeqnrZ0g3IuCvoXq3wBKBSoLuEgmzJwEjC6X62uxB1JNJAcaCKdyDVLlf8MH%2BUaTwPo6aTX6tG1UO0IgxMtM9V8PjURki5qoWD2iIHcrvbFn47tlUySieWFLZJm%2FsfwPZsPlxGnpPx73205w3tEYKbxHDivSkNYvjB9wJ%2F4f7DUiayuRmUEy22Ql6k8%2FCZ%2BVtRzFZ8jix00EFBw5L7TypqSSWJ2SCPXF7Xx0ix%2Bdq%2FxmaT0be9Kb%2FLKYtDspHpINXXZgdUjDmsOe%2BBjqkAVRVXATTxTWD%2BjhUlxhQGvRMxv4X9AlDCtFJs1ges3UjtDsINjzjg99J9%2FZI9kBEhNDDv8fKB9tSzMB1q8rpfiQfFW2v12U0wtPh%2BOMooginm%2FfiIMFT2K0Sn3NDE0TdmoN3Ehz6Q45RsI%2FfCH7YZCE09TnTXPZnognOxmssDTW40gD1SgztXCsPmh%2BK%2F2xRVr07pPKdsgkZIjAWqFhvqwTpOtrc&X-Amz-Signature=17b4d101346e2751dc598f6de54584797fc143dc258452d18c48fe1ffda2bb1f&X-Amz-SignedHeaders=host&x-id=GetObject)



