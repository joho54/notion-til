# [Algorithm] Python - 2



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 재귀: 쿼드트리

https://www.acmicpc.net/problem/1992

## 문제

흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다

위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "(0(0011)(0(0111)01)1)"로 표현된다. N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.

## Phase1. 직접 풀기

생각보다는 쉽게 풀렸다. 단, 괄호를 출력하는 부분에서 재귀의 순서를 제대로 생각하지 않아서 조금 헤맸다. Z보다 좀 더 쉬웠는데, 사실 거의 동일한 문제인 거 같다.

```javascript
# 1. 문제 읽기
# 2. 문제 풀기
# 3. 수도 코드
# 4. 코드 구현

def is_base(A: list, r: int, c: int, n: int):
    """A 배열의 r, c를 시작점으로 하는 n 영역의 합을 구하고, 0이거나 n^2이면 True를 리턴"""
    pixels = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            pixels += A[i][j]
    if pixels == 0: return 0
    elif pixels == n**2: return 1
    return -1

def recur(A: list, r, c, n):
    pixels = is_base(A, r, c, n)
    if pixels != -1:
        print(pixels, end='')
        return
    # 1 사분면 재귀
    half = n//2
    print('(', end='')
    recur(A, r, c, half)
    # 3 사분면 재귀
    recur(A, r, c+half, half)
    # 2 사분면 재귀
    recur(A, r+half, c, half)
    # 4 사분면 재귀
    recur(A, r+half, c+half, half)
    print(')', end='')
        

n = int(input())
arr = [
    tuple(map(int, list(input())))
    for _ in range(n)
]

recur(arr, 0, 0, n)

```

## Phase2. 피드백

아래는 쿼드 트리(BOJ 1992) 문제를 해결한 코드와 그에 대한 상세 피드백입니다.

1. 전체 코드 리뷰

제시하신 코드는 다음과 같습니다:

```python
def is_base(A: list, r: int, c: int, n: int):
    """A 배열의 r, c를 시작점으로 하는 n×n 영역의 모든 원소를 합한다.
       합이 0이면 모두 0, n^2이면 모두 1, 그 외에는 -1을 반환."""
    pixels = 0
    for i in range(r, r+n):
        for j in range(c, c+n):
            pixels += A[i][j]
    if pixels == 0:          # 모두 0
        return 0
    elif pixels == n**2:     # 모두 1
        return 1
    return -1                # 0, 1 섞여 있음

def recur(A: list, r: int, c: int, n: int):
    pixels = is_base(A, r, c, n)
    if pixels != -1:
        print(pixels, end='')  # 압축 결과(0 또는 1)를 바로 출력
        return

    # 0,1이 섞여 있으므로 4등분
    half = n // 2
    print('(', end='')

    # [1] top-left
    recur(A, r, c, half)
    # [2] top-right
    recur(A, r, c + half, half)
    # [3] bottom-left
    recur(A, r + half, c, half)
    # [4] bottom-right
    recur(A, r + half, c + half, half)

    print(')', end='')


n = int(input())
arr = [tuple(map(int, list(input()))) for _ in range(n)]

recur(arr, 0, 0, n)
```

•	is_base 함수: 주어진 구역(r,c 부터 n×n)을 순회하며 합이 0이면 전부 0, 합이 n^2이면 전부 1, 섞여 있으면 -1.

•	배열에 0과 1밖에 없으므로, 합을 통해 “모두 0 or 모두 1”을 빠르게 판별할 수 있습니다.

•	recur 함수:

1.	is_base로 현재 구역이 전부 0 혹은 전부 1인지 확인.

2.	전부 같은 값이면(0 또는 1) 바로 출력.

3.	아니면 4개로 쪼개어 각각 재귀 호출하고, 사이에 괄호를 출력.

정상 동작 및 출력 순서

•	쿼드 트리 문제에서 요구하는 순서(왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래)대로 재귀가 진행되므로 문제 사양과 일치합니다.

