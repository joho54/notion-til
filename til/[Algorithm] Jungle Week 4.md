# [Algorithm] Jungle Week 4



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> 고민: DP를 풀 수 있는 일반론적인 방법을 고민해야함. 

# 4.4. 알고리즘 특강 정리

## 강의 내용

다이내믹 프로그래밍은 테이블 채우기가 아니다! 똑똑한 재귀다! 가장 중요한 부분은 부분 문제 설정과 올바른 점화식을 세우는 것. 

동적 계획법 스텝

1. 계산할 배열의 값들을 명확히 정의한다
  1. 어떻게 계산해야 할지 생각하지 말고
1. 계산할 값의 점화식을 찾는다. → Backtracking에서 했던 것!
1. 점화식을 이용하여 배열에 값들을 계산하여 채운다.
  1. bottom up 방식으로. 적절한 계산 순서를 생각.
1. 원래 문제의 답을 추출한다.
# 동전

## Phase1. 직접 풀기

```python
import sys

if __name__ == '__main__':	
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        m = int(input().strip())
        coins = tuple(map(int, input().split()))
        n = int(input().strip())
        dp = [[0 for _ in range(m)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m):
                if i - coins[j] == 0:
                    dp[i][j] = 1
                else:
                    tmp = 0
                    for k in range(0, j+1):
                        if i-coins[j] >= 0:
                            tmp += dp[i-coins[j]][k]
                    dp[i][j] = tmp
        print(sum(dp[n]))
```

## Phase2. 문제에 대한 회고

DP문제를 강인하게 풀기 위해서 어떻게 접근해야 할지 이 문제를 두고 많이 고민했다. 위의 특강 내용과 CLRS의 동적 계획법 부분도 많이 참고했다. 

일단 테이블 채우기로 접근하면 안 된다. 테이블을 쓰는 이유는 재귀를 영리하게 하기 위해서지, 테이블 자체가 좋아서 쓰는게 아니다. 테이블 채우기로 문제를 접근하면 급 어려워지는 이유가 여기 있는데, DP 테이블은 거기에 저장되는 정보의 의미가 선형적이지 않고 재귀적이기 때문에, 재귀의 그림을 그리지 못하는 채로 테이블을 보면 인지 부조화에 빠지게 된다. 

그래서 CLRS에 나온 DP 4 step을 변용하여 나만의 규칙을 만들었다.

1. 테스트 케이스 정하기. 구조를 잘 반영할 수 있는 정도의 사이즈! (매우 중요)
1. 재귀 트리로 문제를 먼저 구조화 하기.
1. 구조가 제대로 그려지면 테이블에 채울 값을 정의. 
1. 테이블 계산 순서를 명확히 하고 코딩하기
일반적인 방법론에서는 보통 테스트 케이스를 정하는 과정이 빠져 있다. 하지만 나 같은 경우는 복잡한 코드를 디자인하기 전에 테스트 케이스가 없으면 처음부터 꼬이고 유지보수도 할 수 없다. 대신 위와 같이 진행하면, TDD 스타일로 디피 문제를 강인하게 풀 수 있을 것 같다.  아래는 문제를 구조화한 과정이다.

![](./images/IMG_0489.png)

# CLRS가 매우 중요하다! 일요일은 무조건 이 책을 쭉 읽을 것!

# 평범한 배낭

## Phase1. 직접 풀기

```python
"""
1. 문제 읽기
2. 문제 풀기
important thing is that the dp is not about filling the table. 
it's about doing recursion in a delicate way.
3. 수도 코드
4. 코드 구현
"""

import sys

def recur(n, k, stuffs: list):
    dp = [[0 for _ in range(n)] for _ in range(k+1)] # 가로: 물건, 세로: 무개
    # 0번째 물건에 대해
    for i in range(k+1):
        dp[i][0] = stuffs[0][1] if i >= stuffs[0][0] else 0
    # go dp
    for i in range(k+1):
        for j in range(1, n):
            if i >= stuffs[j][0]:
                dp[i][j] = max(dp[i][j-1], dp[i-stuffs[j][0]][j-1] + stuffs[j][1])
            else:
                dp[i][j] = dp[i][j-1]
    # for d in dp:
    #     print(d)
    return dp[k][n-1]

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    stuffs = [
        tuple(map(int, input().split())) 
        for _ in range(n)
    ]
    print(recur(n, k, stuffs))


"""
4 7
6 13
4 8
3 6
5 12
"""
```

