# [Algorithm] Jungle Week 03 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 트리, 재귀: 트리 순회

https://www.acmicpc.net/problem/1991

이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

- 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
- 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
- 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
## Phase 1. 직접 풀기 - 실패

기본 문제지만 도저히 구현이 기억이 안 남.

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1991                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1991                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:04:08 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
1. 문제 읽기: ok
2. 문제 풀기: DFS로 다 풀면 될 거 같음.
그런데 아무리 고민해도 머리속에 구현이 안 나온다. 이거 입력 어떻게 처리했는지 하나도 기억이 안 남.
3. 수도 코드: 
4. 코드 구현
"""

class Node():
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def preorder():
    pass

def inorder():
    pass

def postorder():
    pass

def get_adjacency_array(arr: list):
    pass

import sys

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(str, input().split()))
        for _ in range(n)
    ]
    # pass 1: 노드를 생성한다.
    vertices = []
    for elem in arr:
        val = elem[0]
        Node(value=val)
    # pass 2: 노드를 순회하며 
        
    
```

## Phase 2. 피드백(정답 제외)

좋아, 아주 잘하고 있어. 이 문제는 전형적인 트리 구조 + 재귀 순회 패턴을 묻는 문제고, 멘탈 모델을 확립하기 딱 좋은 사례야. 정답은 아직 안 보여주고, 문제 접근 피드백만 줄게.

✅ 피드백: 어디에서 막혔고, 어떻게 정리하면 좋을까?

1. 막힌 부분의 본질: 입력 처리 & 구조화

•	지금 막힌 핵심은 “어떻게 트리를 만들지 모르겠음” → 트리를 저장할 구조 모델링이 아직 감이 잘 안 잡혔다는 뜻.

•	이 문제에서의 입력은 루트, 왼쪽 자식, 오른쪽 자식의 묶음으로 주어짐.

예: A B C → A의 왼쪽 자식은 B, 오른쪽 자식은 C

👉 이걸 보고 **“Node 클래스를 만들고 트리를 구성해야겠다”**고 한 건 아주 훌륭한 판단이야. 방향은 정확해.

2. 트리를 만드는 구조화의 한 가지 방법

> “노드를 먼저 다 만든 다음, 링크를 이어준다.”

```python
nodes = {}
for val, left, right in arr:
    if val not in nodes:
        nodes[val] = Node(val)
    if left != '.':
        nodes[left] = Node(left)
        nodes[val].left = nodes[left]
    if right != '.':
        nodes[right] = Node(right)
        nodes[val].right = nodes[right]
```

•	여기서 핵심은 값 기준으로 Node들을 미리 생성하고, 자식 노드들을 연결하는 방식.

•	'B'나 'C' 같은 노드가 아직 만들어지지 않았더라도 dict를 통해 관리하면 문제없음.

✅ 너가 작성한 코드 분석

👍 잘한 점

•	Node 클래스를 도입한 점은 훌륭해.

•	arr로 입력 데이터를 구조화한 점도 좋아.

•	전위/중위/후위 순회를 별도 함수로 구성하려는 시도도 구조적으로 잘 잡힘.

🤔 개선하면 좋은 점

•	vertices = []에서 만든 Node 인스턴스들을 저장하지 않음 (dict를 써야함)

•	get_adjacency_array() 함수는 안 써도 될 가능성이 높음 (이 문제는 adjacency list가 아니라 연결 구조 자체를 생성하는 문제임)

•	트리 구조를 만들기 위한 “중심 노드(root)“를 결정하지 않았음 → 이 문제에서는 무조건 첫 줄의 노드가 루트임

📌 멘탈 모델로 요약하면

이 문제는 다음 구조로 이해해야 해:

1.	입력 구조를 보고 트리를 만든다

•	Node 객체들을 만들어 연결한다.

2.	루트에서부터 재귀적으로 순회를 수행한다

•	전위, 중위, 후위 각각을 따로 구현

3.	출력은 각 순회 결과를 이어서 출력한다

> “재귀 순회는 순서만 외우면 된다.

> 전: 루 왼 오 / 중: 왼 루 오 / 후: 왼 오 루”

🔍 연습 질문 (멘탈 모델 강화를 위한 자가점검)

1.	전위/중위/후위 순회의 순서는 왜 그렇게 구성되는가?

2.	루트를 기준으로 왼쪽, 오른쪽을 방문할 때, 어떤 방식이 전체 트리 구조를 가장 잘 복구할 수 있을까?

3.	트리를 배열로 저장하는 방식은 어떤 상황에 유리할까?

원한다면 다음 단계로 정답 코드 없이 “구조 설계부터 완성까지” 같이 진행해볼 수도 있어!

혹은 재귀 순회만 따로 예제와 함께 연습하고 싶다면 그것도 가능해.

## Phase3. 피드백 후 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1991                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1991                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:04:08 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
1. 문제 읽기: ok
2. 문제 풀기: DFS로 다 풀면 될 거 같음.
그런데 아무리 고민해도 머리속에 구현이 안 나온다. 이거 입력 어떻게 처리했는지 하나도 기억이 안 남.
3. 수도 코드: 
4. 코드 구현
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(node: Node):
    # base case
    if node.left == None and node.right == None:
        print(node.value, end='')
        return
    print(node.value, end='')
    # 왼쪽 먼저.
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

def inorder(node: Node):
    # base case
    if node.left == None and node.right == None:
        print(node.value, end='')
        return
    if node.left != None:
        inorder(node.left)
    print(node.value, end='')
    if node.right != None:
        inorder(node.right)

def postorder(node: Node):
    # base case
    if node.left == None and node.right == None:
        print(node.value, end='')
        return
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.value, end='')


def get_adjacency_array(arr: list):
    pass

import sys

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(str, input().split()))
        for _ in range(n)
    ]
    nodes = {}
    for val, left, right in arr:
        if not nodes.get(val, False):
            nodes[val] = Node(val)
        if left != '.':
            nodes[left] = Node(left)
            nodes[val].left = nodes[left]
        if right != '.':
            nodes[right] = Node(right)
            nodes[val].right = nodes[right]
    preorder(nodes['A'])
    print()
    inorder(nodes['A'])
    print()
    postorder(nodes['A'])
    
```

### 풀이에 대한 피드백

너무 잘 풀었어! 직접 구현에 성공했고, 핵심 로직도 잘 짜여 있어.

아래는 리뷰 + 개선 포인트 + 칭찬 포인트를 정리한 피드백이야.

✅ 전체적으로 잘한 점

1. 트리 구성 로직 정확

•	입력을 받아서 노드를 만들고, 자식 노드를 연결하는 부분이 깔끔하고 정확해.

•	dict를 이용해서 중복 생성을 막은 것도 좋고, .left, .right로 연결한 방식도 명확해.

2. 재귀 순회 함수 구현

•	전위/중위/후위 순회 모두 요구된 순서에 따라 잘 작성했어.

•	재귀 흐름을 잘 이해하고 있어서, 각 순회의 논리를 정확히 반영함.

3. 출력 방식

•	print(..., end='') 사용해서 줄바꿈 없이 연결한 것도 문제 조건에 정확히 부합해.

🔧 개선 포인트 (가볍게 리팩터링)

1. 재귀의 base case 단순화 가능

현재는 이렇게 돼 있지:

```plain text
if node.left == None and node.right == None:
    print(node.value, end='')
    return
```

이건 사실 필요 없어! 바로 아래처럼 처리하면 훨씬 깔끔하고 동작은 똑같아:

```python
def preorder(node: Node):
    if node is None:
        return
    print(node.value, end='')
    preorder(node.left)
    preorder(node.right)
```

다른 순회들도 같은 방식으로 개선 가능해.

2. 노드 중복 생성 방지 로직 개선

지금 이렇게 돼 있지:

```python
if not nodes.get(val, False):
    nodes[val] = Node(val)
```

더 간단하게 if val not in nodes:로 쓰는 게 일반적이야.

또한 자식 노드들 생성도 조건을 두는 게 좋아:

```python
if left != '.':
    if left not in nodes:
        nodes[left] = Node(left)
    nodes[val].left = nodes[left]
```

지금처럼 하면 이미 있는 노드라도 무조건 새로 생성될 수 있어서 구조가 꼬일 수 있어.

🧠 멘탈 모델 강화 포인트

너는 지금 이미 트리를 노드 단위로 구성 → 순회 구현 → 결과 출력이라는 기본적인 트리 문제의 구조를 익힌 상태야.

앞으로는 이런 질문으로 스스로 사고를 확장해봐:

•	트리를 리스트로 표현하는 방식과 어떻게 다를까?

•	순회 결과를 문자열로 저장해서 리턴하려면 어떻게 바꿔야 할까?

•	비재귀로 구현하면 어떤 식으로 스택을 활용할 수 있을까?

✨ 총평

•	✔️ 트리 구조 완성도 높음

•	✔️ 순회 구현 정확

•	✔️ 입출력 처리 문제 없음

•	🔄 base case 개선 가능

•	🔄 dict 활용 방식 리팩터링 여지 있음

너무 잘했고, 이 문제를 제대로 구현한 것만으로도 앞으로 나올 모든 순회 관련 문제에 자신감을 가져도 돼.

다음으로는 레벨업된 트리 문제 (예: 이진 탐색 트리 삽입/삭제, 최소 공통 조상 LCA, 직렬화/복원) 쪽으로 가봐도 좋아!

필요하면 다음 추천 문제도 이어서 정리해줄게. 계속 가보자! 💪🌳

### 피드백 수정 반영

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1991                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1991                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:04:08 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


"""
1. 문제 읽기: ok
2. 문제 풀기: DFS로 다 풀면 될 거 같음.
그런데 아무리 고민해도 머리속에 구현이 안 나온다. 이거 입력 어떻게 처리했는지 하나도 기억이 안 남.
3. 수도 코드: 
4. 코드 구현
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(node: Node):
    # base case
    if node == None:
        return
    print(node.value, end='')
    # 왼쪽 먼저.
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)

def inorder(node: Node):
    # base case
    if node == None:
        return
    if node.left != None:
        inorder(node.left)
    print(node.value, end='')
    if node.right != None:
        inorder(node.right)

def postorder(node: Node):
    # base case
    if node == None:
        return
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.value, end='')


def get_adjacency_array(arr: list):
    pass

import sys

if __name__ == '__main__':
    
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(str, input().split()))
        for _ in range(n)
    ]
    nodes = {}
    for val, left, right in arr:
        if val not in nodes:
            nodes[val] = Node(val)
        if left != '.':
            if left not in nodes:
                nodes[left] = Node(left)
            nodes[val].left = nodes[left]
        if right != '.':
            if right not in nodes:
                nodes[right] = Node(right)
            nodes[val].right = nodes[right]
    preorder(nodes['A'])
    print()
    inorder(nodes['A'])
    print()
    postorder(nodes['A'])
    
```

# 이진트리: 이진 검색 트리

https://www.acmicpc.net/problem/5639

이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성하시오.

## Phase 1. 직접 풀기 - 실패

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5639                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:51:32 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 노드 입력
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

def generate_bs_tree(nodes: list):
    bs_tree = defaultdict()
    bs_tree[nodes[0]] = Node(val=nodes[0])
    # print(ptr)
    # 1. 현재 값으로 노드를 생성한다.
    for val in nodes[1:]:
        ptr = bs_tree[nodes[0]]
        # print("ptr", ptr)
        bs_tree[val] = Node(val=val)
        # 2. bs_tree에서 누구 자식으로 만들지 결정한다. 일단 루트 포인터 지목?
        while True:
            if bs_tree[val].val < ptr.val:
                if ptr.left == None:
                    ptr.left = bs_tree[val]
                    break
                ptr = ptr.left
            elif bs_tree[val].val > ptr.val:
                if ptr.right == None:
                    ptr.right = bs_tree[val]
                    break
                ptr = ptr.right
        # 3. 순회 끝. 지금 ptr은 어떤 노드의 left, right 빈 슬롯을 참조.
        ptr = bs_tree[val]
    # for value in bs_tree.values():
        # print(value.val, value.left.val if value.left != None else 'None', value.right.val if value.right != None else 'None')
    # 문제점: 주어지는 값이 프리오더 서치라서 그대로 bs tree를 만들면 안 됨 
    # -> 그게 문제가 아니었음. 루트 포인터가 처음부터 업데이트되지 않은게 문제였음.
    return bs_tree[nodes[0]], bs_tree

def pre_search(node: Node, tree):
    # print(f'recursion start: {node.val}')
    if node.val == None:
        return
    if node.left != None:
        pre_search(node.left, tree)
    if node.right != None:
        pre_search(node.right, tree)
    print(node.val)

from collections import deque

def pre_search_stack(node: Node, tree):
    stack = deque()
    stack.append(node)
    while stack:
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
        print(node.val)
        node = stack.pop()


import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.


if __name__ == "__main__":

    nodes = []
    for line in sys.stdin:
        nodes.append(int(line.strip()))
    root, bs_tree = generate_bs_tree(nodes)
    pre_search(root, bs_tree)
    # print(nodes)

"""
이슈: recursion error

Phase1.
환경: 파이썬
로그: maximum recursion exceeded
최근 변경 사항: bs-tree를 만들고, 재귀적으로 후위탐색을 하는 코드 작성.

Phase2.
확인: 재귀식 논리에 에러가 없는 한 최대 재귀 설정이 묶여 있어서 그런 것으로 보임
시도: 
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

분석: 재귀 에러는 없어짐.
"""

"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 28프로에서 시간 초과 발생.
최근 변경 사항: 재귀적인 후위 순회 구현이 문제인가? 스택으로 바꿔야할지도.

Phase2.
확인: 스택으로 변경 시도.
시도: 

from collections import deque

def pre_search_stack(node: Node, tree):
    stack = deque()
    stack.append(node)
    while stack:
        if node.right != None:
            stack.append(node.right)
        if node.left != None:
            stack.append(node.left)
        print(node.val)
        node = stack.pop()

분석: 똑같은 지점에서 에러가 남. 구조적인 문제가 있음. 
""" 
```

## Phase2. 피드백 - 봐도 이해가 잘… 일단 패스.

아래는 Baekjoon 5639(이진 검색 트리 후위 순회) 문제를 효율적으로 해결하기 위한 방법입니다.

주어진 입력(전위 순회 결과)을 바탕으로 **이진 검색 트리(BST)**를 재구성하고, 후위 순회 결과를 출력합니다.

문제 요약

•	입력:

•	표준 입력으로 여러 줄에 걸쳐 정수가 들어옵니다. (EOF까지)

•	이 수들은 BST의 전위 순회(preorder) 형태로 주어집니다.

•	출력:

•	해당 BST의 후위 순회(postorder) 결과를 한 줄씩 출력합니다.

주의해야 할 점

1.	입력이 전위 순회라는 점

•	첫 번째 값이 루트 노드입니다.

•	두 번째부터는 왼쪽 서브트리에 속하는 값들(루트보다 작음), 그 뒤로는 오른쪽 서브트리에 속하는 값들(루트보다 큼)이 전위 순회 순서대로 이어집니다.