•	출력 형식((0(0011)(0(0111)01)1))도 괄호를 열고 닫는 순서가 맞다면 정상적인 결과를 얻습니다.

2. 세부 피드백

2.1 사분면(쿼드) 순서와 주석

코드에서 사분면을 호출하는 순서는:

1.	recur(A, r, c, half) → top-left

2.	recur(A, r, c+half, half) → top-right

3.	recur(A, r+half, c, half) → bottom-left

4.	recur(A, r+half, c+half, half) → bottom-right

그런데 주석에서 “1사분면, 3사분면” 식으로 표현하셨다면, 수학적 좌표계나 일반적 쿼드트리 표기와 약간 다를 수 있어서 혼동될 여지가 있습니다.

•	보통 “1사분면(top-left), 2사분면(top-right), 3사분면(bottom-left), 4사분면(bottom-right)”라는 식으로 명명하면, 순서와 주석이 어긋날 수 있습니다.

•	문제에서 요구하는 처리 순서는 “왼위, 오른위, 왼아래, 오른아래”이므로, 코드처럼 명확히 주석을 달아두면 좋습니다(예: “top-left”, “top-right”, “bottom-left”, “bottom-right”).

2.2 시간 복잡도: 모든 분할 시 매번 합 계산

•	현재 코드는 매 분할마다 n×n 원소를 전부 순회(is_base)하고, 0/1 판별 후 필요시 4분할을 합니다.

•	최악의 경우(모두 서로 다른 패턴)에는 각 분할마다 n×n을 스캔 → 분할이 log(n) 단계(2차원적)로 진행 → 대략 O(n^2 log n) 이 될 수 있습니다.

•	N 최대 64 정도라면 전혀 문제 없고, 일반적인 BOJ 1992 제한(N ≤ 64) 안에서는 충분히 빠릅니다.

•	만약 N이 더 커진다면 프리픽스 합(2D prefix sum) 등을 이용해 서브 구역의 합을 O(1)에 구하면 더 효율적이긴 하지만, 이 문제에선 필요 없습니다.

2.3 “모두 같은 값” 판별하는 다른 방법

•	합을 사용하지 않고, “첫 번째 원소를 기준으로 전부 비교”해서 다른 값이 하나라도 나오면 분할” 하는 식도 있습니다:

```python
first_val = A[r][c]
all_same = True
for i in range(r, r+n):
    for j in range(c, c+n):
        if A[i][j] != first_val:
            all_same = False
            break
    if not all_same:
        break

if all_same:
    print(first_val, end='')
    return
# else 분할
```

•	성능상 큰 차이는 없고(역시 O(n^2)), 0/1만 다루는 문제에서는 합을 통해 n^2과 비교하는 방법이나, 모든 값이 동일한지 비교하는 방법이나 자유롭게 선택 가능합니다.

2.4 출력 방식(문자열 vs print)

•	현재는 함수 내에서 print(..., end='')로 바로바로 출력하고 있습니다.

•	BOJ 환경에서는 이렇게 해도 문제 없지만, 문자열을 모아 마지막에 한 번에 출력하는 방식을 선호하는 경우도 있습니다(성능 및 유지보수).

•	원하시면 return 값으로 문자열을 넘기고 최종에 print(result_str)를 한 번에 찍는 방식으로 바꿀 수도 있습니다.

예시 (문자열 합치는 버전):

```python
def quad_tree(A, r, c, n):
    val = is_base(A, r, c, n)
    if val != -1:
        return str(val)
    half = n // 2
    top_left = quad_tree(A, r, c, half)
    top_right = quad_tree(A, r, c + half, half)
    bottom_left = quad_tree(A, r + half, c, half)
    bottom_right = quad_tree(A, r + half, c + half, half)
    return "(" + top_left + top_right + bottom_left + bottom_right + ")"
```

이렇게 하면 마지막에 print(quad_tree(A, 0, 0, n))로 깔끔하게 한 번에 출력 가능합니다.

3. 결론 정리