## Phase2. 회고

이번 문제 역시 이미 여러번 풀어 본 문제지만, 강인하게 풀기 위해 재귀 트리를 어떻게 하면 collaps 시킬 수 있을지 고민하며 풀어봤다. j 인덱스를 좀 잘못 줘서 헤맸지만, 전체적인 문제의 구조를 이해하고 있는 상태에서 이건 사소한 에러였다. (j값에서 1만 빼주니 완벽한 정답이었음. 그런데 실전에서 이런 거 틀리면 어떡하지. 답이 없을 거 같다. 정신 차리고 반례를 찾을 수 있을까? GPT: 가능한 한 단위 테스트나 간단한 반례들로 확인하는 습관이 중요합니다.)

![](./images/IMG_0199.png)

## Phase3. 단위 테스트나 반례 정하는 노하우

단위 테스트와 반례를 만드는 것은 문제의 모든 부분을 꼼꼼하게 확인하고, 예상치 못한 오류를 조기에 찾아내는 데 매우 중요한 역할을 합니다. 아래에 몇 가지 노하우와 팁을 정리해 보았습니다.

1. 단위 테스트(Unit Testing) 작성 방법

1.1. 테스트 대상 함수 분리

•	함수 단위 분리:

먼저, 테스트 대상이 되는 기능(함수)을 가능한 독립적으로 분리해 둡니다. 하나의 함수가 하나의 책임만 맡게 되면, 어느 부분에서 문제가 발생하는지 쉽게 파악할 수 있습니다.

1.2. 경계 값과 기본 케이스부터

•	경계 조건 테스트:

입력 값이 최소/최대일 때, 혹은 극단적인 값일 때 어떻게 동작하는지 확인합니다. 예를 들어, 피보나치 함수라면 fib(0), fib(1) 같은 기본 케이스, 혹은 큰 값에 대해서도 테스트해 봅니다.

•	기본 케이스:

예상 가능한 기본 조건(예: 빈 입력, 하나의 원소 등) 에 대한 테스트를 작성합니다.

1.3. 자동화 도구 활용

•	Python의 unittest 또는 pytest:

Python에서는 unittest 모듈이나 pytest 라이브러리를 사용해 쉽게 단위 테스트를 작성할 수 있습니다. 예를 들어, 다음과 같이 작성할 수 있습니다:

```python
import unittest

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

class TestFib(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_recursive_cases(self):
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)

    def test_large_value(self):
        # 큰 값에 대해서도 시간을 고려하여 올바른 값이 나오는지 확인
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()
```

이 방식은 함수의 입력과 예상 결과를 미리 지정하여, 코드가 변경될 때마다 테스트를 빠르게 수행해 볼 수 있습니다.

1.4. 테스트 케이스 작성 시 주의점

•	상태 공유 문제:

위의 피보나치 예제처럼 기본 인자로 mutable 객체(예: memo={})를 사용할 경우 함수가 여러 번 호출되면 이전 상태가 남아있을 수 있습니다.

테스트 시 각각의 테스트 케이스마다 독립적인 상태를 보장하거나, 기본값을 None으로 받고 내부에서 새 객체를 생성하는 방식이 좋습니다.

2. 간단한 반례 만들기

2.1. 알고리즘의 특성과 취약점 분석

•	문제의 제약 조건 이해:

예를 들어 배낭 문제의 경우, 각 물건은 한 번만 사용해야 한다는 조건(0/1 배낭 문제)과 “물건을 여러 번 선택할 수 있는 경우”가 있는지 등에 따른 특성을 잘 분석합니다.

•	잘못 구현될 수 있는 포인트 찾기:

재귀 호출 시 인덱스 처리, 혹은 dp 테이블의 범위 설정, 혹은 상태 업데이트 순서 등에서 실수할 수 있는 부분을 미리 생각합니다.

