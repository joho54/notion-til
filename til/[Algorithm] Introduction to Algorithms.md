# [Algorithm] Introduction to Algorithms

> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> 키워드 중심으로 볼 필요가 있습니다.

> 체계: 개구코, 수구(수도코드→구현)로 합시다.

> 전반적인 해더는 타이틀 중심으로, ###은 위 체계를 따릅니다.

> 읽을 때는 모, 그 정도로? 일단. 
딱히 구현 material이 없어도 구현을 이런 저런 핑계삼아 해보는 것도 좋겠다. 정렬은 자다가 건드려도 튀어나와야 한다니까.

# 이 책을 읽는 방법 - 체크리스트로 사용

📖 “Introduction to Algorithms” (CLRS) 효과적으로 활용하는 방법

CLRS는 알고리즘 학습의 바이블이지만, 너무 방대해서 처음부터 끝까지 읽기는 현실적으로 어렵습니다. 따라서 필요한 부분만 전략적으로 학습하는 것이 중요합니다.

2. CLRS에서 꼭 봐야 할 핵심 내용 (우선순위 학습 순서)

🚀 2단계: 탐색과 그래프 알고리즘 (면접 대비 필수)

✅ Chapter 9: 선택 알고리즘 (Median & Order Statistics)

✅ Chapter 10-12: 해시 테이블(Hash Table), BST(이진 검색 트리), Red-Black Tree

✅ Chapter 15: 동적 계획법 (DP, Dynamic Programming)

✅ Chapter 22-24: 그래프 탐색 (BFS, DFS), 최단 경로 알고리즘 (Dijkstra, Bellman-Ford, Floyd-Warshall), 최소 신장 트리 (MST)

➡ 면접 대비나 대회 준비를 한다면 이 단계가 매우 중요하며, 구현 연습도 반드시 함께해야 한다.

🚀 3단계: 심화 및 고급 주제 (연구나 심층 학습 목적)

✅ Chapter 25-26: 최대 유량(Maximum Flow)

✅ Chapter 30: NP-완전 문제(NP-Completeness)

✅ Chapter 34: 알고리즘 설계 기법 (근사 알고리즘, 탐욕 알고리즘)

➡ 이 단계는 코딩 테스트보다는 “이론적인 알고리즘 공부”가 필요할 때 활용하는 것이 좋다.

3. CLRS 학습법 (효율적으로 공부하는 방법)

📌 1. 알고리즘 개념 학습 + 간단한 구현 연습

•	각 챕터에서 중요한 알고리즘을 공부한 뒤,

•	직접 Python이나 C++로 간단히 구현해보며 핵심 원리를 익힌다.

•	예제 코드가 너무 복잡하면, 핵심 부분만 추려서 직접 구현하는 것이 효과적이다.

예시) 힙 정렬을 공부할 때

1.	CLRS에서 힙 정렬(Heap Sort) 개념 읽기

2.	파이썬으로 힙 정렬을 직접 구현

3.	LeetCode / 백준 / 프로그래머스에서 힙 관련 문제 풀기

📌 2. 수식이나 증명은 선택적으로 학습

•	CLRS는 수학적 증명이 많지만, 모든 증명을 이해하려고 할 필요는 없다.

•	증명이 너무 어려우면, 핵심 아이디어와 개념만 익히고 넘어가도 괜찮다.

•	다만, 시간 복잡도 분석(빅오 표기법, 마스터 정리 등)은 꼭 익혀야 한다.

📌 3. 문제 풀이 병행

•	CLRS의 이론을 공부한 뒤, 코딩 문제를 바로 풀어보는 것이 가장 중요하다.

•	백준(BOJ), LeetCode, Codeforces, 프로그래머스에서 관련 문제를 찾아서 연습하는 것이 효과적.

•	특히 그래프, DP, 정렬 문제는 CLRS 내용을 공부한 후 바로 문제를 풀면 학습 효과가 좋다.

4. CLRS를 활용한 추천 학습 플랜

> ✅

> ✅

📅 1~2주차 (기본 개념 + 정렬 + 탐색)

✅ 알고리즘 개념 + 시간 복잡도 분석 (Ch. 13)

✅ 정렬 (힙 정렬, 퀵 정렬, 계수 정렬) (Ch. 68)