1.	코드 기능: 요구 사항대로 잘 동작합니다.

2.	사분면 순서: 문제에서 제시한 “왼위, 오른위, 왼아래, 오른아래” 순서를 정확히 준수하면 됩니다.

3.	시간 복잡도: N=64 이하라면 현재 구현(매 분할 시 n×n 스캔)도 성능상 충분합니다.

4.	출력 방식: 지금처럼 print를 재귀 안에서 바로 쓰는 것도 문제 없지만, 문자열을 합쳐서 한 번에 출력하는 패턴도 좋습니다.

전체적으로 “쿼드 트리” 문제 의도에 맞는 전형적인 재귀 구현이며, 로직은 완벽하게 작성되었다고 볼 수 있습니다.

주석과 변수명만 조금 더 명확하게 정리하면, 가독성과 유지보수성이 좋아질 것입니다. 축하드립니다!

# 재귀: 이진 검색 트리 

https://www.acmicpc.net/problem/5639

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

## Phase1. 누더기 코드 

```python
"""
1. 문제 읽기 
그냥 재귀를 하는데, 후위는 빠져나올 때 프린트 하면 됨.
그런데 입력이 전위순회 결과라서. 아 그냥 빈 배열 하나 만들고, 
전위 순회 타이밍에 그냥 삽입하면 안 되나, 안 된다. 완전 이진 트리가 아니다!

2. 문제 풀기

3. 수도 코드

4. 코드 구현
"""

import sys


def post_search(idx: int):
    global arr
    """크기가 n인 배열의 idx 번째 요소를 후위순회 합니다."""
    # 만약 왼쪽 자식이 존재 하면
    if idx >= len(bt): return
    post_search(idx*2+1)
    post_search(idx*2+2)
    if bt[idx] != 0: print(bt[idx])


def insert_binary_tree(val: int):
    print(f'inserting: {val}')
    global bt
    if bt[0] == 0: 
        bt[0] = val # 첫 번째 값 삽입
        return
    ptr = 0
    while True:
        print(f'current ptr: {ptr}')
        if val < bt[ptr]: # 왼 자식으로 삽입
            if bt[ptr*2+1] != 0: # 왼쪽 자식이 존재하면 그쪽으로 포인터 이동
                ptr = ptr*2+1
                print('moving to left child')
                continue
            else: #왼쪽 자식이 없으면 거기에 삽입
                bt[ptr*2+1] = val
                print(f'inserting {val} as left child of {bt[ptr]}')
                break
        elif val > bt[ptr]: # 오른 자식으로 삽입
            print(f'{val} > {bt[ptr]}')
            if bt[ptr*2+2] != 0:
                ptr = ptr*2+2
                print('moving to right child')
                continue
            else:
                bt[ptr*2+2] = val
                print(f'inserting {val} as right child of {bt[ptr]}')
                break


arr = []
for line in sys.stdin:
    # line은 '\n'을 포함하므로 line.strip()으로 개행 제거
    arr.append(int(line.strip()))

n = len(arr)
bt = [0]*(n**4) # 모두 양의 정수만 입력됨
for a in arr:
    insert_binary_tree(a)

post_search(0)


"""
이슈: binary search tree에 값 인서트가 이상하게 됨
Phase1.
환경: 파이썬
로그: '50', '30', '98', '24', '5', '52', 0, 0, '28', '45', 0, 0, '60'
최근 변경 사항: 이진트리 삽입 부분 구현

def insert_binary_tree(val: int):
    print(f'inserting: {val}')
    global bt
    if bt[0] == 0: 
        bt[0] = val # 첫 번째 값 삽입
        return
    ptr = 0
    while True:
        if val < bt[ptr]: # 왼 자식으로 삽입
            if bt[ptr*2+1] != 0: # 왼쪽 자식이 존재하면 그쪽으로 포인터 이동
                ptr = ptr*2+1
                continue
            else: #왼쪽 자식이 없으면 거기에 삽입
                bt[ptr*2+1] = val
                break
        elif val > bt[ptr]: # 오른 자식으로 삽입
            if bt[ptr*2+2] != 0:
                ptr = ptr*2+2
                continue
            else:
                bt[ptr*2+2] = val
                break
Phase2.
확인: 오른쪽 자식으로 가는 부분이 좀 이상한 거 같은데. 문자열을 그대로 쑤셔박으니 그렇지!

moving to left child
current ptr: 1
5 > 30
inserting 5 as right child of 30

로그 확인 결과 이런 기가막힌 연산을 하고 있었음을 확인. 이건 그냥 디버거 봤으면 더 빨리 캐치했을 거 같기도 하고.
이슈방지위원회, 줄여서 이방위를 열어야겠다.
시도: 정수형으로 입력값 캐스팅
결과: 해결

이슈: 후위순회가 안 돼요
Phase1. 
환경: 파이썬
로그: 잘못된 후위 순위 검색 결과
최근 변경 사항: 없음

Phase2.
확인: 재귀 과정을 확인하고, 출력문을 찍으면 좋을 적절한 타이밍을 탑다운 방식으로 분석해보기.
시도: 그냥 배열과 인덱스를 통째로 잘못 참조하고 있었음. 
결과 분석: 해결. 코드의 로직은 구현 완료. 그런데 누더기로 작성한 자료구조 덕분에 메모리 초과가 발생

"""
```

