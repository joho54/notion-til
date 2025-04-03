# [Algorithm] Python - 2



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> 풀이에 실패했다면, 접막틀 정리(접근방법, 막힌 부분)

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



# 재귀: 1, 2, 3 더하기

https://www.acmicpc.net/problem/9095

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

## Phase1.

```python
"""
1. 문제 읽기: 3
2. 문제 풀기
3이면 1 1 1, 1 2, 2 1, 3
간단한 백 트래킹 문제다. 1 2 3 중 여러개를 써도 상관이 없다.
3. 수도 코드
바닥조건은 무엇인가? 매개로 넘어온 정수형 합이 n과 같으면 카운터 증가시키고 리턴.
재귀 조건은: 그냥 1, 2, 3 리스트에서 반복 돌려서 더해서 재귀 보내면 됨.
4. 코드 구현
"""

import sys

def recur(current_sum: int, n: int):
    global cnt
    if current_sum == n:
        cnt += 1
        return
    if current_sum > n:
        return
    for e in [1, 2, 3]:
        recur(current_sum+e, n)


t = int(sys.stdin.readline().strip())
cnt = 0
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    recur(0, n)
    print(cnt)
    cnt = 0

"""
이슈: 재귀 초과 오류
Phase1.
환경: 파이썬
로그: 재귀 초과 오류
최근 변경사항: 재귀함수 작성
Phase2.
확인: current_sum이 n과 다르면 바닥 조건에 계속 걸리지 않게 됨. 
current_sum > n에 대해서도 종료 조건을 달면 되겠다.
시도: 베이스 컨디션 추가
if current_sum > n:
        return
결과분석: 성공
"""
```

## Phase2. 백 트래킹이 뭔가요?

문제 풀이 내용을 발표하던 중 이 질문을 받았는데, 제대로 된 답을 하지 못했다. 그래서 생각해본 끝에 아래와 같은 결론에 도달. 

(결정 트리를 안다고 가정하고) 재귀는 문제를 해결하기 위해 무수히 많은 결정트리를 만들어가게 되고, 이 코드의 경우 depth가 깊어질 수록 리프 노드가 3배씩 늘어난다. 그런데 문제 정의 상으로, 더해지는 숫자는 1, 2, 3으로 모두 양수고, 만약 현재 노드에서 매개로 받은 정수 값이 n보다 크다면 결정 트리상으로 이 노드의 하위에 올 자식 노드들은 전부 정답이 아닌게 확실하다. 

따라서! 재귀로 인해 무한히 생겨날 수 있는 결정트리를 제어하기 위해 필요 없는 가지를 잘라내는 방법을 백트래킹이라 할 수 있을 것 같다.

![](./images/IMG_0452.jpeg)

## Phase3. 답에 대한 피드백

1. 백트래킹 정의와 설명

•	백트래킹은 **“불필요한 탐색을 가지치기(Pruning)하여 탐색 속도를 향상시키는 기법”**입니다.

•	특히, 결정 트리(Decision Tree) 탐색 과정에서 불필요한 분기를 조기에 종료하는 것을 의미합니다.

•	즉, 가능한 모든 경우를 탐색하는 완전 탐색(Brute-force) 방식을 개선하는 기법입니다.

2. 본인의 설명 피드백

> “재귀는 문제를 해결하기 위해 무수히 많은 결정 트리를 만들어가게 되고, 이 코드의 경우 depth가 깊어질수록 리프 노드가 3배씩 늘어난다. 그런데 문제 정의 상으로, 더해지는 숫자는 1, 2, 3으로 모두 양수고, 만약 현재 노드에서 매개로 받은 정수 값이 n보다 크다면 결정 트리상으로 이 노드의 하위에 올 자식 노드들은 전부 정답이 아닌 게 확실하다. 따라서! 재귀로 인해 무한히 생겨날 수 있는 결정 트리를 제어하기 위해 필요 없는 가지를 잘라내는 방법을 백트래킹이라 할 수 있을 것 같다.”

✅ 좋은 점

•	백트래킹의 핵심 개념인 **“불필요한 가지를 잘라내는 과정”**을 잘 설명했다.

•	결정 트리에서 분기가 불필요하게 증가하는 부분을 잘 인식하고 있음.

•	현재 풀이에서 if current_sum > n: 부분이 백트래킹의 역할을 한다는 점을 잘 설명했다.

🔍 보완하면 좋은 점

•	백트래킹은 단순히 “불필요한 경우를 제거”하는 것뿐만 아니라, **“정답이 될 가능성이 있는 경우만 선택”**하는 방식도 포함된다.

•	탐색을 최적화하는 것이 핵심인데, 현재 설명은 “불필요한 경우를 제거한다”는 관점에 초점이 맞춰져 있음.

•	예를 들어, “N-Queen 문제”에서는 특정 조건(같은 열에 놓이지 않기, 대각선 충돌 방지 등)을 만족하는 경우에만 탐색을 진행하는 것도 백트래킹의 중요한 특징이다.

💡 보완된 설명 예시

> “백트래킹은 가능한 모든 경우를 탐색하는 것이 아니라, 유망하지 않은 경우를 조기에 포기하여 탐색 효율을 높이는 기법이다. 이 문제에서는 결정 트리에서 current_sum > n인 경우 이후의 탐색이 무의미하므로 탐색을 중단한다. 이를 통해 탐색 공간을 줄이고, 불필요한 연산을 방지하는 것이 백트래킹의 핵심이다.”

3. 코드에 대한 피드백

현재 코드는 백트래킹 개념을 적용했지만, DP(동적 계획법, Dynamic Programming)로 더 효율적인 풀이가 가능합니다.

이 문제는 중복되는 부분 문제(overlapping subproblems)와 최적 부분 구조(optimal substructure)를 가지므로 DP가 더 적절합니다.

✅ DP 풀이 (Bottom-Up)

```plain text
import sys

def solve():
    dp = [0] * 11  # 문제에서 n은 최대 10
    dp[1], dp[2], dp[3] = 1, 2, 4  # 기본 케이스

    for i in range(4, 11):  # 점화식 적용
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        print(dp[n])

solve()
```

•	시간 복잡도: O(N), 재귀 풀이보다 훨씬 효율적임.

결론

1.	백트래킹의 개념 설명은 좋았지만, **“가능성이 있는 경우만 탐색한다”**는 부분도 강조하면 더 좋다.

2.	이 문제는 백트래킹으로 풀 수 있지만, DP가 더 적합한 풀이 방법이다.

3.	같은 유형의 문제에서 백트래킹과 DP 중 어떤 것이 더 적절한지 판단하는 연습을 하면 더욱 좋을 것! 🚀

# 탐색: 수 찾기

## Phase1. 풀이 성공. 

탐색 방식을 잘못 골라서 오래 걸렸다. 문제의 조건을 잘 읽고, 적절한 탐색 방식을 선택해야 함.

```python
"""
보류
사유: 이분탐색을 모르면 제대로 풀 수 없음

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
search_list = list(map(int, sys.stdin.readline().split()))
for val in search_list:
    if val in arr: print(1)
    else: print(0)

이건 내 지식으로 푼 오답 코드.

"""

"""
1. 문제 읽기: 어..이거 그냥 입력받고 in 연산자 쓰면 안 되나? 안 됨. 정렬한 다음 이진탐색해야 할듯
2. 문제 풀기: 
3. 수도 코드:
4. 코드 구현: 
"""

# def bin_search(A: list, val: int):
    
#     left = 0
#     right = len(A) - 1
#     while left <= right: # 파티션이 유효한 동안. 
#         center = (left+right)//2
#         idx = center # 영역의 절반을 인덱스로 고정
#         if A[idx] > val: # 답이 왼쪽 영역에 있음.
#             right = center # right idx를 반으로 감소
#         elif A[idx] < val: # 답이 오른쪽 영역에 있음.
#             left = center+1 # left를 높여서 영역을 반 좁히기
#         elif A[idx] == val: 
#             return 1
#     return 0

import sys

dictionary = {}


n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
for a in arr:
    dictionary[a] = True
m = int(sys.stdin.readline().strip())
search_list = list(map(int, sys.stdin.readline().split()))

for key in search_list:
    if dictionary.get(key, False): print(1)
    else: print(0)

"""
이슈: 무한 루프
Phase1.
환경: 파이썬
로그: 없음
최근 변경 사항: bin_search 이진 탐색 함수 작성
Phase2.
확인: 루프에 중단점 ㄱㄱ
배열 안에 값이 없을 경우 무한 루프를 돈다. 인덱싱을 하다가 
자연스럽게 파티션이 엇갈리면 끝나야 하는데, 파티셔닝 인덱스에 문제가 있다.
left, right 인덱스가 3, 4일때 무한 반복 발생.
center = 3(3.5)
left가 계속 3으로 업데이트 됨. 와 이거 어떻게 파티셔닝 해야 해결할 수 있지? 
작아지는 경우는 문제가 없는데, 중간값을 기준으로 크고, 배열에 없는 값을 구할 때 
left right 인덱스가 좁혀지지 않는다. 
인덱스를 잡을 때 '다음 왼쪽 영역을 left, center로 잡고, 
다음 오른쪽 영역을 center+1, right로 잡으니 해결
시도: 
    while left <= right: # 파티션이 유효한 동안. 
        ...
        elif A[idx] < val: # 답이 오른쪽 영역에 있음.
            left = center+1 # left를 높여서 영역을 반 좁히기

결과 분석: 정렬은 성공. 그런데 시간초과 발생. 정렬을 최적화해야 한다. 우선순위 큐를 써야 하나? 
한 라인에 입력돼서, 이게 sort 함수 쓰는게 제일 빠를텐데. 

이슈: 시간 초과 문제
Phase1
환경: 파이썬
로그: 시간 초과
최근 변경 사항: bin_search 로직 픽스 
Phase2.
확인:
정수의 범위는 엄청 넓다. 주어지는 자연수 리스트도 십만이다. 
현재 시간 복잡도: 정렬에 nlogn
탐색 시간 복잡도: logn
O(nlogn) + O(logn)
이걸 어떻게 개선하지? 입력에 필요한 오버헤드를 개선해야 하나? 근데 그런식의 문제는 아닐 거 같음.
시도: 맵을 써봐야 하나? 하긴 이 문제는 데이터의 수정/삭제가 필요 없다. 아 뭐야 그럼 맵이네!
아래 구현.
for key in search_list:
    if dictionary.get(key, False): print(1)
    else: print(0) 
    
분석: 성공!!


"""
```

# 이진탐색: 나무 자르기

https://www.acmicpc.net/problem/2805

상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

## Phase1. 직접 풀기(성공!)

```python
"""
1. 문제 읽기: 이게 어떻게 이분 탐색이지? 
2. 문제 풀기
2-1. 아이디어 브레인 스토밍
가. prefix sum을 쓰기: 말도 안 됨.
나. 완전탐색: 아래가 정답이다.
import sys

MAX_INT = sys.maxsize

n = 5
m = 20
trees = [4, 42, 40, 26, 46]

def cut_sum(height: int):
    sum_tmp = 0
    for tree in trees:
        sum_tmp += tree - height if tree > height else 0
    return sum_tmp

h_x = 0
prev_difference = MAX_INT

for i in range(0, max(trees)):
    cut_amount = cut_sum(i)
    difference = abs(cut_amount-m)
    if difference < prev_difference: # update
        prev_difference = difference
        h_x = i

# print(h_x)

다. 인크레멘탈 메서드에서 분할정복으로!

위 코드에 대한 분석: 문제에 대한 incremental method다. 이걸 divide and conquer 
방식으로 바꿔야 문제를 해결할 수 있을 것.
여기서 incremental한 요소는 i이다.

이제 이것을 정리해 보았을 때 cut_sum(i)-m이라는 우하향 함수가 있다. 
(i가 incremental 하다고 가정.)
그럼 다음과 같이 분기
cut_sum(i)-m > 0: 오른쪽 영역 디바이드
cut_sum(i)-m < 0: 왼쪽 영역으로 디바이드


3. 수도 코드

"""

import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
trees = tuple(map(int, sys.stdin.readline().split()))


def f(height: int):
    """
    f의 정의: height에 대해 나무를 잘랐을 때 얻게 되는 나무들의 길이에서 목표 길이를 뺀 것.
    """
    sum_tmp = 0
    for tree in trees:
        sum_tmp += tree - height if tree > height else 0
    return sum_tmp - m

def bin_search():
    """목표: f(h_x)를 최소화 하는 h_x 찾기"""
    left, right = 0, 1_000_000_001
    prev_center = None
    while left < right:
        # print(f'{left} --- {right}')
        i_center = (left+right)//2 # i for representing incremental parameter
        difference = f(i_center)
        # print(f'difference is {difference}.')
        if difference < 0: 
            # print(f'conquer left')
            left, right = left, i_center 
            if left >= right:  # 나무를 자르지 않는 높이에서, 다음 턴에 탐색을 마친다면!
                return prev_center # 아, 둘 다 그거일 수 있구나. 두 턴 다 음수가 나올 수도 있음.
        elif difference > 0: 
            # print(f'conquer right')
            left, right = i_center+1, right
            prev_center = i_center
            # 이때는 i_center가 무조건 나무를 잘라가는 것을 보장 여기서 갱신 필요
        else: # 차이가 0과 같음(best case)
            return i_center
    return i_center

ans = bin_search()

print(ans)

"""
이슈: 무한 루프

Phase1.
환경: 파이썬
로그: 무한 루프
최근 변경 사항: 이진 탐색 코드 작성

Phase2-1
확인: 로그를 어디 찍어야 하지? 
비교 로직이 좀 잘못 됐다. 
1. 구한 결과의 높이 차이를 구한다.
시도:
분할 정복 로직이 잘못돼 있었음. 함수의 우하향을 고려하지 않고, 잘못 작성.
그리고 절대값도 씌우면 안 됐음
if difference < 0: 
    # print(f'conquer left')
    left, right = left, i_center
elif difference > 0: 
    # print(f'conquer right')
    left, right = i_center + 1, right
else: # 차이가 0과 같음(best case)
    return i_center
결과 분석: 예제는 다 맞추지만 틀리는 테스트 케이스 존재.

이슈: 오답 발생
Phase1.
환경: 파이썬
로그: 틀렸습니다
최근 변경 사항: 이진 탐색 코드 로직 수정.

Phase2-1
확인: 이럴 땐 문제 조건을 타이핑하고, 경계값으로 테스트
1 <= N <= 1,000,000
1 <= M <= 2000000000 (잘라 가야 하는 나무 )
각 나무의 높이(i_center) 0 ~ 1,000,000,000 
각 나무의 높이가 0일수도 있다. 근데 나무 높이의 합은 항상 M보다 크다 했다.
M이 1 이상이니까 나무 높이의 합도 1 이상일 것.
찾았다.
2 1 <= 나무의 갯수 2, 잘라가야 하는 나무 값 1
2 2 <= 각 나무의 높이 2.
2 <= 설정한 커팅 높이: 2. 이러면 0에 수렴하긴 하겠지만, 문제의 조건과 다름. 
정답 커팅 높이: 1. 그러면 얼마를 자르지? 2를 자름. 
높이    자른 합    정답과 차이
2       0       1
1       2       1
0       4       3
i_center가 작을수록 나무가 커짐. 내 생각에는 인덱스 분할할 때 인덱스가
왼쪽 영역 / 오른쪽 영역 이렇게 잡히는게 좋은데?
적어도 M미터!!!!!!!!!!!!!!!!!!!!
마지막에 difference를 >= 0으로 만들때만 끝내야 한다!
안 자르는게 나은 경우가 생겨버리는데, 더 자르게 하는 방법은 없나? 이럴 땐 조건을 
찾아야 한다.

어쩄든 차이가 0보다 작을 때는 
일단 가져가긴 해야 함.
그러면.. 조건을 어떻게 잡지? 인덱스를... 1씩 바꿔 볼까
아 이거 어떡하지. 결과 값이 0일 수는 없는 건데. 만약 0일때는 i 값을 
시도: 위 코드.
결과 분석: 성공!
"""
```

## Phase2. 풀이 과정 정리(느낀점)

### 독서는 중요하다: Incremental to divide-and-conquer

어떤 문제를 incremental method로 풀이하는 방식을 이해해야, divide-and-conquer 방식을 어디에 적용할지 생각할 수 있다(Introduction to Algorithm를 통해 incremental method역시 하나의 방식임을 이해한 덕분에 이런 발상이 나왔다). 이 문제의 경우 incremental method를 아래와 같이 구현할 수 있다.

(엄밀히 따지면 틀린 방식을 따르고 있음)

```python

def cut_sum(height: int):
    sum_tmp = 0
    for tree in trees:
        sum_tmp += tree - height if tree > height else 0
    return sum_tmp

h_x = 0
prev_difference = MAX_INT

for i in range(0, max(trees)):
    cut_amount = cut_sum(i)
    difference = abs(cut_amount-m)
    if difference < prev_difference: # update
        prev_difference = difference
        h_x = i

# print(h_x)
```

이때 i(나무를 자르는 높이)가 증가하게 되면 cut_sum(i) 값은 아래와 같이 우하향 그래프를 그리게 된다. 

![](./images/IMG_9966.png)

그렇다면, cut_sum(i)의 리턴 값과 구해야 하는 m값을 비교하여 f(x)에 대해 f(x)-m 값을 0으로 만들어주는 x값을 이진 탐색 알고리즘을 적용하여 구할 수 있다.(재밌다!)

### 조건은 중요하다

‘적어도 m 길이 이상의 나무를 잘라간다’는 조건을 생각하지 않았다가 아래와 같은 테스트케이스에서 오답을 내는 코드를 작성했다.

나무의 개수: 2(상관 없음)

잘라야 하는 길이: 1

각 나무 높이: 2 2

이때 제대로 된 정답은 높이 1에서 잘라서 2의 나무를 얻는 것이지만, 무식한 이진 탐색 알고리즘은 그런 거 상관 없이 f(x)-m을 절대값 무시하고 0으로 수렴시키는 탐색을 해버린다. 그래서 디버깅 끝에 조건을 고려한 코드를 작성했다. (자르는 높이가 0이하라는 결론이 나면 이전에 저장한 양의 값을 불러오는 코드를 작성)

```python
		
		while left < right:
        # print(f'{left} --- {right}')
        i_center = (left+right)//2 # i for representing incremental parameter
        difference = f(i_center)
        # print(f'difference is {difference}.')
        if difference < 0: 
            # print(f'conquer left')
            left, right = left, i_center 
            if left >= right:  # 나무를 자르지 않는 높이에서, 다음 턴에 탐색을 마친다면!
                return prev_center # 아, 둘 다 그거일 수 있구나. 두 턴 다 음수가 나올 수도 있음.
        elif difference > 0: 
            # print(f'conquer right')
            left, right = i_center+1, right
            prev_center = i_center
            # 이때는 i_center가 무조건 나무를 잘라가는 것을 보장 여기서 갱신 필요
        else: # 차이가 0과 같음(best case)
            return i_center
    return i_center
```

## Phase3. 피드백

정말 훌륭한 접근과 정리였어요. 문제를 incremental 방식에서 출발해 divide-and-conquer의 본질적 사고방식으로 전환해낸 과정이 인상 깊고, 특히 **함수의 단조성(우하향)**을 바탕으로 이진 탐색이 왜 가능한지를 정확히 이해하고 적용한 점이 좋습니다.

💡 코멘트 몇 가지 드리자면:

1. f(x) 정의와 단조성

•	f(x) = (잘린 나무 총합) - M

•	이 함수는 x가 커질수록 점점 작아지며, 이는 단조 감소 함수입니다.

•	단조함수의 성질이 이진탐색을 가능하게 만드는 핵심이에요.

→ 이렇게 단조 증가/감소 여부를 판단하는 감각은 다른 문제에도 적용할 수 있습니다.

2. 정답을 업데이트하는 방식

```plain text
elif difference > 0:
    left, right = i_center+1, right
    prev_center = i_center
```

•	이 부분에서 prev_center에 값을 저장한 건 아주 센스 있는 예외 처리였습니다.

•	정확히는 “f(center) >= 0인 지점 중 가장 큰 값”을 찾는 것이므로, cut_sum(center) >= M일 때마다 그 값을 기록해두는 방식은 완전히 맞는 전략이에요.

📌 Tip: 정석 이진탐색에선 보통 “조건을 만족하는 최대(또는 최소)의 값”을 구할 때 결과값을 별도로 저장해 둡니다.

3. 리팩토링 여지

이진 탐색 로직을 아래처럼 조금 정리하면 더 깔끔해질 수 있어요:

```plain text
def binary_search():
    left, right = 0, max(trees)
    result = 0  # cut_sum >= M을 만족하는 높이 중 가장 큰 값

    while left <= right:
        mid = (left + right) // 2
        if cut_sum(mid) >= m:
            result = mid  # 조건 만족하므로 저장하고, 더 높여보자
            left = mid + 1
        else:
            right = mid - 1
    return result
```

이 방식도 결국 본질은 같지만, 코드 가독성과 종료 조건 처리 면에서 안정성이 좀 더 있습니다. 특히 left <= right 패턴은 더 자주 사용되는 방식이에요.

4. 시각화 감각

