# [Algorithm] Introduction to Algorithms

> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> 키워드 중심으로 볼 필요가 있습니다.

> 체계: 개구코, 수구(수도코드→구현)로 합시다.

> 전반적인 해더는 타이틀 중심으로, ###은 위 체계를 따릅니다.

> 읽을 때는 모, 그 정도로? 일단. 
딱히 구현 material이 없어도 구현을 이런 저런 핑계삼아 해보는 것도 좋겠다. 정렬은 자다가 건드려도 튀어나와야 한다니까.



# Sorting and Order Statistics

## Heapsort

## Quicksort

### 개구코 1

개념: 퀵 정렬은 병합 정렬과 달리 스테이블하다. 

구현

1. 수도코드
![](./images/IMG_9905.heic)

1. 구현코드
```python
import sys
n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

def quick_sort(A: list) -> list:
    # base condition 
    n = len(A)
    if n == 2:
        return [A[0], A[1]] if A[0] > A[1] else [A[1], A[0]]
    elif n <= 1:
        return A
    # get pivot
    pivot = A[n//2]
    smaller, equal, larger = [], [], []
    for a in A:
        if a < pivot:
            smaller.append(a)
        elif a == pivot:
            equal.append(a)
        elif a > pivot:
            larger.append(a)
    return [*quick_sort(smaller), *equal, *quick_sort(larger)]

print(quick_sort(arr))

```

코멘트

각 구현을 내가 잘 이해하고 있으면 이게 외워질텐데. 아쉽네. 아 이거 근데 내 기억에는 구현 방법에 따라 스테이블 할 수도 있고 아닐 수도 있었는데.

그렇다면 위 2. 구현코드는 스테이블한가? equal 처리 방식에 주목하면 될 거 같다. 배열에서 차례로 피벗과 비교할 대상을 까게 되고, 발견하게 되면 앞에 있던 equal 요소가 배열에 먼저 들어가게 된다. 나중에 언팩 돼서 다시 완성된 배열에 리턴 되므로, 스테이블하다고 할 수 있다.

그런데 이걸 스택으로 바꾸기가 쉽지 않아 보인다. 일단 한 줄에 붙어 있는 재귀를 다 풀어야 한다. 이거 오늘 해 말아?



> 쉬어가는 주제
2PMMS(2 Phase memory merge/sort)






# 이슈: 스택으로 퀵 정렬 구현 중 무한루프 발생

## Phase1. 환경, 로그, 변경사항

### 환경: 파이썬

### 로그: 무한 루프

### 변경사항

```python
import sys
from collections import deque


n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

s = deque()

def quick_sort(A: list) -> list:
    global s
    s.append(A)
    result = []
    
    
    # base condition 
    while True:
        if len(A) == 2:
            tmp = [A[0], A[1]] if A[0] > A[1] else [A[1], A[0]] 
            result.append(tmp) # 결과에 정렬된 배열을 입력합니다.
        elif len(A) <= 1:
            result.append(A) # 결과에
        # 스택에 요소가 있다면 꺼내줍니다.
        if len(s) != 0:
            A = s.popleft()
            # 만약 바닥 조건을 치지 못했다면 다시 배열을 구별해서 스택에 쑤셔 넣어줍니다.
            # get pivot
            pivot = A[len(A)//2]
            smaller, larger = [], []
            equal = []
            for a in A:
                if a < pivot:
                    smaller.append(a)
                # 퀵 정렬을 스택으로 구현할 때는 이처럼 이퀄을 따로 처리해주기가 어려움
                elif a == pivot:
                    equal.append(a)
                elif a > pivot:
                    larger.append(a)
            # return [*quick_sort(smaller), *equal, *quick_sort(larger)]
            
            # A를 smaller로 업데이트하고 함수의 처음으로 돌아갑니다.X 
            # smaller를 스택에 푸시해야 하나?
            if larger:
                s.append(larger)
            # 그런데 이퀄은 어떻게 처리하지? 일단 버려야 하나? 아 그래서 unstable이 됐구나.
            if equal:
                result.append(equal)
            if smaller:
                s.append(smaller)
            
            continue # break한 다음 이상한데로 점프하는데. 아 정상이구나. 
        break

A = s.append(arr)
quick_sort(arr)

```