2.	일반적인 삽입 방식으로 BST를 구성하는 경우

•	입력이 정렬(혹은 역정렬) 상태에 가깝다면, 트리가 한쪽으로 치우치게 됩니다(스큐드 트리, skewed tree).

•	각 값 삽입 시 최악의 경우 O(N), 전체적으로 O(N^2) 시간이 걸릴 수 있습니다.

•	파이썬으로는 시간이 많이 소요되어 시간 초과가 날 가능성이 큽니다.

3.	재귀 호출 깊이

•	입력 데이터가 많아 트리가 매우 깊어질 수 있으므로, sys.setrecursionlimit를 늘려두어야 합니다.

효율적 풀이 아이디어 (min/max 범위 방식)

전위 순회 배열을 이용해 BST를 재구성하면서 동시에 후위 순회를 출력하는 방법을 사용합니다.

이 알고리즘은 흔히 “min/max 범위 검사 방식”으로 불리며, 다음과 같은 로직으로 동작합니다:

1.	전역 인덱스 idx로 전위 순회 리스트(preorder)를 순회합니다.

2.	재귀 함수 build_postorder(lb, ub)는 현재 서브트리에 해당하는 값이 (lb, ub) 범위 안에 있을 때만 노드를 생성합니다.

•	preorder[idx]가 lb < 값 < ub 범위 밖이라면, 현재 서브트리를 만들 수 없으므로 즉시 반환합니다.

3.	유효한 값이라면, 현재 값(root_val)으로 노드를 만든 뒤,

•	왼쪽 서브트리는 (lb, root_val) 범위,

•	오른쪽 서브트리는 (root_val, ub) 범위로 재귀적으로 만들고,

•	최종적으로 현재 root_val을 출력(후위 순서)합니다.

이 방식은 한 번의 DFS(깊이 우선 탐색)로 각 노드를 딱 한 번씩만 처리하므로, 입력이 BST 전위 순회라는 전제하에 O(N) 시간에 트리를 재구성할 수 있습니다.

코드 예시

실행 흐름 설명

1.	입력 읽기

•	EOF까지 줄 단위로 읽어서 preorder 리스트에 담습니다.

2.	전역 인덱스 idx

•	전위 순회에서 아직 사용하지 않은 노드의 위치를 가리킵니다.

•	각 노드를 소비할 때마다 idx를 1씩 증가시킵니다.

3.	build_postorder(lb, ub)

1.	만약 idx가 이미 preorder 길이만큼 커졌다면, 사용할 값이 없으므로 바로 종료합니다.

2.	preorder[idx]가 (lb, ub) 범위에 해당하지 않으면, 이 위치에는 노드를 만들 수 없으므로 종료합니다.

3.	유효하다면 preorder[idx]를 현재 서브트리 루트로 하고, idx += 1로 소모합니다.

4.	그 뒤 (lb, root_val) 범위로 왼쪽 서브트리, (root_val, ub) 범위로 오른쪽 서브트리를 만들기 위해 재귀 호출합니다.

5.	좌우 서브트리 생성이 끝나면, 루트(= root_val)를 출력합니다(후위 순회).

4.	결과

•	모든 노드에 대해 후위 순회 순서대로 root_val이 출력되어 최종 정답이 됩니다.

복잡도

•	시간 복잡도: O(N)

•	전위 순회 배열을 처음부터 끝까지 한 번씩만 탐색하고, 각 요소에 대해 재귀 호출을 한 번씩만 진행합니다.

•	공간 복잡도: O(N)

•	입력 데이터 저장용 리스트 preorder가 O(N).

•	재귀 호출 최대 깊이는 N까지 가능(스큐드 트리)하므로, sys.setrecursionlimit을 넉넉하게 설정합니다.

결론

1.	주어진 전위 순회로부터 min/max 범위 검사를 활용하여 BST를 한 번에 복원하며,

2.	그 과정에서 후위 순회를 출력하는 방법을 사용하면, 시간초과와 재귀 제한 문제를 모두 해결할 수 있습니다.

이 코드를 제출하면 Baekjoon 5639 문제를 파이썬으로 효율적으로 통과할 수 있습니다.

## Phase3. 1차 재도전 - 30분 - 실패

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5639                           #+#        #+#      #+#     #
#    Solved: 2025/03/27 21:51:32 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
50
30
24
5
28
45
98
52
60
아 스택을 활용하면 되나?

3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

def solve(nodes: list):
    # 일단 쭉 입력을 받는다. 
    # left, right 포인터를 유지하면서 '가족'을 확인한다. 위쪽 가족은 스택에 박아 넣는다.
    queue = deque() # 완성된 가족을 저장
    stack = deque([nodes[0]]) # 위에 있는 가족을 저장
    ptr = 0
    # 50 30 24 5 28 45 98 52 60
    while True:
        current_node = stack.popleft()
        if ptr < len(nodes):
            ptr += 1
        else: 
            break
        # 50 30 
        if current_node > nodes[ptr]:
            stack.append(current_node)
            stack.append(nodes[ptr])
        elif current_node < nodes[ptr]:
            queue.append([current_node, nodes[ptr]])

if __name__ == "__main__":

    nodes = []
    for line in sys.stdin:
        nodes.append(int(line.strip()))
    

```

## Phase4. 2차 피드백

아래는 전위 순회(preorder)로 주어진 이진 검색 트리를 다시 복원한 뒤, 후위 순회(postorder) 결과를 출력하는 전형적인 방법입니다.

설명을 먼저 간단히 하고, 이후에 예시 코드(파이썬)를 제시하겠습니다.

전체 아이디어

1.	전위 순회(preorder)는 항상 다음과 같은 순서로 노드를 방문합니다.

•	루트(root) → 왼쪽 서브트리(left subtree) → 오른쪽 서브트리(right subtree)

2.	따라서 전위 순회 결과에서,

•	첫 번째 원소가 항상 현재(부분)트리의 루트가 됩니다.

•	루트 이후로 루트 값보다 작은 값들은 왼쪽 서브트리로,

•	루트 값보다 큰 값들은 오른쪽 서브트리로 가야 합니다.

3.	전위 순회 배열 preorder 내에서

•	preorder[0] : 루트 노드의 값

•	preorder[1 ... k-1] : 루트보다 작은 값 → 왼쪽 서브트리

•	preorder[k ... end] : 루트보다 큰 값 → 오른쪽 서브트리

여기서 k는 배열을 순회하며 처음으로 루트 값보다 큰 값이 나오는 인덱스가 됩니다.

4.	위 로직을 재귀적으로 적용하여 트리를 만들 수 있습니다.

5.	트리가 복원되면 후위 순회(postorder) 결과는

•	왼쪽 서브트리 → 오른쪽 서브트리 → 루트

순서대로 방문하며 출력하면 됩니다.

구체적인 단계

1.	입력 받기

•	전위 순회 결과를 입력으로 받습니다(EOF까지 반복해서 int 형태로 입력).

2.	트리 복원 함수 build_tree(preorder, start, end)

•	종료 조건: start > end → 서브트리가 비었으므로 None 반환.

•	root_value = preorder[start] → 현재 서브트리의 루트 값

•	idx 탐색: start+1부터 end까지 확인하면서 root_value 보다 처음으로 큰 값의 인덱스 idx를 찾습니다.

•	만약 끝까지 큰 값을 못 찾으면, 즉 전부 루트보다 작으면 idx = end + 1로 둡니다.

•	왼쪽 서브트리는 (start+1, idx-1), 오른쪽 서브트리는 (idx, end) 범위로 재귀적으로 트리를 만듭니다.

•	현재 루트 노드를 만들어서 (root.left, root.right)를 연결한 뒤 루트를 반환합니다.

3.	후위 순회 함수 postorder(node)

•	노드가 None이면 즉시 반환

•	postorder(node.left)

•	postorder(node.right)

•	print(node.value)

4.	최종적으로 postorder를 통해 후위 순회 결과를 출력합니다.

예시 코드

동작 예시

•	입력(전위 순회):

```plain text
50
30
24
5
28
45
98
52
60
```

•	위 코드를 통해 복원하면, 원래의 이진 검색 트리가 재구성됩니다.

•	이후 후위 순회하면 결과로

```plain text
5
28
24
45
30
60
52
98
50
```

가 차례대로 출력됩니다.

이렇게 전위 순회 정보만으로 BST를 정확히 복원할 수 있고, 이후에는 후위 순회를 통해 원하는 출력 결과를 얻을 수 있습니다.

## Phase5. 포기

도저히 모르겠다. 머리에 그림이 안 그려짐

### 일단 코드 필사

```python
import sys
sys.setrecursionlimit(10**6)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    if start >= end:
        return
    
    root = preorder[start]
    idx = start + 1

    # 오른쪽 서브트리의 시작점을 찾기
    while idx < end and preorder[idx] < root:
        idx += 1

    # 왼쪽 서브트리
    postorder(start + 1, idx)
    # 오른쪽 서브트리
    postorder(idx, end)
    # 루트 출력
    print(root)

postorder(0, len(preorder))
```

### 안 보고 코드 쓰고 채점

### 코딩

# MST: 최소 스패닝 트리

https://www.acmicpc.net/problem/1197

그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

## Phase1. 직접 풀기

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1197                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1197                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 13:45:11 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

class Node:
    def __init__(self, value=None):
        self.value = value

# class Bucket:
#     def __init__(self, node: Node, next=None, w=None):
#         self.node = node
#         self.next = next
#         self.w = w

# class AdjacencyList:
#     def __init__(self, v_num: int):
#         self.table = [
#             Bucket(Node(i)) for i in range(1, v_num+1)
#         ]

from collections import defaultdict

if __name__ == '__main__':	
    input = sys.stdin.readline
    v, e = tuple(map(int, input().split()))
    E = [
        tuple(map(int, input().split()))
        for _ in range(e)
    ]
    # 1. 입력받기. 어떻게? 연결 리스트? 
    # 근데 인접 리스트 어떻게 만들어? 그냥 linked list 구현하면 되나?

    # al = AdjacencyList(v)
    # for bucket in al.table:
    #     print(bucket.node.value)
    # 그래프 입력부터 또 막히네. 똑같이 딕셔너리 쓰면 안 되나. 
    # 일단 간선 정보를 어떻게 저장해야할지 모르겠음!!
    graph = defaultdict()
    for e in E:
        u, v, w = e
        graph[u] = 
```

## Phase2. 피드백(정답 제시 금지)

피드백:

•	그래프 저장 구조

•	최소 스패닝 트리는, 간선을 정렬해서 처리하는 크루스칼(Kruskal) 알고리즘이 많이 쓰이는데, 이 경우엔 간선 리스트만 있어도 충분합니다.

•	간선 리스트는 (u, v, w) 형태로 전부 모아서 w 기준 오름차순 정렬 후, 유니온 파인드(Union-Find) 자료구조로 사이클 여부를 관리하면서 MST를 완성하는 방법입니다.

•	굳이 인접 리스트(Adjacency List)를 직접 구현하지 않아도 되고, collections.defaultdict나 간단한 리스트로도 간선 목록을 처리할 수 있습니다.

•	연결 리스트 방식

•	예제 코드에서 Node, Bucket, AdjacencyList 등을 만들고 있는데, 굳이 링크드 리스트 구조를 직접 구현할 필요는 없어 보입니다.

•	파이썬에서는 리스트/딕셔너리로 충분히 인접 리스트나 간선 리스트를 표현할 수 있어서, 직접 class로 링크드 리스트를 구성하면 오히려 구현이 복잡해질 수 있습니다.

•	중복 정의 주의

•	Node 클래스에 value만 저장하고, 그걸 다시 Bucket으로 감싸는 식은 구조가 중복될 수 있습니다.

•	간단하게 정점 번호를 정수로 취급하고, 간선을 (u, v, w) 튜플로 보관하는 쪽이 더 직관적일 수 있습니다.

•	입력 처리

•	지금 E = [tuple(map(int, input().split())) for _ in range(e)]처럼 입력을 받아서,

[(u_1, v_1, w_1), (u_2, v_2, w_2), \dots]

형태로 저장하는 방식은 이미 괜찮아 보입니다.

•	이후 이 리스트를 가지고 MST 알고리즘(예: Kruskal)에서 정렬 + 유니온 파인드 절차만 구현하면 됩니다.

•	유니온 파인드

•	MST 구현에서 핵심은 사이클 판정이므로, 유니온 파인드(Disjoint Set Union, DSU) 자료구조가 사실상 필수적인데, 현재 코드에는 그 부분이 안 보입니다.

•	유니온 파인드를 어떻게 설계할지, parent 배열과 rank(또는 size) 배열을 두고 find, union 함수로 구현하는 방법을 우선 고민해 보세요.

•	성능 고려

•	정점 V와 간선 E의 최대 크기에 따라,

•	정렬에 O(E \log E)

•	유니온 파인드 연산(거의 O(\alpha(V)), 매우 작음)

•	전체 시간 복잡도 O(E \log E)를 만족하면 충분히 빠를 것입니다.

•	출력

•	MST의 가중치 합만 출력하면 되므로, 각 단계에서 선택된 간선들의 w를 누적해서 출력하면 됩니다.

•	“최소 스패닝 트리” 자체를 출력하는 문제(간선 목록)를 요구하는 게 아니니, 최종 합만 구해서 프린트하면 됩니다.

결론적으로,

1.	간선 리스트만 준비해도 MST 구현(특히 크루스칼)은 충분하다.

2.	Node, Bucket 같은 링크드 리스트 기반 구조는 굳이 작성 안 해도 된다.

3.	유니온 파인드(Disjoint Set)를 작성해, 정렬된 간선을 순서대로 확인하며 MST를 구성하는 흐름을 잡아보자.

이 정도 피드백을 토대로 코드를 이어서 수정해 보시길 추천드립니다.

### 피드백에 대한 계획

- 크루스칼: Introduction to algorithm 개개구코로 읽기
- Union find 작성 연습 - gpt
## Phase3. 피드백 후 재시도

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1197                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1197                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 13:45:11 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# class Node:
#     def __init__(self, value=None):
#         self.value = value

# class Bucket:
#     def __init__(self, node: Node, next=None, w=None):
#         self.node = node
#         self.next = next
#         self.w = w

# class AdjacencyList:
#     def __init__(self, v_num: int):
#         self.table = [
#             Bucket(Node(i)) for i in range(1, v_num+1)
#         ]

from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x]) # x = find(parent[x])로 했다가 재귀 에러 발생. parent[x]가 갱신되지 않으면 find를 재귀할 의미가 없으므로 당연
    return parent[x]

def union(x, y, c):
    global parent
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return c
    return 0