### 로그 없는 버전

```python
"""
1. 문제 읽기 
그냥 재귀를 하는데, 후위는 빠져나올 때 프린트 하면 됨.
그런데 입력이 전위순회 결과라서. 아 그냥 빈 배열 하나 만들고, 
전위 순회 타이밍에 그냥 삽입하면 안 되나, 안 된다. 완전 이진 트리가 아니다!

2. 문제 풀기

3. 수도 코드

4. 코드 구현
"""

import sys


def post_search(idx: int):
    global arr
    """크기가 n인 배열의 idx 번째 요소를 후위순회 합니다."""
    # 만약 왼쪽 자식이 존재 하면
    if idx >= len(bt): return
    post_search(idx*2+1)
    post_search(idx*2+2)
    if bt[idx] != 0: print(bt[idx])


def insert_binary_tree(val: int):
    global bt
    if bt[0] == 0: 
        bt[0] = val # 첫 번째 값 삽입
        return
    ptr = 0
    while True:
        if val < bt[ptr]: # 왼 자식으로 삽입
            if bt[ptr*2+1] != 0: # 왼쪽 자식이 존재하면 그쪽으로 포인터 이동
                ptr = ptr*2+1
                continue
            else: #왼쪽 자식이 없으면 거기에 삽입
                bt[ptr*2+1] = val
                break
        elif val > bt[ptr]: # 오른 자식으로 삽입
            if bt[ptr*2+2] != 0:
                ptr = ptr*2+2
                continue
            else:
                bt[ptr*2+2] = val
                break


arr = []
for line in sys.stdin:
    # line은 '\n'을 포함하므로 line.strip()으로 개행 제거
    arr.append(int(line.strip()))

n = len(arr)
bt = [0]*(n**2) # 모두 양의 정수만 입력됨
for a in arr:
    insert_binary_tree(a)

post_search(0)


```

## Phase2. 피드백 및 반성

### 반성

1. 인덱스 이름, 함수 이름만 좀 길게 써도 많은 삽질을 피할 수 있을 거 같다. 구체적으로 쓰면 인지가 되는데, 그냥 알파벳만 작성하면 개념이 안 잡히고, 잘못 적힌 인덱스도 알아보기 어렵다.
1. 이진 탐색 트리 자료구조를 전혀 구현하지 못하겠다. 위의 배열을 활용한 구조는 공간복잡도가 정신 나간다.
1. 입력 값의 개수가 주어지지 않고 입력마다 개행문자가 있는 경우의 입력 매커니즘을 잘 모르겠다. sys.stdin은  line1\n, line\n 이렇게 주어지고, 각 줄에 주어진 입력을 이터레이션하며 line.strip() 작업을 하여 whitespace를 제거하는가?
### 피드백