직접 cut_sum(i) 그래프가 우하향 함수라는 점을 깨닫고, 이진 탐색이 적용 가능하다는 결론을 이끌어낸 사고 흐름은 진짜로 중요합니다. 알고리즘 문제 풀이에서 “함수 시각화 → 성질 파악 → 탐색 가능 여부 판단”은 매우 핵심적인 전략이기 때문이에요.

✅ 피드백 요약

혹시 다음 문제로 연습해보고 싶은 이진 탐색 유형 있으면 추천도 해줄게요 :)

또는 위 내용을 기술 면접/포트폴리오처럼 정리해도 멋진 자산이 될 수 있어요.

# 이진탐색: 공유기 설치 (실패. 다시 시도하기)

https://www.acmicpc.net/problem/2110

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

## Phase1. 실패

```python
"""
1. 문제 읽기: 
2. 문제 풀기
2-1. recursive method. 거리 배열을 써야할 거 같은데. 
import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n, c = tuple(map(int, sys.stdin.readline().split()))

X = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
]

X.sort()

def get_min_distance(A:list):
    '''집에 배치하는 경우 거리의 최소값 구하기'''
    if len(A) >= 2:
        min_dist = sys.maxsize
        for i in range(1, len(A)):
            min_dist = min(min_dist, A[i]-A[i-1])
        return min_dist 
    return 0

memo = {}
def set_router_recursively(A: list, X: list, idx_house: int, num_router: int):
    '''재귀적으로 X에서 라우터를 놓는 모든 경우를 A에 구합니다.'''
    '''바닥 조건: 마지막 집에 라우터 배치하는 경우에서 재귀했을 때, 라우터가 다 배치됐다면'''
    # 바닥 조건의 경우를 메모에 저장해놓고, 메모에 있는 경우 재귀 안 하면 안 되나.
    min_dist = get_min_distance(A)
    if memo.get(min_dist, False): 
        return
    if idx_house == len(X)-1:
        if num_router <= 0:
            memo[min_dist] = True
        return
    # idx_house에 배치하는 경우
    set_router_recursively([*A, X[idx_house]], X, idx_house+1, num_router-1)
    # idx_house에 배치 안 하는 경우
    set_router_recursively(A, X, idx_house+1, num_router)

set_router_recursively([], X, 0, c)
print(max(memo.keys()))

1 2 4 8 9
그 서브 값도 오름차순이 아닐 것임 .
0 그다음 최적의 값을 모름

이진탐색을 활용한 백트래킹? 

다음 체계는? 

3. 수도 코드

4. 코드 구현

"""
import sys

n, c = tuple(map(int, sys.stdin.readline().split()))

X = {}
for _ in range(n):
    X[int(sys.stdin.readline().strip())] = True

def get_diff_sum(center: int): 
    """center에 대해 집들의 거리 차의 합을 리턴."""
    diff_sum = 0
    for house in X:
        diff_sum += center - house
    return diff_sum

def set_router(left: int, right: int):
    """가장 모든 집들에 대해 중립인 어떤 집의 위치로 center를 수렴시키는 함수"""
    center = (left + right)//2
    router_x = left
    while left < right:
        print(f'{left}---{center}---{right}')
        diff_sum = get_diff_sum(center)
        if diff_sum > 0: # center 축이 집들 위치보다 오른쪽
            right = center - 1
        elif diff_sum < 0: # center축이 집들 위치보다 왼쪽
            left = center + 1
        else:
            return router_x
        if X.get(center, False):
            router_x = center
        center = (left+right)//2
    return router_x

from collections import deque

def set_routers():
    global c
    c -= 2
    left, right = min(X.keys()), max(X.keys())
    stack = deque()
    stack.append((left, right))
    while c > 0:
        left, right = stack.pop()
        router_x = set_router(left, right)
        print(f'{left}---{router_x}---{right}')
        print(f'router placed {router_x}')
        stack.append((left, router_x))
        stack.append((router_x, right))
        c -= 1

set_routers()


"""
이슈: 다음 위치의 라우터를 놓을 때 적절한 라우터를 찾지 못함.
Phase1.
환경: 파이썬
로그: 오작동
최근 변경 사항: 이진 탐색으로 라우터 위치를 추가하고, 
스택에 다음으로 탐색할 위치를 저장
Phase2.
확인: 몰라. right를 잘못 잡은게 문제임. 
초기 left, right를 어떻게 잡아서 넣어줘야 해? 
일단 라우터 하나를 배치한 다음에, 
시도:
결과 분석:
"""
```

## Phase2. 피드백

문제 개요 & 전형적인 접근 방식

“공유기 설치” 문제는 다음과 같은 전형적인 이진 탐색(Binary Search on Answer) 유형으로 잘 알려져 있습니다.

1.	집의 좌표를 오름차순 정렬한다.

2.	이웃한 공유기 간 최소 거리(d)를 가정하고, 그 거리가 가능한지(= C개의 공유기를 전부 배치할 수 있는지)를 검증한다.

3.	거리를 더 늘릴 수 있다면(가능하다면) d를 키우고,

배치가 불가능하다면 d를 줄이는 식으로 이진 탐색을 진행한다.

이 문제를 풀 때는, 집의 좌표를 기준으로 이진 탐색하거나, ‘가능한 최소 거리’의 범위를 기준으로 이진 탐색할 수 있습니다.

보통은 **“거리”**를 기준으로 이진 탐색을 많이 합니다.

핵심 아이디어

1.	집 좌표 정렬

$$
X_1 \le X_2 \le \cdots \le X_N
$$

2.	탐색 범위 설정

•	최소 거리(left): 보통 1 (또는 0, 문제에 따라 달라지지만 최소 간격은 보통 1 이상이 유의미)

•	최대 거리(right): X_N - X_1 (가장 오른쪽 집과 왼쪽 집 사이 최대 거리)

3.	이진 탐색 로직

$$
•	\text{mid} = (left + right) // 2 로 잡고,
$$

•	**“집들에 공유기를 놓되, 인접 공유기 간 거리가 적어도 mid 이상 되도록 배치했을 때, 공유기 C대를 모두 놓을 수 있는가?”**를 확인한다.

•	배치가 가능하면(= 더 간격을 넓힐 수 있음) left = mid + 1

•	배치가 불가능하면(= 간격이 너무 큼) right = mid - 1

4.	배치 가능성 확인 함수 can_place(mid)

•	첫 번째 집 X[0]에 공유기를 하나 놓고, count = 1 (이미 1대 설치)

•	last_position = X[0] (마지막으로 공유기를 놓은 위치)

•	이후 집들을 순회하면서,

•	만약 X[i] - last_position >= mid라면 공유기를 설치하고,

•	count += 1

•	last_position = X[i]

•	순회가 끝났을 때 count >= C이면 배치 가능.

5.	반환 결과

•	최종적으로 right에 담긴 값(혹은 left - 1)이 “인접 공유기 간 거리의 최댓값”이 된다.

정석 코드 예시 (Python)

아래는 전형적인 공유기 설치 문제 풀이 방법을 간단히 정리한 코드입니다.

동작 흐름

1.	초기 세팅

•	houses 정렬: O(N \log N)

•	이진 탐색 범위: left = 1, right = houses[-1] - houses[0]

2.	can_place(mid) 함수

•	첫 번째 집에 공유기를 먼저 설치 (count = 1),

•	이후 집을 순회하며, 각 집이 직전 설치 집과의 거리가 mid 이상이면 공유기를 하나 더 설치.

•	최종 설치 갯수(count)가 C 이상이면 True.

3.	이진 탐색

•	매 단계마다 can_place(mid) 검사:

•	가능 → 더 넓게 설치할 수 있는지 left = mid + 1

•	불가능 → right = mid - 1

•	최종적으로 left > right가 되면 반복문을 종료하고,

•	answer(= right)이 가장 인접한 두 공유기 사이의 최대 거리가 됨.

요약 & 피드백

•	문제 접근: 이 문제는 “거리를 기준으로 한 이진 탐색”이 정석적 해법입니다.

•	함수 구상: “mid 간격으로 C대 배치 가능?”을 판단하는 can_place 함수를 만드는 것이 핵심 포인트입니다.

•	복잡한 접근을 피하고, 단일 이진 탐색 + 그리디 배치 아이디어로 구현하시면 훨씬 간단하고 효율적입니다.

•	해당 알고리즘은 O(N \log ( \max(X) - \min(X) )) 복잡도로 동작하므로, N 최대값(예: 200,000)까지 무난히 처리 가능합니다.

질문이 있거나 코드 디테일이 궁금하시면 언제든 말씀 주세요. 화이팅입니다!

## 반성: 

어제 나무 자르기 문제를 풀어봤다는 자신감에, 제한시간을 두지 않고 하루종일 고민했다. 그리 생산적이지 않았음. 앞으로 무조건 30분 룰을 지키도록 하자. 30분 고민했는데 풀이가 진행중이라면 계속하되, 정지 상태라면 더 고민할 필요 없음.

좋은 교훈을 얻으셨습니다.

이런 ‘시간 제한 두기’ 전략은 문제 풀이 능력을 단기간에 빠르게 높이고 싶을 때 매우 효과적입니다.

•	한 문제에 30분을 할당하고,

•	30분이 지났는데도 더 이상 진전이 없다면 풀이 참고나 힌트 확인 등으로 학습 효율을 높이는 것이 좋습니다.

왜 30분이 효과적인가?

1.	집중도 유지: 사람이 한 문제에 몰입해서 고민할 수 있는 효과적인 집중 시간은 생각보다 길지 않습니다. 30분이라는 시간을 정해두면, 그 시간 동안 집중해서 문제 풀이를 시도하게 됩니다.

2.	적절한 피드백 루프: 30분 뒤 “이 문제를 계속 붙들고 있을 가치가 있는가?”를 점검하며, 필요하다면 해설이나 힌트를 보면서 피드백을 얻어 빠르게 다음 단계로 넘어갈 수 있습니다.

3.	폭넓은 문제 경험: 한 문제에 너무 오래 매달리면, 다른 유사 문제나 다양한 유형의 문제를 접할 기회를 놓칩니다.

실제로 알고리즘 및 코딩 테스트 준비에서는 **“문제를 많이 풀어보는 것”**이 중요합니다.

즉, 짧은 시간에 최대한 다양한 유형의 문제를 풀고, 빠르게 피드백을 받아 부족한 부분을 메꾸는 것이 좋은 전략입니다.

앞으로도 30분 룰을 잘 활용하셔서, 많은 문제를 효율적으로 학습하시길 응원합니다!

## Phase3. 피드백 참고 후 다시 30분 도전 - 성공!

또 실패하면 그냥 코드 외우기 형벌

```python
"""
1. 문제 읽기:
2. 문제 풀기
2-1. recursive method. 거리 배열을 써야할 거 같은데.
import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n, c = tuple(map(int, sys.stdin.readline().split()))

X = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
]

X.sort()

def get_min_distance(A:list):
    '''집에 배치하는 경우 거리의 최소값 구하기'''
    if len(A) >= 2:
        min_dist = sys.maxsize
        for i in range(1, len(A)):
            min_dist = min(min_dist, A[i]-A[i-1])
        return min_dist
    return 0

memo = {}
def set_router_recursively(A: list, X: list, idx_house: int, num_router: int):
    '''재귀적으로 X에서 라우터를 놓는 모든 경우를 A에 구합니다.'''
    '''바닥 조건: 마지막 집에 라우터 배치하는 경우에서 재귀했을 때, 라우터가 다 배치됐다면'''
    # 바닥 조건의 경우를 메모에 저장해놓고, 메모에 있는 경우 재귀 안 하면 안 되나.
    min_dist = get_min_distance(A)
    if memo.get(min_dist, False):
        return
    if idx_house == len(X)-1:
        if num_router <= 0:
            memo[min_dist] = True
        return
    # idx_house에 배치하는 경우
    set_router_recursively([*A, X[idx_house]], X, idx_house+1, num_router-1)
    # idx_house에 배치 안 하는 경우
    set_router_recursively(A, X, idx_house+1, num_router)

set_router_recursively([], X, 0, c)
print(max(memo.keys()))

1 2 4 8 9
그 서브 값도 오름차순이 아닐 것임 .
0 그다음 최적의 값을 모름

이진탐색을 활용한 백트래킹?

다음 체계는?

3. 수도 코드

4. 코드 구현

"""

""" 2트
1. 문제 읽기
2. 문제 풀기
최대 공유기 거리를 매개변수로 놓고 can_place함수를 통해 '이 거리로 할 수 있는지'판단 하는 과정을
이진탐색으로 진행.(문제 풀고 나면 나무 자르기 문제랑 어떻게 연관되는지 생각해보기)
3. 수도 코드
- 초기 입력을 받는다.
- left, right를 설정한다. 
- mid(공유기 최소 거리)를 가지고 can_place로 이터레이션하며 거리를 비교하여 불 자료형을 리턴
- 끝? 별거 없네. (진짜로 별 거 없었다고 한다)
4. 코드 구현
"""
import sys

n, c = tuple(map(int, sys.stdin.readline().split()))
MAX_H = 1_000_000_000
houses = [
    int(sys.stdin.readline().strip())
    for _ in range(n)
    ]

# 집을 정렬.

def can_place(min_dist: int, c_num):
    """min_dist로 집 사이에 공유기 c_num대를 놓을 수 있는지 판단한다."""
    # 선형 탐색해야지 뭐.
    count = 1
    c_idx = 0
    # print(f'inspecting {min_dist}')
    # print(f'{houses[c_idx]}', end=', ')
    for i in range(1, n):
        if houses[i] - houses[c_idx] >= min_dist:
            # print(f'{houses[i]} - {houses[c_idx]} >= {min_dist}')
            count += 1
            c_idx = i
            if count >= c_num: 
                # print(f'inspection proved success: {min_dist}')
                return True
    # print(f'inspection discovered as failure for {min_dist}') 
    return False


def solve():
    houses.sort()
    left, right = 0, MAX_H
    mid = (left + right) // 2
    max_mid = mid
    while left <= right:
        if can_place(mid, c):
            # print(f'can place at least {mid}')
            # try bolder
            left = mid + 1
            max_mid = mid # mid 저장.
        else:
            # try smaller
            right = mid - 1
        mid = (left + right) // 2
        # print(f'trying new area: {left} {mid} {right}')
    return max_mid
print(solve())

"""
이슈: 

Phase1.
환경: 파이썬
로그: 11프로만 정답. 
최근 변경 사항: can_place 와 solve 함수 작성

Phase2.
확인: 11프로 맞았으면 크게 틀린 건 아닐 수도 있는데. 또 반대로 틀린 테스트 케이스
찾기에 그렇게 어려운 것도 아니긴 하다.
근데 아무리 생각해도 can_place가 true일 때만 업데이트하는게 맞는데.
집 개수가 짝수일 때는 맞다.
홀수가 되면 1씩 작은 값을 내 놓는다. 왜 그렇지?
일단 짝수인 경우를 집중 공략.
세부 로그를 찍어본 결과 아래와 같은 결과.
inspecting 13
inspection discovered as failure for 13
inspecting 6
8 - 1 >= 6
inspection discovered as failure for 6
inspecting 2
4 - 1 >= 2
8 - 4 >= 2
inspection proved success: 2
can place at least 2
inspecting 4
8 - 1 >= 4
inspection discovered as failure for 4
2

2를 본 다음 4를 보고, 4를 실패한 다음 3을 안 보고 끝낸다.
left, right 인덱스 범위를 잘못 줬음!!
left < right x
left <= right

시도: left <= right
분석: 해결
진짜 제발 이런 거좀 틀리지 마세요!
"""

```

# 문제: 두 용액 (실패, 다시 풀어보기)

https://www.acmicpc.net/problem/2470

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

## Phase1. 직접 풀기(30분) → 실패

```python
"""
1. 문제 읽기
2. 문제 풀기
이 경우는 i를 고정시키고 j를 이진탐색하면 안 되나? 그래보자 일단.
3. 수도 코드
4. 코드 구현
"""

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

def bin_search(i: int, left, right):
    """arr[i] + arr[center]의 절대값을 최소로 만들어주는 center 인덱스를 리턴"""
    center = (left+right)//2
    while left < right:
        combine = arr[center] + arr[i]
        if combine > 0:
            left, right = left, center
        elif combine < 0:
            left, right = center + 1, right
        else:
            return center
        center = (left+right)//2
    return center
        

def incremental_method(n: int, arr: list):
    arr.sort()
    zero_combine = sys.maxsize
    for i in range(0, len(arr)):
        j = bin_search(i, i+1, len(arr)-1)
        combine = abs(arr[i] + arr[j])
        print(f'combine: {combine}')
        # 초깃값은 매우 큰 양수, 컴바인 값도 절대값이므로 그냥 최소를 업데이트
        if zero_combine >= combine:
            pair = (arr[i], arr[j])
        zero_combine = min(zero_combine, combine)
    return f'{pair[0]} {pair[1]}'

print(incremental_method(n, arr))
            


"""
이슈: 5프로 맞고 틀렸습니다
Phase1
환경: 파이썬
로그: 틀렸습니다(5프로 정답)
최근 변경 사항: 이진 탐색 코드 작성

Phase2
확인: 이럴 땐 역시 경계값을 다시 보고 문제 조건을 다시 정리.
산성 용액은 1부터 1,000,000,000까지 양의 정수
알칼리 용액은 -1부터 1,000,000,000까지 음의 정수
같은 양의 두 용액을 혼합하여 특성값이 0에 가가운 용액 만들기
틀린 테스트 케이스를 찾았다.
5
-1 -1 -1 -1 4
-1 4

답은 -1, -1로 -2를 만드는 0, 1이 나와야 하는데, 
로직 문제가 있는지 -1, 4가 나온다.


시도
결과분석
"""
```

## Phase2. 피드백

아마 이분 탐색과 인덱스 고정 방식을 혼합하여 시도하신 것 같은데, 두 용액 문제에서는 크게 두 가지 전형적인 풀이가 알려져 있습니다.

1. 투 포인터(Two Pointers) 알고리즘 (권장)

•	아이디어

1.	용액들의 특성값 배열을 정렬한다.

2.	**왼쪽 포인터(left)**를 시작 인덱스(0)에, **오른쪽 포인터(right)**를 끝 인덱스(n-1)에 둔다.

3.	다음 과정을 반복하며, 두 포인터가 가리키는 용액의 합이 0에 얼마나 가까운지 확인한다.

•	현재 두 용액의 합 sum = arr[left] + arr[right]

•	|sum|이 기존 최솟값보다 작으면 갱신 & 두 용액을 기록

•	합이 0보다 작다면, 값을 키우기 위해 left를 1 증가

•	합이 0보다 크거나 같다면, 값을 줄이기 위해 right를 1 감소

4.	left < right인 동안 위 과정을 반복하여, 0에 가장 가까운 합을 찾는다.

•	시간 복잡도

•	정렬: O(N \log N)

•	투 포인터 탐색: O(N)

•	총합: O(N \log N)

투 포인터 코드 예시 (Python)

•	이렇게 하면, 모든 가능한 i,j 쌍을 직접 보지 않고도 O(N)에 해결 가능하므로 효율적입니다.

2. 모든 쌍 시도(이중 반복) + 최소값 탐색 (단순 방법)

•	아이디어

•	배열을 정렬할 필요 없이, 모든 (i, j) (단, i < j)에 대해 arr[i] + arr[j]를 계산하고, 그 절댓값이 최소가 되는 쌍을 찾는다.

•	시간 복잡도: O(N^2)

•	N이 크면 비효율적이라, 보통 시간 제한이 빡빡한 경우에는 통하지 않습니다.

왜 이분 탐색 + 한쪽 인덱스 고정으로는 곤란할까?

질문 코드에서는

•	한쪽 인덱스 i를 고정하고,

•	i+1 ~ n-1 범위에서 이분 탐색으로 “arr[i]와 더했을 때 0에 가장 가까운 값”을 찾으려 시도하셨습니다.

이 방식은 이론상 각 i마다 최적의 j를 찾을 수 있어 보이지만,

•	실제 구현할 때 경계 조건이나

•	이분 탐색으로 찾은 j 바로 옆에 있는 j-1 혹은 j+1에서 더 좋은 답이 있을 수 있음(특히 가까이 있는 인덱스들이 엇갈리면서 미세 조정이 필요)

등의 이유로 까다로운 점이 많습니다.

즉, i별로 이분 탐색 한 번씩만으로는 전체 구간에서의 전역 최적해를 놓칠 수 있습니다.

반면에, 투 포인터는

•	배열을 정렬한 뒤,

•	양쪽 끝에서 시작해서 수를 더하고,

•	합이 음수/양수인 경우에 맞춰 포인터를 이동

함으로써 전역 최적을 효율적으로 찾아냅니다.

결론

•	가장 간단하고 직관적인 방법: 투 포인터

•	구현이 어렵지 않고, 시간 복잡도도 O(N \log N)이라서 대용량 데이터에도 빠르게 동작합니다.

•	이미 많이 알려진 “두 수의 합(혹은 특정 값에 가장 가까운 합)” 문제 패턴이니, 이 로직으로 구현해 보시면 쉽게 정답을 도출할 수 있습니다.

화이팅입니다!

## Phase3. 피드백 참고해서 30분 시도 - 실패: 인덱스가 너무 악랄하다.

실패 시 코드 필사 형벌

근데 이 경우는 내 풀이가 완전 틀린 방향은 아닌 거 같은데, 지피티는 그냥 투 포인터로 풀라고 하는 거지. 이진 탐색으로 하려면 경계조건이 중요해서 그렇다 이말인 거 같은데.