✅ BST(이진 검색 트리) 기본 개념 익히기 (Ch. 10-12)

✅ 문제 풀이: 기본 정렬 문제, 힙 문제 풀기

📅 3~4주차 (탐색 + 그래프 알고리즘)

✅ 탐색(이진 탐색, 선택 알고리즘) (Ch. 9)

✅ 그래프 탐색 (BFS, DFS) (Ch. 22)

✅ 최단 경로 알고리즘 (Dijkstra, Bellman-Ford) (Ch. 24)

✅ 문제 풀이: 그래프 기본 문제, 최단 경로 문제 풀기

📅 5~6주차 (동적 계획법 + 고급 그래프)

✅ 동적 계획법 (DP) 개념 및 대표 문제 (Ch. 15)

✅ 최소 신장 트리(MST, Kruskal, Prim) (Ch. 23)

✅ 문제 풀이: DP 문제 + MST 문제

📅 7~8주차 (응용 및 심화 주제)

✅ 네트워크 플로우 (Ch. 25-26)

✅ NP-완전성 개념 (Ch. 30)

✅ 근사 알고리즘 (Ch. 34)

✅ 문제 풀이: Hard 난이도 문제 도전

5. 정리

🔹 CLRS는 완독하는 책이 아니라, 필요할 때 찾아보는 참고서로 활용하는 것이 좋다.

🔹 우선순위를 정하고, 중요한 부분(정렬, 그래프, DP)부터 학습하면 효율적이다.

🔹 이론만 공부하지 말고, 반드시 코딩 문제를 병행하면서 학습해야 실력이 는다.

🔹 초보자는 너무 어려운 증명보다는 개념과 알고리즘 구현에 집중하는 것이 좋다.

📌 결론: CLRS를 무작정 처음부터 읽기보다는, 필요할 때 참고하고, 코딩 문제 풀이와 병행하며 효율적으로 학습하는 것이 가장 효과적인 활용법이다. 🚀



# Chapter 1-3: 알고리즘 개념 및 복잡도 분석 (O(n), O(log n))

> 여기도 일단 책 먼저 스캔하고, 개구코로 정리? ㅇㅇ.

## 개구코 1.

# Sorting and Order Statistics

## Heapsort

## Quicksort

### 개구코 1

개념: 퀵 정렬은 병합 정렬과 달리 스테이블하다. 

구현

1. 수도코드
![](./images/IMG_9905.png)

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

바닥 조건 수행 후에 스택이 비어있지 않으면 자연스럽게 다음으로 넘어가서 s에서 팝 하게 되는데, 그럼 결국 마지막에 s.popleft()가 실행된 다음에 larger나 smaller가 없으면 스택은 자연스럽게 비어야 하지 않나? 왜지? if larger, if smaller의 의미가 불분명하다.

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

# Designing Algorithms 

> 개구코로 읽으시죠

## 개구코1. 

### 개념: incremental methods vs divide and conquer

insertion sort uses the incremental methods.

### 구현

없음

### 코멘트

문제를 해결하는 두가지 방식 분류를 이제야 알게 된 느낌. incremental methods와 divide and conquer.

## 개구코2.

### 개념: Advantage of the algorithm following divide and conquer method is that analyzing its running time is often straightforward.

### 구현: 

없음

### 코멘트

분할정복은 메서드가 더 복잡해보이지만 오히려 실행 시간을 더 명확히 계산할 수 있다고 한다. 왜?

> 좋은 질문이에요. “분할정복(Divide and Conquer)“이 실행 시간이 더 명확하게 계산될 수 있는 이유는 주로 다음과 같은 구조적 특징 덕분입니다:

## 개구코3.

### 개념: steps of divide and conquer method

in the divide-and-conquer method, if the problem is small enough-the base case- you just solve it directly without recursing. Otherwise - the recursive case -you perform three characterstic steps

- Divide: the problem into one or more subprolems that are smaller instances of the same problem
- Conquer: the subproblems by solving them recursively
- Combine: the subproblem solutions to form a solution to the original problem.
### 구현

Steps of merge sort