if __name__ == '__main__':	
    input = sys.stdin.readline
    v, e = tuple(map(int, input().split()))
    E = [
        tuple(map(int, input().split()))
        for _ in range(e)
    ]
    # 1. 입력받기. 어떻게? 연결 리스트? 
    # 근데 인접 리스트 어떻게 만들어? 그냥 linked list 구현하면 되나?

    # al = AdjacencyList(v)
    # for bucket in al.table:
    #     print(bucket.node.value)
    # 그래프 입력부터 또 막히네. 똑같이 딕셔너리 쓰면 안 되나. 
    # 일단 간선 정보를 어떻게 저장해야할지 모르겠음!!
    E.sort(key=lambda x: x[2])
    parent = [i for i in range(v+1)]
    cost = 0
    for u, v, c in E:
        cost += union(u, v, c)
    print(cost)
```

### 추가: 파이썬 언더바 컨벤션

### 추가: MST 간선 수를 고려한 최적화

보너스 제안

✔ 크루스칼에서 간선 개수 체크

•	MST는 항상 정점 수 - 1개의 간선을 선택합니다.

•	불필요한 반복을 줄이기 위해 아래와 같이 최적화할 수 있어요.

```python
edge_count = 0
for u, v_, c in E:
    if edge_count == v - 1:  # MST 완성
        break
    added = union(u, v_, c)
    if added:
        cost += added
        edge_count += 1
```

# 그래프탐색: DFS와 BFS

## Phase1. 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 16:42:43 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque, defaultdict

def bfs(root: int):
    que = deque()
    is_visited = [False for _ in range(n+1)] # 각 간선의 방문 여부
    que.appendleft(root)
    is_visited[root] = True
    while que:
        v = que.pop()
        print(v, end=' ')
        # 아직 방문하지 않았고 또, 여러개일 수 있으니 리스트로 만들어야 하나?
        for u in sorted(E[v]): # 정점 번호 작은 것 우선 탐색
            if not is_visited[u]:
                que.appendleft(u)
                is_visited[u] = True


def dfs(v: int, is_visited: list):
    # dfs 어떻게 구현하지? 간단하지 뭐
    print(v, end=' ')
    for u in sorted(E[v]):
        if not is_visited[u]:
            is_visited[u] = True
            dfs(u, is_visited)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m, v = tuple(map(int, input().split()))
    E = {
        i:[] for i in range(n + 1)
    }
    # print(E)
    for _ in range(m):
        u, v_ = tuple(map(int, input().split()))
        E[u].append(v_)
        E[v_].append(u)
    # print(E)
    is_visited = [False for _ in range(n+1)] # 각 간선의 방문 여부
    is_visited[v] = True
    dfs(v, is_visited)
    print()
    bfs(v)
    print()
```

## Phase2. 피드백

### 의문: dfs 탐색에서 is visited 테이블을 더 깔끔하게 관리하는 방법은 없을까?

### 답: 그냥 업데이트만 함수로 넘기고 전역으로 쓰는게 안전

좋은 고민이에요! 👀

DFS의 is_visited 테이블 관리를 더 깔끔하게 하려는 시도는 아주 바람직한 습관입니다.

지금 코드도 기능적으로 완벽하게 잘 작동하지만, 가독성, 재사용성, 일관성을 좀 더 높이는 방향으로 개선해볼 수 있어요.

✅ 현재 구조

```plain text
is_visited = [False for _ in range(n+1)]
is_visited[v] = True
dfs(v, is_visited)
```

•	is_visited를 외부에서 만들어서 dfs()에 넘겨줌

•	루트 노드만 방문 처리하고 넘김

✅ 개선 방법 제안

1. dfs() 함수 내부에서 방문 처리까지 책임지게

```plain text
def dfs(v: int, is_visited: list):
    is_visited[v] = True
    print(v, end=' ')
    for u in sorted(E[v]):
        if not is_visited[u]:
            dfs(u, is_visited)
```

→ 호출부는 더 깔끔해짐:

```plain text
is_visited = [False] * (n + 1)
dfs(v, is_visited)
```

2. 방문 테이블을 전역으로 다뤄도 되는 문제라면, 함수 인자로 넘기지 않고 내부에서 선언

이건 깔끔해보이지만, 재귀 호출할 때마다 is_visited가 리셋되므로 ❌

(파이썬의 기본 인자 값으로 넘기면 mutable default argument 문제 생길 수도 있어요.)

그래서 외부에서 만들어서 넘겨주는 방식이 가장 안정적이고 선호됩니다.

3. 클래스형 구조로 바꿔보기 (연습용)

조금 고급 스타일이지만, 상태를 객체에 묶어두는 방식도 있어요:

```plain text
class GraphSearch:
    def __init__(self, E):
        self.E = E
        self.is_visited = []

    def dfs(self, v):
        self.is_visited[v] = True
        print(v, end=' ')
        for u in sorted(self.E[v]):
            if not self.is_visited[u]:
                self.dfs(u)
```

호출 예시:

```plain text
search = GraphSearch(E)
search.is_visited = [False] * (n + 1)
search.dfs(v)
```

🧼 결론 (추천 방식)

> 함수 안에서

```plain text
def dfs(v, is_visited):
    is_visited[v] = True
    print(v, end=' ')
    for u in sorted(E[v]):
        if not is_visited[u]:
            dfs(u, is_visited)

is_visited = [False] * (n + 1)
dfs(v, is_visited)
```

필요하다면 스택을 이용한 반복 DFS 방식도 예시로 보여드릴 수 있어요!

또는 BFS도 유사하게 리팩토링해볼 수도 있고요.

어떤 방식으로 더 연습하고 싶은지 알려줘요 :)

# 그래프 탐색 기본: 연결 요소의 개수

https://www.acmicpc.net/problem/11724

## Phase1. 직접 풀기 - 성공 - union find로 다시 풀어보기!

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11724                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11724                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 17:21:49 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

def bfs(root: int):
    que = deque() # 큐 정의
    que.appendleft(root) # 루트 어펜드
    
    while que: # 큐가 존재하는 동안
        # u = E[que.pop()] # 들어간 노드가 갈 수 있는 노드를 확인
        for u in E[que.pop()]:
            if not is_visited[u]: # 그 노드가 방문되지 않았다면
                is_visited[u] = True # 방문 실시
                que.appendleft(u)

import sys

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    # E = defaultdict() # 간선이 하나밖에 없어도 버텍스의 차수가 여럿일 수 있어서 리스트 필요
    E = {
        i: [] for i in range(1, n+1)
    }
    # print(E)
    # print(arr)
    for u, v in arr:
        # print(u, v)
        E[u].append(v)
        E[v].append(u)
    is_visited = [False for _ in range(n+1)] # V + 1
    cnt = 0
    # print(E)
    for v in range(1, n+1): # 모든 버텍스에 대해 순회
        if not is_visited[v]: # 실행 시점에 방문되지 않았다면
            # print(f'{v} is not traveled') # 방문 실시
            cnt += 1
            is_visited[v] = True #
            bfs(v)
    print(cnt)
        
```

# 트리의 부모 찾기

https://www.acmicpc.net/problem/11725

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

## Phase1. 직접 풀기 - 실패

```python
import sys
# this reminds me the find function

# what was the find?
def find(x):
	if parent[x] != x:
		parent[x] = find(x)
	return parent[x]

from collections import deque

def bfs(root: int):
	que = deque()
	que.appendleft(root)
	visited = [False for _ in range(n+1)]
	while que:
		v = que.pop()
		for u in v:
			if not visited[u]:
				visited[u] = True
				parent[u] = v
				print(f'parent[{u}]={v}')
				print(parent)
				# then what? appendleft to que
				que.appendleft(E[u])
	

if __name__ == '__main__':
	input = sys.stdin.readline
	n = int(input().strip())
	arr = [
			tuple(map(int, input().split()))
			for _ in range(n-1)
		]
	
	E = {
		i:[] for i in range(n+1)
	}
	
	for v, u in arr:
		# 간선 그래프 생성
		E[v].append(u)
		E[u].append(v)
	print(E)
	parent = [i for i in range(n+1)]
	bfs(E[1])
	for p in parent:
		print(p)

```

## Phase2. 피드백

좋아요, 트리의 부모를 찾는 문제를 직접 시도하셨고, BFS를 이용하려는 접근도 좋았습니다. 하지만 bfs 함수에서 약간의 실수가 있어요. 차근차근 피드백을 드릴게요!

✅ 문제 요약

•	루트 없는 트리(무방향 그래프)가 주어지고,

•	루트를 1번 노드로 정했을 때,

•	각 노드의 부모 노드를 출력하는 문제입니다.

❌ 문제점 분석

1. for u in v 잘못된 반복

```plain text
for u in v:
```

이 부분에서 v는 정수형 노드 번호인데, for u in v:는 문자열이나 리스트에서나 가능한 구문이에요. TypeError: 'int' object is not iterable가 발생합니다.

➡️ 수정: E[v]에서 연결된 노드를 가져와야 하므로,

```plain text
for u in E[v]:
```

가 되어야 해요.

2. visited 배열이 함수 내부에 있음

visited 배열이 bfs() 함수 안에 있어서 매번 새로 초기화됩니다. 그래도 이 문제는 한 번만 bfs()를 돌리기 때문에 큰 문제는 없지만, 그래도 보통은 함수 밖에서 선언하고 재사용할 수 있게 관리하는 것이 좋아요.

3. parent 초기값

```plain text
parent = [i for i in range(n+1)]
```

이렇게 되면 루트 노드의 부모가 자기 자신이 됩니다. 일반적으로는 0이나 -1로 초기화하고, 추후 부모를 저장합니다.

✅ 개선된 코드 예시

✅ 핵심 아이디어 정리

•	트리는 사이클이 없는 연결 그래프이므로, 아무 노드에서 시작해도 나머지 노드에 도달 가능.

•	BFS나 DFS로 트리를 순회하면서 parent[자식] = 부모로 저장.

•	출력은 **루트(1번 노드)**를 제외한 노드들의 부모만 출력.

필요하시면 DFS 방식으로도 코드 드릴게요.

또, 아직 이해 안 되거나 헷갈리는 부분이 있다면 편하게 질문 주세요!

# 이분 그래프

https://www.acmicpc.net/problem/1707

그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

## Phase1. 직접 풀기

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 20:24:35 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys

# 평범한 dfs에서 visited에 대한 서치를 시도하면 bipartite graph가 아닌 건가.

def dfs(v: int, cnt: int):
    # dfs 절차. 
    # 1. set v flag
    visited[v] = True
    count_map[v] = cnt
    # 2. loop for each nodes
    for u in E[v]:
        if visited[u] == True: #이걸로는 사이클 확인 불가
            # 왜? 무방향 그래프에서는 온 길도 True로 보게 됨.
            # 그럼 출발하기 전에 없애버리면 안 되나.
            # print(f'already visited {u}')
            # print(f'count map. {count_map[v]} meets {count_map[u]}')
            if (count_map[v] - count_map[u])%2 == 0:
                return False
        else: # not true
            # print(f'exploring {u}, {E[u]}, {v}')
            # 이렇게.
            E[u].remove(v)
            visited[u] = True
            return dfs(u, cnt+1)
    return True



if __name__ == '__main__':	
    input = sys.stdin.readline
    k = int(input().strip()) # number of test cases
    for _ in range(k):
        v, e = tuple(map(int, input().split()))
        E = {
            i: [] for i in range(v+1)
        }
        arr = [
            tuple(map(int, input().split()))
            for _ in range(e)
        ]
        for u, v_ in arr:
            E[v_].append(u)
            E[u].append(v_)
        visited = [False for _ in range(v+1)]
        # print(E)
        count_map = [0 for _ in range(v+1)]
        result = dfs(1, 1)
        out = 'YES' if result else 'NO'
        print(out)
        # print(count_map)
        
"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 그냥 사이클이 없으면 틀린 걸로 판단하는 dfs 함수를 짰는데, 그냥 문제 이해를 
잘못 한 거일수도? 그러네. 어쨌든 사이클 검사하는 함수는 제대로 썼잖아. 한잔해~
그리고 다시 생각해보니, 사이클을 이루는 버텍스 수가 홀수면 안 된다. 
사이클 수를 측정하는 방법은 없나?

Phase2.
확인: count_map이라는 걸 만들어서 서로 사이클을 형성하는 노드의 번호 차가 짝수면 이분 트리 아닌 걸로 시도
시도: 
for u in E[v]:
    if visited[u] == True: #이걸로는 사이클 확인 불가
        # 왜? 무방향 그래프에서는 온 길도 True로 보게 됨.
        # 그럼 출발하기 전에 없애버리면 안 되나.
        # print(f'already visited {u}')
        # print(f'count map. {count_map[v]} meets {count_map[u]}')
        if (count_map[v] - count_map[u])%2 == 0:
            return False
    else: # not true
        # print(f'exploring {u}, {E[u]}, {v}')
        # 이렇게.
        E[u].remove(v)
        visited[u] = True
        return dfs(u, cnt+1)
분석
실패.

"""
```

## Phase2. 피드백

좋은 시도였어요! 이 문제는 이분 그래프(Bipartite Graph) 판별 문제로, DFS나 BFS를 이용해서 정점을 두 그룹으로 나누는 아이디어가 핵심입니다.

현재 코드의 시도는 창의적이지만, 몇 가지 핵심적인 부분에서 로직이 어긋나고 있어요. 자세히 짚어볼게요.

✅ 이분 그래프 판별 핵심 아이디어

•	모든 정점에 대해 두 가지 색(또는 그룹) 중 하나를 칠하되,

•	인접한 정점은 서로 다른 색이 되도록 해야 합니다.

•	DFS 또는 BFS를 하면서 인접 정점에 서로 다른 색을 번갈아 칠하는 방식으로 진행하면 됩니다.

•	만약 인접한 두 정점이 같은 색으로 칠해져 있다면 이분 그래프가 아닙니다.

🔍 현재 코드의 문제점

1.	E[u].remove(v)를 직접 수정 → 그래프 정보를 직접 바꾸는 건 위험한 방식입니다. 사이클 제거 목적이지만, 방향성이 없는 그래프에서 삭제하면 다른 경로 탐색에 지장을 줍니다.

2.	return dfs(...)를 바로 해버림 → 하나의 이웃만 탐색하고 리턴해버려서 전체 탐색이 안 됩니다. for 루프를 끝까지 순회해야 해요.

3.	색 칠하기 방식이 애매 → count_map을 cnt로 하셨는데, 사실 이분 그래프에서는 정확한 depth보다는 현재 노드가 어떤 색인지만 구분하면 됩니다. 예: 0 또는 1

✅ 추천 구조 (DFS 방식)

✅ 핵심 포인트 요약

💡 보너스 (BFS 버전도 궁금하시면 알려드릴게요!)

필요하다면 위 코드에 print()로 디버깅 포인트 찍어보거나, 실패 원인 디테일하게 같이 분석해볼 수도 있어요.

원리만 잘 이해하면 이 유형은 여러 문제에 응용할 수 있어요!

- 아 뭐야 그냥 색칠하면 되잖아.
- 아니 왜 안 되지.
## Phase3. 피드백 후 재도전