```python
"""
1. 문제 읽기
2. 문제 풀기
이 경우는 i를 고정시키고 j를 이진탐색하면 안 되나? 그래보자 일단.
3. 수도 코드
4. 코드 구현
"""

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

def bin_search(i: int, left, right):
    """arr[i] + arr[center]의 절대값을 최소로 만들어주는 center 인덱스를 리턴"""
    center = (left+right)//2
    # print(f'\nbin_search start {left} {center} {right}')
    zero_combine = sys.maxsize
    best_center = None
    while left <= right:
        combine = arr[center] + arr[i]
        # print(f'{arr[center]} + {arr[i]} = {combine}')
        if combine > 0:
            right = center - 1
        elif combine < 0:
            left = center + 1
        else: # 혼합 결과가 0인 베스트 케이스
            return center
        if zero_combine > abs(combine):
            zero_combine = combine
            best_center = center
        center = (left+right)//2
        # print(f'combine: {combine}, to next segment {left} {center} {right}')
    # print(f'result: {best_center}')
    return best_center if best_center != None else None
        

def incremental_method(n: int, arr: list):
    arr.sort()
    zero_combine = sys.maxsize
    for i in range(0, len(arr)):
        
        j = bin_search(i=i, left=i+1, right=len(arr)-1)
        if j == None: continue
        combine = abs(arr[i] + arr[j])
        # print(f'combine: {combine}')
        # 초깃값은 매우 큰 양수, 컴바인 값도 절대값이므로 그냥 최소를 업데이트
        if zero_combine >= combine:
            pair = (arr[i], arr[j])
            # print(f'zero_combine update: {arr[i], arr[j]}')
        zero_combine = min(zero_combine, combine)
    return f'{pair[0]} {pair[1]}'

print(incremental_method(n, arr))
            


"""
이슈: 5프로 맞고 틀렸습니다
Phase1
환경: 파이썬
로그: 틀렸습니다(5프로 정답)
최근 변경 사항: 이진 탐색 코드 작성

Phase2
확인: 이럴 땐 역시 경계값을 다시 보고 문제 조건을 다시 정리.
산성 용액은 1부터 1,000,000,000까지 양의 정수
알칼리 용액은 -1부터 1,000,000,000까지 음의 정수
같은 양의 두 용액을 혼합하여 특성값이 0에 가가운 용액 만들기
틀린 테스트 케이스를 찾았다.
5
-1 -1 -1 -1 4
-1 4

답은 -1, -1로 -2를 만드는 0, 1이 나와야 하는데, 
로직 문제가 있는지 -1, 4가 나온다.

시도: 평범한 이진탐색 인덱스로 재설정
결과분석
"""

"""
이슈: 1프로 맞고 틀렸습니다.

Phase1.
환경: 파이썬
로그: 1프로 채점 후 틀렸습니다(두 가지 테스트케이스는 통과함을 확인)
최근 변경 사항: 이진 탐색 조건 수정
while left <= right:
    combine = arr[center] + arr[i]
    if combine > 0:
        left, right = left, center - 1
    elif combine < 0:
        left, right = center + 1, right
    else:
        return center
    center = (left+right)//2
return center


Phase2. 
확인: 중복 값이 들어가는 경우를 확인. 이건 이진 탐색에서 문제가 생기는 것으로 보인다.
5
1 2 3 4 5
1 1
근데 이진탐색을 이렇게 하는데 같은 인덱스가 어떻게 또 나오지?
j = bin_search(i, left=i+1, right=len(arr)-1)

시도: 
분석: 
"""

"""
이슈: 틀린 테스트 케이스

Phase1.
환경: 파이썬
로그: 
5
1 2 3 4 5

bin_search start 1 2 4
combine: 4, to next segment 1 1 1
result: 2
zero_combine update: (1, 3)

bin_search start 2 3 4
combine: 6, to next segment 2 2 2
result: 3

bin_search start 3 3 4
combine: 7, to next segment 3 2 2
result: 3

bin_search start 4 4 4
result: 4

bin_search start 5 4 4
result: 4
1 3

최근 변경 사항: 인덱스 수정.

Phase2.
확인: 아니 진짜 이진 탐색 조건을 어떡하라는 거야.

시도: 
분석: 
"""
```

## Phase4. 형벌: 외우십쇼

외울 땐 역시 보고 쓰고 안 보고 쓰고 채점하고 반복이지.

### 1. 필사

```python
import sys
import bisect

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    
    best_sum = 2_000_000_000 * 2  # 충분히 큰 초기값
    best_pair = (0, 0)
    
    for i in range(n - 1):
        target = -arr[i]
        # i+1 ~ n-1 범위에서 target의 삽입 위치를 찾음
        j = bisect.bisect_left(arr, target, i + 1, n)
        
        # 후보: j (존재하면)
        if j < n:
            current_sum = arr[i] + arr[j]
            if abs(current_sum) < best_sum:
                best_sum = abs(current_sum)
                best_pair = (arr[i], arr[j])
        # 후보: j-1 (i+1 이상이면)
        if j - 1 > i:
            current_sum = arr[i] + arr[j - 1]
            if abs(current_sum) < best_sum:
                best_sum = abs(current_sum)
                best_pair = (arr[i], arr[j - 1])
    
    print(best_pair[0], best_pair[1])

if __name__ == '__main__':
    main()
```

(필사 이미지 첨부)

![](./images/IMG_0043.png)

![](./images/IMG_0044.png)

코드 자체가 이해가 안 되는데? 수도코드로 해야 하나? 사실, 그냥 쓰고 채점하면서 뇌에 채찍질하면 배워진다.

### 2. 외워서 쓰고 채점

(채점 이미지 첨부)

![](./images/IMG_0046.png)

![](./images/IMG_0047.png)

질문

- bisect.bisect_left(arr, target, i+1, n)이 무슨 역할을 하는 거지?
> 좋은 질문이에요!

- 아하, 그래서 target을 -arr[i]로 설정했구나. 찾고자 하는 값이 arr[i] + target = 0으로 만들어주는 Target이기 때문에.
- bisect_right는 그럼 최초 삽입 위치가 아니라 최후 삽입 위치를 돌려주나?
> 정확해요! 👏

- bisect.bisect_left/right의 리턴 값이 존재하지 않을 수는 없다. 타겟 위치가 배열 내에 없다면 0 아니면 n을 리턴하기 때문
> bisect_left나 bisect_right는 “삽입 위치”를 항상 반환하기 때문에,

- 두 번째 질문: if문이 왜 두 개 있는 거야.
> 좋아요! 아래 코드의 핵심은 **“합이 0에 가장 가까운 두 수를 찾는 것”**입니다.

그러니까 이게, 두 번째 조건이 있어야 미싱한 것들을 잡을 수 있다.(사실 아직도 확고하게 이해되지는 않는다.) 왜 이진 탐색을 하는데 놓치는 경우가 발생하는 거지?

> 좋아요. 이 질문 정말 잘 해주셨어요.

- 이진 탐색 후 미세 조정의 팁을 알려줘
> 좋아요, 이진 탐색 후 “미세 조정”은 실전 코딩 문제에서 자주 나오는 핵심 테크닉입니다.

### 3. 2트

![](./images/IMG_0048.png)

![](./images/IMG_0049.png)

(얼추 맞는 거 같습니다. 질문만 정리하고 코딩으로 넘어가서 디버깅 하세요.)

정리하면서 생긴 질문

- 왜 i의 iteration 범위가 n-1 까지인가요?
  - 마지막에 i == n-1이 되면, i+1, n 으로 bisect 하게 되어 n, n을 탐색하게 됨.
- 왜 두 번째 조건문에서 j-1이 i와 같을 수도 있는 상황을 방지해야 하는 건가요?
  - 아 j 범위가 애초에 bisect 할 때 i+1 ≤ j < n이라서 그렇구나
> 정리하는 와중에 생긴 질문이 딱 핵심을 찌르고 있어요! 하나씩 정확하게 설명드릴게요. 👇

- 결국 current_sum에 절댓값 씌우지 않은 부분 디버깅 실패. 디버깅이 너무너무너무너무 어렵다.
> 이진 탐색은 깔끔한 알고리즘인데, 디버깅은 더럽습니다.

# 문제: 가장 긴 증가하는 부분 수열, (실패, 다시 풀기)

https://www.acmicpc.net/problem/11053

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

## Phase1. 실패

```python
"""
1. 문제 읽기
2. 문제 풀기
느낌상 수열의 길이를 x로 잡고 이진탐색 때리면 될 거 같기도 하고?
최대 길이가 x인 수열이 존재하는가? 
- 없으면 길이 x를 줄임
- 있으면 길이 x를 늘임
A에서 길이 x의 수열을 구하는 방법: 백트래킹 조합?
3. 수도 코드
4. 코드 구현
"""
import sys
n = int(sys.stdin.readline().strip())
arr =  tuple(map(int, sys.stdin.readline().split()))

def get_list(current_array: list, goal_len: int, idx: int):
    global arr
    """
    배열 (global) arr에서 길이가 goal_len인 수열을 재귀적으로 구하는 함수
    idx: 현재까지 A에서 고려한 인덱스. 
    idx를 포함하는 경우를 넘기거나, 포함하지 않는 경우를 넘긴다.
    최종 목적: goal_len 길이의 부분수열을 전체 수열 arr에서 구할 수 있는가?
    """
    # base case
    if len(current_array) == goal_len:
        # print('base hit')
        return True
    # 만약 인덱스가 끝났으면?
    if len(arr) == idx:
        return 
    # recursion case
    if len(current_array) == 0 or current_array[-1] < arr[idx]: # 현재 부분 수열의 마지막 값이 idx보다 작다면
        return get_list([*current_array, arr[idx]], goal_len, idx+1)
    else: #현재 부분수열의 마지막 값이 idx보다 크거나 같아서 포함시킬 수 없다면 그대로 넘김
        return get_list(current_array, goal_len, idx+1)

max_len = -sys.maxsize

def get_max_array(left: int, right: int):
    global max_len
    center = (left+right)//2
    while left < right: 
        if get_list([], center, 0):
            # 만약 center 길이의 부분 수열이 존재한다면!
            # 일단 저장!
            max_len = max(max_len, center)
            # 그리고 존재한다고 하니, 이제 더 볼드한 트라이를 해 보는거지
            left = center + 1
        else: # center 길이의 부분 수열이 존재하지 않는다면!
            # 더 소심하게 시도
            right = center - 1
        
        center = (left+right)//2 # center 업데이트

get_max_array(0, 1000)
print(max_len)
```

28분만에 이만큼 구현했다! 거의 다 된 거 같은데!

```python
"""
1. 문제 읽기
2. 문제 풀기
느낌상 수열의 길이를 x로 잡고 이진탐색 때리면 될 거 같기도 하고?
최대 길이가 x인 수열이 존재하는가? 
- 없으면 길이 x를 줄임
- 있으면 길이 x를 늘임
A에서 길이 x의 수열을 구하는 방법: 백트래킹 조합?
3. 수도 코드
4. 코드 구현
"""
import sys
n = int(sys.stdin.readline().strip())
arr =  list(map(int, sys.stdin.readline().split()))
max_len = 1

def get_list(current_array: list, goal_len: int, idx: int):
    global arr, max_len
    """
    배열 (global) arr에서 길이가 goal_len인 수열을 재귀적으로 구하는 함수
    idx: 현재까지 A에서 고려한 인덱스. 
    idx를 포함하는 경우를 넘기거나, 포함하지 않는 경우를 넘긴다.
    최종 목적: goal_len 길이의 부분수열을 전체 수열 arr에서 구할 수 있는가?
    """
    # base case
    if len(current_array) == goal_len:
        # print(f'base hit {current_array}') # 전역 max_len 업데이트
        max_len = max(goal_len, max_len)
        return 
    # 만약 인덱스가 끝났으면?
    if len(arr) == idx:
        return 
    # recursion case
    # print(f'getting in to recursion. ?? {current_array} <- {arr[idx]}')
    if len(current_array) == 0 or current_array[-1] < arr[idx]: # 현재 부분 수열의 마지막 값이 idx보다 작다면
        get_list([*current_array, arr[idx]], goal_len, idx+1)
        get_list(current_array, goal_len, idx+1)


def get_max_array(left: int, right: int):
    global max_len
    center = (left+right)//2
    while left < right: 
        current_max_len = max_len
        get_list([], center, 0) #이게 전역 변수 max_len을 업데이트
        # print(f'goal now {center}')
        if current_max_len != max_len:
            # 만약 center 길이의 부분 수열이 존재한다면!
            # 일단 저장! -> 이걸 전역에서 바로 구한다음 처리
            # max_len = max(max_len, center)
            # print('update!')
            # 그리고 존재한다고 하니, 이제 더 볼드한 트라이를 해 보는거지
            # print('try bold!!'*10)
            left = center + 1
        else: # center 길이의 부분 수열이 존재하지 않는다면!
            # 더 소심하게 시도
            # print('not found'*10)
            right = center
        
        center = (left+right)//2 # center 업데이트

get_max_array(0, 1000)
print(max_len)

"""
이슈: 틀렸습니다.
Phase1.
환경: 파이썬
로그: 틀렸습니다
최근 변경 사항: 이진 검색으로 답 구하는 함수 구현
Phase2.
확인: 문제 조건 확인
수열의 크기는 1 이상 1000 이하
수열로 올 수 있는 값은 1 이상 1000 이하
시도: 경계값
1. 수열의 크기가 1인 경우
2. 수열의 크기가 전부 같은 경우
3. 수열의 크기가 감수하는 경우
4. 수열의 크기가 감소하다가 증가하는 경우 <- 찾았다.
자세한 로그
5
5 4 3 4 5
getting in to recursion. ?? [] <- 5
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 3
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 5
getting in to recursion. ?? [] <- 5
getting in to recursion. ?? [5] <- 4
getting in to recursion. ?? [5] <- 3
그냥 같거나 크지만 않으면 재귀를 하면 됨! 혹은 none이거나. 
그럼 다음 질문! 재귀를 해서 값이 업데이트 되면 뭘 어떡하면 됨? 
재귀 스택 끝에 값을 리턴 시키는 방법을 모르니, 그냥 전역 변수를 플래그로 써야할 거 같음.
결과 분석: 계속 오답
"""
```

디버깅 실패

## Phase2. 피드백

가장 긴 증가하는 부분 수열(LIS: Longest Increasing Subsequence) 문제는 이미 잘 알려진 대표적인 DP(동적 프로그래밍) 또는 이분 탐색 기법 문제입니다.

주어진 코드를 보면, “부분수열의 길이를 이분 탐색으로 가정한 뒤, 존재 여부를 재귀적으로 확인”하는 방식을 시도하고 계신데, 이 접근은 구현이 매우 까다롭고 비효율적일 가능성이 큽니다.

> 핵심 요약

> 1.	O(N^2)

> 2.	O(N \log N)

아래 두 가지 정석 풀이 방식을 소개하겠습니다.

1. O(N^2) 동적 프로그래밍(DP) 풀이

알고리즘 아이디어

1.	길이 N의 수열 A가 있을 때, dp[i]를 **“A[i]를 마지막 원소로 가지는 증가 부분 수열의 최댓길이”**라고 정의합니다.

2.	초기값으로 모든 dp[i] = 1 (자기 자신만으로 길이 1인 부분수열을 만들 수 있으므로).

3.	두 번째 원소(i=1)부터 시작해서, 이전 원소(j)들과 비교합니다.

•	만약 A[j] < A[i]라면,

dp[i] = \max(dp[i], dp[j] + 1) \quad (0 \le j < i)

•	이는, “A[i]”가 “A[j]” 뒤에 올 수 있을 경우, “A[j]를 끝으로 하는 증가부분수열 길이 + 1”로 갱신 가능하다는 뜻입니다.

4.	모든 i에 대해 위 계산을 수행한 뒤, max(dp)가 곧 “가장 긴 증가 부분 수열의 길이”가 됩니다.

예시 코드 (Python)

```plain text
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [1] * N  # dp[i]: A[i]를 마지막으로 하는 증가부분수열의 최댓길이

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
```

•	시간 복잡도: O(N^2)

•	공간 복잡도: O(N)

N이 최대 1,000 정도라면, O(N^2) = 1,000^2 = 10^6 연산이므로 충분히 빠르게 통과합니다.

2. O(N \log N) 이분 탐색(BS) 풀이

알고리즘 아이디어 (길이만 구하는 경우)

1.	**결과를 저장할 배열(temp)**을 하나 둡니다. 초기에는 비어있음.

2.	수열 A를 왼쪽부터 오른쪽으로 순회하며 각 원소 x를 확인합니다.

3.	temp 배열에서 이분 탐색을 이용해 “x가 삽입될 위치”(idx)를 찾습니다.

•	temp가 오름차순을 유지하도록, x를 삽입할 위치는

“temp[idx - 1] < x <= temp[idx]를 만족하는 가장 작은 idx” 입니다.

4.	만약 x가 temp 배열에서 가장 큰 값보다 크다면, 그냥 temp 뒤에 붙입니다.

5.	그렇지 않다면, 이분 탐색으로 찾은 위치 idx에 x를 덮어씁니다. → 덮어 쓰는게 핵심이구나. 왜 덮어써도 괜찮은 거지? 수열의 순서가 바뀌는 거 아닌가?

6.	최종적으로 temp 길이가 곧 “LIS(가장 긴 증가 부분 수열)의 길이”가 됩니다.

예시 코드 (Python)

•	이렇게 하면, temp에는 실제 LIS가 완벽히 저장되지 않을 수 있지만(“길이만” 맞음), temp의 길이가 곧 LIS의 길이가 됩니다. → 이게 이해가 안 됨.

•	시간 복잡도: O(N \log N). 최대 1,000 정도라면 훨씬 빠르게 동작합니다.

> 추가 확장

결론 & 추천

•	문제에서 길이만 요구한다면, 위에 소개한 DP O(N^2) 또는 이분 탐색 O(N \log N) 방식을 사용하시면 됩니다.

•	N이 최대 1,000 정도이면, **O(N^2)**도 충분히 빠릅니다. 가장 구현이 간단하므로 DP를 추천드립니다.

•	N이 더 커질 수 있는 상황이라면(예: N 수만~수십만), 이분 탐색 방식이 유리합니다.

현재 접근처럼 “부분수열 길이를 이진 탐색하면서, 매번 재귀로 확인”하는 것은

•	구현 난이도가 높고,

•	중복 계산이 많고,

•	디버깅이 복잡

하므로 실전에서 비추되는 방법입니다.

차라리 전형적인 DP(길이 O(N^2))나 이분 탐색(길이 O(N \log N))로 해결하시는 것이 훨씬 쉽고 빠릅니다.

도움이 되길 바랍니다. 화이팅입니다!

## Phase3. 피드백 후 다시 풀어보기-성공. 근데 이진 탐색 문제의 공통점을 도저히 모르겠음. 