## Phase2.

### 확인

무한 루프가 발생하는 이유는 당연히 len(s) ≠ 0 조건이 안 먹혀서 그런 것임. 그렇다면 s.popleft()가 적절히 이루어지지 않는다는 의미. 

바닥 조건 수행 후에 스택이 비어있지 않으면 자연스럽게 다음으로 넘어가서 s에서 팝 하게 되는데, 그럼 결국 마지막에 s.popleft()가 실행된 다음에 larger나 smaller가 없으면 스택은 자연스럽게 비어야 하지 않나? 왜지? 

if larger, if smaller의 의미가 불분명하다.

```python
>>> if []: print('hi')
...
>>> if [4]: print('hi')
...
hi
```

내 예상과 맞게 작동하는데? larger나 smaller는 무조건 내용이 있는 리스트다.

이게 무한루프에 빠질 이유가 없는 거 같은데? 조건이 문제가 아닌 건가.

### 시도

```python
import sys
from collections import deque


n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

s = deque()

def quick_sort(A: list) -> list:
    global s
    s.append(A)
    result = []
    
    
    # base condition 
    while True:
        if len(A) == 2:
            tmp = [A[0], A[1]] if A[0] > A[1] else [A[1], A[0]] 
            result.append(tmp) # 결과에 정렬된 배열을 입력합니다.
        elif len(A) <= 1:
            result.append(A) # 결과에
        # 스택에 요소가 있다면 꺼내줍니다.
        if len(s) != 0:
            # 만약 바닥 조건을 치지 못했다면 다시 배열을 구별해서 스택에 쑤셔 넣어줍니다.
            # get pivot
            pivot = A[len(A)//2]
            smaller, larger = [], []
            equal = []
            for a in A:
                if a < pivot:
                    smaller.append(a)
                # 퀵 정렬을 스택으로 구현할 때는 이처럼 이퀄을 따로 처리해주기가 어려움
                elif a == pivot:
                    equal.append(a)
                elif a > pivot:
                    larger.append(a)
            # return [*quick_sort(smaller), *equal, *quick_sort(larger)]
            
            # A를 smaller로 업데이트하고 함수의 처음으로 돌아갑니다.X 
            # smaller를 스택에 푸시해야 하나?
            if larger:
                s.append(larger)
            # 그런데 이퀄은 어떻게 처리하지? 일단 버려야 하나? 아 그래서 unstable이 됐구나.
            if equal:
                result.append(equal)
            if smaller:
                s.append(smaller)
            A = s.popleft()

            
            continue # break한 다음 이상한데로 점프하는데. 아 정상이구나. 
        break

A = s.append(arr)
quick_sort(arr)

```

처음에 A에다 팝을 하지 않는게 문제였다. 팝 순서를 변경

### 결과분석

일단 무한 루프 문제는 해결했다. 그러나 정렬 값이 이상하게 저장되는 문제가 있다. 새로 이슈 파서 합시다.

# 이슈: 정렬값 저장이 이상함.

## Phase1. 

### 환경: 파이썬

### 로그(입/출력 결과)

```python
5
5 4 3 2 1
[2, 1, 3, 5, 4]
```

### 최근 변경 사항

```python
5
5 4 3 2 1
----- 출력 -----
[[3], [3], [3], [5, 4], [4], [2, 1], [1], [5, 4], [4], [2, 1], [1], [5, 4], [4], [2, 1], [1], [5], [5], [2], [2], [5], [5], [2], [2], [5], [5], [2]]
```

## Phase2-1.

### 확인

결국 equal 값을 어떻게 처리하느냐가 문제임. 스택에 푸시하는 순서는 다음과 같음

1. larger
1. smaller
equal은 그냥 이 둘 사이에서 결과 배열에 어펜드 되는데, 이게 당연히 적절한 순서가 아님. 

제대로 처리를 하고 싶다면 스택의 요소 처리 순서를 고려해서 처리해야 하는데, 그냥 배열 값을 업데이트 할 게 아니라 포인터 값을 저장하는게 나을 수도 있겠음.

### 시도