- Divide the subarray A[p:r] to be sorted into two adjacent subarray, each of half the size. To do so, compute the midpoint q of A[p:r](taking the average of p and r) and divide A[p:r]into subarrays A[p:q] and A[q+1:r].
- Conquer by sorting each of the two subarrays A[p:q] and A[q+1:r] recursively using merge sort.
- Combine by merging the two sorted subarrays A[p:q] and A[q+1:r] back into A[p:r], producing the sorted answer.
### 코멘트

이미 divide 시점에서도 주어진 배열이 무언가의 부분 배열이라는 점에 눈에 띈다. 어떤 집합을 대상으로 작업을 한다고 치면, 그 집합 전체도 그 집합의 부분집합이라는 점에 주목하는 것처럼 느껴진다. 이게 결정 트리를 이용한 풀이에서도 마찬가지겠지?

> 이야, 정말 날카로운 통찰이에요(^0^). 맞아요—당신이 말한 그 **“전체도 부분집합이다”**라는 개념은 **결정 트리(decision tree)**나 **분할정복(divide and conquer)**의 사고방식에서 굉장히 핵심적인 철학이에요.

# Divide and Conquer

## 개구코 1. Well defined vs ill defined recurrence.

### 개념

There may be zero, one, or many functions that satisfy the statement of the recurrence. The recurrence is well defined if there is at least one function that satisfies it, and ill defined otherwise.

### 코멘트: 무슨 의미지?

해당 문장은 “주어진 점화식을 만족하는 함수(혹은 수열)가 없을 수도, 하나만 존재할 수도, 여러 개 존재할 수도 있다”는 뜻입니다.

•	어떤 점화식을 정의할 때, 그 점화식을 만족할 수 있는 해(함수나 수열)가 하나도 존재하지 않는다면, 그 점화식 자체가 모순적이거나 불가능한 정의가 되어 **‘ill defined(정의가 성립하지 않는다)’**라고 합니다.

•	반대로 적어도 하나라도 점화식을 만족하는 함수(혹은 수열)가 존재하면, 그 점화식은 ‘well defined(정의가 성립한다)’ 라고 합니다.

•	그 점화식을 만족하는 함수가 유일(단 하나)할 수도 있고, 둘 이상(무한히 많을 수도 있음) 존재할 수도 있지만, 적어도 하나라도 존재해야 점화식이 제대로 정의되었다고 볼 수 있습니다.

요약하자면,

•	“zero”: 해가 아예 없는 경우 → 점화식이 모순이므로 ill defined(정의가 성립하지 않음)

•	“one”: 해가 정확히 하나 있는 경우 → well defined(정의가 성립함)

•	“many”: 해가 여러 개 존재하는 경우 → 역시 well defined(정의가 성립함)

결국 “해가 단 하나라도 존재하는가?”가 ‘well defined’의 기준이 된다는 의미입니다.

## 개구코 2.  Algorithmic recurrences

### 개념

A recurrence T(n) is algorithmic if, for every sufficient large threshold constant $n_0>0$, the following two properties hold:

1. For all n < n_0, we have T(n) = O(1)
1. For all n \ge n_0, every path of recursion terminates in a defined base case within a finite number of recursive invocations.
### 개념: Break down

- Why would a recurrence T(n) that represents a (correct) divide-and-conquer algorithm’s worst-case running time satisfy these properties for all sufficiently large threshold constants? (왜 점화식은 위 조건만 만족해도 의외로 모든 큰 문제를 해결할 수 있는가?)
- The first property says that there exist constants c1, c2 such that 0 < c1 ≤ T(n) ≤ c2 for n < n0. 
- For every legal input, the algorithm must output the solution to the problem it’s solving in finite time. 
- Thus we can let c1 be the minimum amount of time to call and return from a procedure which must be positive, because machine instructions need to be executed to invoke a procedure.
- The running time of the algorithm may not be defined for some values of n if there are no legal inputs of that size, but it must be defined for at least one, or else the “algorithm” doesn’t solve any problem.
- Thus we can let c2 be the algorithm’s maximum running time on any input of size n < n0, where n0 is sufficiently large that the algorithm solves at least one problem of size less than n0.
- The maximum is well defined, since there are at most a finite number of inputs of size less than n0, and there is at least one if n0 is sufficiently large. 
- Consequently, T(n) satisfies the “first property”
- If the second property fails to hold for T(n), then the algorithm isn’t correct, because it would end up in an infinite recursive loop or otherwise fial to compute a solution.
- Thus, it stands to reason that a recurrence for the worst-case running time of a correct divide-and-conquer algorithm would be “algorithmic”.
### 구현: 없음