2.2. 간단한 테스트 케이스 작성

•	예제 케이스:

문제에서 제공되는 예제 입력은 물론, 직접 만들어 본 극단적 또는 모순되는 상황의 케이스를 준비합니다.

•	반례 아이디어:

예를 들어, 배낭 문제에서 물건의 무게와 가치가 극단적으로 낮거나 높은 경우, 혹은 물건의 무게가 knapsack 용량과 딱 맞거나, 약간 부족한 경우 등을 생각해 볼 수 있습니다.

```python
def test_knapsack_edge_cases():
    # 예시: 물건이 한 개 뿐인 경우
    stuffs = [(3, 10)]  # (무게, 가치)
    capacity = 2
    # 물건의 무게가 용량보다 크므로, 선택할 수 없는 경우
    assert recur(1, capacity, stuffs) == 0

    # 물건의 무게가 용량과 딱 맞는 경우
    stuffs = [(2, 10)]
    capacity = 2
    assert recur(1, capacity, stuffs) == 10

    # 여러 물건 중, 하나를 선택하는 것이 최선인 경우 등
    stuffs = [(1, 2), (2, 3), (3, 4)]
    capacity = 4
    # 두 번째와 첫 번째 물건을 선택하는 것이 최선일 경우
    assert recur(3, capacity, stuffs) == 5

# 위와 같이 간단한 반례들을 여러 개 만들어서 테스트해 볼 수 있습니다.
```

2.3. 디버깅과 출력 확인

•	디버깅 출력 활용:

때로는 테스트 케이스가 실패할 때 디버깅을 위해 dp 테이블이나 중간 결과를 출력해 보는 것이 도움이 됩니다.

다만, 최종 제출 전엔 이러한 출력문은 제거하거나 주석 처리해야 합니다.

2.4. 단계별 테스트

•	작은 단위부터 전체까지:

함수나 모듈 단위로 테스트를 작성한 후, 전체 시스템이 통합되었을 때 다시 테스트해보는 것이 좋습니다.

•	수동 검증:

아주 간단한 케이스에 대해 손으로 계산한 예상 결과와 비교하면서 테스트합니다.

3. 테스트 노하우 정리

•	Test-Driven Development (TDD) 접근법:

코드를 작성하기 전에 테스트 케이스를 먼저 작성하고, 테스트 케이스를 통과하도록 코드를 개선하는 방식은 버그를 줄이는 데 큰 도움이 됩니다.

•	자동화된 테스트 스크립트 작성:

여러 테스트 케이스를 한 번에 실행할 수 있는 스크립트를 만들어, 코드 변경 후에도 일관되게 동작하는지 확인합니다.

•	Edge Case 우선 테스트:

보통 간과하기 쉬운 경계 조건(예: 빈 입력, 최소값, 최대값, 반복되는 값 등)을 먼저 테스트해 봅니다.

•	리팩토링 후 재검증:

코드를 개선하거나 리팩토링할 때, 기존에 통과했던 테스트 케이스들을 다시 실행해 “회귀(regression)”가 발생하는지 확인합니다.

단위 테스트와 반례 테스트를 습관화하면, 문제 해결 과정에서 작은 오류나 알고리즘의 취약점을 쉽게 찾아낼 수 있습니다. 이 과정은 코드의 신뢰성을 크게 높여주며, 대회나 실제 프로젝트에서 시간과 노력을 절약할 수 있게 해줍니다.

## Phase4. 노하우 제시에 대한 정리

```python
def test_knapsack_edge_cases():
    # 예시: 물건이 한 개 뿐인 경우
    stuffs = [(3, 10)]  # (무게, 가치)
    capacity = 2
    # 물건의 무게가 용량보다 크므로, 선택할 수 없는 경우
    assert recur(1, capacity, stuffs) == 0

    # 물건의 무게가 용량과 딱 맞는 경우
    stuffs = [(2, 10)]
    capacity = 2
    assert recur(1, capacity, stuffs) == 10

    # 여러 물건 중, 하나를 선택하는 것이 최선인 경우 등
    stuffs = [(1, 2), (2, 3), (3, 4)]
    capacity = 4
    # 두 번째와 첫 번째 물건을 선택하는 것이 최선일 경우
    assert recur(3, capacity, stuffs) == 6

# 위와 같이 간단한 반례들을 여러 개 만들어서 테스트해 볼 수 있습니다.

import sys

def recur(n, k, stuffs: list):
	...

if __name__ == '__main__':	
    input = sys.stdin.readline
    # n, k = tuple(map(int, input().split()))
    # stuffs = [
    #     tuple(map(int, input().split())) 
    #     for _ in range(n)
    # ]
    # print(recur(n, k, stuffs))
    test_knapsack_edge_cases()
```