서브트리간에 간선이 없는 경우를 생각 못해서 한참 걸림! 앞으로 그래프 문제 풀 때 주의할 것!

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1707                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1707                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 20:24:35 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
3. 수도 코드
4. 코드 구현
"""

import sys
sys.setrecursionlimit(10**8)

def dfs(v: int, color: int):
    global flag
    visited[v] = color
    for u in E[v]:
        if visited[u] != -1:
            if visited[v] == visited[u]: # 0 == 0 or 1 == 1
                flag = True
                return 
        else: 
            visited[u] = color
            dfs(u, 1-color)

if __name__ == '__main__':	
    input = sys.stdin.readline
    k = int(input().strip()) 
    for _ in range(k):
        v, e = tuple(map(int, input().split()))
        E = {
            i: [] for i in range(v+1)
        }
        arr = [
            tuple(map(int, input().split()))
            for _ in range(e)
        ]
        for u, v_ in arr:
            E[v_].append(u)
            E[u].append(v_)
        visited = [-1 for _ in range(v+1)]
        flag = False
        # edge가 없을 수도 있자나!
        for v in E.keys():
            if visited[v] == -1:
                dfs(v, 0)
        out = 'NO' if flag else 'YES'
        print(out)
"""
이슈: 틀렸습니다.

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 그냥 사이클이 없으면 틀린 걸로 판단하는 dfs 함수를 짰는데, 그냥 문제 이해를 
잘못 한 거일수도? 그러네. 어쨌든 사이클 검사하는 함수는 제대로 썼잖아. 한잔해~
그리고 다시 생각해보니, 사이클을 이루는 버텍스 수가 홀수면 안 된다. 
사이클 수를 측정하는 방법은 없나?

Phase2.
확인: color이라는 걸 만들어서 서로 사이클을 형성하는 노드의 번호 차가 짝수면 이분 트리 아닌 걸로 시도
시도: 
for u in E[v]:
    if visited[u] == True: #이걸로는 사이클 확인 불가
        # 왜? 무방향 그래프에서는 온 길도 True로 보게 됨.
        # 그럼 출발하기 전에 없애버리면 안 되나.
        # print(f'already visited {u}')
        # print(f'count map. {color[v]} meets {color[u]}')
        if (color[v] - color[u])%2 == 0:
            return False
    else: # not true
        # print(f'exploring {u}, {E[u]}, {v}')
        # 이렇게.
        E[u].remove(v)
        visited[u] = True
        return dfs(u, cnt+1)
분석
실패.

"""

"""
이슈: 피드백 반영해서, 순회하며 색을 직접 탐색하는 방법으로 처리. 46프로에서 오답 발생

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 뭘 확인해야 함? 46프로에서 틀리는데... 하 진짜 뭐가 문제지. 
시도: 
분석: 
"""
```

# BFS: 미로찾기 

## Phase1. 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2178                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2178                           #+#        #+#      #+#     #
#    Solved: 2025/03/28 18:05:32 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque

def in_range(x: int, y: int):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x: int, y: int):
    if not in_range(x, y) or maze[x][y] == 0 or is_visited[x][y] != -1: 
        return False
    return True

def bfs(root: tuple):
    que = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    que.appendleft(root)
    rx, ry = root
    is_visited[rx][ry] = 1
    cnt = 1
    while que:
        x, y = que.pop() # 큐
        for dx, dy in zip(dxs, dys): # 사방을 본 다음
            nx, ny = x + dx, y + dy

            if can_go(nx, ny): # 갈 수 있으면 출발.
                # print(f'moving to {nx, ny}')
                is_visited[nx][ny] = is_visited[x][y]+1
                que.appendleft((nx, ny))
            # else: 
            #     print(f'can not go to {nx, ny}')
            #     if not in_range(nx, ny): 
            #         print('out of range')
            #     else:
            #         if maze[nx][ny] == 0: 
            #             print('maze no way')
            #         if is_visited[nx][ny]: print('already visited')
                
    return cnt

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    maze = [
        tuple(map(int, tuple(input().strip())))
        for _ in range(n)
        ]
    is_visited = [[-1 for _ in range(m)] for _ in range(n)]
    mark_board = [[0 for _ in range(m)] for _ in range(n)]
    # for m_ in maze:
    #     print(m_)
    c = bfs((0,0))
    # print(c)
    # for v in is_visited:
    #     print(v)
    print(is_visited[n-1][m-1])
```

격자 사이즈를 n, m으로 가정했다가 한참 죽 쒔다. 아래 로그를 모두 찍어본 끝에 in range 함수가 범인임을 발견했다.

# BFS: 특정 거리의 도시 찾기

## Phase1. 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18352                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18352                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 10:34:11 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
1. 문제 읽기
2. 문제 풀기
미로 문제와는 그래프 입력이 다름. 딕셔너리를 사용한 인접리스트를 구현해야 함.
3. 수도 코드
4. 코드 구현
"""

import sys
from collections import deque

def bfs(root: int):
    que = deque()
    que.appendleft(root)
    visited = [-1 for _ in range(n+1)]
    visited[root] = 0
    ans = []
    while que:
        v = que.pop()
        # print(v)
        for u in E[v]:
            # print(f'u: {u}')
            if visited[u] == -1:
                visited[u] = visited[v]+1
                if visited[u] == k:
                    ans.append(u)
                que.appendleft(u)
    return sorted(ans)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m, k, x = tuple(map(int, input().split()))
    E = {
        i: [] for i in range(n+1)
    }
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    for v, u in arr:
        E[v].append(u)
    result = bfs(x)
    if result:
        for r in result:
            print(r)
    else:
        print(-1)
```

# DFS or BFS: 아침 산책



## Phase1. 직접 풀기 - 부분 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21606                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21606                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 21:44:55 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
그냥 모든 버텍를 루트로 dfs 돌리면 되는 거 같은데

3. 수도 코드
4. 코드 구현
"""

import sys

def dfs(root: int):
    global cnt
    v = root
    for u in E[v]:
        if not visited[u] and A[u-1] != 1: # not visited and not inside
            visited[u] = True
            # print(f'moving to {u}')
            dfs(u)
        elif not visited[u] and A[u-1] == 1: # not visited and inside
            # stop the walk
            # print(f'stop at {u}')
            cnt += 1


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    # 버텍스를 딕셔너리로 관리해야 하나?
    A = tuple(map(int, tuple(input().strip()))) # idx - 1로 접근
    arr = [
        tuple(map(int, input().split()))
        for _ in range(n-1)
    ]
    E = {
        i:[] for i in range(n+1)
    }
    for v, u in arr:
        E[v].append(u)
        E[u].append(v)
    # is_inside = {} # V[vertex val] = 0 or 1
    # for idx, a in enumerate(A, 1):
    #     is_inside[idx] = a
    # print(is_inside)
    cnt = 0
    for v in range(1, n+1):
        if A[v-1] == 1: # 출발은 실내에서
            visited = [False for _ in range(n+1)]
            # print(f'starting: {v}')
            visited[v] = True
            dfs(v)
    print(cnt)
```

# DFS: 연산자 끼워넣기

## Phase1. 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14888                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14888                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 11:31:02 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
주어진 숫자 순서대로 노드고 
각 숫자의 순서대로 순회하는 그래프 탐색?

2. 문제 풀기
연산자가 버텍스인가? 버텍스 탐색 순서만 정해지면 연산 때리면 되잖슴. 그러네

3. 수도 코드
4. 코드 구현
""" 

import sys
MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize

def dfs(op_list: list, current_val: int, num_idx: int):
    global max_ans, min_ans
    if len(op_list) == n-1: # 모든 연산을 끝냈다면
        max_ans = max(max_ans, current_val)
        min_ans = min(min_ans, current_val)
        return
    for i in range(len(visited)):
        if visited[i] > 0:
            op_list.append(i)
            visited[i] -= 1
            result = mapper[i]((current_val, A[num_idx]))
            dfs(op_list, result, num_idx+1)
            visited[i]+= 1
            op_list.remove(i)
mapper[0]((1,2)) 

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    A = tuple(map(int, input().split()))
    ops = list(map(int, input().split()))
    mapper = {0: lambda x: x[0]+x[1], 
              1: lambda x: x[0]-x[1], 
              2: lambda x: x[0]*x[1], 
              3: lambda x: x[0]//x[1] if x[0] > 0 else -(-x[0]//x[1])}
    max_ans = MIN_INT
    min_ans = MAX_INT
    for i in range(len(ops)): # 각각의 시작점에 대해
        # 아 알거 같기도 하고 모르겠네. 일단 연산자 쌍을 출력하는 거를 만들어 볼가.
        visited = ops.copy()
        result = 0
        if ops[i] > 0: #연산자를 쓸 수 있다면
            visited[i] -= 1 
            result = mapper[i]((A[0], A[1])) # 최초 연산을 한 다음
            dfs([i], result, 2) # dfs로 넘기기.
    print(max_ans )
    print(min_ans)


## n 최대값이 11이므로 브루트포스 매우 가능함.

```

## Phase2. 피드백

### 고민

어려운 문제는 아니지만 문제 설계가 여러 단계로 나뉘어 시간이 많이 걸렸다. 그리고 람다 표현을 저렇게 해도 괜찮은지, 더 나은 풀이가 없는지 궁금하다.

### 답변

좋은 문제 접근과 멋진 성공이에요! 특히 mapper를 활용해서 연산자를 함수처럼 다루는 방식이 굉장히 깔끔하고 함수형적입니다. 람다 + 딕셔너리 패턴은 파이썬에서 흔히 쓰이는 좋은 습관이기도 해요. 다만 약간의 리팩토링으로 더 간결하고 읽기 쉽게 만들 수 있어요.

✅ 코드 스타일 피드백 및 개선 제안

1. op_list는 없어도 됩니다!

•	op_list는 DFS에서 탐색 경로를 기록하기 위해 만든 것 같지만, 연산만 하고 그 결과만 넘기면 되기 때문에 없어도 무방합니다.

•	대신 visited 상태만 잘 관리하면 됩니다.

2. 시작점 루프는 필요 없습니다

•	모든 연산자 조합을 DFS로 탐색하므로, 시작 연산자를 고를 필요 없이 한 번만 DFS를 호출하면 됩니다.

✨ 리팩토링 예시 코드

```python
import sys
input = sys.stdin.readline

# 나눗셈 연산 함수 정의 (음수 처리 포함)
def divide(a, b):
    if a < 0:
        return -(-a // b)
    return a // b

def dfs(idx, result):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                dfs(idx + 1, result + A[idx])
            elif i == 1:
                dfs(idx + 1, result - A[idx])
            elif i == 2:
                dfs(idx + 1, result * A[idx])
            else:
                dfs(idx + 1, divide(result, A[idx]))
            ops[i] += 1  # 백트래킹

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    ops = list(map(int, input().split()))  # +, -, *, //

    max_ans = -sys.maxsize
    min_ans = sys.maxsize

    dfs(1, A[0])  # 첫 숫자는 그대로 시작

    print(max_ans)
    print(min_ans)
```

📌 성능 분석

•	최대 10개의 연산자 → 10! = 3,628,800

•	파이썬에서 충분히 돌아갑니다.

•	DFS+백트래킹으로 완전 탐색을 하되, 필요 이상 반복은 줄인 구조입니다.

💡 추가적으로 생각해볼 점

•	itertools.permutations로도 연산자 순열을 만들어서 계산할 수 있지만, 중복 연산자 존재 시 같은 연산 순열이 중복될 수 있어 DFS가 더 효율적입니다.

•	코드 구조만 살짝 정리하면 대회 때도 매우 신속하게 풀 수 있어요.

✅ 결론

필요하다면 itertools 기반 풀이 예시도 드릴게요. 계속해서 이렇게 멋지게 풀어가시는 거 보기 좋아요!

### 리팩토링

```python

import sys
MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize

def dfs(current_val: int, num_idx: int):
    global max_ans, min_ans
    if num_idx == n: # 모든 연산을 끝냈다면
        max_ans = max(max_ans, current_val)
        min_ans = min(min_ans, current_val)
        return
    for i in range(len(visited)):
        if visited[i] > 0:
            visited[i] -= 1
            result = mapper[i]((current_val, A[num_idx]))
            dfs(result, num_idx+1)
            visited[i]+= 1

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    A = tuple(map(int, input().split()))
    visited = list(map(int, input().split()))
    mapper = {0: lambda x: x[0]+x[1], 
              1: lambda x: x[0]-x[1], 
              2: lambda x: x[0]*x[1], 
              3: lambda x: x[0]//x[1] if x[0] > 0 else -(-x[0]//x[1])}
    max_ans = MIN_INT
    min_ans = MAX_INT
    dfs(A[0], 1) # dfs로 넘기기.
    print(max_ans)
    print(min_ans)


```

# DFS: 빙산

## Phase1. 직접 풀기 - 31프로 실패

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2573                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2573                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 14:04:01 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

"""
1. 문제 읽기
2. 문제 풀기
일단 빙산 녹이기 먼저 해야 함.
이 작업을 완전 탐색 말고 방법 없지? ㅇㅇ 그리고 300 이하라서 최대 30000 칸에 대해서만 보면 됨
녹이기 연산은 거기서 더 줄어들고.
그리고 탐색 연산으로 몇 덩어리인지 판단
이걸 시뮬레이션 함수로 반복
3. 수도 코드
4. 코드 구현
"""

import sys


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def a_year_later(): # 2 * n^m
    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0:
                get_melt_val(i, j) # n^m * 4
    for i in range(n): # n^m
        for j in range(m):
            icebergs[i][j] -= tmp_map[i][j] if icebergs[i][j] >= tmp_map[i][j] else icebergs[i][j]

def get_melt_val(x: int, y: int): # 4
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and icebergs[nx][ny] == 0:
            tmp += 1
    tmp_map[x][y] = tmp

from collections import deque

def bfs(x, y):
    que = deque()
    que.appendleft((x, y))
    
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and icebergs[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.appendleft((nx, ny))    


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))  # n, m 차이에 주의!!!
    icebergs = [list(map(int, input().split())) for _ in range(n)]
    year = 0
    flag = True
    while flag:
        year += 1
        tmp_map = [[0 for _ in range(m)] for _ in range(n)]
        a_year_later()
        # 시작지점은 완탐으로 구해야할듯?
        visited = [[False if icebergs[i][j] > 0 else True for j in range(m)] for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    cnt += 1
                    if cnt >= 2:
                        flag = False
                    bfs(i, j)

    print(year)
```

## Phase2.  피드백

분리되는 시점(2덩어리 이상)만 체크하고, 모두 녹았을 때(빙산이 하나도 남지 않았을 때) 조건을 빠뜨린 것이 주된 원인으로 보입니다.

BOJ 2573(빙산) 문제에서는

1.	“빙산이 전부 녹아 없어질 때까지 분리되지 않으면 0을 출력”

2.	“2덩어리 이상으로 분리되는 해의 시간을 출력”

이 두 가지를 모두 만족해야 합니다.

그런데 제공해주신 코드에서는 “빙산이 하나도 안 남은 상황”에 대한 처리를 별도로 하지 않으므로, 이미 전부 녹아버렸는데도 계속 반복문이 돌아가거나, 원하는 시점에 종료되지 않아서 오답/오류가 발생할 수 있습니다.

수정 포인트

```python
...
while True:
    year += 1
    a_year_later()

    # 빙산 덩어리 수 확인
    visited = [[False if icebergs[i][j] > 0 else True for j in range(m)] for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j)
                if cnt >= 2:
                    print(year)
                    sys.exit(0)

    # 빙산이 하나도 안 남았으면 -> 0 출력 후 종료
    if cnt == 0:
        print(0)
        sys.exit(0)
```

1.	a_year_later()에서 빙산을 녹인 후

2.	BFS로 연결된 빙산 덩어리 개수(cnt)를 계산합니다.

3.	덩어리 수(cnt)가 2 이상이면 곧바로 정답(year)을 출력하고 종료합니다.

4.	덩어리가 0개라면 빙산이 전부 녹은 것이므로 0을 출력하고 종료합니다.

5.	덩어리가 1개라면 다음 해 시뮬레이션을 계속 진행합니다.

이 로직을 만족해주면, **‘분리되었을 때’와 ‘모두 녹았을 때’**를 모두 제대로 체크하여 문제를 해결할 수 있습니다.

추가 개선/주의 사항

1.	성능

•	입력 크기가 최대 300×300이므로, 현재와 같은 단순 BFS+시뮬레이션(매년 빙산 전체 완탐 후 녹이기) 방식도 크게 문제되지 않습니다.

•	다만 매 해 마다 in_range를 여러 번 호출하므로, 자주 쓰는 연산은 상수화하거나 배열 범위를 미리 체크하는 구조로 바꿔도 좋습니다.

2.	코드 가독성

•	tmp_map을 만든 뒤 녹이는 과정은 a_year_later() 함수에서 정리되어 있어 비교적 깔끔합니다.

•	get_melt_val()도 제자리에서 계산만 하고, 실제 빙산 감소는 연산 끝나고 일괄 적용하는 방식이라 오류가 날 위험이 적습니다.

3.	출력 시점

•	while flag: 구조보다 while True: 문 안에서 ‘조건을 만족하면 break 또는 sys.exit()’로 처리하는 것이 조금 더 직관적인 편입니다.

•	혹은 flag를 쓰되, 매 해 분리 개수를 조사하고 if cnt >= 2: break, if cnt == 0: break 같은 식으로 탈출 조건을 설정한 뒤 탈출 직후 어떤 값을 찍을지 결정하는 식도 가능합니다.

결국 가장 중요한 점은 “빙산이 모두 녹았을 때(cnt == 0)가 되면 0을 출력하고 종료한다”는 체크를 반드시 넣는 것이므로, 이 부분만 반영해주시면 31%에서 틀리는 문제는 해결될 것입니다.

# DFS: 구슬 찾기

## Phase1. 직접 풀기 - 성공(40분)

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2617                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2617                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 15:14:50 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기

4 > 2 > 1
  > 3
5 > 1
4번은 안 된다. 왜? 자기보다 가벼운 구슬이 3개 있으므로((n+1)//2)개 이상 있으므로
1번도 안 된다. 자기보다 무거운게 2, 4, 5로 똑같이 3개 이상 있음.

2 1
4 3
5 1
4 2

각 구슬에 dfs한 다음 depth > ((n+1)//2)이상이 되면 false 하면 되겠네

3. 수도 코드
4. 코드 구현
"""