### 코멘트

1번째 조건은 base case, 2번째 조건은 recursion case를 의미하는거 같다? 아니다. 2번째 조건은 ‘유한번 내로’ 재귀가 끝나는 조건을 의미한다. 합당한 입력값의 경계선인 n0를 넘어서는 입력에 대해서는, 모든 재귀가 제거된다는 뜻이다.

### 자세한 설명

두 조건을 “1. 베이스 케이스”와 “2. 재귀가 유한 단계 내에 베이스 케이스로 도달함을 보장하는 조건” 정도로 해석하시면 됩니다. 다만 엄밀히는,

1.	(베이스 케이스로서의 O(1) 조건)

“상수 n_0”보다 작은 모든 n에 대해 T(n) = O(1) 이라는 것은,

‘n_0’ 미만 영역(즉 충분히 작은 문제 크기)에 대해서는 상수 시간에 해결이 가능하다는 의미입니다.

보통 알고리즘 구현 시, 문제 크기가 충분히 작아지면(예: n = 1 혹은 n이 작을 때)

재귀를 멈추고 직접(상수 시간) 처리하는 “베이스 케이스”와 대응합니다.

2.	(재귀 호출이 유한 번 안에 끝남을 보장)

“n_0 이상의 모든 n에 대해, 어떤 경로로 재귀 호출을 타고 내려가도

유한 횟수 안에 정의된 베이스 케이스로 도달”한다는 것은,

문제 크기가 충분히 큰 경우에도 재귀가 무한히 이어지지 않고

반드시 더 작은 문제로 내려가서 결국 (1)번의 베이스 케이스를 만나게 된다는 뜻입니다.

즉 잘 정의된 재귀 구조(well-founded recursion)라는 점을 보장합니다.

정리하면,

•	조건 (1): “충분히 작은 입력에 대해선, T(n)을 상수 시간으로 처리한다(= 베이스 케이스).”

•	조건 (2): “충분히 큰 입력에 대해서도, 재귀가 결국 (1)의 케이스까지 유한 번 만에 도달한다.”

이렇게 두 조건을 만족해야, 점화식(재귀식) 자체가 현실적으로 구현 가능한 알고리즘을 반영하게 되고, 이를 **‘algorithmic recurrence(알고리즘적 점화식)’**라고 부릅니다.

## 개구코 3. 재귀식 풀기

### 개념: 재귀식을 푸는 4가지 방법론

1. substitution method: you guess the form of a bound and then use mathematical induction to prove your guess correct and solve for constants. This method is perhaps the most robust method for solving recurrences, but it also requires you to make a good guess and to procedure an inductive proof.
1. recursion-tree method: models the recurrence as a tree whose nodes represent the costs incurred at various levels of the recursion. To solve the recurrence, ou determine the costs at each level and add them up, perhaps using techniques for bounding summations from Section A.2. Even if you don’t usse this mehtod to formally prove a bound, it cna be helpful in guessing the form of the obund for use in the substitution method.
1. master method: the easiest method, wen it applies. It provides bounds for recurrences of the form T(n)=aT(n/b) + f(n), where a > 0 and b > 1 are constants and f(n) is a given “driving” function. This type of recurrence tends to arise more frequently in the study of algorithms than any other. It characterizes a divide-and-conquer algorithm that creates a subproblems, each of which is 1/ times the size of the original problem, using f(n) time for the divide and combine steps. To apply the master method, you need to memorize three cases, but once you do, you can easily determine asymptotic bounds on running times for many divide-and-conquer algorithms
1. Akra-Bazzi method: a general method for solving divide-and-conquer recurrences. Although it involves calculus, it can be used to attack more complicated recurrences than those addressed by the master method.
## 개구코 4.

### 개념

### 구현

```plain text
MATRIX-MULTIPLICATION-RECURSIVE(A, B, C, n)
	if n == 1
	// Base case.
		c11 = c11 + a11*b11
		return
	//Divide
	partition A, B, and C into n/2 x n/2 submatrices
		A11, A12, A21, A22; B11, B21, B22
```

### 코멘트