아래 내용은 이진 검색 트리(BST) 문제(BOJ 5639)를 풀 때 흔히 겪는 문제점(배열 인덱스로 구현 시 메모리 낭비, 전위순회 입력에서 트리를 복원하는 방법 등)에 대한 피드백과, 권장 구현(노드 기반 + 재귀 복원) 예시입니다.

1. 현재 코드(배열 사용) 문제점과 개선 방향

1.1 배열 인덱스 기반 ‘완전이진트리’ 방식의 비효율성

•	현재 시도하신 방식은 “배열 인덱스를 이용해 왼쪽 자식 = 2i+1, 오른쪽 자식 = 2i+2” 구조를 흉내 내며 BST를 구성하고 있습니다.

•	BST가 편향되었을 때, n^2, 심지어 n^4 같은 큰 배열을 잡아야 하고, 실제로는 대부분 비어 있을 수 있어 메모리 낭비 가 심각합니다.

•	노드가 1만 개만 되어도, 완전이진트리 인덱스를 쓰려면 엄청난 크기의 배열이 필요해질 수 있습니다.

1.2 전위순회 결과로부터 BST 복원 시의 일반적인 접근

•	주어진 입력은 BST를 전위순회(Pre-order)한 결과입니다.

•	우리는 이 배열(전위순회 결과)로 트리를 복원한 뒤, 후위순회(Post-order) 결과를 출력해야 합니다.

•	가장 흔한 방법은 **“노드 기반(Node class) + 재귀”**로 직접 BST를 구성한 뒤, 후위순회를 수행하는 것입니다.

> 결론

2. 권장 구현: 노드 기반 BST 복원 + 후위순회

2.1 로직 개요

1.	입력: 전위순회 결과 preorder[] (예: 50, 30, 24, 5, 28, 45, 98, 52, 60, …)

2.	BST 구성: 전위순회 특성상,

•	첫 번째 원소 = 루트 값

•	이후 “루트보다 작은 값들”은 왼쪽 서브트리, “루트보다 큰 값들”은 오른쪽 서브트리

3.	하지만, 단순히 “작은 거 전부 왼쪽, 큰 거 전부 오른쪽”으로 구간을 나누면 최악 O(n^2).

•	문제에선 N 최대 10,000까지 가능.

•	다행히, **“BST 전위순회 배열”**에서 “루트보다 큰 값이 처음 나오는 지점”이 곧 오른쪽 서브트리의 시작 지점이 됩니다.

4.	더 효율적인 방법: 상한(bound)을 이용한 재귀. 전위 순회를 왼→오른쪽 순으로 탐색하며, “현재 만들어야 할 서브트리 값이 bound(부모보다 큰 값 한계)”를 넘어서면 stop 하는 기법이 자주 사용됩니다.

2.2 예시 코드: Bound 기법 (전위순회 → BST)

```python
import sys
sys.setrecursionlimit(10**9)  # 혹시 깊은 트리 대비

preorder = []
for line in sys.stdin:
    val = line.strip()
    if val == '':  # 공백 라인 방어
        continue
    preorder.append(int(val))

# 전위순회 리스트
n = len(preorder)

# 전위순회 배열을 재귀적으로 읽어가며 트리 복원
# index는 preorder를 순회하는 인덱스
index = 0

class Node:
    __slots__ = ('val', 'left', 'right')  # 메모리 절약 (선택사항)
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildBST(bound):
    """
    bound보다 큰 값이 나오면(= 현재 subtree 범위를 벗어남)
    재귀를 멈춘다.
    """
    global index
    if index >= n:  # 더 이상 원소가 없으면 None
        return None

    root_val = preorder[index]
    # 만약 현재 값이 bound보다 크면, 이 subtree에 속할 수 없음
    if root_val > bound:
        return None

    # 현재 값이 subtree에 속한다면, 노드 생성
    node = Node(root_val)
    index += 1

    # 왼쪽 서브트리: bound = node.val
    #   => node.val보다 큰 값이 나오면 왼쪽 subtree 불가
    node.left = buildBST(node.val)

    # 오른쪽 서브트리: bound = 상위 bound
    #   => "node.val < X <= bound" 범위의 값은 오른쪽 subtree
    node.right = buildBST(bound)

    return node

# 1) 트리 구성 (최대값을 아주 크게 잡는다)
root = buildBST(bound=10**10)  # 문제에서 값이 1,000,000까지 가능하므로 더 큰 수 잡기

# 2) 후위순회
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

postorder(root)
```