import sys

def dfs_lighter(v: int):
    global l
    visited[v] = True
    for u in lighter[v]:
        if not visited[u]:
            # print(f'lighter: {v} -> {u}')
            l += 1
            dfs_lighter(u)

def dfs_heavier(v: int):
    global h
    visited[v] = True
    for u in heavier[v]:
        if not visited[u]:
            # print(f'heavier: {v} -> {u}')
            h += 1
            dfs_heavier(u)

if __name__ == '__main__':	
    input = sys.stdin.readline
    n, m = tuple(map(int, input().split()))
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]

    lighter = {
        i: [] for i in range(n+1)
    }
    heavier = {
        i: [] for i in range(n+1)
    }
    for v, u in arr:
        lighter[v].append(u)
        heavier[u].append(v)
    cnt = 0
    for v in range(1, n+1):
        visited = [False for _ in range(n+1)]
        l, h = 0, 0
        dfs_lighter(v)
        dfs_heavier(v)
        # print(f'l: {l}, h: {h}')
        if l >= (n+1)//2 or h >= (n+1)//2:
            cnt += 1
    print(cnt)

"""
이슈: depth 만 체크하면 서로 이어지지 않은 버텍스를 탐지할 수 없음. 
그렇다고 heavier, lighter를 각각 해서 하나의 dfs에서 처리하면 당연히 꼬임.
그럼? dfs함수 두개 만들면 안 되나?

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 함수 따로 분리
분석: 성공
"""
```



# 그래프: 트리의 부모 찾기

https://www.acmicpc.net/problem/11725

## Phase1. 직접 풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11725                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11725                          #+#        #+#      #+#     #
#    Solved: 2025/03/29 17:36:04 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque
def bfs(v: int):
    que = deque()
    que.appendleft(v)
    visited[v] = True
    while que:
        v = que.pop()
        for u in E[v]:
            if not visited[u]:
                visited[u] = True
                que.appendleft(u)
                parent[u] = v
                
if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        list(map(int, input().split()))
        for _ in range(n-1)
    ]
    visited = [False for _ in range(n+1)]
    E = {
        i: [] for i in range(n+1)
    }
    for v, u in arr:
        E[v].append(u)
        E[u].append(v)
    parent = [i for i in range(n+1)]
    bfs(1)
    for p in parent[2:]:
        print(p)
```

## Phase2. 피드백

### 의문

union find로 풀 수 있다는 소문을 듣고 고민해봤는데 도저히 안 됐다. 그래서 그냥 bfs로 풀었다. union find는 안 되는게 맞나?

### 답변

좋은 질문이에요!

11725번: 트리의 부모 찾기 문제를 BFS로 정확히 풀어내셨고, 코드도 매우 깔끔합니다. 🎯

이제 의문 주신 **“유니온 파인드(Union-Find)로는 풀 수 없는가?”**에 대한 답변을 드릴게요.

✅ 결론부터 말하자면:

> 유니온 파인드는 이 문제를 직접적으로 푸는 데 적합하지 않습니다.

🔍 이유: 유니온 파인드는 “집합의 소속 여부” 확인이 목적

Union-Find (Disjoint Set Union, DSU)는 다음과 같은 상황에 최적화된 알고리즘이에요:

•	여러 개의 서로소 집합(disjoint set) 관리

•	두 원소가 같은 집합에 속해 있는지를 빠르게 판단

•	두 집합을 합치는 연산(union)

즉, 대표적인 용도는:

📌 반면, 이 문제는?

•	트리의 구조 자체는 이미 주어져 있음

•	우리는 트리의 부모 관계를 알아내는 것이 목표예요

•	즉, 노드 간 탐색을 통해서 관계를 만들어야 하며,

•	유니온 파인드처럼 “한 번에 소속을 판별하는 방식” 으로는 부모 노드를 알아낼 수 없습니다

> 유니온 파인드는 “너랑 나랑 같은 그룹인가?“에는 강하지만,

> “너의 부모는 누구인가?“에는

🆚 비교 요약

✅ 결론

BFS/DFS 방식으로 푸신 게 정석이자 최선의 방법이에요.

유니온 파인드가 사용되는 대표 문제로는:

•	싸이클 찾기 문제

•	도시 분할 계획 (MST)

•	여행 가자 (집합 연결성)

등이 있습니다. 참고하시면 좋아요!

궁금하시면 “트리의 루트를 유니온 파인드로 간접적으로 유도할 수 있는 예외 상황” 도 설명해드릴 수 있어요.

하지만 이 문제 자체는 BFS/DFS가 유일하게 직관적이고 정확한 풀이입니다.

다음에도 좋은 질문 기대할게요 :)

# 토마토

## Phase1. 직접 풀기 - 1시간 반 초과 

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 19:08:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
익은 토마토만 루트가 될 수 있음.
익었는데 방문된 토마토는 어떻게 표현? 3?
-1: 토마토 없음(탐색 불가)
0: 익지 않은 토마토(탐색 가능, 모든 익지 않은 토마토는 방문하지 않은 토마토다.)
1: 익은 토마토(탐색은 가능, 모든 익은 토마토는 방문하지 않은 토마토가 아니다. )
2: 익은 방문한 토마토(탐색 가능)

3. 수도 코드
4. 코드 구현
"""
# 동, 서, 남, 북, 상, 하
dxs = [0, 0, 1, -1, 0, 0]
dys = [1, -1, 0, 0, 0, 0]
dzs = [0, 0, 0, 0, 1, -1]

EMPTY = -1
UNRIPE = 0
RIPEN_NOT_VISITED = 1
RIPEN_VISITED = 2

def in_range(x, y, z):
    return x >= 0 and x < h and y >= 0 and y < n and z >= 0 and z < m

import sys
from collections import deque

def bfs(root: list): # only ripen tomato!
    has_ripen = False
    que = deque()

    que.appendleft(root)
    # print(f'root: {root}')
    x, y, z = root
    tomato[x][y][z] = RIPEN_VISITED
    
    cnt = 0
    while que:
        x, y, z = que.pop()
        # print(f'discovering {x, y, z}')
        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = x + dx, y + dy, z + dz
            if in_range(nx, ny, nz):
                if tomato[nx][ny][nz] == UNRIPE:
                    # print(f'tomato {nx, ny, nz} not ripped')
                    has_ripen = True
                    tomato[nx][ny][nz] = RIPEN_NOT_VISITED
                    que.appendleft((nx, ny, nz))
                elif tomato[nx][ny][nz] == RIPEN_NOT_VISITED:
                    tomato[nx][ny][nz] = RIPEN_VISITED
                    que.appendleft((nx, ny, nz))

        print(f'result on {cnt} ==========')
        print_tomato(tomato)
        cnt += 1
    return has_ripen

def print_tomato(tomato):
    for i, level in enumerate(tomato):
        print(f'level {i}')
        for row in level:
            print(row)

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, h = tuple(map(int, input().split()))
    tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    print_tomato(tomato)
    # while True:
    # 완전 탐색으로 루트 찾기
    ### 여기부터가 1일
    day = 0
    while True:
        day_flag = False
        # gather roots
        roots = []
        for x in range(h):
            for y in range(n):
                for z in range(m):
                    # print(f'x:{x}, y:{y}, z:{z}')
                    if tomato[x][y][z] == RIPEN_NOT_VISITED:
                        roots.append((x, y, z))
        for root in roots:
            bfs(root)
        #만약 1일의 탐색이 끝났는데 has_ripen == False라면 이제 그만~ ^0^
        print(f'day {day}')
        print_tomato(tomato)
        if not day_flag: 
            break
        day += 1

    print('result')
    print_tomato(tomato)
    print(day)
```

## Phase2. 디버깅 후 성공

테스트케이스 사이트에서 찾아서 일일이 돌려가며 생각보다 금방 디버깅 할 수 있었음(실제로는 이 방법을 지양할 필요가 있지만…)

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7569                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7569                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 19:08:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
익은 토마토만 루트가 될 수 있음.
익었는데 방문된 토마토는 어떻게 표현? 3?
-1: 토마토 없음(탐색 불가)
0: 익지 않은 토마토(탐색 가능, 모든 익지 않은 토마토는 방문하지 않은 토마토다.)
1: 익은 토마토(탐색은 가능, 모든 익은 토마토는 방문하지 않은 토마토가 아니다. )
2: 익은 방문한 토마토(탐색 가능)

3. 수도 코드
4. 코드 구현
"""
# 동, 서, 남, 북, 상, 하
dxs = [0, 0, 1, -1, 0, 0]
dys = [1, -1, 0, 0, 0, 0]
dzs = [0, 0, 0, 0, 1, -1]

EMPTY = -1
UNRIPE = 0
RIPEN_NOT_VISITED = 1
RIPEN_VISITED = 2

def in_range(x, y, z):
    return x >= 0 and x < h and y >= 0 and y < n and z >= 0 and z < m

import sys
from collections import deque

def bfs(roots: list): # only ripen tomato!
    global day
    que = deque(roots)
    # print(f'root: {root}')
    
    while que:
        is_over = True
        for _ in range(len(que)):
            x, y, z = que.pop()
            # p1: tomato[0][0][1]
            # p2: tomato[0][1][0]
            tomato[x][y][z] = RIPEN_VISITED
            # print(f'discovering {x, y, z}')
            for dx, dy, dz in zip(dxs, dys, dzs):
                nx, ny, nz = x + dx, y + dy, z + dz
                if in_range(nx, ny, nz):
                    if tomato[nx][ny][nz] == UNRIPE:
                        # print(f'tomato {nx, ny, nz} not ripped')
                        tomato[nx][ny][nz] = RIPEN_VISITED
                        que.appendleft((nx, ny, nz))
                        is_over = False
                    elif tomato[nx][ny][nz] == RIPEN_NOT_VISITED:
                        tomato[nx][ny][nz] = RIPEN_VISITED
                        que.appendleft((nx, ny, nz))
                        is_over = False
        # print(f'result on {cnt} ==========')
        if not is_over:
            day += 1
            # print(f'day update--------day {day}')
            # print_tomato(tomato)
        else:
            # print(f'day over on --- day {day}')
            return

def print_tomato(tomato):
    for i, level in enumerate(tomato):
        print(f'level {i}')
        for row in level:
            print(row)

if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, h = tuple(map(int, input().split()))
    tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    # print_tomato(tomato)
    day = 0
    all_ripen = True
    while True:
        day_flag = False
        # gather roots
        roots = []
        for x in range(h):
            for y in range(n):
                for z in range(m):
                    if tomato[x][y][z] == RIPEN_NOT_VISITED:
                        roots.append((x, y, z))
                    if tomato[x][y][z] == UNRIPE:
                        all_ripen = False
        # roots = [아무튼 하나만 1이어야 함]
        if all_ripen: 
            print(0)
            sys.exit(0)
        else:
            bfs(roots)
            for x in range(h):
                for y in range(n):
                    for z in range(m):
                        if tomato[x][y][z] == UNRIPE:
                            print(-1)
                            sys.exit(0)
            # print(f'day {day}')
            # print_tomato(tomato)
            if not day_flag: 
                break


    # print('result')
    # print_tomato(tomato)
    print(day)
```

# 그래프: 탈출

https://www.acmicpc.net/problem/3055

## Phase1. 직접 풀기 - 시간 초과



```python
import sys
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and  x < r and y >= 0 and y < c