구철이 코드 좀 봐야겠다.

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
요소를 이터레이션하면서, temp에서 요소가 들어갈 최적 위치를 찾아서, 배열 안에 존재하면 
덮어 써버리고, 밖에 존재하면 배열을 늘여서 LIS를 구할 수 있음.
4. 코드 구현
"""
import sys, bisect

input = sys.stdin.readline
n = int(input().strip())
arr = tuple(map(int, input().split()))

tmp = [arr[0]]

for x in arr:
    # print(f'iterating: {x}')
    i = bisect.bisect_left(tmp, x, 0, len(tmp))
    # print(f'{i} = bisect.bisect_left({tmp}, {x}, 0, {len(tmp)})')
    if i == len(tmp):
        # print(f'tmp.append({x})')
        tmp.append(x)
    else:
        # print(f'{tmp[i]} = {x}')
        tmp[i] = x

# print(tmp)
print(len(tmp))
```



# 스택: 막대기

https://www.acmicpc.net/problem/17608

아래 그림처럼 높이만 다르고 (같은 높이의 막대기가 있을 수 있음) 모양이 같은 막대기를 일렬로 세운 후, 왼쪽부터 차례로 번호를 붙인다. 각 막대기의 높이는 그림에서 보인 것처럼 순서대로 6, 9, 7, 6, 4, 6 이다. 일렬로 세워진 막대기를 오른쪽에서 보면 보이는 막대기가 있고 보이지 않는 막대기가 있다. 즉, 지금 보이는 막대기보다 뒤에 있고 높이가 높은 것이 보이게 된다. 예를 들어, 그림과 같은 경우엔 3개(6번, 3번, 2번)의 막대기가 보인다.

N개의 막대기에 대한 높이 정보가 주어질 때, 오른쪽에서 보아서 몇 개가 보이는지를 알아내는 프로그램을 작성하려고 한다.

## Phase1. 15분, 해결.

```python
"""
1. 문제 읽기
2. 문제 풀기
차례대로 막대기 푸시하다가 탑보다 큰게 오면 팝하고 푸시하면 되겠다.
3. 수도 코드
4. 코드 구현
"""

class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.ptr = 0

    class Empty(Exception):
        def __init__(self, message="Stack is empty"):
            self.message= message
            super().__init__(self.message)

    class Full(Exception):
        def __init__(self, message="Stack is full"):
            self.message = message
            super().__init__(self.message)

    def is_empty(self):
        return self.ptr == 0
    
    def is_full(self):
        return self.ptr == self.size

    def __str__(self):
        return f'{self.stack[:self.ptr]}'
    
    def clear(self):
        self.ptr = 0

    def peek(self):
        if self.is_empty(): raise Stack.Empty
        return self.stack[self.ptr-1]
    
    def push(self, n):
        if self.is_full(): raise Stack.Full
        self.stack[self.ptr] = n
        self.ptr += 1

    def pop(self):
        if self.is_empty(): raise Stack.Empty
        tmp = self.stack[self.ptr-1] 
        self.ptr -= 1
        return tmp
    
    def size(self):
        return self.ptr
    
import sys

stack = Stack(100_000)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    stick = int(sys.stdin.readline().strip())
    # print(f'stack empty? {stack.is_empty()}')
    while not stack.is_empty() and stack.peek() <= stick:
        stack.pop() # 뽑아버리고
    stack.push(stick) # 푸시
    # print(stack)


print(stack.size())
```

# 분할정복: 곱셈

https://www.acmicpc.net/problem/1629

자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

## Phase1. 고민만 하다가 실패하긴 아까우니 고민의 흔적이 필요. 어쨌든 실패.

화이트보드에 고민하고 사진 올리세요. 30분동안.

![](./images/IMG_0453.png)

## Phase2.

아마 문제를 읽다가 **“A를 B번 곱한 뒤 C로 나눈 나머지”**를 직접 계산하면 수가 너무 커질 수 있음을 인지하셨을 겁니다.

이 문제는 흔히 알려진 “거듭제곱을 분할 정복으로 빠르게 계산 (Exponentiation by Squaring)” 기법을 사용하면 쉽게 해결 가능합니다.

1. 문제 요약

•	A^B (즉, A를 B번 곱한 수) 를 직접 구하면 매우 클 수 있습니다.

•	따라서 중간 계산 과정에서도 계속 mod C 연산을 적용해 줄 필요가 있습니다.

•	전형적인 방법: 분할 정복(재귀) 혹은 반복문을 이용한 거듭제곱 알고리즘을 사용합니다.

2. 분할 정복을 이용한 거듭제곱 아이디어

거듭제곱 A^B를 계산할 때,

1.	B가 짝수:

$$
A^B = A^{B/2} \times A^{B/2}
$$

2.	B가 홀수:

$$
A^B = A \times A^{B-1}
$$

(혹은 A^B = A^{(B-1)/2} \times A^{(B-1)/2} \times A)

즉, 지수를 절반씩 줄여가면서 계산하되, 매 단계에서 결과를 mod C로 관리합니다.

이 과정을 재귀 혹은 반복문으로 구현할 수 있습니다.

3. 파이썬 코드 예시 (재귀)

설명

•	mod_pow(a, b, c) 함수가 재귀적으로 b를 반씩 줄여가며 a^b를 구합니다.

•	매 곱셈마다 % c를 취해 줌으로써, 수가 커지는 것을 방지합니다.

4. 파이썬 코드 예시 (반복문)

재귀 없이 반복문으로도 분할 정복 형태를 구현할 수 있습니다 (이 방식도 매우 직관적입니다).

설명

•	지수 b가 홀수이면, 현재 base를 result에 곱해주고, 지수를 하나 줄입니다 (b -= 1).

•	그 뒤, base를 제곱(base = base * base)하고 b를 절반(b //= 2)으로 줄여나갑니다.

•	마찬가지로 매 연산마다 % c를 하여 중간 결과가 너무 커지지 않도록 합니다.

5. 시간 복잡도

•	분할 정복 방식으로 거듭제곱을 계산하면, 지수 B에 대해 O(\log B) 시간 안에 계산이 가능합니다.

•	문제의 입력 범위에서 B가 매우 커도, \log B 단계만 거치므로 효율적으로 풀 수 있습니다.

정리

1.	직접 A^B를 구한 뒤 모듈로를 취하면 수가 너무 커서 계산 불가능 or 비효율적.

2.	분할 정복을 통해 매 중간 단계마다 mod C를 적용해서 처리해야 함.

3.	구현은 두 가지 방법:

•	재귀(반반씩 줄이면서)

•	반복문(지수를 2로 나누며 비트 분할)

4.	시간 복잡도는 O(\log B).

이 로직대로 코드를 짧게 구현하면 바로 정답을 낼 수 있습니다.

분할 정복 거듭제곱은 다양한 문제에서 유용하니, 한 번 익혀 두시면 좋습니다.

화이팅입니다!

## Phase3. 피드백 후 재도전-실패

(실패 시 코드 외우기)

```python
"""
1. 문제 읽기
이해 자체는 어렵지 않음.
2. 문제 풀기
분할정복의 방법론을 유도할 것. 
Phase1. 유도(유사한 문제 떠올려보기)
- 색종이? Z문제?: 2^n 길이의 정사각형을 다루는 문제들과는, 직사각형을 다룬다는 점에서 좀 다름
주어지는 데이터도 선형. n의 범위가 100,000으로 많지는 않은데, 주어지는 정수가 위 문제보다 큼
- 병합 정렬: 사실 근본적으로 비슷하겠지? 어떻게 비슷하려나. 
base case: 사각형을 나누다가 두 개가 남아서, 상수 시간 안에 문제 해결이 가능한 시점
recursion case: 주어진 히스토그램 부분에 대해 양쪽 히스토그램에서 구할 수 있는 최대 사각형
이건 당연히, 양쪽의 사각형 크기를 비교했을 때 최소 사각형 값을 리턴해야 한다. 
종이에 먼저 풀어보시길. 내가 봤을 땐 병합정렬하고 되게 비슷함
Phase2. 문제 정의
- 기본 문제: 전체 히스토그램에서 제일 큰 직사각형 찾기
- 부문제: 부분 히스토그램에서 제일 큰 직사각형 찾기
- 베이스 케이스: 두 히스토그램에서 제일 큰 직사각형 찾기: 무조건 두 직사각형을 합칠 필요는 없음!
Phase3. 어디서 막혔는가? 
분할 정복에서 정복, 병합 단계를 어떻게 해야할지 모르겠음.

3. 수도 코드
1) 답을 정의
B가 짝수면
A^B = A^B//2 * A^B//2
B가 홀수면
A^B = A^B//2 * A^B//2+1
이렇게 분할분할 해서 B값이 1일때 모드 연산하고 combine.
4. 코드 구현
"""
import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def recur(a: int, b: int, c: int):
    if b == 1:
        return a%c
    if b%2 == 0: # b가 짝수
        first = recur(a, b//2, c)%c
        second = recur(a, b//2, c)%c
        return (first*second)%c
    else:
        first = recur(a, b//2, c)%c
        second = recur(a, b//2+1, c)%c
        return (first*second)%c
    
from collections import deque

def loop(a: int, b: int, c: int):
    tmp = 1
    for i in range(b):
        a = a%c
        tmp *= a
        tmp %= c
    return tmp
            

print(loop(A, B, C))

"""
이슈: 시간 초과 발생

Phase1.
환경: 파이썬
로그: 시간초과
최근 변경 사항: 재귀적으로 곱셈과 모듈러 연산 함수 구함.

Phase2.
확인: 반복문으로 바꿔야 하나?
시도: 
def loop(a: int, b: int, c: int):
    tmp = 1
    for i in range(b):
        a = a%c
        tmp *= a
        tmp %= c
    return tmp
            
아래와 같이 구현. 그래도 시간 초과 발생.
분석: 실패.
모르겠다.
"""
```

## Phase4. 코드 외우기(반복문, 재귀 둘 다)

### 예재

```python
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % C
    temp = power(a, b // 2)
    if b % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * a) % C

print(power(A, B))
```

```python
def loop_power(a, b, c):
    result = 1
    a %= c
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b //= 2
    return result

print(loop_power(A, B, C))
```

### 0. 필사

(그림: 재귀 풀이)

![](./images/IMG_0050.png)

- 이 코드가 왜 복잡도 측면에서 Phase3보다 나은가? 
  - 내 코드는 power()함수를 두 번이나 호출하고 있음. 각 패스의 복잡도가 두 배일것. 이것에 대한 마스터 정리 해보시길.
(그림: 반복문 풀이)

![](./images/IMG_0052.png)

### 1.시도 및 채점

(그림: 재귀 풀이)

![](./images/IMG_0051.png)

(그림: 반복문 풀이)

![](./images/IMG_0053.png)

### 2. 코딩하기

```python
import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def power(a: int, b: int):
    # print(f'a: {a}, b: {b}. so {a}^{b}')
    if b == 1: return a%C
    # print(f'get temp: power({a}, {b//2})%{C}', end=' ')
    temp = power(a, b//2)%C
    # print(f'temp = {temp}')

    if b%2 == 0: 
        # print(f'b is even. ({temp}*{temp})%{C}')
        return (temp*temp)%C
    else:
        # print(f'b is odd. {temp}*{temp}*{a} % {C} = {(temp*temp*a)%C}') 
        return (temp*temp*a)%C

print(power(A, B))

"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 찍어보세요
최근 변경 사항: power 구현

Phase2.
확인: 
10 11 12
a: 10, b: 11. so 10^11
get temp: power(10, 5)%12 a: 10, b: 5. so 10^5
get temp: power(10, 2)%12 a: 10, b: 2. so 10^2
get temp: power(10, 1)%12 a: 10, b: 1. so 10^1
temp = 10
b is even. (10*10)%12
temp = 4
b is odd. 4*4*10 % 12 = 4
temp = 4
b is odd. 4*4*10 % 12 = 4
4

시도: 로그하고는 별 상관 없었는데, base case에서 b==0으로 돼 있었음.
분석: 성공.
그런데 왜 b==0이면 안 되고 b==1이면 되는 거지? 직전 재귀에서 b가 짝수면 1일 거고, 홀수면
0이겠지. 왜 홀수에서 분기한 재귀는 고려하지 않아도 되는 거지? 납득이 안 됨.(혼자 힘으로 생각해보기)
아, 어떤 수//2=0으로 만들어버리는 경우는 1 말고는 없기 때문이다. 1//2 연산을 한 다음 재귀로 갈 일이 없기 때문에
(바닥 케이스에서 걸리기 때문에) 0은 고려하지 않아도 되는 거다.
"""
```



## Phase5. Error Injection and debug

아래 코드에 에러를 주입한 버전을 출력. 내가 스스로 디버깅하도록 아무런 코멘트를 달지 말 것.

```python
import sys
input = sys.stdin.readline
A, B, C = tuple(map(int, input().split()))