```python
import sys
from collections import deque


n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

s = deque()

def quick_sort(A: list, start_idx, end_idx) -> list:
    global s
    s.append(start_idx, end_idx)
    result = []
    
    while True:
        if end_idx - start_idx == 2:
            tmp = [A[start_idx], A[end_idx]] if A[end_idx] > A[start_idx] else [A[start_idx], A[end_idx]] 
            result.append(tmp)
        elif end_idx - start_idx <= 1:
            result.append(A) 
        if s:
            pivot = A[(start_idx + end_idx)//2]
            smaller, equal, larger = [], [], []
            for i in range(start_idx, end_idx + 1):
                if A[i] < pivot:
                    smaller.append(A[i])
                elif A[i] == pivot:
                    equal.append(A[i])
                elif A[i] > pivot:
                    larger.append(A[i])
            if larger:
                s.append(larger)
            if equal:
                result.append(equal)
            if smaller:
                s.append(smaller)
            A = s.popleft()
            
            continue 
        print(result)
        break

A = s.append(arr)
quick_sort(arr)


```

확인에서 한 생각이 틀렸다는 걸 알게 됐다. 퀵 정렬에서 포인터 값을 저장하는 건 아무 의미가 없다. 

### 결과 분석

실패. 

# 이슈: 스택이 제대로 비워지지 않는 문제

## Phase1. 

### 환경: 파이썬

### 로그(증상) 

```python
10
10 9 8 7 6 5 4 3 2 1
current stack: deque([(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)]), deque([])
len(A) = 10
A = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
popping: (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
current stack: deque([[4, 3, 2, 1], [10, 9, 8, 7, 6]]), deque([5])
len(A) = 10
 A = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
popping: [4, 3, 2, 1]
current stack: deque([[10, 9, 8, 7, 6], [4, 3, 2, 1], [10, 9, 8, 7, 6]]), deque([5, 5])
len(A) = 4
 A = [4, 3, 2, 1]
popping: [10, 9, 8, 7, 6]
current stack: deque([[4, 3, 2, 1], [10, 9, 8, 7, 6], [1], [4, 3]]), deque([5, 5, 2])
len(A) = 5
 A = [10, 9, 8, 7, 6]
popping: [4, 3, 2, 1]
```



### 최근 변경 사항

```python
import sys
from collections import deque


n = int(input())
arr = tuple(map(int, sys.stdin.readline().split()))

s = deque()
ms = deque() # median stack. always exists.

def quick_sort(A: list) -> list:
    global s, ms
    s.append(A)
    result = []
    
    
    # base condition 
    while True:
        print(f'current stack: {s}, {ms}')
        if len(A) == 2:
            tmp = [A[0], A[1]] if A[1] > A[0] else [A[1], A[0]] 
            result = [*result, *tmp, ms.popleft()]
            print(f'appending: {tmp} and medians. {result}')
        elif len(A) <= 1:
            result = [*result, *tmp, ms.popleft()]
            print(f'appending: {tmp} and medians. {result}')
        # 스택에 요소가 있다면 꺼내줍니다.
        if s:
            # 만약 바닥 조건을 치지 못했다면 다시 배열을 구별해서 스택에 쑤셔 넣어줍니다.
            # get pivot
            pivot = A[len(A)//2]
            print(f'len(A) = {len(A)}\n A = {A}')
            smaller, larger = [], []
            equal = []
            for a in A:
                if a < pivot:
                    smaller.append(a)
                # 퀵 정렬을 스택으로 구현할 때는 이처럼 이퀄을 따로 처리해주기가 어려움
                elif a == pivot:
                    ms.append(a)
                elif a > pivot:
                    larger.append(a)
            # return [*quick_sort(smaller), *equal, *quick_sort(larger)]
            
            # 그런데 이퀄은 어떻게 처리하지? 일단 버려야 하나? 아 그래서 unstable이 됐구나.
            if smaller:
                s.append(smaller)
            # A를 smaller로 업데이트하고 함수의 처음으로 돌아갑니다.X 
            # smaller를 스택에 푸시해야 하나?
            if larger:
                s.append(larger)
            A = s.popleft()
            print(f'popping: {A}')

            
            continue # break한 다음 이상한데로 점프하는데. 아 정상이구나. 
        print(result)
        break

quick_sort(arr)

```

너무 시간을 많이 써서 일단 이만큼 하고 그냥 다음 개념으로 넘어갑시다. 