def bfs(water_roots: list, start: list):
    que = deque(water_roots)
    visited = [[False for _ in range(c)] for _ in range(r)]
    s_que = deque([start])
    visited2 = [[False for _ in range(c)] for _ in range(r)]
    # print(que)
    cnt = 1
    while que:
        for _ in range(len(que)):
            x, y = que.pop()
            visited[x][y] = True
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and not visited[nx][ny] and \
                    forest[nx][ny] not in ('X', 'D'):
                    que.appendleft([nx, ny])
                    forest[nx][ny] = '*'
        # 이 루프가 끝나면 하루의 물 이동이 끝난것. 이제 고슴도치를 이동 
        for _ in range(len(s_que)):
            x, y = s_que.pop()
            visited2[x][y] = True
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and not visited2[nx][ny] and \
                forest[nx][ny] not in ('X', '*'):
                    if forest[nx][ny] == 'D':
                        # print('escaped!')
                        return (True, cnt)
                    s_que.appendleft([nx, ny])
                    forest[nx][ny] = 'S'
        cnt += 1
        # print(f'cnt = {cnt}')
        # for f in forest:
            # print(f)
        # print()
    return (False, None)
                    


if __name__ == '__main__':	
    input = sys.stdin.readline
    r, c = tuple(map(int, input().split()))
    forest = [
        list(input().strip())
        for _ in range(r)
    ]
    # for f in forest:
        # print(f)
    water_roots = []
    start = None
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                water_roots.append((i, j))
            if forest[i][j] == 'S':
                start = (i, j)
    # print(f'waters: {water_roots} \nstart: {start}')
    is_escaped, days = bfs(water_roots, start)
    # print(f'result: {result}')
    if not is_escaped:
        print('KAKTUS')
    else:
        print(days)
```

## Phase2. 피드백

현재 코드에서도 ‘물 이동 후 고슴도치 이동’이라는 문제 조건 자체는 일단 충족하긴 합니다. 다만, 각 반복에서 for _ in range(len(que)): 형태로 모든 물/고슴도치 칸을 순회하고 매번 forest 배열을 수정하면서 visited 여부도 따로 따져야 하므로, 구현이 다소 복잡해지고 비효율이 발생할 여지가 있습니다.

일반적으로 ‘탈출(3055)’ 문제에서는 다음과 같은 방식의 이중 BFS(정확히는 ‘물 확산 시간을 미리 구해두고, 그 정보를 바탕으로 고슴도치 BFS를 실행’) 접근이 좀 더 간결하고 효율적입니다.

핵심 아이디어 요약

1.	물의 도달 시간을 먼저 구한다.

•	모든 물( '*' ) 위치를 큐에 넣고, 멀티 소스 BFS를 수행하여 각 칸에 물이 몇 초(또는 몇 일) 후에 도달하는지를 계산합니다.

•	물이 도달할 수 없는 칸은 INF(혹은 -1, 또는 매우 큰 수)로 남겨둡니다.

2.	고슴도치 이동 BFS를 수행한다.

•	고슴도치는 다음 위치로 이동할 때, “해당 칸의 물 도달 시간 > 고슴도치가 그 칸에 도착하는 시간” 이어야만 이동할 수 있습니다.

•	즉, 이미 물이 찼거나, 도착과 동시에 물이 차는 칸은 갈 수 없게 됩니다.

이 방식을 따르면, 매 시점마다 물을 퍼뜨리고 고슴도치를 퍼뜨리는 과정을 일일이 뒤섞어 구현하지 않아도 되므로, 시간 복잡도와 구현 면에서 더 간결해집니다.

예시 코드 (파이썬)

주요 로직 설명

1.	물 확산 BFS

•	water_time[x][y]를 (x, y)에 물이 도착하는 시간으로 정의합니다.

•	초기에 물('*') 위치는 water_time을 0으로 잡고 큐에 넣습니다(멀티 소스).

•	BFS로 퍼져나가며, X(바위)나 D(비버 굴)에는 물이 도달하지 않도록 조건을 걸어 둡니다.

2.	고슴도치 BFS

•	고슴도치가 (x, y)에 도달한 시간이 dist[x][y]라 할 때,

•	다음 칸 (nx, ny)에 도달하는 시간은 dist[x][y] + 1입니다.

•	이때, water_time[nx][ny] > dist[x][y] + 1 이어야만 갈 수 있습니다. (고슴도치 도착 시점보다 물 도착 시간이 늦어야 이동 가능)

•	비버 굴 D에 도착하면 dist[x][y]를 곧바로 정답으로 출력합니다.

시간복잡도

•	물 BFS: 최대 R*C칸을 한 번씩 방문하므로 O(R*C).

•	고슴도치 BFS: 마찬가지로 최대 R*C칸을 한 번씩 방문하므로 O(R*C).

•	전체적으로 O(R*C)에 수렴하여, R, C가 최대 50일 때 충분히 빠르게 동작합니다.

정리

•	물과 고슴도치를 한 큐에서 번갈아가며 처리(‘하루에 물 움직이고 → 고슴도치 움직이고…’) 하는 방법도 물론 가능하지만, 구현이 복잡해지기 쉽습니다.

•	물 도착 시간을 먼저 전부 구해놓고, 그 정보를 이용해 고슴도치 이동 BFS를 수행하는 방식이 구현상 훨씬 깔끔하고, 시간 초과도 방지하기 쉽습니다.

•	특히, Python에서 deque.pop과 appendleft를 섞어 쓰면 직관적인 선입선출(FIFO) 흐름이 깨져 헷갈릴 수 있으므로, 일반적인 BFS에서는 popleft/append 쌍을 쓰는 편이 안전합니다.

이 방식대로 작성하면 시간 초과 없이, 보다 깔끔하게 문제를 해결하실 수 있을 것입니다.

## Phase3. 2차 재도전 - 30분 - 실패

```python
import sys
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    global water_time
    # water_time init
    queue = deque()
    for r, c in water_source:
        water_time[r][c] = 0
        queue.append((r, c))
    water_time[dest[0]][dest[1]] = float('inf')
    # -1을 not visited 플래그로 쓰면 됨
    cnt = 0
    
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and water_time[nx][ny] == -1:
                    if forest[nx][ny] == 'X':
                        water_time[nx][ny] = -2 # -2라서 비버도 절대 못 감
                    elif forest[nx][ny] == 'D': # 목적지는
                        water_time[nx][ny] = float('inf')
                    else: 
                        water_time[nx][ny] = cnt
                        queue.append((nx, ny))

def in_range(x, y):
    return x >= 0 and x < r and y >= 0 and y < c
        
def bfs_hodge(s: tuple):
    queue = deque([s])
    # 따로 관리해야 하나? water맵을 쓰면 안 되나? 
    # 물 도착 숫자가 변경되면 곤란한다.
    # visited 대신 -1로 바꾸고 그게 아니면 갈 수 있는 식으로 해야할듯? 인덱스를 충돌 안
    # 나게 잘 설정하는 훈련도 필요하긴 하지. (끄덕)
    # 물이 안 가면 업데이트가 안 되는 문제도 있다
    # 끝이 없네 이걸 혼자서 어떻게 풀지? '진짜 못 가는 경우'와 '초기 값'이 구분돼야 한다.
    # 물이 진짜 못 가는 경우 = 목적지거나 돌인 경우: inf
    # 그런데 비버는 목적지는 갈 수 있고 돌은 못 간다.
    # inf값을 만날 때마다 판단? 아니면 
    # 그냥 돌은 -2로 watermap에 업데이트
    # -1은 물이 도달 못한 경우로 정의
    # 물이 사용하는 초기값: -1
    # 비버는 -2를 절대 못 가는 걸로.
    # 비버는 
    water_time[s[0]][s[1]] = -2
    cnt  = 0 
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) \
                and (water_time[nx][ny] > cnt\
                or water_time[nx][ny] == -1): # 물이 도달하는 시간이 느리거나 (돌은 -2라서 배재됨. -1이라서 안 오거나)
                    if (nx, ny) == dest:
                        print(cnt)
                        return
                    queue.append((nx, ny))
                    water_time[nx][ny] = -2
        # for wt in water_time:
        #     print(wt)
    print('KAKTUS')
    return

if __name__ == '__main__':	
    input = sys.stdin.readline
    r, c = tuple(map(int, input().split()))
    forest = [
        list(input().strip())
        for _ in range(r)
    ]

    water_time = [[-1 for _ in range(c)]for _ in range(r)]
    water_source = []
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                water_source.append((i, j))
            if forest[i][j] == 'D':
                dest = (i, j)
            if forest[i][j] == 'S':
                start = (i, j)
    bfs()
    # for wt in water_time:
    #     print(wt)
    bfs_hodge(start)

# 고슴도치가 움직일 수 있는 방법. 고슴도치 데이가 있고, 
# 그 값보다 이동하려는 water_time 값이 커야 이동 가능.
# -1은 그럼 나쁜 비교가 되는데? 무한으로 바꿔서 항상 이동 가능하게 해야함
# [-1, 3, 2, 1, 0, 1]
# [7, -1, 3, -1, 1, 2]
# [6, 5, 4, 3, 2, 3]
```

## Phase4. 2차 피드백 (정답 제외)

아래는 주어진 코드를 간단히 살펴보고, 전형적으로 “고슴도치 문제(물의 확산과 고슴도치의 이동을 각각 BFS로 처리)”를 풀 때 자주 혼동하는 포인트 위주로 로직상의 피드백을 정리한 것입니다. (실행 결과나 정답 여부 자체는 언급하지 않습니다.)

1. water_time 배열의 의미 명확화

현재 코드에서 water_time 배열은

•	물이 도달하는 시간을 기록 (0, 1, 2, …)

•	혹은 절대 물이 도달하지 못하거나(돌, 비버 굴) 특별한 값(-2 또는 inf)으로 처리

•	아직 물이 도달하지 않은 칸은 -1로 처리

처럼 다양한 값을 섞어서 쓰고 있습니다.

이런 식의 “한 배열에 여러 가지 의미”를 담는 방법 자체는 가능하지만, 값 의미가 모호해지면 디버깅할 때 헷갈리기 쉽습니다. 예를 들어 돌(X)을 -2로, 굴(D)을 inf로, 이미 방문한 칸을 다시 -2로 바꾸는 과정에서 “정말 의도대로 데이터가 세팅된 것인지” 계속 주의해야 합니다.

> 개선 아이디어

> •

> •	돌(X)이나 비버 굴(D)은 별도의 그래프/맵에서 따로 확인(또는 None, 특수한 marker로)하는 방식을 쓰면 한결 명확해집니다.

> •	혹은 현재처럼 한 배열에 모두 담되, -2 등의 “특수값”을 세분화해야 한다면, 그에 맞는

2. 물 확산 BFS와 고슴도치 BFS의 시간 관계

일반적으로 “고슴도치 문제”는 다음과 같은 로직으로 풀립니다.

1.	물 먼저 BFS로 확산 시간을 water_time에 저장.

•	물이 도달할 수 없는 칸이면 water_time[r][c] = float('inf').

2.	고슴도치 BFS

•	고슴도치가 시간 t에 칸 (x, y)에 도달했다고 가정할 때,

•	다음 칸 (nx, ny)로 이동 가능하려면 “고슴도치가 t+1에 이동한 시점 < 물이 도달하는 시점” 이어야 합니다. 즉,

t + 1 < water\_time[nx][ny]

•	이를 만족해야 고슴도치가 물에 안 잠기고 살아서 이동 가능해집니다.

하지만 현재 코드를 보면, 고슴도치 쪽에서

```plain text
if in_range(nx, ny) and (water_time[nx][ny] > cnt or water_time[nx][ny] == -1):
    ...
```

이런 식으로 조건을 주고 있습니다.

•	cnt는 고슴도치 BFS에서의 “단계 수”

•	water_time[nx][ny] > cnt이면 고슴도치가 cnt 시점에 갈 수 있다고 판단

이 로직 자체는 얼핏 보면 맞을 수도 있지만, 보통은 t+1 < water_time[nx][ny] 형태로 비교해야 정확합니다.

예를 들어,

•	고슴도치가 시간 t=2에 (x, y)에 있고, 다음 스텝에 (nx, ny)로 가려 합니다.

•	물이 (nx, ny)에 t=3에 도착한다면, 고슴도치는 t=3에 그 칸에 들어가게 되는데, 이때 “동시에 도착해서 안전한지 / 물에 잠기는지” 문제를 어떻게 처리하고 있는지가 중요합니다.

결국, 문제 설명에 따라

•	“물이 t=3에 도착한다면, 고슴도치는 t=3에 들어가면 잠긴다”고 보는 경우엔 t+1 < water_time[nx][ny] 라는 strict 비교가 필요합니다.

•	“동시에 도착하면 괜찮다”고 보는 경우라면 t+1 <= water_time[nx][ny] 식도 가능할 수 있습니다.

이는 문제의 조건(“물과 동시에 도착 시 살아남느냐?”)에 따라 달라지므로, 문제 원문 예시나 공식 해설을 꼭 확인하여, 정확한 부등호 처리를 해야 합니다.

3. -2로의 갱신 타이밍

코드에서

```plain text
water_time[nx][ny] = -2
...
water_time[s[0]][s[1]] = -2
```

등으로 갱신하고 있습니다.

•	고슴도치 BFS에서 (nx, ny)로 이동 시에 water_time[nx][ny] = -2로 갱신

•	돌(X)도 -2, 이미 방문한 칸도 -2

등 여러 곳에서 -2가 쓰이는데, 나중에 이 칸을 다시 방문하려고 할 때 조건문에서 -2가 의미하는 게 무엇인지 즉각 알아보기 어려울 수 있습니다.

> 개선 아이디어

> •	고슴도치가 방문했다면 “visited_hedge[x][y] = True” 처리를 별도의 2차원 배열로 두는 것이 일반적입니다.

> •	돌(X)을 굳이 water_time에 -2로 넣는 대신, 물 BFS 로직에서 아예 if forest[nx][ny] == 'X': continue로 패스만 하면 됩니다.

> •	“비버 굴(D)”이나 “경계 밖”도 마찬가지로 물이 확산될 수 없는 대상이므로 “그냥 확산 로직에서 걸러내고” water_time에는 기록하지 않습니다(혹은 inf로 기록).

이렇게 “물 확산”과 “고슴도치 이동”에서 각자 필요한 visited/queue/조건을 분리하면 훨씬 단순해집니다.

4. BFS 레벨(cnt) 증가 방식

현재 bfs()에서

```plain text
while queue:
    cnt += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        ...