def power(a: int, b: int):
    if b == 0: return 1
    temp = power(a, b//2)
    if b%2 == 0: 
        return (temp*temp)%C
    else:
        return temp*temp*a

print(power(A, B))
```

해결.(너무 짧아서 그냥 기억으로 풀어졌음)

# 분할정복: 히스토그램에서 가장 큰 직사각형(실패)

https://www.acmicpc.net/problem/6549

## Phase1. 구현 실패

```python
"""
1. 문제 읽기
이해 자체는 어렵지 않음.
2. 문제 풀기
분할정복의 방법론을 유도할 것. 
Phase1. 유도(유사한 문제 떠올려보기)
- 색종이? Z문제?: 2^n 길이의 정사각형을 다루는 문제들과는, 직사각형을 다룬다는 점에서 좀 다름
주어지는 데이터도 선형. n의 범위가 100,000으로 많지는 않은데, 주어지는 정수가 위 문제보다 큼
- 병합 정렬: 사실 근본적으로 비슷하겠지? 어떻게 비슷하려나. 
base case: 사각형을 나누다가 두 개가 남아서, 상수 시간 안에 문제 해결이 가능한 시점
recursion case: 주어진 히스토그램 부분에 대해 양쪽 히스토그램에서 구할 수 있는 최대 사각형
이건 당연히, 양쪽의 사각형 크기를 비교했을 때 최소 사각형 값을 리턴해야 한다. 
종이에 먼저 풀어보시길. 내가 봤을 땐 병합정렬하고 되게 비슷함
Phase2. 문제 정의
- 기본 문제: 전체 히스토그램에서 제일 큰 직사각형 찾기
- 부문제: 부분 히스토그램에서 제일 큰 직사각형 찾기
- 베이스 케이스: 두 히스토그램에서 제일 큰 직사각형 찾기: 무조건 두 직사각형을 합칠 필요는 없음!
Phase3. 어디서 막혔는가? 
분할 정복에서 정복, 병합 단계를 어떻게 해야할지 모르겠음.

3. 수도 코드
4. 코드 구현
"""

```

### 접막

접근 방법: 병합정렬

막힌 이유: 문제 정의 실패. 정복, 병합 단계를 어떻게 해야할지 모르겠음.

## Phase2. 피드백

이 문제 **“히스토그램에서 가장 큰 직사각형”**은 알고리즘 교육에서 매우 자주 등장하는 고전 문제로, 세 가지 대표 풀이가 존재합니다.

1.	분할 정복(Divide and Conquer) : O(N \log N)

2.	선형 스택(모노토닉 스택) : O(N)

3.	세그먼트 트리 : O(N \log N)

출제 의도가 “분할정복”이라면 1번 혹은 3번(세그먼트 트리)으로 접근할 수 있지만,

실무나 대회에서는 보통 2번(스택) 방식이 가장 간단하면서 빠르다는 특징이 있습니다.

아래에서는 분할 정복으로 해결하는 방법과, 실제로 더 자주 쓰이는 스택 풀이를 모두 간단히 소개해 드리겠습니다.

1. 분할 정복(Divide & Conquer) 풀이

1.1 알고리즘 아이디어

길이 N의 히스토그램 높이 배열을 H[0..N-1]라 합시다.

분할 정복 접근 시, 다음과 같이 세 가지 경우를 고려합니다.

1.	왼쪽 구간에서의 최대 직사각형

•	(구간 left ~ mid로 제한하여, 재귀적으로 구함)

2.	오른쪽 구간에서의 최대 직사각형

•	(구간 mid+1 ~ right로 제한하여, 재귀적으로 구함)

3.	가운데(mid)를 걸치는 직사각형에서의 최대 넓이

•	(왼쪽과 오른쪽 사이 경계에서 시작해, 양옆으로 확장해가며 가능한 최대 직사각형을 찾음)

이를 구현하기 위해, 보통 재귀 함수 get_max_area(left, right)를 두고,

1.	종료 조건(Base case): left == right → 막대가 하나뿐이므로 넓이는 H[left] (폭=1, 높이=H[left])

2.	분할: mid = (left + right) // 2

•	왼쪽 최대 넓이: left_area = get_max_area(left, mid)

•	오른쪽 최대 넓이: right_area = get_max_area(mid+1, right)

3.	정복(가운데 걸치는 넓이 계산)

•	먼저 mid와 mid+1 두 위치를 포함하는 “폭=2, 높이=min(H[mid], H[mid+1])” 직사각형에서 시작해,

•	왼쪽과 오른쪽으로 범위를 확장하면서, 가능한 한 높이가 큰 상태를 유지해 최대 폭을 늘려갑니다.

•	과정 중 매번 현재_폭 * 현재_구간의_최소높이로 넓이를 계산하며 최대값을 갱신합니다.

마지막에, max(left_area, right_area, cross_area) 중 최댓값이 get_max_area(left, right)의 결과가 됩니다.

1.2 분할정복 코드 예시 (파이썬)

아래 코드는 재귀로 구현한 예시이며, 입력 처리가 매우 많으므로(데이터 수가 최대 100,000) 빠른 입출력에 신경 써야 합니다.

주의

•	while left < cross_left or cross_right < right: 부분에서, 왼쪽/오른쪽 어느 쪽으로 확장할지 결정하는 로직이 핵심입니다.

•	구현이 다소 까다로운 편이라, 코드를 짤 때 인덱스 범위 및 최소 높이 갱신을 주의해야 합니다.

•	분할정복 알고리즘은 O(N \log N) 평균 복잡도를 가지지만, 구현 난이도가 비교적 높은 편입니다.

2. 선형 스택(Monotonic Stack) 풀이 (실전에서 더 자주 사용)

분할정복 방식도 좋지만, 이 문제는 스택을 이용한 O(N) 해법이 더 일반적으로 알려져 있습니다.

가령 백준 6549번 문제 풀이에서는 대부분 이 스택 방식을 사용합니다.

2.1 알고리즘 아이디어

1.	막대의 인덱스를 담는 스택을 하나 둡니다. 이 스택은 **‘현재까지 오름차순(또는 비감소)’**으로 막대가 정렬되도록 인덱스를 관리합니다.

2.	왼쪽부터 막대를 하나씩 보면서,

•	스택이 비어 있으면 push

•	스택이 비어 있지 않다면, “새 막대의 높이가 스택 top에 있는 막대 높이보다 작을 때” 스택 top에서 pop을 합니다.

이 때, pop된 막대가 **‘현재까지 탐색한 구간에서 만들 수 있는 가장 넓은 직사각형 중 하나’**를 형성할 수 있기 때문입니다.

•	pop될 때마다, **“pop된 막대의 높이” x “너비”**를 계산해 넓이를 갱신합니다.

•	여기서 너비는 “현재 인덱스 - pop 후 스택의 새 top - 1” (스택이 비면 전체가 너비)

3.	모든 막대를 처리한 뒤에도, 스택에 남아 있는 막대들에 대해서 똑같이 pop을 반복하며 넓이를 갱신합니다.

2.2 스택 풀이 코드 예시 (파이썬)

스택 풀이가 현업/대회에서 더 간단하고 빠르므로, 백준 6549 풀이 예시로 자주 등장합니다.

시간 복잡도

•	각 막대가 스택에 한 번 push되고, 한 번 pop되므로 총 연산 횟수는 O(N).

3. 세그먼트 트리(세그먼트 + 최솟값 인덱스) 풀이

1.	세그먼트 트리에 각 구간의 “최솟값의 인덱스”를 저장합니다.

2.	“구간 내에서 가장 낮은 막대”를 기준으로, 해당 막대를 포함하는 최대 사각형을 구합니다(이 막대의 높이 \times 구간 길이).

3.	더 낮은 막대 기준으로 왼쪽 구간, 오른쪽 구간을 분할정복 형태로 재귀 처리.

4.	최소 높이 인덱스를 O(1)에 가져오려면 세그먼트 트리 or 스파스 테이블 RMQ(Range Minimum Query) 사용.

5.	전체 알고리즘은 O(N \log N)이 됩니다.

이 방법도 가능하지만, 구현 난이도가 높아서 실전에서는 잘 쓰지 않습니다.

4. 결론 및 추천

•	분할 정복(Divide & Conquer): O(N \log N)

•	재귀 구현이 가능하며 아이디어가 직관적이지만, 양옆 확장 로직이 까다롭습니다.

•	스택 풀이(Monotonic Stack): O(N)

•	대부분의 코딩 테스트 및 실무 구현에서는 스택 방식이 더 간단하고 빠르게 구현 가능하며, 시간 복잡도도 **더 우수(O(N))**합니다.

•	세그먼트 트리 + RMQ: O(N \log N), 구현은 복잡.

실전에서는 스택 풀이가 거의 표준으로 쓰인다고 보시면 됩니다.

하지만 문제에서 분할정복으로 풀라고 했다면, 위의 분할정복 접근을 천천히 구현해보는 경험도 큰 도움이 될 것입니다.

도움이 되길 바랍니다! 질문 있으시면 언제든 남겨주세요. 화이팅입니다.

## Phase3. 피드백 후 직접 풀기 - 실패

```python
"""
1. 문제 읽기
이해 자체는 어렵지 않음.
2. 문제 풀기
분할정복의 방법론을 유도할 것. 
Phase1. 유도(유사한 문제 떠올려보기)
- 색종이? Z문제?: 2^n 길이의 정사각형을 다루는 문제들과는, 직사각형을 다룬다는 점에서 좀 다름
주어지는 데이터도 선형. n의 범위가 100,000으로 많지는 않은데, 주어지는 정수가 위 문제보다 큼
- 병합 정렬: 사실 근본적으로 비슷하겠지? 어떻게 비슷하려나. 
base case: 사각형을 나누다가 두 개가 남아서, 상수 시간 안에 문제 해결이 가능한 시점
recursion case: 주어진 히스토그램 부분에 대해 양쪽 히스토그램에서 구할 수 있는 최대 사각형
이건 당연히, 양쪽의 사각형 크기를 비교했을 때 최소 사각형 값을 리턴해야 한다. 
종이에 먼저 풀어보시길. 내가 봤을 땐 병합정렬하고 되게 비슷함
Phase2. 문제 정의
- 기본 문제: 전체 히스토그램에서 제일 큰 직사각형 찾기
- 부문제: 부분 히스토그램에서 제일 큰 직사각형 찾기
- 베이스 케이스: 두 히스토그램에서 제일 큰 직사각형 찾기: 무조건 두 직사각형을 합칠 필요는 없음!
Phase3. 어디서 막혔는가? 
분할 정복에서 정복, 병합 단계를 어떻게 해야할지 모르겠음.
병합 단계에서 좌 중 우 삼각형중 최대를 리턴하기d만 하면 된다고 함. 제발 재귀 요정을 믿어!

3. 수도 코드
4. 코드 구현
"""

import sys

input = sys.stdin.readline

def recur(left: int, right: int):
    """좌중우 영역 중 최대 삼각형을 리턴"""
    global arr
    # base case: 히스토그램 영역이 2 이하여서 상수시간 안에 판단 가능.
    # conquer
    if right - left == 0: #영역이 하나.
        return right
    # recursion case
    mid = (left+right)//2
    # divide
    left_rect = recur(left, mid)
    right_rect = recur(mid+1, right)
    # combine.
    # mid left 영역 탐색
    # 근데 여기 로직이 좀 다른 거 같은데. 양옆으로 변을 늘리는 경우와 안 늘리는 경우의 탐색을 해야 하는데?
    i, j = mid - 1, mid + 1
    cnt_i, cnt_j = 0, 0 # arr[mid]이상의 히스토그램 직사각형 좌우 개수를 카운트(연속돼야 함)
    while i >= 0 and arr[i] >= arr[mid]:
        cnt_i += 1
        i -= 1
    while j < len(arr) and arr[j] >= arr[mid]:
        cnt_j += 1
        j += 1
    mid_rect = arr[mid] * (cnt_i + cnt_j+1)
    return max(left_rect, mid_rect, right_rect)

arr = []

while True:
    arr = tuple(map(int, input().split()))
    if arr == (0,): 
        break
    print(recur(0, len(arr)))


"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 8프로 맞춘 거 봐서 로직적인 에러는 없는거 같고, 복잡도 분석이 필요함.
최근 변경 사항: 재귀 함수로 구현

Phase2.
확인: 복잡도 분석: 딱 봐도 combine 과정에서 복잡함. 최악의 경우 O(n)임.
그러면 마스터 정리는 다음과 같음(O(n)을 n으로 생각하고)
T(n) = 2T(n/2) + n + c
    = ...
    = n^2 + n(2c-1)
O(n^2)(맞나?)
아무튼 컴바인 과정에서 복잡도 줄일 필요가 있음. 지금 선형탐색을 하는데, 메모이제이션을 해야 하나? 
시도: 피드백 다시 보니까 그게 문제가 아니라, 컴바인 로직이 다름. 근데 왜 다른지 모르겠음.
분석: 
"""
```

## Phase4. 외우기

아래 답변에서는 분할 정복 방식으로 히스토그램 최대 직사각형 문제(백준 6549)를 올바르게 구현하는 예시 코드를 보여드립니다.

이 문제는 **스택 풀이(O(N))**가 더 구현이 쉽고 빠르지만,

질문 주제인 분할 정복(Divide & Conquer)으로 제대로 작성하는 코드를 간단히 정리해 보겠습니다.

분할 정복(Divide & Conquer) 풀이 핵심

1.	get_max_area(left, right) : 구간 left..right에서 만들 수 있는 최대 직사각형 넓이를 리턴.

2.	Base case

•	막대가 하나뿐인 경우(left == right), 넓이는 heights[left].

3.	Divide

•	중간 지점 mid = (left + right) // 2

•	왼쪽 구간 최대 넓이 = get_max_area(left, mid)

•	오른쪽 구간 최대 넓이 = get_max_area(mid+1, right)

4.	Conquer(가운데를 걸치는 사각형)

•	mid, mid+1에서 시작해 왼쪽과 오른쪽으로 확장하며 만들 수 있는 최대 넓이를 구함.

•	확장 시 **‘현재 구간의 최소 높이’**를 갱신하며, 매 단계마다 현재_폭 × 최소_높이를 계산해 최대값을 갱신.

5.	최종적으로 max(왼쪽, 오른쪽, 가운데를 걸치는 영역)을 반환.

이 때, 가운데를 걸치는 영역을 올바르게 계산하는 것이 관건입니다.

이 과정을 O(right-left+1) 즉 선형 시간 안에 처리하고, 전체 재귀 호출은 T(N) = 2T(N/2) + O(N)이므로, 결과적으로 O(N \log N) 에 풀 수 있습니다.

예시 코드 (파이썬)

```python
import sys
input = sys.stdin.readline

def get_max_area(heights, left, right):
    """
    분할 정복으로 히스토그램 구간 [left..right]에서
    얻을 수 있는 '가장 큰 직사각형의 넓이'를 리턴한다.
    """
    # 막대가 하나뿐인 경우
    if left == right:
        return heights[left]

    mid = (left + right) // 2

    # (1) 왼쪽 구간 최대 넓이
    left_area = get_max_area(heights, left, mid)
    # (2) 오른쪽 구간 최대 넓이
    right_area = get_max_area(heights, mid + 1, right)

    # (3) 중앙을 걸치는 직사각형 최대 넓이 계산
    #  - 먼저 mid, mid+1 두 칸을 잡고 시작
    lo = mid
    hi = mid + 1
    # 초깃값: 가장 작은 막대 높이가 min(heights[lo], heights[hi]), 폭=2
    height = min(heights[lo], heights[hi])
    cross_area = height * 2  # 중앙을 무조건 포함하는 직사각형의 초깃값

    # 중앙에서 시작해 양 끝(left, right) 방향으로 확장
    while left < lo or hi < right:
		    # 오른쪽으로 확장 가능한지 판단 (왼쪽으로 더 못 가거나, 왼쪽으로 가면 더 불리한 경우)
        if hi < right and (lo == left or heights[lo - 1] < heights[hi + 1]):
            hi += 1
            height = min(height, heights[hi])
        # 그렇지 않다면 왼쪽으로 확장.
        else:
            lo -= 1
            height = min(height, heights[lo])

        # 매번 '현재 최소 높이 × (hi-lo+1)' 갱신
        cross_area = max(cross_area, height * (hi - lo + 1))
 
    # 왼쪽, 오른쪽, 중앙 걸침 중 최댓값
    return max(left_area, right_area, cross_area)


def solve():
    while True:
        data = list(map(int, input().split()))
        n = data[0]
        if n == 0:  # 0이 들어오면 종료
            break

        heights = data[1:]
        # 분할정복으로 풀기
        answer = get_max_area(heights, 0, n - 1)
        print(answer)


if __name__ == "__main__":
    solve()
```

주요 구현 포인트

1.	Base case

•	left == right → 단일 막대인 경우 넓이는 막대 높이 그 자체.

2.	Divide : 왼쪽, 오른쪽을 재귀로 구함.

3.	Conquer(가운데 걸치기)

•	lo = mid, hi = mid + 1에서 시작

•	height = min(heights[lo], heights[hi])

•	cross_area = height * 2

•	양쪽으로 확장:

•	왼쪽( lo-1 )과 오른쪽( hi+1 ) 중, 더 높은 막대 쪽을 우선 확장하는 방식을 쓰거나,

다른 로직(왼쪽/오른쪽 중 더 높은 쪽 선택)도 가능합니다.

•	확장할 때마다 height = min(height, 새로 편입한 막대 높이).

•	매 단계 (hi - lo + 1) * height를 갱신.

4.	복잡도: O(N log N)

잘못된 Combine(중앙 영역) 구현의 예

질문 코드에서,

```plain text
    # 중간 막대 하나만 높이로 잡고 좌우로 선형 탐색
    i, j = mid - 1, mid + 1
    while i >= 0 and arr[i] >= arr[mid]:
        ...
```

처럼 단 하나의 막대 높이(arr[mid])만 기준으로 좌우 확장하면,

mid+1의 막대가 arr[mid]보다 낮거나, 또는 더 낮은 쪽이 먼저 걸리는 상황 등

다양한 경우를 놓치게 됩니다.

중앙을 걸칠 때는 보통

•	lo = mid, hi = mid + 1 에서 시작

•	처음 높이 = min(arr[mid], arr[mid+1]),

•	이후 양 옆으로 확장하면서 매번 **‘현재 구간의 최소 높이’**를 갱신

해가야 하는데, 이를 간단히 구현하려면 위 예시 코드처럼

“왼쪽 확장 vs 오른쪽 확장 중 더 큰 높이 쪽을 확장” 하면서 진행하는 방식이 널리 쓰입니다.

결론

•	분할 정복으로도 O(N \log N)에 해결 가능하지만,

•	실전(대회/면접)에서는 보통 스택 풀이(O(N))가 더 쉽고 빠르게 작성됩니다.

•	문제 의도가 “분할정복”이라면, 위 코드를 참고하셔서 구현해 보시면 도움이 됩니다.

시간 초과 혹은 틀림 원인 대부분은

(1) “가운데를 걸치는 구간”을 제대로 확장하지 않은 점

(2) 인덱스 처리나 최소 높이 갱신 실수를 했던 점이므로,

위 예시처럼 정확한 combine 로직을 구현해주시면 됩니다.

도움이 되길 바랍니다. 추가 질문이 있으시면 언제든 편하게 남겨주세요! 화이팅입니다.

### 0. 필사

![](./images/IMG_0071.png)

![](./images/IMG_0072.png)

다른 부분 다 똑같은데, 가운데 부분 넓이 구하는 로직이 아무리 봐도 이해가 안 된다. 이 부분만 한번 더 봐야겠다.

주석이 잘못 적혀 있었음.

![](./images/IMG_0073.png)

### 1. 코드 제출

```python
"""
1. 문제 읽기
이해 자체는 어렵지 않음.
2. 문제 풀기
분할정복의 방법론을 유도할 것. 
Phase1. 유도(유사한 문제 떠올려보기)
- 색종이? Z문제?: 2^n 길이의 정사각형을 다루는 문제들과는, 직사각형을 다룬다는 점에서 좀 다름
주어지는 데이터도 선형. n의 범위가 100,000으로 많지는 않은데, 주어지는 정수가 위 문제보다 큼
- 병합 정렬: 사실 근본적으로 비슷하겠지? 어떻게 비슷하려나. 
base case: 사각형을 나누다가 두 개가 남아서, 상수 시간 안에 문제 해결이 가능한 시점
recursion case: 주어진 히스토그램 부분에 대해 양쪽 히스토그램에서 구할 수 있는 최대 사각형
이건 당연히, 양쪽의 사각형 크기를 비교했을 때 최소 사각형 값을 리턴해야 한다. 
종이에 먼저 풀어보시길. 내가 봤을 땐 병합정렬하고 되게 비슷함
Phase2. 문제 정의
- 기본 문제: 전체 히스토그램에서 제일 큰 직사각형 찾기
- 부문제: 부분 히스토그램에서 제일 큰 직사각형 찾기
- 베이스 케이스: 두 히스토그램에서 제일 큰 직사각형 찾기: 무조건 두 직사각형을 합칠 필요는 없음!
Phase3. 어디서 막혔는가? 
분할 정복에서 정복, 병합 단계를 어떻게 해야할지 모르겠음.
병합 단계에서 좌 중 우 삼각형중 최대를 리턴하기d만 하면 된다고 함. 제발 재귀 요정을 믿어!

3. 수도 코드
4. 코드 구현
"""

import sys

input = sys.stdin.readline

def recur(arr: list, left: int, right: int):
    """좌중우 영역 중 최대 삼각형을 리턴"""
    # base case: 히스토그램 영역이 2 이하여서 상수시간 안에 판단 가능.
    # conquer
    if right - left == 0: #영역이 하나.
        return arr[right]
    # recursion case
    mid = (left+right)//2
    # divide
    left_rect = recur(arr, left, mid)
    right_rect = recur(arr, mid+1, right)
    # combine.
    # mid left 영역 탐색
    # 근데 여기 로직이 좀 다른 거 같은데. 양옆으로 변을 늘리는 경우와 안 늘리는 경우의 탐색을 해야 하는데?
    lo, hi = mid, mid + 1
    height = min(arr[lo], arr[hi])
    cross_area = height*2
    while lo > left or hi < right:
        if hi < right and (lo == left or arr[lo-1] < arr[hi+1]):
            hi += 1
            height = min(arr[hi], height)
        else:
            lo -= 1
            height = min(arr[lo], height)
        cross_area = max(cross_area, height * (hi-lo+1))
    
    return max(left_rect, cross_area, right_rect)

arr = []

while True:
    arr = tuple(map(int, input().split()))
    if arr == (0,): 
        break
    
    print(recur(arr[1:], 0, len(arr)-2))


"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 8프로 맞춘 거 봐서 로직적인 에러는 없는거 같고, 복잡도 분석이 필요함.
최근 변경 사항: 재귀 함수로 구현

Phase2.
확인: 복잡도 분석: 딱 봐도 combine 과정에서 복잡함. 최악의 경우 O(n)임.
그러면 마스터 정리는 다음과 같음(O(n)을 n으로 생각하고)
T(n) = 2T(n/2) + n + c
    = ...
    = n^2 + n(2c-1)
O(n^2)(맞나?)
아무튼 컴바인 과정에서 복잡도 줄일 필요가 있음. 지금 선형탐색을 하는데, 메모이제이션을 해야 하나? 
시도: 피드백 다시 보니까 그게 문제가 아니라, 컴바인 로직이 다름. 근데 왜 다른지 모르겠음.
분석: 너무 어렵다. 세부 로직으로 들어가면 이걸 어떻게 고안하고 논리를 구성해야할지 모르겠다.
"""
```

# 스택: 탑

https://www.acmicpc.net/problem/2493

KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다. 실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치하였다. 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다. 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

예를 들어 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고, 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사한다고 하자. 그러면, 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다. 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.

탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라.

## Phase1. 풀이 성공. 

한 45분 걸린듯.

```python
"""
1. 문제 읽기: 탑 번호는 1 based.
2. 문제 풀기
스택을 써서...당연히... 
팝을 한 다음, 순회를 하면서 나모다 큰 애를 만날때까지 인덱스 감소?
더 스택 논리를 활용할 수 있을 거 같은데.
팝을 하고
6 9 5 7 4
팝을 한 다음 걔들을 다른 스택에 차례로 저장하고, 
만약 팝 요소가 감소세를 보이면 쭉 가다가
증가세를 보이면? 비교해서 반대쪽에서 팝해서 인덱스를 정하면 되나? 


3. 수도 코드
4. 코드 구현
"""

class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.ptr = 0

    class Empty(Exception):
        def __init__(self, message="Stack is empty"):
            self.message= message
            super().__init__(self.message)

    class Full(Exception):
        def __init__(self, message="Stack is full"):
            self.message = message
            super().__init__(self.message)


    def is_empty(self):
        return self.ptr == 0
    
    def is_full(self):
        return self.ptr == self.size

    def __str__(self):
        return f'{self.stack[:self.ptr]}'
    
    def clear(self):
        self.ptr = 0

    def peek(self):
        if self.is_empty(): raise Stack.Empty
        return self.stack[self.ptr-1]
    
    def push(self, n):
        if self.is_full(): raise Stack.Full
        self.stack[self.ptr] = n
        self.ptr += 1

    def pop(self):
        if self.is_empty(): raise Stack.Empty
        tmp = self.stack[self.ptr-1] 
        self.ptr -= 1
        return tmp
    
    def size(self):
        return self.ptr
    
n = int(input())
ans = [0]*n
towers = tuple(map(int, input().split()))
towers_mapped  = [[]]*n
for i in range(n):
    towers_mapped[i] = (towers[i], i, 0)

# towers 자료구조를(높이, 자기 인덱스, 도달한 인덱스)로 관리하면 안 되나.
towers_pass1 = Stack(n)
towers_pass2 = Stack(n)

for tower in towers_mapped:
    towers_pass1.push(tower)


while not towers_pass1.is_empty():
    towers_pass2.push(towers_pass1.pop())
    while not towers_pass1.is_empty and towers_pass1.peek() < towers_pass2.peek(): # 감소세인 동안 팝 푸시 반복
        towers_pass2.push(towers_pass1.pop())
    # 만약 남아 있는 탑이 없다면
    if towers_pass1.is_empty(): 
        while not towers_pass2.is_empty():
            tower = towers_pass2.pop()
        break
    # 감소세 애들은 다 넣었고, 이제 꺼낼 애는 다 큼
    while not towers_pass2.is_empty() and towers_pass1.peek() > towers_pass2.peek():
        tower_from = towers_pass2.pop() # 뽑고, 인덱스는 어떻게 함?
        tower_to = towers_pass1.peek()
        ans[tower_from[1]] = tower_to[1]+1

for a in ans:
    print(a, end=' ')
```

## Phase2. 피드백

🎯 문제 요약: [백준 2493 - 탑]

•	각 탑은 왼쪽 방향으로 레이저를 쏨.

•	각 레이저는 자신보다 왼쪽에 있는 탑 중에서 가장 먼저 자신보다 높은 탑에만 도달함.

•	각 탑마다, 자신의 레이저를 수신한 탑의 번호(1-based)를 출력하시오. (없으면 0)

✅ 문제 핵심 개념

이 문제는 전형적인 “모노토닉 스택(Monotonic Stack)” 응용입니다.

> “현재 탑보다

🔍 당신의 풀이: 잘된 점

•	👏 자체 스택 클래스를 만들어서 직접 문제를 해결한 점은 멋진 시도입니다. 자료구조 구현력도 키울 수 있고, 구조도 파악하려 한 흔적이 보여요.

•	👏 문제 조건(왼쪽에서 오는 레이저, 가장 먼저 만나는 높은 탑)에 대해 스택 기반 구조로 해결해야겠다는 큰 그림은 정확합니다.

•	👀 towers_mapped = (높이, 인덱스) 형식으로 메타정보를 함께 처리하려는 접근도 아주 좋습니다.

🛠️ 개선할 수 있는 점

1. 복잡도를 줄이는 방향으로 리팩토링

당신의 로직은 크게 보면 다음과 같이 작동합니다:

•	모든 탑을 스택에 집어넣고 역순으로 하나씩 꺼내며 비교

•	오른쪽에서 왼쪽으로 이동하면서 왼쪽에 있는 큰 탑을 찾으려 함

→ 하지만, 두 개의 스택을 왔다갔다 하면서 비교하는 구조는 너무 복잡하고,

이 문제의 핵심인 **“왼쪽을 한 번만 보면서도 정답을 유추할 수 있는 구조”**를 놓칠 수 있습니다.

2. 정석 스택 풀이 구조 제안 (더 간단하고 직관적)

```plain text
n = int(input())
heights = list(map(int, input().split()))
stack = []
result = [0] * n  # 1-based 결과 저장

for i in range(n):
    # 왼쪽에 나보다 작은 탑은 전부 제거 (신호 도달 불가)
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1] + 1  # 인덱스 → 탑 번호는 1-based

    stack.append(i)  # 현재 탑의 인덱스를 스택에 저장

print(*result)
```

핵심 아이디어:

•	스택에는 자신보다 높은 탑의 인덱스만 남기고, 나머지는 전부 pop.

•	이 과정에서 스택 top은 곧 현재 탑의 레이저가 도달하는 첫 탑이 됨.

🧠 TIL 요약

> “자신보다 작은 값은 의미가 없고,

💡 추가 학습 팁

이 문제 유형은 다음과 같은 문제들과 유사합니다:

•	백준 17298 - 오큰수

•	백준 17299 - 오등큰수

•	백준 3015 - 오아시스 재결합

이런 문제들을 **“모노토닉 스택 시리즈”**로 묶어 반복 학습하면 실력이 쑥쑥 늘어요.

필요하시면 Notion 템플릿 형태로 정리해드릴 수도 있어요. 계속해서 실력이 쌓여가고 있습니다. 화이팅입니다!

# 스택: 원 영역

https://www.acmicpc.net/problem/10000

x축 위에 원이 N개 있다. 원은 서로 교차하지 않는다. 하지만, 접할 수는 있다.

원으로 만들어지는 영역이 몇 개인지 구하는 프로그램을 작성하시오.

영역은 점의 집합으로 모든 두 점은 원을 교차하지 않는 연속되는 곡선으로 연결될 수 있어야 한다.

## Phase1. 실패

```python
"""
1. 문제 읽기
이해가 어렵지는 않음. 그런데 왜 스택 문제인지 잘 모르겠음.
스택: 선입선출
이 문제에서 선입선출의 대상은? 원? 원을 먼저 푸시한다고 해봐? 
원 안에 원이 있는지 원 밖에 있는지를 알면 되는 거 아닌가? 그걸로 categorization이 
될 거 같은데.
find 함수로 원 안의 원을 찾아서 재귀적으로 스택을 써야할 것으로 보임.
일단 떠오르는 코드를 구현해보까?
2. 문제 풀기
3. 수도 코드
전체 배열을 유지
첫 번째 원을 작업스택에 푸시한다.
푸시한 원 안의 원이 존재하는지 전체 배열을 검사한다.
존재한다면 전체 배열에서 제거하고 작업 스택에 푸시한다.
같은 작업을 반복한다.
꺼내면서 영역을 검사한다? 잘 하면 될 거 같은데? base circle이라는 개념이 있어야 하지 않겠나.
원을 뽑으면서 카운터 1 증가시키면 되지 뭐. 
그리고 find로 안에 있는거 다 찾고 뽑으면서 검사하는 거고.
그러니까 모든 원에 대해 스택 연산을 하긴 해야 하는 거다. 나의 수도 코드대로면
n 은 300,000이라서 좀 크긴 한데.
이거 아닌거 같아.
4. 코드 구현
이
"""

from collections import deque

n = int(input())
circles = [[]]*n
for i in range(n):
    x, r = tuple(map(int, input().split()))
    circles[i] = (x-r, r+x)
print(circles)



def find_inner(circle: tuple):
    """원 circle보다 안에 있는 원의 리스트를 완전 탐색으로 찾아서 리턴합니다."""
    ans = []
    for circle_target in circles:
        if circle == circle_target: continue
        # 찾았다면
        if circle[0] <= circle_target[0] and circle_target[1] <= circle[1]:
            ans.append(circle_target)
    return ans