이렇게 assert를 활용한 테스트 케이스 함수를 쓰고, 제출할 때 주석만 풀어서 제출하면 딱 좋다! 이걸 이제 알았네.

# 행렬 곱셈

## Phase1.

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import defaultdict

def get_cost(n: int, m: int, k: int):
    return n * m * k

def recur(matrices: list, memo = defaultdict(tuple)):
    # 행렬들 matrices의 최소 연산 비용을 반환한다.
    if len(matrices) <= 1: return 0
    # 첫 번째 행렬만 단독으로 나머지와 연산할 경우를 위해
    head = matrices[0]
    n, m1 = head[0], head[1]
    rest = matrices[1:] 
    k = rest[-1][1]
    memo[(m1, k)] = recur(rest, memo)
    cost1 = get_cost(n, m1, k) + memo[(m1, k)]
    # 두 번째 행렬과 함께 연산할 경우를 위해 
    cost2 = sys.maxsize
    if len(matrices) > 2:
        head = matrices[0:2]
        rest = matrices[2:]
        m2 = head[1][1]
        k = rest[-1][1]
        memo[(m2, k)] = recur(rest, memo)
        cost2 = get_cost(n, m2, k) + memo[(m2, k)]
    memo[(n, k)] = min(cost1, cost2)
    return memo[(n, k)]



if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    matrices = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    memo = defaultdict()
    recur(matrices=matrices, memo=memo)
    
    print(memo)

```

갈피는 대충 잡았지만, 구현에서 좀 애를 먹고 있음. 일단 패스.

## Phase2. CLRS의 예제를 공부한 뒤 그냥 수도코드 그대로 작성

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def matrix_chain_order(p, n):
    # 그럼 뭘 해? new array
    m = [[0 for _ in range(n)]for _ in range(n)]
    # 자기 자신만 곱하는 경우 초기화
    for i in range(n):
        m[i][i] = 0
    # 이 아래부터 i < j
    for l in range(2, n+1): #배열의 각 길이. 짧은 경우부터 이터레이션
        for i in range(0, n-l+1):
            # 대체 뭘 구하는 거야? i가 어디까지 커져야 하는지.
            # n - l 이러면? i = n - L - 1
            # 그러면 j는 어떻게 정의해? 
            # i + l - 1 = n 이려면? 
            # i = n - l + 1까지 커질 수 있음.
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i][0] * p[k][1] * p[j][1]
                if q < m[i][j]:
                    m[i][j] = q
    return m[0][n-1]

def test():
    n = 3
    p = [(5, 3), (3, 2), (2, 6)]
    assert matrix_chain_order(p, n) == 90 

def submit(matrix_chain_order):
    input = sys.stdin.readline
    n = int(input().strip())
    p = [
        tuple(map(int, input().split()))
        for _ in range(n)
    ]
    print(matrix_chain_order(p, n))

if __name__ == '__main__':	
    submit(matrix_chain_order)
    # test()

```

Phase1.에서 작성한 스타일로도 문제를 풀 순 없을까?

# 가장 긴 증가하는 부분 수열

## Phase1. 아 진짜 어렵다

모든 문제가 재귀 트리로 만들기에 적절한 건 아니다.

![](./images/IMG_0202.png)

## Phase2. Elements of Dynamic Programming을 읽고 나서…