```

이런 구조를 쓰고 있습니다. 전형적인 “한 번의 while 루프 = 1초(또는 1단계) 경과” 패턴입니다.

이 로직 자체는 문제 없습니다만, 다음 사항을 주의해야 합니다.

1.	cnt를 0에서 시작하여, 첫 레벨에서 cnt=1이 되는 구조.

•	그렇다면 “물은 시작 지점에서 0초 시점에 있다가, 1초 후에 인접 칸으로 이동”이라는 의미가 됩니다.

•	혹은 “시작점을 0레벨, 인접 칸을 1레벨” 식으로도 볼 수 있으므로, 문제 의도와만 일치하면 괜찮습니다.

2.	이후 고슴도치 BFS에서도 같은 방식을 쓰되, “고슴도치가 t에 있는 칸에서 t+1에 인접 칸으로 이동” 식으로 맞춰줘야, 서로 시간이 정확히 비교 가능합니다.

만약 물 BFS에서 1단계 경과 시점을 cnt=1로 간주했다면, 고슴도치 BFS에서도 동일한 기준을 써줘야 합니다.

Tip: 보통은

•	시작점(물 혹은 고슴도치)의 time = 0 (queue에 넣을 때)

•	while 한 바퀴 돌 때마다 “해당 레벨의 노드들 전부 처리 → time + 1”

이런 식으로 맞춥니다.

5. 요약

•	배열 값들의 의미를 지나치게 “특수값” 여러 개로 혼합하기보다,

•	물 도달 시간 = 정수(또는 inf)

•	돌/비버굴/방문 불가 = 따로 처리

•	고슴도치 방문 여부 = visited_hedge[][]

식으로 분리하는 것이 디버깅에 훨씬 유리합니다.

•	고슴도치가 이동 가능 여부를 체크할 때는 보통

\text{hedgehog\_time}[x][y] + 1 < \text{water\_time}[nx][ny]

와 같이 “고슴도치가 가려는 시점보다 물의 도달 시점이 더 늦거나(또는 무한대)”인지 정확히 비교하는 방식을 많이 사용합니다.

•	BFS에서 레벨 증가(cnt) 타이밍이 서로 맞는지(물 확산 BFS vs 고슴도치 이동 BFS) 꼼꼼히 챙겨야 합니다.

•	“돌(X)이나 비버 굴(D)을 만났을 때 어떻게 처리할 건지” 로직을 명확히 분리하면 훨씬 보기가 쉬워집니다.

이런 부분들을 정리/조정하시면, 코드가 좀 더 직관적이고 유지보수하기 쉬워질 것입니다.

# DP: 동전 2

https://www.acmicpc.net/problem/2294

n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

## Phase1. 직접 풀기 - 초기 조건 못 잡아서 실패

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 14:16:16 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
워낙 많이 풀어 봤던 그거라서. 기억을 더듬어 풀어 봅시다.
dp[n] = min(dp[n-A[0~]] + 1)
3. 수도 코드
4. 코드 구현
"""

import sys

def init():
    global dp
    dp[0] = 0
    for coin in coins:
        if coin <= k:   
            dp[coin] = 1

def make_dp():
    for i in range(1, k+1):
        min_val = sys.maxsize
        for coin in coins:
            if i - coin >= 0:
                min_val = min(min_val, dp[i-coin]+1)
                dp[i] = min_val


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    coins = [
        int(input().strip())
        for _ in range(n)
    ]
    # init
    dp = [-1 for _ in range(k+1)]
    init()
    make_dp()
    # print(dp)
    result = dp[k] if dp[k] != 0 else -1
    print(result)
```

## Phase2. 피드백

동전 문제(특히 동전 2, 2294번)에서는 “DP 배열을 큰 수로 초기화하고, 유효한 상태에 대해서만 갱신” 하는 표준 접근 방식을 사용하면 구현이 더 간결해지고, -1 처리를 별도로 신경 쓰지 않아도 되는 장점이 있습니다.

아래에서는 (1) 전형적인 DP 점화식과 (2) 코드 구현 시 주의할 점을 짚어드리겠습니다.

1. 전형적인 DP 접근

•	dp[i] = 가치 합이 i원이 되도록 만드는 데 필요한 동전 개수의 최솟값.

•	초기값:

•	dp[0] = 0 (0원을 만드는 데 필요한 동전 개수 = 0개)

•	그 외 dp[i](1 ≤ i ≤ k)는 매우 큰 수(예: INF)로 설정

•	점화식:

dp[i] = \min\bigl(dp[i],\, dp[i - \text{coin}] + 1\bigr)

•	단, i - coin이 0 이상이고, dp[i - coin]이 유효한 상태(= INF가 아님)이어야 함.

이 로직에 따라 O(n×k) 시간에 문제를 해결할 수 있습니다.

2. Python 예시 코드

아래 코드는 가장 흔히 쓰이는 형태의 동전 2 문제 풀이 예시입니다.

dp[k]가 INF로 남아 있으면 만들 수 없는 금액이므로 -1을 출력하고, 그렇지 않으면 dp[k]를 출력합니다.

주요 포인트

1.	중복 체크 필요 X

•	동일한 동전을 여러 개 사용할 수 있기 때문에, for coin in coins: 안에서 다시 for i in range(coin, k+1):를 순회하며 계속 갱신해주면 됩니다.

2.	-1 대신 INF

•	“만들 수 없는 금액”을 dp[i] = INF로 유지한 뒤, 최종에 dp[k] == INF인지를 판별하여 -1을 출력하는 방식을 쓰는 것이 일반적입니다.

•	이렇게 하면 “이미 -1인 상태에서 +1을 더하는” 문제를 따로 처리할 필요가 없어 코드가 단순해집니다.

3.	시간 복잡도

•	최대 n(동전의 종류) * k(목표 금액)번 연산이 일어나므로, n, k가 10^4 이하 정도면 충분히 가능한 방식입니다. (BOJ 2294에서 제한은 n ≤ 100, k ≤ 10,000)

3. 기존 코드에서의 문제점

질문에 올려주신 코드에서 발생 가능한 문제점은 다음과 같습니다.

1.	dp[i-coin]이 -1인 경우를 체크하지 않음

```plain text
if i - coin >= 0:
    min_val = min(min_val, dp[i - coin] + 1)  # dp[i-coin]이 -1이면?
```

•	dp[i-coin]이 -1이라면 “i-coin 원을 만들 수 없다”는 뜻인데, 단순히 +1을 해버리면 0이 되어 버려 잘못된 값을 갱신하게 됩니다.

•	따라서 “dp[i - coin] != -1”인 경우에만 갱신해야 합니다.

2.	dp[i]가 -1인지, 아니면 0 이상인지 체크

•	dp[i]가 -1 상태라면, 아직 i원을 만들 수 없다는 뜻이므로 갱신 시점에 dp[i] = min_val 형태로 바로 바꿔줘야 합니다.

•	또는 위에서 언급한 것처럼 애초에 INF로 초기화하는 방식을 택하면 이중처리를 피할 수 있습니다.

3.	init()에서 dp[coin] = 1로 세팅

•	사실 모든 동전에 대해 dp[coin] = 1을 지정하는 것은 틀린 건 아니지만, 자동으로 BFS/DP를 돌리면서 자연스럽게 갱신되므로 생략해도 무방합니다.

•	동전이 1개인 경우에만 유효하다는 점은 DP 점화식에서도 곧바로 반영됩니다.

4. 결론

•	가장 단순한 구현은 “dp 전체를 INF로 초기화 + dp[0] = 0” → “동전을 돌면서 dp[i]를 갱신” → 결과적으로 dp[k]가 INF이면 -1, 아니면 dp[k].

•	이렇게 하면 중간에 -1 처리를 따로 할 필요가 없고, 코드가 짧고 직관적입니다.

위 코드를 참고해서 수정해보시면, 더 간결하고 안전하게 문제를 해결하실 수 있을 것입니다.

## 피드백 후 재도전

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2294                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2294                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 14:16:16 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
워낙 많이 풀어 봤던 그거라서. 기억을 더듬어 풀어 봅시다.
dp[n] = min(dp[n-A[0~]] + 1)
3. 수도 코드
4. 코드 구현
"""

import sys
INF = sys.maxsize


def make_dp():
    dp[0] = 0
    for i in range(1, k+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)


if __name__ == '__main__':	
    input = sys.stdin.readline
    n, k = tuple(map(int, input().split()))
    coins = [
        int(input().strip())
        for _ in range(n)
    ]
    # init
    dp = [INF for _ in range(k+1)]
    make_dp()
    # print(dp)
    result = dp[k] if dp[k] != INF else -1
    print(result)
```

BFS로도 이걸 풀 수 있음을 알았다. 머리가 말랑말랑해져야 그렇게 할 수 있을텐데.

# 위상정렬: 장난감 조립



우리는 어떤 장난감을 여러 가지 부품으로 조립하여 만들려고 한다. 이 장난감을 만드는데는 기본 부품과 그 기본 부품으로 조립하여 만든 중간 부품이 사용된다. 기본 부품은 다른 부품을 사용하여 조립될 수 없는 부품이다. 중간 부품은 또 다른 중간 부품이나 기본 부품을 이용하여 만들어지는 부품이다.

예를 들어보자. 기본 부품으로서 1, 2, 3, 4가 있다. 중간 부품 5는 2개의 기본 부품 1과 2개의 기본 부품 2로 만들어진다. 그리고 중간 부품 6은 2개의 중간 부품 5, 3개의 기본 부품 3과 4개의 기본 부품 4로 만들어진다. 마지막으로 장난감 완제품 7은 2개의 중간 부품 5, 3개의 중간 부품 6과 5개의 기본 부품 4로 만들어진다. 이런 경우에 장난감 완제품 7을 만드는데 필요한 기본 부품의 개수는 1번 16개, 2번 16개, 3번 9개, 4번 17개이다.

이와 같이 어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어져 있을 때 하나의 장난감 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산하는 프로그램을 작성하시오.

## Phase1. 직접 풀기 - 시간초과

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2637                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2637                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 22:45:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 아니 이거는 그거잖아. 
#  위상정렬을 하고, shortest path estimate 대신 all paths estimate로 노드를 업데이트하면
# 되지 않겠나?

import sys
from collections import deque, defaultdict
# 그래프 표현 컨벤션을 너무 섞어 쓰는 거 같다.
def topological_sort(V: int, E):
    in_degree = [0]*(V+1)
    adj = defaultdict(list)
    V_ = [i for i in range(V+1)]
    weights = defaultdict(int)
    for v, u, w in E:
        adj[u].append(v)
        in_degree[v] += 1
        weights[(u,v)] = w
    result = []
    initials = [v for v in V_ if in_degree[v] == 0]
    que = deque(initials)
    while que:
        u = que.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)
    return result[1:], adj, initials[1:], weights
    

def dag_shortest_path(s:int, adj: list, weights: list):
    """뭐 어떻게 하면 되지? 일단 하나의 버텍스를 기준으로? 그냥 모든 간선을 돌면서?"""
    p[s] = 1
    que = deque([s])
    while que:
        u = que.popleft()
        for v in adj[u]:
            # tmp = p[v]
            p[v] += p[u]*weights[(u,v)]
            # print(f'p[{v}] = {tmp} + {p[u]} * {weights[(u, v)]} = {p[v]}')
            que.append(v)



if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    E = [ 
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    result, adj, initials, weights = topological_sort(n, E)
    for s in initials:
        p = [0 for _ in range(n+1)]
        dag_shortest_path(s, adj, weights)
        print(f'{s} {p[n]}')

"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 
p 초기화 함수 삭제,
relax 함수 삭제

분석: 의미 없음
"""
```

## Phase2. 피드백 (정답 제시 금지)

1.	그래프 구성 방향

•	입력을 보면 “v를 만들기 위해서는 w개의 u가 필요하다”라고 주어지는데, 현재 코드에서 adj[u].append(v) 구조로 그래프를 만든 뒤, in_degree[v]를 올려주고 있습니다. 즉, u -> v 방향으로 간선을 구성하신 것으로 보입니다. 이때도 위상정렬 자체는 맞게 동작할 수 있지만, 이후 “어떤 노드(제품)를 만드려면 이전 노드(부품)들이 어떻게 필요하다”라는 값을 누적할 때에는, 간선 방향을 잘 활용하거나(예: u에서 v로 누적), 혹은 반대로 뒤집은 그래프를 쓸지(예: v에서 u로 누적) 미리 결정해야 합니다. 그래프 구성 방향과 누적 방식이 엇갈리면 값이 맞지 않거나, 중복 계산이 생길 가능성이 높습니다.

2.	위상 정렬 후 계산 방식(중간 부품 → 완제품 누적)

•	기본 아이디어는 “(기본 부품) → (중간 부품) → (완제품)” 순으로, 부품마다 필요한 기본 부품의 개수를 누적하는 과정이 필요합니다.

•	이를 위해 대개 2차원 배열(또는 딕셔너리) 형태로 count[x][i] = x(부품/완제품)을 만들 때 필요한 i(기본 부품)의 개수를 보관하고, 위상 정렬 순서대로 업데이트하곤 합니다.

•	예를 들어, v를 만들기 위해 w개의 u가 필요하다고 할 때, count[v]는 count[u]를 참고하여 count[v][i] += count[u][i] * w 형태로 누적합니다(만약 u 자체가 기본 부품이면 거기에 대해서도 직접 반영).

3.	한 번의 순회로 누적하기

•	현재 코드를 보면, initials(진입차수 0인 노드들)에 대하여 매번 dag_shortest_path를 호출하는 구조처럼 보입니다. 이렇게 하면 노드 수가 많을 때 매번 BFS/DFS를 돌게 되어 시간복잡도가 커져서 시간 초과가 날 가능성이 큽니다.

•	보통은 위상정렬로 얻은 순서를 한 번 순회하면서, 차례대로 필요한 부품들을 누적해나가는 방식으로 구현합니다. 이렇게 해야 중복 계산을 피하고, 각 간선마다 딱 한 번씩만 업데이트를 수행할 수 있어서 시간 복잡도가 크게 줄어듭니다.

4.	relax 함수 로직 점검

•	relax(u, v, w)에서 p[v] += p[u] * w 형태로 누적하고 있는데, 이는 “v를 만들려면 u 부품이 몇 개 필요한가?”를 저장하고 싶은 의도로 보입니다.

•	다만, p[v]가 한 개의 스칼라값이라면, 여러 기본 부품이 섞여 있는 경우를 제대로 표현하지 못합니다. 결국 u가 기본 부품인지, 중간 부품인지에 따라 “기본 부품별 갯수”로 확장해서 관리해 주어야 합니다(즉, p를 단순 배열이 아니라, 각 기본 부품마다의 요구량을 담는 구조로 바꿔야 할 가능성이 큽니다).

5.	기본 부품 판별

•	문제에서 “기본 부품은 다른 부품을 사용하여 만들 수 없는 부품”이라고 했습니다. 즉, 간선이 나가는 곳이 전혀 없는(= ‘A를 만들기 위해선 B가 필요하다’에서 B로 등장한 적이 없는) 노드가 기본 부품이라는 의미가 됩니다.

•	위상 정렬 과정에서 진출 간선이 없거나, 혹은 입력을 다 읽은 뒤 “어떤 부품을 만들기 위해 등장한 적이 없다”로 구분할 수 있습니다.

•	기본 부품인지 여부를 정확히 파악하고, 기본 부품인 경우에는 count[기본부품][기본부품] = 1로 시작하시면, 중간 부품 노드에 대해서는 위상정렬 순서에 맞춰 누적하는 식으로 진행이 가능합니다.

위 사항들을 참고해서,

•	그래프 방향을 어떻게 설정하고,

•	기본 부품부터 시작해 중간 부품, 최종 부품 순으로 “기본 부품의 필요 개수”를 한 번의 위상 정렬 순회에서 누적**,

•	“기본 부품별 카운트를 저장할 자료구조”를 구축

이렇게 세 가지를 중점으로 로직을 다듬어 보시면 좋을 것 같습니다. (정답 코드를 제시하지 않고 개념적인 피드백만 드렸습니다.)

### p를 벡터로 바꾸고 초기 부품에 대해 모두 DAG shortest paths 계산을 해야 하나? 그게 맞을 거 같다.

## Phase3. 디버깅 후 풀이 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2637                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2637                           #+#        #+#      #+#     #
#    Solved: 2025/03/30 22:45:21 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
# 아니 이거는 그거잖아. 
#  위상정렬을 하고, shortest path estimate 대신 all paths estimate로 노드를 업데이트하면
# 되지 않겠나?

import sys
from collections import deque, defaultdict
# 그래프 표현 컨벤션을 너무 섞어 쓰는 거 같다.
def topological_sort(V: int, E):
    # 내적 초기화
    # e. in_degree = [0, 0, 0, 0, 0, ]
    in_degree = [0]*(V+1)
    # 인접 리스트 초기화
    adj = defaultdict(list)
    # v 초기화
    V_ = [i for i in range(V+1)]
    # 가중치
    weights = defaultdict(int)
    
    # p1. 5, 1, 2
    # p2. 5, 2, 2
    # p3. ...
    for v, u, w in E:
        adj[u].append(v)
        in_degree[v] += 1
        weights[(u,v)] = w
    result = []
    # 내적이 0인 버텍스 초기화
    
    initials = [v for v in V_ if in_degree[v] == 0]
    # initials = [1, 2, 3, 4]
    for i in initials:
        p[i-1][i-1] = 1 # 자기자신을 만들 때 하나씩 필요

    que = deque(initials)
    que.popleft() # 0 제거
    # que = deque([1, 2, 3, 4])
    while que:
        # p1. u = 1
        u = que.popleft()
        # p1. result = [1]
        result.append(u)
        # 내적을 제거하고 위상정렬. v를 만드는데 u가 가중치만큼 필요할 것.
        # pick: u = 6
        for v in adj[u]:
            # v 내적 제거
            # v 부품 만들때 필요한 정보 업데이트. u번째 부품이 몇 개 필요한가?
            # 기존 u의 내적값...아 여기서 모든 부품에 대한 이터레이션 필요
            # p1. i = 0 
            # p2. i = 1
            # n = 7
            # 6번 부품이 7번부품 만들 때 몇개 필요한지 반영이 안 됨
            # pick: 
            for i in range(n):
                # i = 0
                # p[v-1=6][0~6] += p[5][0~6]*weight
                p[v-1][i] += p[u-1][i]*weights[(u,v)]
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)

    for i in initials:
        if i != 0:
            print(i, p[n-1][i-1] )

def dag_shortest_path(s:int, adj: list, weights: list):
    """뭐 어떻게 하면 되지? 일단 하나의 버텍스를 기준으로? 그냥 모든 간선을 돌면서?"""
    p[s] = 1
    que = deque([s])
    while que:
        u = que.popleft()
        for v in adj[u]:
            
            que.append(v)



if __name__ == '__main__':	
    input = sys.stdin.readline
    # n = 7
    n = int(input().strip()) 
    # m = 8
    m = int(input().strip())
    # E = [(5, 1, 2), ...]
    # 
    E = [ 
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    # p는? i번째 부품을 만드는데 m번째 부품이 몇 개 필요한지 계산.
    """
    p = [ 
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    """
    p = [[0 for j in range(n)] for _ in range(n)]
    topological_sort(n, E)
    # for s in p:
    #     print(s)
    # for s in initials:
    #     p = [0 for _ in range(n+1)]
    #     dag_shortest_path(s, adj, weights)
    #     print(f'{s} {p[n]}')

"""
이슈: 시간초과

Phase1.
환경: 파이썬
로그: 
최근 변경 사항: 

Phase2.
확인: 
시도: 
p 초기화 함수 삭제,
relax 함수 삭제

분석: 의미 없음
"""
```