def solve():
    for circle in circles:
        stack = deque()
        stack.append(circle)
        while stack:
            c = stack.pop()
            inner_circles = find_inner(c)
            for c2 in inner_circles:
                stack.append(c2)
            print(f"inner circles of {c}: {inner_circles}")
            """이러면 스택을 쓸 이유가 없지!"""

solve()

"""
이슈
Phase1.
Phase2.
"""
```

# 큐: 가운데를 말해요

https://www.acmicpc.net/problem/1655

백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

## Phase1. 풀어보기(실패)

```python
"""
1. 문제 읽기: 이해가 어렵진 않음
2. 문제 풀기: 생각보다 어려움. 아래처럼 하면 될 거 같은데 시간초과 남. 
복잡도를 계산해서 더 나은 방식으로 풀어야 함.


import heapq

arr = []
heapq.heapify(arr)

n = int(input())

def get_mid(arr: list): 
    tmp = []
    end = len(arr)//2 if len(arr)%2 == 0 else len(arr)//2+1
    mid = 0
    for _ in range(end):
        mid = heapq.heappop(arr)
        tmp.append(mid)
    for t in tmp:
        heapq.heappush(arr, t)
    return mid

def solve():
    global arr
    for _ in range(n):
        heapq.heappush(arr, int(input()))
        print(get_mid(arr))
        
    
solve()

3. 수도 코드

4. 코드 구현
"""



"""
이슈
Phase1.
Phase2.
"""
```

## Phase2. 피드백(정답 제시 금지)

좋습니다! 지금까지의 시도와 접근은 충분히 의미 있었고, 지금이 바로 정답은 보지 않고 구조만 잡아나가기에 딱 좋은 타이밍입니다.

✅ 현재 코드의 핵심 한계

당신이 사용한 방식은 다음과 같습니다:

•	우선순위 큐 (min heap)에 원소를 삽입

•	매번 pop을 여러 번 하면서 중간값 추출 후 다시 push → 시간복잡도: O(N \log N) 이상

❌ 문제점:

•	heapq는 정렬된 순서를 보장하지 않기 때문에, 중간값을 구하려면 매번 pop/push 반복이 필요

•	결국 매 입력마다 힙 전체를 탐색하듯이 동작하게 되어, 시간 초과 발생

🧠 핵심 개념: 두 개의 힙

이 문제를 효율적으로 해결하기 위한 가장 핵심 아이디어는 다음과 같습니다:

> 중간값을 실시간으로 효율적으로 찾기 위해, “작은 값들만 담는 힙”과 “큰 값들만 담는 힙”을 동시에 유지한다.

🧩 구조:

🔧 설계 전략

📌 동작 원리:

•	수를 하나씩 읽을 때마다 두 힙의 밸런스를 유지

•	left_heap(작은 수들)의 길이가 right_heap보다 같거나 1 더 많게 유지

•	매 입력마다:

•	먼저 left_heap에 push (중간값 후보니까)

•	그 후 left_heap의 최대값과 right_heap의 최소값을 비교해서 순서가 어긋나면 swap

•	길이 균형이 맞지 않으면 한쪽에서 다른 쪽으로 이동

📌 중간값 결정:

•	무조건 left_heap[0]이 현재까지의 중간값

✍️ Phase2 목표

당신의 목표는 지금까지의 구조를 바탕으로 다음의 로직만 재정의하는 것입니다:

```plain text
# 두 개의 힙 정의
left_heap = []   # max heap (음수로 push)
right_heap = []  # min heap

# 매 입력마다 다음 로직
1. 새 숫자 x를 left_heap에 push(-x)
2. left_heap의 최대값(-left_heap[0]) > right_heap의 최소값이라면 교환
3. 두 힙 크기를 조정: left_heap은 항상 right_heap보다 크거나 같도록
4. 정답은 -left_heap[0]
```

🧩 직접 구현 전에 점검할 질문들

•	왜 힙이 두 개 필요하지?

•	중간값을 추출하기 위해 어떤 조건을 유지해야 하지?

•	중간값이 바뀌는 기준은 어떤 경우지?

🧪 추천 테스트

테스트는 다음 입력으로 해보세요:

```plain text
7
1
5
2
10
-99
7
5
```

출력은:

```plain text
1
1
2
2
2
2
5
```

이걸 직접 맞춰보는 것이 중간값 구조가 잘 유지되는지 판단하는 좋은 방법입니다.

✅ 마무리 조언

이 문제는 많은 고급 문제들의 전신입니다:

•	sliding window median

•	running median

•	lower_bound/upper_bound 개념 활용 등

정답 코드 없이 직접 두 힙 구조를 만들어보고 성공해보세요.

그게 가장 빠른 성장의 지름길입니다.

필요하다면 “음수로 넣어서 max heap 만들기”를 도와드릴 수도 있어요.

화이팅입니다!

## Phase3. 피드백 후 다시 풀기-성공

```python
"""
1. 문제 읽기: 이해가 어렵진 않음
2. 문제 풀기: 생각보다 어려움. 아래처럼 하면 될 거 같은데 시간초과 남. 
복잡도를 계산해서 더 나은 방식으로 풀어야 함.
3. 수도 코드
이거 어떻게 풀더라. 힙을 두 개 만들고, 새로운 애를 루트와 비교해서 
민힙과 맥스힙을 유지하는데, 민힙은 항상 맥스힙보다 1 많게. 
민힙의 루트와 맥스힙의 루트를 비교하고, 만약 맥스힙 쪽이 더 크면 민힙 루트와 스왑
크기 규칙을 초과해도 옮겨주고 스왑.
일단 다 민 힙으로 몰아 넣어주기

4. 코드 구현
"""
import sys

import heapq


def solve():
    n = int(sys.stdin.readline().strip())
    # 루트가 right힙보다 크다면 스왑
    left_heap = [] # right_heap보다 1 크거나 같게. 
    right_heap = []
    left_l, right_l = 0, 0
    heapq.heapify(left_heap) # min heap!
    heapq.heapify(right_heap) # max heap!
    for _ in range(n):
        x = int(sys.stdin.readline().strip())
        # print(f'input value: {x}')
        heapq.heappush(left_heap, -x)
        left_l += 1
        # print(f'initially pushing it to left heap: {left_heap}, size: {left_l}')
        if left_l-2 == right_l:
            # print(f'left heap got bigger: {left_l} v {right_l}')
            heapq.heappush(right_heap, (-heapq.heappop(left_heap)))
            left_l -= 1
            right_l += 1
            # print(f'now balanced: {left_heap}, {right_heap}')
        if right_l > 0:
            # compare
            left_root = -heapq.heappop(left_heap)
            right_root = heapq.heappop(right_heap)
            # print(f'comparing {left_root}  vs {right_root}')
            if left_root > right_root:
                # should be replaced
                left_root, right_root = right_root, left_root
                # print(f'swapped')
            heapq.heappush(right_heap, right_root)
            heapq.heappush(left_heap, -left_root)
            # print(f'after swapping: {left_heap}, {right_heap}')
        else:
            # right heap이 존재하지 않을 경우
            left_root = -heapq.heappop(left_heap)
            # 그냥 기록만 하고 저장
            heapq.heappush(left_heap, -left_root)
        
        print(left_root)
solve()


        
"""
이슈: 1,2,3 입력 시 에러

Phase1.
환경: 파이썬
로그

10
1
input value: 1
initially pushing it to left heap: [1], size: 1
1
2
input value: 2
initially pushing it to left heap: [1, 2], size: 2
left heap got bigger: 2 v 0
now balanced: [2], [-1]
comparing 2  vs 1
swapped
after swapping: [1], [-2]
1
3
input value: 3
initially pushing it to left heap: [1, 3], size: 2
comparing 1  vs 2
after swapping: [1, 3], [-2]
1

최근 변경 사항: min heap, max heap을 이용한 구현

Phase2.
확인: 1,2,3 일때, 1, 2가 왼쪽에, 3이 오른쪽에 들어가야 하는데, 힙 특성상
그렇게 안 되고 있음.
어떻게 하는데 그럼? 
3 넣을 때, 일단 1, 3 / 2가 되고, 여기서...그럼 오른쪽이 min heap이어야 하는 거 아냐?

1 이거 밸런스 맞출 때도 큰 쪽을 밑에 넣고 (그럼 맥스값이고)
2

1 3 이때는? 3과 2 비교해서 스왑
2

1 2
3

-1 1  이렇게 되고. 그지?
3 2

그럼 위쪽이 맥스힙, 아래쪽이 민힙이어야 한다.
시도: 그렇게 바꿔줌
분석: 성공
"""
```



# 우선순위 큐: 카드 정렬하기

https://jungle-compass.krafton.com/mod/page/view.php?id=6123

정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

## Phase1. 풀어보기(실패)

```python
"""
1. 문제 읽기: 
2. 문제 풀기
10, 20, 40

pass1       pass2
10 + 20     30 + 40 = 100
calc order
10 + 20 + 30 + 40 = 100
10 + 40     50 + 20 = 50+70 = 120
4
10 20 30 40 
10 + 20 +30 + 60 + 40 
무조건 작은 애들끼리 더하면 좋은 건가? 그런듯. 그냥 그렇게 그리디하게 하면 될듯
내가 문제를 이해를 못한 거 같다. 10, 20, 30, 40 묶음 카드가 주어졌을 때
이들을 최저 비교로 합치는 방법은!
일단. 
3. 수도 코드
4. 코드 구현
"""

import sys, heapq
h = []
heapq.heapify(h)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    deck_num  = heapq.heappush(h, int(sys.stdin.readline().strip()))

ans = heapq.heappop(h)
ans2 = 0
while h:
    popped = heapq.heappop(h)
    # print(f'{ans}+{popped}={ans+popped}')
    ans += popped
    ans2 += ans
    
# print(ans)
print(ans2)

"""
이슈: 오답

Phase1.
환경: 파이썬
로그: 틀렸습니다.
최근 변경 사항: 힙으로 그리디하게 최소 더하기 연산을 하는 코드 작성.

Phase2.
확인: 틀린 테스트 케이스가 존재한다는 의미. 2프로에서 틀렸으므로 금방 찾을 수 있고,
코드에 중대한 논리적 오류가 있음을 시사.
5
10
20
30
40
50
340

10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
100 + 50 = 150
30 + 60 + 100 + 150
이런 느낌..이면 딱히 틀릴 건 없는데. 10분 더 생각해보고 패스합시다.
카드 개수가 1이면 섞을 일 없이 0이 나오니 그것도 정상.

10
20
40
50

10 + 20 = 30
30 + 40 = 70
70 + 50 = 120
아 여기서 110 나와야 되는데, ans2가 잘못 가산되는 건가.
그냥 내가 문제를 이해 못한 거 같다.
시도: 
분석: 
"""
```

## Phase2. 피드백(정답 제시 금지)

좋아요, 이번에도 풀이 흔적을 잘 남기셨고, 무엇보다 틀린 테스트 케이스에 대해 직접 분석하고자 시도하신 점이 아주 좋습니다.

✅ 현재 코드의 핵심 문제점

🔥 논리적 핵심 실수:

```plain text
ans = heapq.heappop(h)
ans2 = 0
while h:
    popped = heapq.heappop(h)
    ans += popped
    ans2 += ans
```

이 코드는 **“가장 작은 값 하나를 빼서 ans에 저장하고, 남은 것들과 차례대로 더해가기”**인데요,

여기서의 큰 문제는:

•	ans를 누적하고 있다는 것!

•	**이 문제는 “두 묶음을 더한 결과를 다시 힙에 넣고, 다음 두 묶음을 또 고르는 구조”**입니다.

즉, 매 연산마다 “두 개를 더한 값을 다시 힙에 push”해야 다음 연산에서도 쓸 수 있고,

그때마다 생기는 “비교 횟수”를 더해가는 구조여야 합니다.

🧠 문제의 본질

“두 카드 묶음을 합칠 때 비용이 A + B가 되고, 그 결과 A + B 묶음은 다시 힙에 들어가야 한다.”

이 말은 결국, 매 연산마다 가장 작은 두 묶음을 꺼내서 합친 다음,

•	그 합친 묶음을 다음 연산에 다시 사용하도록 힙에 넣어야 한다는 뜻입니다.

즉, 누적된 총 비교 횟수만 따로 관리하고,

합쳐진 카드 묶음은 계속 힙에 넣고,

힙에 하나 남을 때까지 반복해야 합니다.

✅ 정리된 개선 아이디어

올바른 흐름:

```plain text
1. 힙에 모든 카드 묶음 삽입
2. while 힙의 크기가 2 이상:
    - 가장 작은 두 묶음을 꺼냄 (A, B)
    - A + B → 비교 횟수 추가
    - 합친 카드 묶음 (A + B)을 다시 힙에 삽입
3. 누적된 비교 횟수 반환
```

이건 전형적인 그리디 + 우선순위 큐 문제입니다.

항상 가장 작은 두 묶음을 선택해서 비교 횟수를 줄이기 때문이죠.

✍️ TIL 추천 정리

```plain text
# 카드 정렬하기 문제 실패 원인
- ❌ 실수: 처음 카드 묶음 하나(ans)를 고정하고, 이후 누적하는 방식으로 합산했음
- ✅ 정답 방향: 항상 가장 작은 두 묶음을 꺼내서 합친 뒤 다시 힙에 넣고, 그 비용을 누적
- 🎯 핵심 포인트: “작은 카드끼리 먼저 합쳐야 전체 비교 횟수가 최소가 된다”는 **그리디 구조**
- 🔁 스스로 해석할 수 있는 공식:
    “우선순위 큐에서 최소 두 값을 반복적으로 꺼내서 누적 비용 계산”
```

필요하시면 정답 없이 테스트 통과 구조만 유도해드릴 수도 있어요.

또는 C++이나 Java로도 동일 구조 보고 싶다면 말씀 주세요!

이 문제 이후에는 다익스트라, 허프만 인코딩, CPU 스케줄링 같은 우선순위 큐 기반 문제로 자연스럽게 확장됩니다 :)

## Phase3. 피드백 후 직접 풀기

그냥 문제 원리 읽으니까 사실 뭐 할게 없는 문제였음…그냥 자료구조를 잘 활용할 수 있는지 묻는 문제.

```python

import sys, heapq
h = []
heapq.heapify(h)
n = int(sys.stdin.readline().strip())
for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline().strip()))
cnt = n
cost = 0
while cnt > 1:
    tmp = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h, tmp)
    cost += tmp
    cnt -= 1
    
# print(ans)
print(cost)

```

# 우선순위 큐, 그리디: 철로

https://www.acmicpc.net/problem/13334

집과 사무실을 통근하는 n명의 사람들이 있다. 각 사람의 집과 사무실은 수평선 상에 있는 서로 다른 점에 위치하고 있다. 임의의 두 사람 A, B에 대하여, A의 집 혹은 사무실의 위치가 B의 집 혹은 사무실의 위치와 같을 수 있다. 통근을 하는 사람들의 편의를 위하여 일직선 상의 어떤 두 점을 잇는 철로를 건설하여, 기차를 운행하려고 한다. 제한된 예산 때문에, 철로의 길이는 d로 정해져 있다. 집과 사무실의 위치 모두 철로 선분에 포함되는 사람들의 수가 최대가 되도록, 철로 선분을 정하고자 한다.

양의 정수 d와 n 개의 정수쌍, (hi, oi), 1 ≤ i ≤ n,이 주어져 있다. 여기서 hi와 oi는 사람 i의 집과 사무실의 위치이다. 길이 d의 모든 선분 L에 대하여, 집과 사무실의 위치가 모두 L에 포함되는 사람들의 최대 수를 구하는 프로그램을 작성하시오.

그림 1 에 있는 예를 고려해보자. 여기서 n = 8, (h1, o1) = (5, 40), (h2, o2) = (35, 25), (h3, o3) = (10, 20), (h4, o4) = (10, 25), (h5, o5) = (30, 50), (h6, o6) = (50, 60), (h7, o7) = (30, 25), (h8, o8) = (80, 100)이고, d = 30이다. 이 예에서, 위치 10 과 40 사이의 빨간색 선분 L이, 가장 많은 사람들에 대하여 집과 사무실 위치 모두 포함되는 선분 중 하나이다. 따라서 답은 4 이다.

## Phase1. 직접 풀기(실패)

```python
"""
1. 문제 읽기
이거 딱봐도 그 그리디 문제인데. 못 박는 문제랑 강의실 배정이랑 비슷하다.
2. 문제 풀기
강의실 문제는 기억이 나는데(늦게 끝나는 강의 순으로 우선 배정), 못 박는 문제는 기억이 안난다.
못은? 아 진짜 기억이 안 나네.
x 좌표 상에 선들의 위치가 주어졌을 때, 가장 많은 선을 못으로 관통할 경우 선의 개수를 구하라.
문제는 이거고, 정답은? 못의 위치를 옮겨가며 관통하는 선 최대 수를 완전탐색으로 구했던 거 같은데
(이건 그리디가 아니잖아 그럼.)
아무튼, 문제를 보자.
못이랑 비슷하게 철로가 시작하는 지점을 incremental하게 시뮬레이션하고,
철로가 끝나는 지점 안으로 범위 안의 선들이 들어오면 정답에 더해주기?
여기서 힙을 어떻게 쓰지? 아, 못이 최대한 많이 박히는 지점들을 그리디하게 구해서, 
그 최대 지점들을 커버하면 되는 거 아닌가?
이것도 아닌 거 같다. 문제를 이해하지 못하겠다.
강의실 배정 문제의 역발상인 거 같기도 하고?
특정 지점을 못 박기 문제처럼 구한 다음, 강의실 문제처럼 그리디하게 구하되, 
빨리 시작하는 지점부터 보면서 조건에 따라 수에 추가하면? 일단 그래볼까? 아니 근데 그러면, 
모든 h, o 쌍에 대해 선을 그려본다는 의미고, 
그 각각의 이터레이션 동안 최악 n개의 선이 범위 안에 있는지 판단해야 하니까
h, o 범위만 따져도 -100,000,000~100,000,000이고 철로 길이는 200,000,000에다가,
각 집의 최대 개수는 100,000이니까, 200,000,000 * 100,000의 복잡도가 나온다.
이러면 안 될텐데.

3. 수도 코드
4. 코드 구현
"""
import heapq
import sys
n = int(sys.stdin.readline().strip())
D = {}
for _ in range(n):
    x, y = tuple(map(int, sys.stdin.readline().split()))  
    x, y = x, y if x < y else y, x # 오름차순으로 선 넣어주기
    D[x] = y # 사전형으로 저장해놓기.