동작 설명

•	buildBST(bound) 함수는 preorder 배열을 왼→오른쪽으로 스캔(index 전역변수)하면서 노드를 생성합니다.

•	현재 노드값이 bound를 초과하면, “이 값은 상위(혹은 다른) 서브트리로 가야 한다” → None 리턴하여 재귀를 종료합니다.

•	이렇게 하면 전위순서에 맞춰 왼쪽 subtree(node.val을 bound로), 오른쪽 subtree(상위 bound 그대로) 순으로 채워나가면서도, 값이 범위를 벗어나면 자연스럽게 재귀를 종료해 “부모의 오른쪽 subtree”로 넘어갈 수 있습니다.

•	이 알고리즘은 각 노드가 정확히 한 번씩만 재귀 처리되므로, 최악의 경우(편향 트리)라도 O(n)에 가까운 성능을 냅니다(실제로는 평균 O(n), 특정 편향 패턴에서도 빠르게 동작).

> 이 로직은 **“BST 전위순회 + 상한(bound) 기법”**으로 알려진 전형적인 트리 복원 방법입니다.

3. 추가 사항

3.1 “입력 개수 미지정” → sys.stdin 사용 시

•	문제에서 입력 줄 수가 따로 안 주어지면, 보통 EOF까지 읽어야 합니다.

•	for line in sys.stdin: 사용 시, 빈 줄이나 개행을 처리하고 싶다면 line.strip() 후 조건 검사하면 됩니다.

3.2 파이썬 재귀 제한

•	기본적으로 파이썬 재귀 한도는 약 1000이므로, 노드가 1만 개 이상이고 편향 트리가 된다면 RecursionError 가 날 수 있습니다.

•	문제 5639에서는 최대 10,000개 입력이 가능하므로, sys.setrecursionlimit(10**9) 정도로 여유를 주는 게 안전합니다. (메모리 내에서 처리 가능)

3.3 후위순회 출력

•	문제 요구사항대로, 각 노드를 후위순회 시 방문할 때마다 출력하면 됩니다.

•	“print(node.val)”을 찍을 때 개행으로 구분하면 정답 포맷에 부합합니다.

3.4 “배열 인덱스를 좀 더 명확히…”에 대한 팁

•	변수명을 idx, start, end 등으로 길게 써주거나, 주석을 부지런히 달면 디버깅 시 혼선을 줄일 수 있습니다.

•	또한, (node-based)트리를 구성하면, “왼쪽·오른쪽”을 직관적으로 코드로 표현할 수 있어, 인덱스 연산 실수를 줄이는 데 도움이 됩니다.

4. 마무리

1.	문제(5639) 핵심: 전위순회 배열로부터 BST를 재구성 후, 후위순회 출력.

2.	가장 간단한 정석 접근: 노드 기반으로 트리를 만들고, 후위순회를 재귀로 구현.

3.	배열 인덱스 기반의 완전이진트리는 BST에는 비효율적(편향 트리 시 메모리 폭증).

4.	EOF 입력 처리:

```plain text
import sys
arr = []
for line in sys.stdin:
    val = line.strip()
    if val == '':
        continue
    arr.append(int(val))
```

이렇게 하면 파일 끝(EOF)까지 읽어들일 수 있습니다.

> 결론적으로,