디버깅을 하며 기대값을 주석에 적고, step into를 적극 활용했다. 작은 테스트케이스에 대해 차근차근 진행하면 생각보다 금방 유의미한 수정을 할 수 있다!

### 작은 테스트케이스에 대해 차근차근 진행하면 생각보다 금방 유의미한 수정을 할 수 있다!

# 다익스트라: 최소 비용 구하기

https://www.acmicpc.net/problem/2665

## Phase0. 문제 이해

![](./images/IMG_0463.png)

그림이 있어서 좀 겁 먹었었지만, 생각보다 어렵지는 않았음. 다익스트라를 dx, dy 테크닉을 이용해 bfs처럼 활용할 수 있는지 묻는, 생각보다 간단한 문제.

## Phase1. 직접 풀기

그냥 다익스트라 보고 구현하는 거라…코드를 외우고 넘어가야 의미가 있긴 함. 

다음 문제도 다익스트라니까, 안 보고 짜보도록 하세요.

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1916                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1916                           #+#        #+#      #+#     #
#    Solved: 2025/03/29 10:54:48 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
N개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 
도시의 번호는 1부터 N까지이다.

2. 문제 풀기
이거 다익스트라인데... 먼저 이론을 짚고 넘어가야 합니다.

3. 수도 코드
4. 코드 구현
"""

import heapq, sys
from collections import defaultdict

def dijkstra(G, n ,s):
    # 거리 정보를 무한으로 초기화
    distances = [float('inf') for _ in range(n+1)]
    # 그리고? 스타트 인덱스 초기화 하고 우선순위 큐에 집어 넣기
    distances[s] = 0
    queue = [(s, 0)]
    while queue:
        # current_node, current_distance
        current_node, current_distance = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue

        for neighbor, weight in G[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (neighbor, distance))
    # print(distances)
    return distances

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    buses = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    G = defaultdict(list)
    for u, v, w in buses:
        G[u].append((v, w))
        # G[v].append((u, w))
    start, end = tuple(map(int, input().split()))
    # print(n, m, G, start, end)
    distances = dijkstra(G, n, start)
    print(distances[end])
    
```

if distances[current_node] < current_distance: continue 부분에서 부등호를 거꾸로 해서 시간 초과가 났다. 이 부분은 어떻게 써도 에러는 안 나지만, 시간 복잡도에 상당히 기여하는 부분이니 주의. 

# 다익스트라:  미로 만들기

## Phase1. 직접풀기 - 성공

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2665                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2665                           #+#        #+#      #+#     #
#    Solved: 2025/03/31 21:16:37 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys, heapq
from collections import deque

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs_var():
    # init starting point
    maze_time[0][0] = 0
    queue = [[0, 0, 0]]

    while queue:
        _, x, y = heapq.heappop(queue)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 여기서 그 최적화를 해줄 수 있다. 
            if in_range(nx, ny):
                if maze[nx][ny] == 0: w = 1
                else: w = 0
                if maze_time[x][y] + w > maze_time[nx][ny]:
                    continue
                distance = maze_time[x][y]+w
                if distance < maze_time[nx][ny]:
                    maze_time[nx][ny] = distance
                    heapq.heappush(queue, (distance, nx, ny))
    # print('-'*10)
    # for mt in maze_time:
    #     print(mt)

if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    maze = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]
    # for m in maze:
    #     print(m)
    maze_time = [
        [float('inf') for _ in range(n)]
        for _ in range(n)
    ]
    bfs_var()
    print(maze_time[n-1][n-1])

"""
8
11100110
11010010
10011010
11101100
01100111
00110001
11011100
11000111
"""
```

### 디버그 노트

```python

def bfs_var():
    # init starting point
    maze_time[0][0] = 0
    queue = [[0, 0, 0]]

    while queue:
        _, x, y = heapq.heappop(queue)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 여기서 그 최적화를 해줄 수 있다. 

            if in_range(nx, ny):
                if maze_time[x][y] + 1 > maze_time[nx][ny]:
                    continue
                # update shortest path estimate of nx, ny
                # if nx, ny belongs to grey one
                if maze[nx][ny] == 0:
                    distance = maze_time[x][y]+1
                else:
                    distance = maze_time[x][y]
                if distance < maze_time[nx][ny]:
                    maze_time[nx][ny] = distance
                heapq.heappush(queue, (distance, nx, ny))
```

함수를 이렇게 작성했을 때 83프로에서 시간초과 발생했다. 일단 문제점이 뭐였냐면, 

1. heapq.heappush 구문이 shortest path estimate가 갱신되지 않은 시점에도 업데이트 되고 있었고(큐에 과도한 푸쉬 연산 발생했을 것)(이게 핵심)
1. 초기 비교에서 가중치를 일괄적으로 1로 가정해서 업데이트하지 않아도 되는 경우를 패스했는데,
2번은 그다지 문제가 아니었고(차이가 좀 있었을 거 같긴 한데, 직접 비교한 수행 시간은 64ms로 동일) heapq.heappush 연산 위치가 문제였다.

아무튼 잘 해결해서 풀이 성공. 재미있는 다익스트라 활용 문제였다. 

# 위상정렬: 그래프 수정

## Phase1. 첫 번째 시도

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1432                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1432                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 10:45:06 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
일단 위상정렬해서 차례로 매긴 번호를 원래 번호 순서대로 출력하면 됨.
3. 수도 코드
4. 코드 구현
"""

import sys, heapq
from collections import defaultdict


# 위상 정렬 알고리즘
def topological_sort(n: int, graph):
    in_degree = [0 for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1
    cnt = 1
    que = [u for u in range(n) if in_degree[u] == 0]
    if not que:
        print(-1)
        return
    result = [0 for _ in range(n)]
    while que:
        for _ in range(len(que)):
            u = heapq.heappop(que)
            result[u] = cnt
            cnt += 1
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    heapq.heappush(que, v) 
    if not que and sum(in_degree) > 0:
        print(-1)
        return
    else:
        for r in result:
            print(r, end=' ')


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]   
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                graph[i].append(j)
    topological_sort(n, graph)
    # print(graph)



```

## Phase2. 

사전순으로 출력이 안 돼서 내적 기준 대신 외적 기준으로 정렬을 함. 

‘사전 역순’ 출력일 경우 내적 기준으로 정렬하면 됨. 

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1432                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1432                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 10:45:06 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
1. 문제 읽기
2. 문제 풀기
일단 위상정렬해서 차례로 매긴 번호를 원래 번호 순서대로 출력하면 됨.
3. 수도 코드
4. 코드 구현
"""

import sys, heapq
from collections import defaultdict


# 위상 정렬 알고리즘
def topological_sort(n: int, graph):
    # 내적 초기화
    # out_degree = [0, 0, 0, 0]
    out_degree = [0 for _ in range(n)]
    graph_reverse = defaultdict(list)
    for u in range(n):
        for v in graph[u]:
            out_degree[u] += 1
            graph_reverse[v].append(u)
    # out_degree = [2, 0, 0, 1]
    # 내적이 0인 버텍스값들 먼저 큐에 삽입
    # que = [0]
    que = [-u for u in range(n) if out_degree[u] == 0]
    heapq.heapify(que)
    cnt = n
    result = [0 for _ in range(n)]
    while que:
        for _ in range(len(que)):
            # u = 0
            u = -heapq.heappop(que)
            result[u] = cnt
            cnt -= 1
            for v in graph_reverse[u]:
                out_degree[v] -= 1
                if out_degree[v] == 0:
                    heapq.heappush(que, -v) 
    if not que and sum(out_degree) > 0:
        print(-1)
        return
    else:
        for r in result:
            print(r, end=' ')


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    arr = [
        tuple(map(int, list(input().strip())))
        for _ in range(n)
    ]   
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                graph[i].append(j)
    topological_sort(n, graph)
    # print(graph)



```

# 위상정렬: 임계경로

## Phase1. 

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1948                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 17:12:36 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

def topology_sort(arr: list, n: int):
    # in_degree
    graph = defaultdict(list)
    graph_reversed = defaultdict(list)
    in_degree = [0 for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]
    for u, v, w in arr:
        graph[u].append((v, w))
        in_degree[v] += 1
        graph_reversed[v].append((u, w))
    queue = deque([u for u in range(n+1) if in_degree[u] == 0 ])
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v, w in graph[u]:
            in_degree[v] -= 1
            cost[v] = max(cost[v], cost[u]+w)
            if in_degree[v] == 0:
                queue.append(v)
    return cost, graph, graph_reversed

def back_prop(v: int, graph_reversed: defaultdict, path: list):
    global visited, critical_path
    # 역 추적값 구하기
    if v == start:
        # print(path)
        for p in path:
            critical_path.add(p)

    for u, w in graph_reversed[v]:
        if cost[u] >= cost[v] - w: # 현재 가중치를 뺀 값과 일치 ??
            # visited[u] = True
            path.append((u, v))
            back_prop(u, graph_reversed, path)
            path.remove((u, v))
            # visited[u] = False


if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    start, end = tuple(map(int, input().split()))
    # print(n, m, arr, start, end)
    cost, graph, graph_reversed = topology_sort(arr, n)
    visited = [False for _ in range(n+1)]
    critical_path = set()
    back_prop(end, graph_reversed, [])
    print(cost[end])
    
    print(len(critical_path))

```

## Phase2. 다른 시도

```python
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1948                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: joho54 <boj.kr/u/joho54>                    +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1948                           #+#        #+#      #+#     #
#    Solved: 2025/04/02 17:12:36 by joho54        ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**8)

def topology_sort(arr: list, n: int):
    global test
    # in_degree
    graph = defaultdict(list)
    graph_reversed = defaultdict(list)
    in_degree = [0 for _ in range(n+1)]
    cost = [0 for _ in range(n+1)]
    for u, v, w in arr:
        graph[u].append((v, w))
        in_degree[v] += 1
        graph_reversed[v].append((u, w))
    queue = deque([u for u in range(n+1) if in_degree[u] == 0 ])
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v, w in graph[u]:
            in_degree[v] -= 1
            if cost[v] <= cost[u] + w:
                # 그리고? v로 가기 위해서는 u로 꼭 거쳐야 함을 경로에 저장.
                if cost[v] == cost[u]+w:
                    test[v].append(u)
                else: 
                    test[v] = [u]
                cost[v] = cost[u] + w
            if in_degree[v] == 0:
                queue.append(v)
    return cost, graph, graph_reversed

def dfs(v: int, paths: list):
    global test
    if v == start:
        # print('pippip', v)
        for p in paths:
            critical_path.add(p)
        return
    for u in test[v]:
        # print(f'getting into {u}')
        paths.append((u, v))
        dfs(u, paths)
        paths.remove((u, v))



if __name__ == '__main__':	
    input = sys.stdin.readline
    n = int(input().strip())
    m = int(input().strip())
    arr = [
        tuple(map(int, input().split()))
        for _ in range(m)
    ]
    start, end = tuple(map(int, input().split()))
    # print(n, m, arr, start, end)
    test = defaultdict(list)
    cost, graph, graph_reversed = topology_sort(arr, n)
    critical_path = set()
    dfs(end, [])
    print(cost[end])
    # print('critical path test', test)
    print(len(critical_path))


```

back-propagation/dfs 역추적 관계 없이 시간 초과 오류 발생. 문제는 topology_sort에 있음.