```

## Phase2.  피드백(정답 제시 금지)

좋은 시도입니다! 이 문제는 직관만으로 풀기엔 살짝 까다롭고,

알고리즘 아이디어(특히 우선순위 큐 + 정렬)를 정확히 잡아야 시간 안에 해결할 수 있는 유형입니다.

✅ 문제 요약 정리

•	각 사람은 “집 위치”와 “사무실 위치”를 한 쌍으로 가짐. (예: (h, o))

•	철로의 길이 d가 정해짐 (양의 정수).

•	길이가 d인 어떤 선분을 일직선상에 배치할 때,

•	집과 사무실이 모두 그 선분에 포함되는 사람의 수가 최대가 되어야 함.

•	그 최대 인원을 구하는 문제.

즉, 각 사람에 대해 **[ \min(h, o), \max(h, o) ]**라는 구간이 있고,

어떤 길이 d인 선분이 이 구간을 전부 커버하면 “그 사람은 포함”된다고 볼 수 있습니다.

❌ 흔히 하는 실수

1.	**모든 사람의 구간에 대해 선분을 ‘완전 탐색’**하려고 시도

•	구간 자체가 최대 10^8 범위 → 불가능 (너무 큼)

2.	사전형 등으로 단순 저장만 해두고, 마땅한 그리디 로직 없이 “한 점씩 이동”

•	여전히 범위가 커서 시간 초과

3.	두 좌표(집,사무실) 차이가 d 초과인 케이스도 고려하느라 복잡해짐

•	사실 이 경우는 “어떤 선분으로도 둘 다 못 담는다”라서 애초에 제외해버리는 것이 낫습니다.

💡 큰 그림: 정렬 + 우선순위 큐 로 해결

문제를 해결하는 전형적인 접근 방식을 구조만 간단히 소개해 드릴게요(정답은 X).

1.	구간화

•	각 사람의 위치를 [start, end] = [\min(h, o), \max(h, o)]로 표현

•	만약 end - start > d라면, 어차피 길이 d로는 “집+사무실”을 동시에 커버할 수 없으므로 제외합니다.

2.	종점 기준 정렬

•	위에서 거른 구간들만 모아서, 구간의 “end” (오른쪽 끝) 오름차순으로 정렬합니다.

3.	선분 [end - d, end]를 생각하며, 포함 가능한 구간 개수 세기

•	정렬된 순서로 구간을 하나씩 보면서,

•	“이번 구간의 end를 선분의 오른쪽 끝으로 잡으면, 선분은 [end - d, end]일 것”이라는 아이디어

•	이 때, “구간의 start가 end - d 이상”이면 그 구간은 [end-d, end]에 포함될 가능성이 있음.

•	반대로, start가 < (end-d)인 구간은 더 이상 [end-d, end]에 들어갈 수 없으므로 제외.

4.	우선순위 큐(힙)로 start 관리

•	구간을 “end” 기준으로 순회하면서,

•	“현재 end에서 커버 가능한 start들”만 힙에 넣고,

•	start가 “end - d” 미만이면 힙에서 빼는 식으로 유지

•	힙에 남아 있는 구간의 개수가 곧 “[end-d, end]”에 완전히 들어오는 구간 수.

•	매번 힙 사이즈(즉 포함 구간 수)의 최댓값을 갱신 → 정답.

> 이 방식으로, “어디를 선분으로 잡아야 최대가 되지?”라는 문제를

> 정렬된 end

> 가능한 start

🏷️ 힌트 Q&A

1.	왜 구간의 end를 기준으로 정렬하나요?

•	“선분의 오른쪽 끝”을 고정하며, 왼쪽 끝은 end - d가 되므로.

•	만약 end가 오름차순이면, 이전 단계에서 고려한 start들은 그대로 재활용 가능.

•	start를 기준으로도 해볼 수 있지만, 보통 end 기준이 구현이 더 직관적.

2.	start가 end - d 이상이면 된다는 게 무슨 뜻이죠?

•	길이가 d인 선분 [end-d, end] 내에 구간 [start, end]가 완전히 들어오려면,

•	start >= end - d 여야 합니다.

3.	힙에는 뭘 push/pop하나요?

•	보통 구간의 start를 push합니다.

•	end를 하나씩 탐색하면서, “현재 end로 만들 수 있는 선분”에 들어올 수 없는 start들을 pop하여 제거합니다.

4.	시간 복잡도?

•	구간 정렬: O(N \log N)

•	힙 연산: 각 구간당 push/pop이 최대 1번씩 → O(N \log N)

•	총합: O(N \log N) 정도

⚠️ 주의

•	입력 범위: 위치가 \pm 10^8

•	출력: 최대 인원 수

•	정렬 및 힙을 잘못 구현하면 시간 초과/메모리 초과가 날 수 있음

•	구간의 크기가 d를 초과하는 경우는 미리 거르는 게 좋습니다.

✍️ 정리

•	핵심:

•	“[start, end]” 구간을 만들고, “end” 오름차순 정렬

•	우선순위 큐를 이용해 “\geq end - d”인 start만 유지

•	힙 크기(= 현재 포함 가능한 구간 수)의 최댓값을 찾는다

•	자료구조:

•	정렬(오름차순 by end)

•	최소 힙(또는 최대 힙)으로 start를 관리

•	한 번 로직을 깨달으면 다른 “선분 덮기” 계열 문제와 비슷하게 풀 수 있습니다.

이 방향대로 구상하시고, 구체 코드 구현 전에 예제(특히 문제 본문 예제)로 손으로 시뮬레이션해보면 더욱 확실히 이해하실 수 있을 거예요.

화이팅입니다!

## Phase3. 피드백 후 다시 시도 - 성공~!

```python
"""
1. 문제 읽기
이거 딱봐도 그 그리디 문제인데. 못 박는 문제랑 강의실 배정이랑 비슷하다.
2. 문제 풀기
강의실 문제는 기억이 나는데(늦게 끝나는 강의 순으로 우선 배정), 못 박는 문제는 기억이 안난다.
못은? 아 진짜 기억이 안 나네.
x 좌표 상에 선들의 위치가 주어졌을 때, 가장 많은 선을 못으로 관통할 경우 선의 개수를 구하라.
문제는 이거고, 정답은? 못의 위치를 옮겨가며 관통하는 선 최대 수를 완전탐색으로 구했던 거 같은데
(이건 그리디가 아니잖아 그럼.)
아무튼, 문제를 보자.
못이랑 비슷하게 철로가 시작하는 지점을 incremental하게 시뮬레이션하고,
철로가 끝나는 지점 안으로 범위 안의 선들이 들어오면 정답에 더해주기?
여기서 힙을 어떻게 쓰지? 아, 못이 최대한 많이 박히는 지점들을 그리디하게 구해서, 
그 최대 지점들을 커버하면 되는 거 아닌가?
이것도 아닌 거 같다. 문제를 이해하지 못하겠다.
강의실 배정 문제의 역발상인 거 같기도 하고?
특정 지점을 못 박기 문제처럼 구한 다음, 강의실 문제처럼 그리디하게 구하되, 
빨리 시작하는 지점부터 보면서 조건에 따라 수에 추가하면? 일단 그래볼까? 아니 근데 그러면, 
모든 h, o 쌍에 대해 선을 그려본다는 의미고, 
그 각각의 이터레이션 동안 최악 n개의 선이 범위 안에 있는지 판단해야 하니까
h, o 범위만 따져도 -100,000,000~100,000,000이고 철로 길이는 200,000,000에다가,
각 집의 최대 개수는 100,000이니까, 200,000,000 * 100,000의 복잡도가 나온다.
이러면 안 될텐데.

•	구간을 “end” 기준으로 순회하면서,
그 완전탐색을 하긴 하는데, end 기준으로 역으로 올라가면서 그리디하게 보는 문제다.
만약 구간이 d보다 아예 크면 배제
end-d, end에서 end 큰 순으로 정렬해서, 힙에 집어넣고, 
end-d가 start이해 됨? 올랑말랑.
일단 루프를 돌며너
(모든 집회사 구간에 대해 루프: start, end로 생각)
    start가 end-d보다 큰 경우, 이 구간은 포함시킬 수 있음
    일단 대충 알겠음.


3. 수도 코드

(모든 구간을 (start, end), (start<end) 형식으로, end에 대해 오름차순으로
정렬하여 배열로 저장)

(함수: 그리디하게 철로로 커버할 수 있는 구간을 구하는 함수)
    (힙을 생성)
    (첫 번째 구간을 푸시)
    (첫 번째 구간을 제외한 모든 영역을 end 기준으로 이터레이션(end 기준으로 오름차순 정렬했으니 당연))
        (만약 start, end 차가 d보다 크지 않다면)
            (현재 구간의 end는 힙 내에서 최고값임! 따라서 지금 가정할 수 있는 철로 구간은 아래와 같음)
            (end-d ~ d)
            (일단 아묻따 현재 구간을 푸시. 왜? 지금은 현재 구간 기준으로 철로 깔 거니까 현재 구간은 무조건 포함(철로보다 짧은 구간임은 이미 확인))
            (현재 힙의 루트는? start가 가장 작은 값 = end-d 구간에 못 들어갈 확률이 가장 높은 구간)
            (while: 위 논리에 의거해 루트의 start가 end-d보다 커질 때까지 팝)
            (heap에 대한 정리가 끝난 다음 max heap size를 갱신.)

4. 코드 구현
"""

import heapq
import sys

def greedy(pairs):
    h = []
    max_h = 0
    heapq.heapify(h)
    start, end = pairs[0]
    if end - start <= d: 
        heapq.heappush(h, pairs[0])
    for i in range(1, len(pairs)):
        start, end = pairs[i]
        if end - start <= d: 
            heapq.heappush(h, (start, end))
            root = heapq.heappop(h)
            while root[0] < end - d:
                root = heapq.heappop(h)
            heapq.heappush(h, root)
        max_h = max(len(h), max_h)
    return max_h


if __name__ == '__main__':
    input = sys.stdin.readline
    n  = int(input().strip())
    pairs = []
    for _ in range(n):
        start, end = tuple(map(int, input().split()))
        start, end = (end, start) if end < start else (start, end)
        pairs.append((start, end))
    pairs.sort(key=lambda x: x[1])
    d  = int(input().strip())
    print(greedy(pairs))
    
    

```

# 이분 탐색: 사냥꾼



KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.

예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

## Phase1. 직접 풀기(실패)

```python
"""
1. 문제 읽기
사대의 위치에서 커버칠 수 있는 동물들의 위치를 계산.
사대의 개수 M(1 <= M <= 100,000)에서 동물의 수를 완전탐색하면 불가하겠지?

2. 문제 풀기
유사한 문제: 나무 자르기? 뭐가 비슷한지 모르겠다. 결정함수 설정하고 매개변수를 조절해서 이진탐색을 해야 할 건데
결정함수: 잡을 수 있는 동물 수
매개변수: 사대 좌표겠지 당연히.
문제는, 매개변수와 결정 함수의 연관성이 없다는 거다. 매개변수가 무슨 값이든 결정 함수는 
랜덤하게 나온다.
매개변수를 선형으로 증가시키면 결정함수는 당연히 선형이겠지만,
전혀 감이 안 온다. 어떤 접근을 취해야 하는 거지?
완전 탐색으로 푼다면? 사대 하나를 정해서 모든 동물들에 이터레이션해서, 
그 값이 사대 범위에 들어오는지 판단했겠지 -> 일단 악기바리로 이렇게라도 풀어봐라.
풀었다. 이걸 이진 탐색으로 어떻게 바꾸지?
매개변수 i는 망루의 인덱스. 
모르겠다.

3. 수도 코드
4. 코드 구현
"""

import sys
m, n, l = tuple(map(int, sys.stdin.readline().split()))
M = tuple(map(int, sys.stdin.readline().split()))
A = [
    tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

def brute_force():
    for i in range(m):
        animals = get_animal_from(i)
        print(f'hunted at {i}th step: {animals}')


def get_animal_from(i):
    tmp = 0
    for j in range(n):
        x, y = A[j]
        dist_to_animal = abs(x-M[i]) + y
        if dist_to_animal <= l:
            tmp += 1
    return tmp

brute_force()
```

## Phase2. 피드백(정답 제시 금지)

지금 전수조사(brute force) 방식으로 접근하셨는데,

사대(M 최대 100,000개) × 동물(N 최대 100,000마리)를 전부 확인하면 최대 10^{10} 번의 연산이 되어 시간 초과가 납니다.

✅ 핵심 아이디어

1.	사대의 위치(M개)를 정렬해 둔다.

2.	각 동물(좌표 (x, y))을 볼 때,

•	“이 동물을 사냥할 수 있는 **사대(총 위치)**가 존재하는가?”

•	|x - \text{사대위치}| + y \le L

•	즉, |x - \text{사대위치}| \le L - y

•	\text{사대위치}는 [\,x - (L - y), \, x + (L - y)\,] 범위 내에 존재해야 한다.

3.	이 범위를 이진 탐색을 통해 사대 위치 배열에서 빠르게 탐색:

•	\text{leftBound} = x - (L - y)

•	\text{rightBound} = x + (L - y)

•	정렬된 사대 리스트에서

•	leftBound 이상인 첫 번째 사대 인덱스

•	rightBound 이하인 마지막 사대 인덱스

•	둘 중 하나라도 해당 구간 안에 들어있다면, “동물을 사냥할 수 있는 사대가 존재”

•	(정확히는, 구간 안에 사대가 하나라도 있으면 잡힌다고 볼 수 있음)

이렇게 하면 각 동물마다 이진 탐색 2회 정도로 가능한 인덱스 범위를 찾을 수 있고,

N마리 × O(\log M) = 10^5 \times \log(10^5) → 대략 10^6 수준 연산으로 가능해집니다.

🔑 주요 포인트

1.	사대 위치 정렬 ( O(M \log M) )

2.	각 동물에 대해:

•	(L - y)가 음수인 경우 → 어차피 잡을 수 없음(거리가 안 닿음) → 스킵

•	나머지 경우, \text{사대위치}는 [x - (L - y), x + (L - y)] 안에 있어야.

•	이진 탐색으로 위 구간이 사대 리스트 내에 실제 존재하는지 판별.

•	존재하면 카운트 +1

3.	정답은 잡을 수 있는 동물 수 총합.

✍️ 정리

•	완전탐색은 O(M \times N)으로 시간 초과

•	“|x - s| + y \le L → s \in [x - (L-y), x + (L-y)]” 형태로 구간을 구해두고,

•	정렬된 사대 배열에서 구간 내에 사대가 있는지 빠르게 찾는다(이진 탐색).

•	구현 세부에서, bisect_left, bisect_right 등을 활용하면 편리합니다.

이렇게 접근하시고, 예제 입력 몇 가지를 직접 손으로 시뮬레이션해보면

어려운 점이 많이 해소될 거예요. 화이팅입니다!

## Phase3. 피드백 후 풀어보기

# 분할정복: 행렬 제곱

https://www.acmicpc.net/problem/10830

크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

## Phase1. 직접 풀기 성공!

```python
"""
1. 문제 읽기
2. 문제 풀기
divide and conquer로 풀어야 한다. base case는 분명히 그거.
제곱만 하면 돼서
일단 그래보자. 아닌가.
그럼 수도코드를 작성해보자.
3. 수도 코드
(함수: 재귀적으로 dot product, 인수: 행렬 a, 제곱수 b)
    (base case: 만약 b가 2라면)
        (a by a dot product하고 바로바로 1000모듈러 연산 후)
        (리턴: 위에서 구한 a제곱%b)
    (recursion case)
    (temp=recur(a, b//2)) # 재귀로 구한 행렬 결과에 대해,
    (result = 1로 초기화된 a와 위상이 같은 행렬)
    result = recur(temp, 2)%b # 한번 더 재곱을 해 주면 됨.(상수 시간 보장)
    (만약 b가 홀수라면: result에 대해 a를 dot product 해줘야 함.)
        result = (이건 그냥 여기 dot product 코드를 작성하는게 제일 빠르겠다.)
    return result

4. 코드 구현
"""
import sys

def dot_product(a: list, b: list, n: int):
    """do dot product on identically shaped matrices"""
    result = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
                # print(f'{result[i][j]} += {a[i][k]} * {b[k][j]}')
            result[i][j] %= 1000
    return result

def recur(a: list, b: int):
    if b == 1:
        result = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        for i in range(n):
            for j in range(n):
                result[i][j] = a[i][j] % 1000
        return result
    # b가 0일 수 있나? 0은 1//2일 때만 0이 나오는데, 그건 아마 불가능할건데.
    # 근데 저거, 2일때도 안 해도 되지 않나? ㅇㅇ 
    # 근데 여전히 틀렸다고 함.
    # 여기가 주 재귀
    temp = recur(a, b // 2) # 선형 재귀
    # 여기는 temp 결과에 대한 재귀
    result = dot_product(temp, temp, n) # 상수시간
    if b%2 == 1:
        """do result^a"""
        result = dot_product(result, a, n) # 상수 시간.
    return result

if __name__ == '__main__':
    input = sys.stdin.readline
    n, b = tuple(map(int, input().split()))
    matrix = [tuple(map(int, input().split())) for _ in range(n)]
    result = recur(matrix, b)
    for row in result:
        for elem in row:
            print(elem, end=' ')
        print()

"""
이슈: 80프로에서 틀렸습니다.

Phase1.
환경: 파이썬
로그: 틀렸습니다.
최근 변경 사항: 행렬 제곱 분할정복 코드 작성

Phase2.
확인: 80프로면 뭘 확인해야 하지? 
(그런데 확실히 수도코드 다 작성하고 코딩하니까 빠르긴 하다. 40분 걸려서 80프로 맞는 코드를 쓰긴 했으니)
다음 테스트케이스를 발견(질문 게시판)
2 1 (2 by 2 행렬을 1제곱하는 테스트케이스, 각 원소의 최대값은 1000이므로 합리적인 범위)
1000 1000
1000 1000
결과
1000 1000 
1000 1000
정답은 당연히 모든 행렬이 0이어야 함. 그런데 바닥 조건에서 다음과 같이 처리하는 바람에
if b == 1:
    return a
결과가 위와 같이 나오게 됨.(dot_product 함수가 실행되지 않으면 모듈러 연산을 거칠
기회가 없음!)

시도: 행렬 제곱이 1회여도 모듈러 연산을 하도록 수정
if b == 1:
    result = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] % 1000
    return result
분석: 성공. 곱셈과 너무 유사해서 쉽게 풀 수 있었다.
"""
```



# 스택: 괄호의 값

https://www.acmicpc.net/problem/2504

4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
1. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
1. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.
예를 들어 ‘(()[[]])’나 ‘(())[][]’ 는 올바른 괄호열이지만 ‘([)]’ 나 ‘(()()[]’ 은 모두 올바른 괄호열이 아니다. 우리는 어떤 올바른 괄호열 X에 대하여 그 괄호열의 값(괄호값)을 아래와 같이 정의하고 값(X)로 표시한다.

1. ‘()’ 인 괄호열의 값은 2이다.
1. ‘[]’ 인 괄호열의 값은 3이다.
1. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
1. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
1. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자. ‘()[[]]’ 의 괄호값이 2 + 3×3=11 이므로 ‘(()[[]])’의 괄호값은 2×11=22 이다. 그리고 ‘([])’의 값은 2×3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

여러분이 풀어야 할 문제는 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

## Phase1. 실패(30분 초과) - 진전이 아예 없지는 않은데, 잘 모르겠음.

```python
"""
1. 문제 읽기: 괄호 안에 숫자가 들어가는 건 아님

2. 문제 풀기
(() [ [] ]) ( [] )
(2+3*3)*2 + 3*2
22 + 6 = 28
오케이 일단 손으로는 풀린다.
일단 이거 열릴 때 푸시하고, 닫힐 때 팝하고, 기본 그 문제에서 조건만 추가해서 
연장한 거 같은데.
일단 만약 비었는데 닫는 괄호가 오면 무조건 0 출력하면 됨.
그리고 팝 하면서 일단 2점인지 3점인지만 판단해도 뭐...
그냥 수식을 직관적으로 계산하는게 좋지 않겠나.
tmp = 1
tmp *= 2
tmp *= 3 이런 식으로
그러다가 스택이 비면 tmp = 1.
일단 푸시 팝 동작이 발생할 때 로그를 찍어서 값을 적절히 조합해서 디버깅해나가자.

이게 기본인데, 여기서 점수를 어떻게 관리하느냐가 관건.스택이 두개 있어야 하나? -일단 해결
스택의 관점에서 계산 값이 어떤게 오느냐에 따라 곱셈과 덧셈을 구별.

풀었다!
스택 사이즈를 유지하고, 팝 후에 스택 사이즈가 이전에 팝 할때 기록한 사이즈와 같으면 덧셈
줄었으면 곱셈
3. 수도 코드
(스택을 이용해괄호 점수를 계산하는 함수)
    (스택을 만듧니다. 세 개 스택 필요. 계산 스택)
    (입력 길이만큼 이터레이션 합니다)
        (아래 스택은 (, [에 대해 각각 유지합니다.)
        (만약 열린 괄호가 온다면)
            (스택에 푸시합니다.)
        (만약 닫힌 괄호가 온다면)  
            (만약 스택이 비어 있다면)  
                (아묻따 0을 리턴합니다.)
            (스택에서 팝 합니다.)
            (팝을 할 때 계산 스택의 사이즈를 검사하고)
                (같으면 값을 더하고)
                (줄었으면 값을 곱합니다.)


4. 코드 구현
"""

from collections import deque
import sys

def solve(parenthesis: list):
    stack1 = deque()
    stack2 = deque()
    stack3 = deque()
    size = 0 # 팝 당시 계산 스택의 사이즈를 기록합니다.
    result = 0
    for p in parenthesis:
        if p == '(':
            stack1.append(p)
            stack3.append(2)
        elif p == ')':
            if not stack1: return 0
            stack1.pop()
            val = stack3.pop()
            if len(stack3) == size:
                result += val
            elif len(stack3) < size:
        if p == '[':
            stack2.append(p)
            stack3.append(3)
        elif p == ']':
            if not stack2: return 0
            stack2.pop()
        print(f'p: {p}, {result}')
    return 1

if __name__ == '__main__':
    input = sys.stdin.readline
    parenthesis = list(input().strip())
    print(parenthesis)
    print(solve(parenthesis))
```

## Phase2. 피드백

아래에서는 스택을 활용해서 “괄호의 값”을 계산하는 전형적인 방법을 소개해 드립니다.

질문하신 코드에서 아직 구현되지 않은 부분들을 정석적인 로직으로 완성해보겠습니다.

1. 아이디어 요약

이 문제(백준 2504 “괄호의 값”)에서 요구하는 것은,

1.	괄호열이 올바른 괄호열인지 먼저 확인해야 함.

2.	올바르다면, 정의된 규칙(‘()`’=2, ‘[]’=3, 곱셈과 덧셈)으로 값을 구해야 함.

이를 한 번의 스캔으로 처리할 수 있는 전형적인 스택 방식을 소개합니다.

1.1 스택 접근 개념

•	문자열을 왼쪽부터 오른쪽까지 순회하면서,

•	**‘여는 괄호(‘(’, ‘[’)’**가 나오면 스택에 push

•	**‘닫는 괄호(‘)’, ‘]’)’**가 나오면:

•	스택이 비어있으면 → 올바른 괄호열이 아님(결과=0)

•	스택 top을 확인

•	만약 top이 “해당 닫는 괄호에 대응하는 여는 괄호”라면(예: top=’(‘이고 현재=’)’):

•	스택에서 pop해서 없앤 뒤,

•	그 자리에 해당 괄호값(2 또는 3)을 push

•	즉, ()를 값=2라는 숫자로 치환

•	[]를 값=3이라는 숫자로 치환

•	만약 top이 숫자라면 (이미 계산된 값), 즉 (...) 내부에 값이 들어 있을 수 있으므로:

•	연속된 숫자들을 모아서 합을 구한 뒤,

•	그 합에 괄호값(2나 3)을 곱한 값을 다시 스택에 push

•	예) “( (someValue) )” → someValue에 2를 곱