CLRS의 동적 계획법 파트를 좀 읽어보니 좀 갈피가 잡히는 것 같다. 

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def recur(n, arr):
    dp = [1 for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
        ans = max(ans, dp[i])
    return ans

def test():
    n = 6
    arr = (10, 20, 10, 30, 20, 50)
    assert recur(n, arr) == 4
    n = 1
    arr = (10)
    assert recur(n, arr) == 1
    n = 2
    arr = (10, 20)
    assert recur(n, arr) == 2
    n = 2
    arr = (20, 10)
    assert recur(n, arr) == 1
    # 마지막 디피가 최대가 아닌 경우
    n = 6
    arr = (10, 20, 10, 30, 50, 10)
    assert recur(n, arr) == 4

def submit(recur):
    input = sys.stdin.readline
    n = int(input().strip())
    arr = tuple(map(int, input().split()))
    print(recur(n, arr))

if __name__ == '__main__':	
    submit(recur)
    # test()


```

다시 한번 되짚어보는 디피의 패턴

1. 어떤 문제의 해답이 선택의 연속일때(줄 자르기, 행렬 체인 나누기) 디피를 고려.
1. 이미 주어진 문제에 대해 최선의 선택이 이루어졌다고 생각하기(어떻게 선택했는지 지금은 생각하지 않기)
1. 주어진 선택에 대해 어떤 부문제가 잇따라 일어나는지, 부문제의 결과가 어떻게 유형화되는지 결정하기
1. 자르고 붙이기 테크닉으로 문제가 해결됨을 보여주기. 이것은 의외로 ‘반례를 만드는 선택을’ ‘잘라내고’, 최적의 선택을 ‘붙이는’ 방식으로 진행. 솔루션이 하나 이상의 부문제에 대한 해결을 제공한다면, 이를 조금씩만 수정해서 전체 문제를 해결하는 방향으로 갈 수 있음. cut and paste.
# 동전

## Phase1. 풀이

```python
import sys

def solve(coins, k):
    idx = len(coins)-1
    cnt = 0
    while True:
        # 현재 가리키는 동전이 전체 값보다 작을 때까지 포인터 감소
        while k < coins[idx]:
            idx -= 1
        # 이제 k보다 동전 값이 작습니다. 동전 값보다 k가 큰 동안만
        # while k >= coins[idx]:
        #     k -= coins[idx]
        #     cnt += 1
        r = k//coins[idx]
        k -= coins[idx]*r
        cnt += r
        if k == 0:
            return cnt

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    coins = [
        int(input().strip())
        for _ in range(n)
    ]
    print(solve(coins, k))

```

붕어빵처럼 이터레이션 해버리면 안 되는 거에요

# 잃어버린 괄호

## Phase1. 

```python
import sys

def parse(string: str):
    numeric_tmp = ''
    listed = []
    for s in string:
        if s.isnumeric():
            numeric_tmp += s
        else:
            listed.append(int(numeric_tmp))
            listed.append(s)
            numeric_tmp = ''
    
    listed.append(int(numeric_tmp))
    return listed

def greedy(listed: list):
    neg_flag = False
    result = 0
    for l in listed:
        if isinstance(l, int):
            if neg_flag:
                result -= l
            else:
                result += l
        else:
            if l == '-' and neg_flag != True:
                neg_flag = True
    return result

def solve(string):
    listed = parse(string)
    result = greedy(listed)
    return result

def test():
    string = '55-50+40'
    assert solve(string) == -35
    string = '10+20+30+40' 
    assert solve(string) == 100
    string = '00009-00009'
    assert solve(string) == 0
    string = '1231-1231-1231'
    assert solve(string) == -1231

if __name__ == '__main__':	
    input = sys.stdin.readline
    string = input().strip()
    print(solve(string))
    # test()
    
```

테스트를 적극 활용해봤다. 쉬운 문제를 쓸데없이 어렵게 풀게 되는 건가? 그 부분의 고민이 좀 있다. 

## Phase2. 고민. TDD와 고민의 밸런스를 어떻게 잡아야 하지?

요약: 연습할 때는 적극적으로 활용해라! TDD해서 논리적으로 풀어내는게 중요하지, 못 풀고 정답 보는 것보단 낫다.

테스트 코드를 작성하는 것은 분명 문제 해결 능력을 향상시키고, 엣지 케이스나 실수를 미리 잡아주는 데 큰 도움이 됩니다. 하지만 모든 문제에 TDD(Test-Driven Development) 방식을 과도하게 적용하는 것에 대한 고민은 충분히 타당합니다. 아래 몇 가지 팁을 참고해보세요.

1. 문제 난이도에 따른 TDD 적용 수준 조절

•	쉬운 문제(예: 잃어버린 괄호, 단순 구현 문제):

간단한 입력 몇 개(보통 예제, 기본 경계 조건, 특이 케이스 정도)를 대상으로 한 assert 테스트 정도면 충분합니다.

예를 들어,

```plain text
def test_lost_parenthesis():
    # 기본 예제 테스트
    assert solve('55-50+40') == -35
    # 모두 더하는 경우
    assert solve('10+20+30+40') == 100
    # 앞에 0이 있는 경우, 혹은 뺄셈이 연속되는 경우
    assert solve('00009-00009') == 0
```

정도의 간단한 테스트만으로도 함수의 주요 동작을 확인할 수 있습니다.

•	복잡하거나 버그가 쉽게 발생할 수 있는 문제:

이 경우 좀 더 다양한 케이스(경계 조건, 큰 입력 등)를 미리 작성하는 것이 좋습니다.

단, 코딩 테스트 상황에서는 시간 제약이 크므로, 개인 연습 시에 TDD로 충분히 검증한 다음 제출할 때는 테스트 코드를 제거하는 식으로 작업합니다.

2. TDD의 장점과 단점 균형 맞추기

•	장점:

•	버그 조기 발견: 다양한 입력에 대한 반례를 미리 만들어두면, 예상치 못한 상황이나 데이터에 의한 오류를 사전에 잡을 수 있습니다.

•	안전한 리팩토링: 코드 변경이나 개선이 필요할 때, 기존 테스트가 모두 통과하는지 확인하여 회귀를 방지할 수 있습니다.

•	단점:

•	시간 소모: 특히 쉬운 문제에 대해 과도하게 많은 테스트 케이스를 작성하다 보면, 오히려 시간을 낭비할 수 있습니다.

•	과도한 분석: TDD를 지나치게 강조하다 보면 본질적인 문제 풀이보다는 테스트 케이스에 집착해버리는 경우도 생길 수 있습니다.

3. 실전에서의 적용 방법

•	연습 단계에서는 TDD 적극 활용:

연습할 때는 다양한 케이스를 생각하면서 TDD 스타일로 코드를 검증해보세요. 이를 통해 코드의 견고함과 문제 해결에 필요한 사고 과정을 개선할 수 있습니다.

•	실제 코딩 테스트에서는 기본적인 assert 정도로 충분:

코딩 테스트 환경에서는 보통 입력과 출력만 맞으면 되므로, 문제풀이 로직에 집중하세요.

로컬에서 연습할 때 작성한 테스트 코드는 본인만을 위한 디버깅 도구로 활용하고, 제출 시에는 꼭 제거해야 합니다.

•	테스트 케이스 선정 기준 정리:

•	기본/예제 케이스: 문제에서 제시된 예제나 간단한 경우

•	경계 값: 입력의 최솟값, 최댓값, 빈 값, 혹은 0과 같은 특수 값

•	특이 케이스: 문제의 요구사항에 어긋나거나 버그가 발생할 만한 케이스

4. 결론

결국, TDD와 고민의 균형은 ‘연습 단계에서는 충분히 다양한 테스트를 작성하고, 실전에서는 시간과 결과에 초점을 맞춘 최소한의 검증 코드’ 로 정리할 수 있습니다. 연습 시에는 테스트 케이스를 다양하게 만들어 자신의 코드에 확신을 갖는 것이 중요하고, 실제 코딩 테스트에서는 핵심 로직 구현에 집중하는 것이 효율적입니다.

이렇게 접근하면 “쉬운 문제를 쓸데없이 어렵게 푸는” 느낌보다는, 문제 해결 실력을 높이는 데 큰 도움이 될 것입니다.

# 회의실 배정

## Phase1. 

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1931                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1931                           #+#        #+#      #+#     #
#    Solved: 2025/04/05 20:53:58 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def solve(time_table: list):
    time_table.sort(key=lambda x: (x[1], x[0]))
    prev_start = prev_end = -sys.maxsize
    cnt = 0
    result = []
    for current_start, current_end in time_table:
        if current_start >= prev_end:
            cnt += 1
            result.append((current_start, current_end))
            prev_start, prev_end = current_start, current_end
    # print(result)
    return cnt

def test():
    time_table = [(1, 4), (4, 4), (4, 5)]
    assert solve(time_table) == 3
    time_table = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    assert solve(time_table) == 4
    time_table = [(1, 4), (1, 1), (1, 1)]
    assert solve(time_table) == 3
    time_table = [(0, 0)]
    assert solve(time_table) == 1
    time_table = [(0, 2), (5, 5), (0, 0), (5, 10), (3, 5), (6, 9)]
    assert solve(time_table) == 5


if __name__ == '__main__':	
    ###########################
    input = sys.stdin.readline
    n = int(input().strip())
    time_table = []
    for _ in range(n):
        time_table.append(tuple(map(int, input().split())))
    print(solve(time_table))
    ###########################
    # test()


```

반례를 못 찾아서 결국 testcase.ac를 썼다. 3개의 반례가 있었고, 정렬 조건을 수정해주니 해결됐다. 뭐, 반례를 찾기 어려우면 그만큼 코드는 정답에 가깝다는 의미이니, 반대로 쉬운 반례를 찾아 낸 상황보다 그게 나을 수도 있다. 반례를 찾기 어려운 상황보다, 반례를 찾기 쉬운 상황이 더 문제라는 말이다.

# LCS

## Phase1. 직접 풀기

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9251                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9251                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 12:45:39 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

def get_lcs(a: list, b: list):
    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
    # init
    tmp = 0
    # 세로 문자열
    for i in range(0, len(a)):
        if a[i] == b[0]: 
            tmp = 1 
        dp[i][0] = tmp
    
    tmp = 0
    for i in range(0, len(b)):
        if b[i] == a[0]: 
            tmp = 1 
        dp[0][i] = tmp 

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            tmp = 0
            if a[i] == b[j]:
                tmp = dp[i-1][j-1] + 1
            # else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], tmp)

    return dp[-1][-1]

def test():
    a = "ACAYKP"
    b = "CAPCAK"
    assert get_lcs(a, b) == 4
    a = "abc"
    b = "cde"
    assert get_lcs(a, b) == 1
    a = "abcc"
    b = "cdec"
    assert get_lcs(a, b) == 2
    a = "ECGIJEH"
    b = "JHHEAGF"
    assert get_lcs(a, b) == 2

def submit(get_lcs, input):
    a = list(input().strip()) 
    b = list(input().strip())
    print(get_lcs(a, b))

if __name__ == '__main__':	
    input = sys.stdin.readline
    submit(get_lcs, input)
    # test()
```

이 문제도 반례를 못 찾아버렸지 뭐야. 그런데 testcase.ac에서도 반례가 50개나 나와버렸다. 이러면 안 되지. 그냥 로직이 잘못된 거긴 했는데.

# 신입 사원

## Phase1. 

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

def greedy(n, appliers):
    appliers.sort()
    max_cnt = 0
    for i in range(n-1):
        # pivot
        cnt = 1
        pivot_doc, pivot_interview = appliers[i]
        for j in range(i+1, n):
            comp_doc, comp_interview = appliers[j]
            if pivot_interview > comp_interview:
                cnt += 1
                pivot_doc, pivot_interview = comp_doc, comp_interview
        max_cnt = max(cnt, max_cnt)
    return max_cnt


def greedy_2(n, appliers):
    appliers.sort()
    # pivot
    cnt = 1
    pivot_doc, pivot_interview = appliers[0]
    for j in range(1, n):
        comp_doc, comp_interview = appliers[j]
        if pivot_interview > comp_interview:
            cnt += 1
            pivot_doc, pivot_interview = comp_doc, comp_interview
    return cnt

def test():
    n = 5
    appliers = [(3, 2), (1, 4), (4, 1), (2, 3), (5, 5)]
    assert greedy_2(n, appliers) == 4
    n = 7
    appliers = [(3, 6), (7, 3), (4, 2), (1, 4), (5, 7), (2, 5), (6, 1)]
    assert greedy_2(n, appliers) == 3

def submit(greedy):
    input = sys.stdin.readline
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        appliers = [
            tuple(map(int, input().split()))
            for _ in range(n)
        ]
        print(greedy(n, appliers))

if __name__ == '__main__':	
    submit(greedy_2)
    # test()

```

두 개의 함수를 구현했다. 첫 번째는 비교를 시작할 대상을 마지막을 제외한 모든 사원으로 삼았는데, 당연히 알고리즘의 그리디한 성질을 잘 살리지 못한 코드다. 그럼에도 이렇게 구현했던 이유는, 만약 아래와 같이

(1, 2), (2, 100), (3, 99), …

이런 경우가 있다면 첫 비교군부터 쭉 잘못가지 않나 싶어서 그랬는데, 당연히 시간초과가 났다. 그래서 혹시나 싶어 그냥 이런 고려 없이 이터레이션 하나를 없앤 버전을 제출했더니 바로 통과됐다. 그럼, 다시 돌아와서, 위와 같은 테스트 케이스를 통과된 알고리즘이 잡아낼 수 있는가?

```python
n = 3
appliers = [(1, 2), (2, 100), (3, 99)] 
```

정답은 2인데, 1이 나오지 않나?? 

문제를 잘못 읽었다! 값이 작으면 순위가 더 높은 거다. 반대로 값이 클 때 순위가 높은 거라면? 정렬 기준을 거꾸로 잡아 주면 될 거 같다.

# 멀티탭 스케줄링

## Phase1.  실패.

```python
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""
import sys

def init_usetime(k, arr):
    use_time = [0 for _ in range(k+1)]
    # 나머지를 무한대로 초기화하고.
    for elem in arr:
        use_time[elem] += 1
    return use_time
    
def greedy(n, k, arr):
    use_time = init_usetime(k, arr)
    # 이제 힙에는 elem에 대해 (use_time[elem], elem)을 집어 넣으면 됨.
    # 첫 n개의 elem을 집어넣고 시작해야 함.
    multi_tab = set()
    idx = 0 # 고려한 물건 인덱스. 문제가 해결될 때까지 incremental 1 based.
    cnt = 0
    while len(multi_tab) < n:
        if arr[idx] not in multi_tab:
            multi_tab.add(arr[idx])
            use_time[arr[idx]] -= 1
        idx += 1

    for idx_pass2 in range(idx, k):
        if arr[idx_pass2] in multi_tab:
            use_time[arr[idx_pass2]] -= 1
        else:
            # 적절한 최소 인덱스를 찾기
            min_val = float('inf')
            min_idx = 0
            for i in range(1, k+1):
                if use_time[i] < min_val and i in multi_tab:
                    min_idx = i
                    min_val = use_time[min_idx]
            target_idx = min_idx
            multi_tab.remove(target_idx)
            multi_tab.add(arr[idx_pass2])
            use_time[arr[idx_pass2]] -= 1
            cnt += 1
    return cnt
    
    
def test():
    n, k = 2, 7
    arr = (2, 3, 2, 3, 1, 2, 7)
    assert greedy(n, k, arr) == 2
    n, k = 1, 5
    arr = (1, 2, 3, 4, 5)
    assert greedy(n, k, arr) == 4
    n, k = 2, 5
    arr = (1, 2, 1, 2, 3)
    assert greedy(n, k, arr) == 1
    n, k = 3, 7
    arr = (4, 4, 3, 1, 3, 1, 2)
    assert greedy(n, k, arr) == 1
    n, k = 3, 14
    arr = (1, 4, 3, 2, 5, 4, 3, 2, 5, 3, 4, 2, 3, 4)
    assert greedy(n, k, arr) == 4

def submit(greedy):
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    arr = tuple(map(int, input().split()))
    print(greedy(n, k ,arr))

if __name__ == '__main__':	
    # submit(greedy)
    test()


```

## Phase2. 피드백 

문제 정의 및 해결책이 완전히 틀렸음. 