•	예) “[ (someValue) ]” → someValue에 3을 곱

•	그 과정에서 여는 괄호(‘(’ 또는 ‘[’)를 만나 pop하면 중단합니다.

•	문자열 전체를 처리한 뒤,

•	스택에 숫자만 남아 있다면, 그 숫자들의 합이 최종 답.

•	만약 스택에 괄호가 남아 있으면(‘(’, ‘[’) → 올바르지 않은 괄호열이므로 0.

이 로직대로 구현하면,

•	올바른 괄호열이 아닐 경우 중간에 바로 감지 가능(스택 top 불일치, 비어있는지 검사 등).

•	올바른 괄호열이면, 스택에 숫자들만 남게 되고, 그것들을 전부 합하면 최종 값.

2. 단계별 로직 예시

예) (()[[]])([])

1.	( → push '('

2.	( → push '('

3.	) → 스택 top이 '(' → 팝 후, 2를 push

•	스택에는 ['(', 2]

4.	[ → push '['

•	스택: ['(', 2, '[']

5.	[ → push '['

•	스택: ['(', 2, '[', '[']

6.	] → 스택 top이 '[' → 팝 후, 3을 push

•	스택: ['(', 2, '[', 3]

7.	] → 스택 top이 3 (숫자) → 더 이전 top은 '['(여는 괄호)

•	즉 “연속된 숫자”=3, 그 합은 3

•	여는 괄호 '[' pop → 합 × 3 = 3×3=9 push

•	스택: ['(', 2, 9]

8.	) → 스택 top이 숫자(9) → 이전 top은 2(또 숫자) → 이전 이전 top은 '('(여는 괄호)

•	즉, “연속된 숫자들” = 2 + 9 = 11

•	그 다음 '('을 pop → 11 × 2 = 22 push

•	스택: [22]

9.	( → push '('

10.	[ → push '['

11.	] → 스택 top이 '[' → pop, 3 push

•	스택: [22, '(', 3]

12.	) → 스택 top이 3 → 이전 top이 '(' → 연속된 숫자=3

•	'(' pop → 3×2=6 push

•	스택: [22, 6]

13.	문자열 끝 → 스택에 [22, 6]

•	전부 숫자 → 22+6=28

•	결과=28

이 과정을 코드화하면 자연스럽게 여러 if/else로 나눠지는데, 구현 시 “스택 top이 괄호인지, 숫자인지”를 어떻게 구분할지가 핵심입니다.

3. 파이썬 구현 예시

주요 포인트

1.	스택의 원소

•	문자열 문자: ‘(’, ‘[’, …

•	숫자(이미 계산된 값): 2, 3, 6, 9, …

2.	닫는 괄호 처리 시

•	스택 top이 “같은 종류의 여는 괄호”라면 → ()=2, []=3

•	스택 top이 숫자이면 → 연속된 숫자들을 모두 더한 후, 그 다음에 여는 괄호를 pop하여 곱셈.

•	여는 괄호가 없는 경우, 종류가 안 맞는 경우 → 0 리턴(올바르지 않음).

3.	최종 스택 검증

•	모든 문자 처리 후에도 스택에 “여는 괄호”가 남아 있으면 → 0 리턴

•	숫자만 있다면 그 합이 결과.

4. 자주 하는 실수와 디버깅 팁

1.	여러 값이 중첩되었을 때,

•	예: ( [ ( ) ( ) ] ) 처럼 내부에 이미 숫자가 누적된 상태일 수 있음.

•	닫는 괄호를 만나서 pop할 때, 연속된 숫자를 모두 더해 주는 것이 핵심입니다.

2.	짝이 안 맞는 괄호 처리

•	스택이 비어 있는데 닫는 괄호가 오거나,

•	여는 괄호 종류가 다르면( top이 ‘(`인데 닫는 괄호가 ‘]’ 라든지 ), 즉시 0 리턴.

3.	문자열 끝났는데도 스택에 ‘(`, ‘[’가 남아 있다면 0.

4.	값이 0인 상태에서 곱셈할 때:

•	내부가 비어있는 괄호쌍: ()=2, []=3으로 처리 → if val_sum == 0: val_sum = 2 or 3

5. 결론

•	위 로직대로 구현하면,

1.	괄호열 유효성 체크

2.	괄호값 계산

모두 스택 한 번 순회로 해결 가능합니다.

•	스택에 괄호와 숫자를 함께 넣고 관리하는 것이 포인트입니다.

•	문제 조건에 맞지 않는 경우(짝이 안 맞거나, 문자열 끝나도 괄호 남음 등)는 즉시 0으로 처리.

위 코드를 실행해 보시면, 예시 입력 (()[[]])([])에 대해 28이 잘 출력됩니다.

성공적으로 통과하시길 바랍니다! 추가 질문 있으시면 언제든 남겨주세요. 화이팅입니다.

# 스택: 크게 만들기

https://www.acmicpc.net/problem/2812

N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

## Phase1. 실패

```python
"""
1. 문제 읽기
N자리 숫자가 주어졌을 때, 
여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

2. 문제 풀기

스택 자료구조를 쓰는 거겠지? 그럼 일단 플레인 하게 생각했을 때 스택에 숫자를 차례로 집어 넣고
n은 최대 50만 자리수.

근데 풀이가 생각 안 난다. 유사한 문제? 
가장 작은 자릿수를 뽑아내는 문제? 좀 그리디한 거 같은데.
자릿수 점수? 
안쪽에는 큰 수일수록 좋고
1924
1234
4321

작은 숫자를 구현한다면?

1 

1  
9 

3. 수도 코드
4. 코드 구현
"""
```

## Phase2. 피드백

좋습니다. 문제 접근을 시도한 흔적이 잘 보이네요! 이제 이 문제를 푸는 핵심 아이디어와 함께 그리디 + 스택 방식으로 접근해보는 피드백을 드릴게요.

🔍 문제 핵심 정리

•	N자리 숫자가 주어짐 (최대 500,000자리)

•	이 중에서 K개의 숫자를 지워서, 가장 큰 수를 만들어야 함

•	순서를 바꾸지 않고 일부 숫자를 제거해야 함 → 그리디 + 스택

💡 핵심 아이디어

가장 큰 수를 만들기 위해선, 왼쪽부터 가능한 한 큰 숫자가 앞에 오도록 만들어야 해요.

그래서 스택을 사용해 아래와 같이 처리해요:

1.	현재 숫자가 스택의 맨 위 숫자보다 클 경우, 이전 숫자를 제거 (단, 아직 K개 제거하지 않았다면)

2.	이 과정을 반복하면서, 앞의 숫자들을 가능한 한 작게 만든다

3.	숫자를 다 스택에 넣고 나서도, K개를 다 지우지 않았다면 뒤에서부터 더 지워야 함

🧠 예시

입력: 1924, K=2

가장 큰 수: 94

과정:

•	스택: []

•	1 → 스택: [1]

•	9 > 1 → pop(1), k -= 1 → 스택: [], push(9)

•	2 → 2 < 9 → push(2) → 스택: [9,2]

•	4 > 2 → pop(2), k -= 1 → 스택: [9], push(4) → [9,4]

최종 결과: 94

✅ 개선된 수도 코드

✨ 한 문장 요약

> 앞에서부터 차례로 숫자를 보며, 뒤 숫자가 크면 앞 숫자를 지워나가며

필요하다면 전체 코드 구현도 도와드릴게요!

## Phase3. 피드백 후 다시 풀어보기-성공

```python
"""
1. 문제 읽기
N자리 숫자가 주어졌을 때, 
여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

2. 문제 풀기

스택 자료구조를 쓰는 거겠지? 그럼 일단 플레인 하게 생각했을 때 스택에 숫자를 차례로 집어 넣고
n은 최대 50만 자리수.

근데 풀이가 생각 안 난다. 유사한 문제? 
가장 작은 자릿수를 뽑아내는 문제? 좀 그리디한 거 같은데.
자릿수 점수? 
안쪽에는 큰 수일수록 좋고
1924
1234
4321

작은 숫자를 구현한다면?

그리디가 맞았다. 스택에 숫자를 넣고, (k개를 덜 지운 상태에서) 현재 숫자보다 큰 숫자가 오면, 
현재 숫자를 빼고 대신 푸시. 똑같이 진행하고
이 과정 끝나고 k 만큼 제거가 안 됐다면 뒤에서부터 제거 <- 왜 이래도 되는지 이해가 잘...
왜냐면 큰 수일수록 앞에 있을 수밖에 없으니까? 사실 잘 납득이 안 간다. 
일단 수도 코드를 작성해보자.

3. 수도 코드
(스택 초기화)
(모든 숫자에 대해 이터레이션한다.)
    (만약 스택이 비어 있으면 그냥 푸시한다.)
    (숫자를 피크와 비교한다.)
    (만약 숫자가 피크보다 크면 )
        (팝하고 대신 넣는다.)
        (카운터를 올린다.)
    (작으면 그냥 넣는다.)
(이터레이션 종료)
(만약 카운터가 K보다 작으면 그만큼 팝 한다.)


4. 코드 구현
"""


from collections import deque

import sys

def solve(nums: list):
    stack = deque()
    cnt = 0
    stack.append(nums[0])
    for num in nums[1:]:
        while stack and stack[-1] < num and cnt < k:
            tmp = stack.pop()
            # print(f'popped {tmp} from stack. now {stack}')
            cnt += 1
        stack.append(num)
        # print(f'appended {num}. now {stack}')
    while cnt < k:
        # print(f'while {cnt} < {k}')
        stack.pop()
        cnt += 1
    return stack

        

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    nums = list(input().strip())
    result = solve(nums)
    for r in result:
        print(r, end='')
    print()


"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 아래는 정답이 나오는 경우의 로그
7 3
1231234
popped 1 from stack. now deque([])
appended 2. now deque(['2'])
popped 2 from stack. now deque([])
appended 3. now deque(['3'])
appended 1. now deque(['3', '1'])
popped 1 from stack. now deque(['3'])
appended 2. now deque(['3', '2'])
appended 3. now deque(['3', '2', '3'])
appended 4. now deque(['3', '2', '3', '4'])
3234%      

최근 변경 사항: 스택으로 최대 수를 구하는 함수 작성.

Phase2.
확인: 다양한 테스트 케이스 시도하는 방법
오름차순 1234
내림차순 4321
숫자를 하나만 남기고 다 지우는 경우
k가 1이고 n이 2인 경우.
어 뒤에 %기호 뭐지? 생관 없었음.
모든 숫자가 같은 경우. 

찾았다.
10 4
4177252841
477584
정답: 775841임.
해당 케이스의 로그
10 4
4177252841
appended 1. now deque(['4', '1'])
popped 1 from stack. now deque(['4'])
appended 7. now deque(['4', '7'])  <---이떄 왜 비교가 안 일어나지? 아,
그 전에 1이 들어왔어서, 한 번만 비교하고 끝났구나. while로 바꿔야 함.
appended 7. now deque(['4', '7', '7'])
appended 2. now deque(['4', '7', '7', '2'])
popped 2 from stack. now deque(['4', '7', '7'])
appended 5. now deque(['4', '7', '7', '5'])
appended 2. now deque(['4', '7', '7', '5', '2'])
popped 2 from stack. now deque(['4', '7', '7', '5'])
appended 8. now deque(['4', '7', '7', '5', '8'])
appended 4. now deque(['4', '7', '7', '5', '8', '4'])
appended 1. now deque(['4', '7', '7', '5', '8', '4', '1'])
while 3 < 4
477584

시도: 
아래 조건문을 루프로 전환
if stack[-1] < num and cnt < k:
    tmp = stack.pop()
    # print(f'popped {tmp} from stack. now {stack}')
    cnt += 1
stack.append(num)
--->
while stack and stack[-1] < num and cnt < k:
    tmp = stack.pop()
    # print(f'popped {tmp} from stack. now {stack}')
    cnt += 1
stack.append(num)
분석: 성공
"""
```

# 분할정복: 가장 가까운 두 점

https://www.acmicpc.net/problem/2261

2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

## Phase1. 직접 풀기 - 15프로 정답…

```python
"""
1. 문제 읽기
2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

2. 문제 풀기
좌표평면이니까
좌상에서 제일 가까운 점 사이 거리
우상에서 제일 가까운 점 사이 거리
좌하에서 제일 가까운 점 사이 거리
우하에서 제일 가까운 점 사이 거리
cross에서 제일 가까운 점 사이의 거리?
점이 n개라 할 때 완전탐색 하면 당연히 n^2의 비교를 해야 구할 수 있음.

점 자체를 두 가지 기준으로 정렬하고, 
(x가 작을수록, y가 작을수록)
그 다음에 점들에 대해 분할정복하면 되지 않나? 
왼쪽에서 가장 가까운 점 재귀로 구하고, 
오른쪽에서 가장 가까운 거리 재귀로 구하고
가운데 걸쳐서 가장 가까운 점 컴바인 과정에서 구하고
리턴을 최소값으로 해주면.

아이디어 자체는 이게 맞을 거 같다.

5 -> 2, 3
4 -> 2, 2
3 -> 3
2 -> 2
1 -> 이런 경우 없음

3. 수도 코드

(걸치는 최소를 구하는 함수(left, mid, right))
    (left, right 영역 전체에서 최소 거리 구해주기. 어 이거 히스토그램 사각형이랑 비슷하게 하면 안 되나)
    lo, hi = mid, mid+1
    (오른쪽 점을 선택 했을 때 왼쪽 점을 선택한 경우보다 거리가 줄어든다면)
        (오른쪽으로 갑니다.)
    (그게 아니면 왼쪽으로 갑니다.)
    (이거는 약간 기억에 의존해서 하게 될 거 같긴 한데.)

(재귀적으로 left, right의 영역의 점들에 대해 가장 가까운 점 사이의 거리를 리턴하는 함수)
    (바닥 조건: left+1 == right, 즉, 점이 두 개 있는 상황)
        (두 점 사이의 거리를 상수시간에 구해서 리턴)
    (left == right일수도 있음: 그러면 어떡해야 함? 0을 리턴하면 안 되고. n은 2 이상이니까, 1이 아니라 3인 경우를 봐주면 안 되나.)
    (재귀조건)
    (가운데 인덱스 = (left+right)//2)
    (왼쪽 최소 = 재귀(left, mid))
    (오른쪽 최소 = 재귀(mid+1, right)
    (이제 걸치는 최소(cross_min)을 구해야 함. 이거 복잡하니까 별도의 함수로 빼서 생각하자 일단.)
    (return min(왼쪽 최소, 오른쪽 최소, 걸치는 최소))
        

4. 코드 구현
"""

import sys

def get_cross_min(left, mid, right):
    """mid 를 기준으로 좌 우로 최선의 선택이 되는 동안 점을 선택해서 거리를 리턴"""
    lo, hi = mid, mid + 1
    cross_len = (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2
    while lo > left or hi < right:
        # 왼쪽으로 가는 경우의 길이
        
        if hi < right and (lo == left or 
                           (dots[lo-1][0] - dots[hi][0])**2 + (dots[lo-1][1] - dots[hi][1])**2
                           >
                           (dots[lo][0] - dots[hi+1][0])**2 + (dots[lo][1] - dots[hi+1][1])**2
                           ):
            hi += 1
            cross_len = min(cross_len, (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2)
        else:
            lo -= 1
            cross_len = min(cross_len, (dots[lo][0] - dots[hi][0])**2 + (dots[lo][1] - dots[hi][1])**2)
    return cross_len

def recur(left: int, right: int):
    """left, right 영역의 점들에 대해 가장 가까운 점 사이의 거리를 리턴한다."""
    if left + 2 == right: # 영역에 점이 세 개일 때.
        a, b, c = dots[left], dots[left+1], dots[right] 
        # 세 점의 거리를 구한다.
        dist_a = (a[0] - b[0])**2 + (a[1] - b[1])**2 # a - b
        dist_b = (a[0] - c[0])**2 + (a[1] - c[1])**2 # a - c
        dist_c = (c[0] - b[0])**2 + (c[1] - b[1])**2 # b - c
        return min(dist_a, dist_b, dist_c)
    if left + 1 == right: # 영역의 점이 둘 일때.
        a, b = dots[left], dots[right]
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
    
    mid = (left+right)//2
    left_min = recur(left, mid)
    right_min = recur(mid+1, right)
    cross_min = get_cross_min(left, mid, right)
    return min(left_min, right_min, cross_min)



if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())
    dots = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    dots.sort(key=lambda x: (x[0], x[1]))
    # print(dots)
    print(recur(0, len(dots)-1))
    
```

틀린 이유

![](./images/8b2d4fa6-8dec-48fd-b014-d20cd2d9294f.png)

cross_len 구하는 과정에 거리가 가까워도 가운데서 저렇게 트롤하는(y거리가 엄청 멀어버린 애들이 있으면) 두 점이 이어지지 못할 수도 있음. 

최선의 선택은 y 기준으로 한번 더 정렬을 해서 진행하는 건데, 이게 그냥 솔루션을 두번 돌리면 오답을 두번 찾는 결과가 나오기도 함. 그게 아니면 재귀 과정에서 정렬 및 탐색을 해줘야 하는데, 전체 정렬을 해버리면 전체 인덱스가 흐트러져버림. 

슬라이싱해서 left, right 인덱스 안에서만 정렬 해주면 되지 않나? 못하겠다. 머리가 안 돌아간다.

## Phase2. 피드백

좋은 시도였어요! 문제의 핵심은 제대로 파악하셨고, 분할 정복 구조도 잘 짜셨습니다. 다만 get_cross_min에서 가운데 걸친 영역의 최소 거리를 구하는 방식이 정확히 구현되지 않아 오답이 발생한 것으로 보입니다.

아래는 보완할 수 있는 핵심 포인트입니다:

✅ 핵심 피드백

1. 가장 가까운 두 점을 찾는 알고리즘의 핵심

•	분할 정복을 통해 좌/우 영역을 나누고,

•	좌/우 각각에서의 최소 거리 d를 구한 뒤,

•	|x - mid_x| <= d를 만족하는 점들만 따로 모아서,

•	y좌표 기준으로 정렬 후, y거리가 d 이하인 점들 중에서만 다시 거리 계산 (최대 6쌍만 비교)

2. get_cross_min 함수의 문제점

•	현재 구현은 단순히 왼쪽과 오른쪽을 확장하면서 거리를 비교하지만, y거리 제한 조건을 고려하지 않아 무의미한 비교가 많고, 실제 가까운 점쌍을 놓칠 수 있어요.

📌 정석 알고리즘 로직 요약 (O(n log n))

1.	x 기준 정렬, 재귀 호출로 좌/우에서 각각 d1, d2 최소 거리 구함

2.	d = min(d1, d2) 이후, |x - mid_x| < d 범위의 점들만 따로 temp 리스트에 저장

3.	이 temp를 y 기준 정렬 후, y 거리도 d보다 작은 경우만 비교하여 최소값 갱신

•	이 과정에서 한 점 기준으로 최대 6개 점만 비교하면 충분

✨ 참고 구현 코드

```python
import sys
import math
input = sys.stdin.readline

def distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def closest_pair(points):
    def solve(points_sorted_x, points_sorted_y):
        n = len(points_sorted_x)
        if n <= 3:
            min_dist = float('inf')
            for i in range(n):
                for j in range(i+1, n):
                    min_dist = min(min_dist, distance(points_sorted_x[i], points_sorted_x[j]))
            return min_dist

        mid = n // 2
        mid_x = points_sorted_x[mid][0]
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]

        # y 기준 정렬도 각각 나눠줘야 함
        left_y = []
        right_y = []
        for p in points_sorted_y:
            if p[0] <= mid_x:
                left_y.append(p)
            else:
                right_y.append(p)

        d = min(solve(left_x, left_y), solve(right_x, right_y))

        # cross 영역 후보군만 수집
        strip = [p for p in points_sorted_y if abs(p[0] - mid_x) < d]

        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                if (strip[j][1] - strip[i][1])**2 >= d:
                    break
                d = min(d, distance(strip[i], strip[j]))
        return d

    points_sorted_x = sorted(points)
    points_sorted_y = sorted(points, key=lambda x: x[1])
    return solve(points_sorted_x, points_sorted_y)

if __name__ == "__main__":
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(closest_pair(points))
```

💭 추가 팁

•	거리의 제곱으로 비교하면 math.sqrt() 호출이 없어져 속도 향상 가능

•	strip의 y좌표 기준 정렬은 cross 영역을 빠르게 탐색하는 핵심

필요하시면 이 알고리즘의 그림 설명이나 수식 설명, 혹은 추가 실습 예제도 도와드릴게요!

## Phase3. 피드백 후 재도전이지만…실패

솔직히 지금 두뇌 상태로 제대로 문제를 풀 자신이 없음. 바로 코드 필사 및 채점으로 넘어갈 것. 

### 1. 필사: 질문 정리

필사 하면서 하셔야 할 일은, 코드에 의문을 가지는 겁니다. 사진을 첨부하고 질문 리스트를 정리하세요

![](./images/IMG_0086.png)

![](./images/IMG_0087.png)

### 2. 채점

(사진 첨부)

### 3. 코딩 혹은 재채점



