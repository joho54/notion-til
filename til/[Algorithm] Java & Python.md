# [Algorithm] Java & Python



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기



## Phase1. Top down

```java

import java.util.Scanner;

class BOJ2018 {

    public static int MAX_N = 10000000;
    public static int[] arr = new int[MAX_N];

    public static void main(String[] args) {
        int ptr1 = 0;
        int ptr2 = 0;
        int tmp;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }
        int ans = 1;
        while (ptr1 < n - 1 && ptr2 < n) {
            tmp = ((arr[ptr1] + arr[ptr2]) * (arr[ptr2] - arr[ptr1] + 1)) / 2;
            if (tmp == n) {
                ans++;
                ptr1++;
                ptr2++;
            } else if (tmp > n) {
                ptr1++;
            } else if (tmp < n) {
                ptr2++;
            }
        }
        System.out.println(ans);

    }
}

```

## Phase2. Bottom up

### 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

### 손으로 플어보기

투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=25c2e1f0ddc40646b2eb3777544db796fd4d96053ec5db8d20dcc2ba771e04c3&X-Amz-SignedHeaders=host&x-id=GetObject)

- sum > N: sum = sum - start_index; start_index++
- sum < N: end_index++; sum = sum + end_index;
- sum == N: end_index++; sum = sum + end_index; count++;
### 슈도코드

```c
N 변수 저장
사용 변수 초기화(count = 1, start_index = 1, end_index = 1, sum = 1)
while(end_index != N) {
	if(sum == N) count 증가, end_index 증가, sum 값 변경
	else if(sum > N) sum값 변경, start_index 증가
	else if(sum < N) end_index 증가, sum값 변경 
}
count 출력
```

### 코드 구현

정답

```java
import java.util.Scanner;

public class P2018_연속된자연수의합{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 1;
		int start_index = 1;
		int end_index = 1;
		int sum = 1;
		while (end_index != N){
			if(sum == N){
				count++;
				end_index++;
				sum = sum + end_index;
			} else if (sum > N){
				sum = sum - start_index;
				start_index++;
			} else {
				end_index++;
				sum = sum + end_index;
			}
		}
		System.out.println(count);
	}
}
```

개선

```java

import java.util.Scanner;

class BOJ2018 {

    public static void main(String[] args) {
        int ptr1 = 1;
        int ptr2 = 1;
        int tmp;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 1;
        while (ptr2 < n) {
		        // 조건문에서 합을 구하는 대신 여기서 한번에 값을 구해도 논리적으로는 상관 없지 않나?
		        // 연속된 배열이 등차수열이 아닐 때는 이 방법을 못 쓰겠지. 예재처럼 풀면 모든 오름차순배열에 대해서 같은 답을 낼 수 있고
            tmp = ((ptr1 + ptr2) * (ptr2 - ptr1 + 1)) / 2; 
            if (tmp == n) {
                ans++;
                ptr1++; // 정답에는 이 부분이 없지만, 논리상으로 어차피 첫 번째 포인터도 옮겨야 한다.
                ptr2++;
            } else if (tmp > n) {
                ptr1++;
            } else if (tmp < n) {
                ptr2++;
            }
        }
        System.out.println(ans);

    }
}

```

# 투포인터: 주몽



## Phase1. Top down

```c
import java.util.Scanner;
import java.util.Arrays;

// 그래서 어떻게 풀어? 무슨 문제야?
// 일단 뺄셈을 이용하면 좋다.
// 같은 숫자가 주어지는가? 아니, 고유한 번호가 주어진다.
// 일단은 주어진 번호를 인덱스로 하는 불 배열을 만드는 것도 좋지 않나?
// 그러나 투 포인터가 아니잖아.
// 투 포인터를 어떻게 하면 써먹지?
// 재료의 개수가 15000으로 매우 많나? 그러니까 nlogn으로는 풀면 안 되는 건가
// 만약 n으로 풀 수 있는 문제인가? 그냥 정렬하는게 낫지 않아? 
// 일단 정렬 + 투포인터가 제일 합당한 거 같다.
// end index 값 증가 로직이 적절하지 않다.어떻게 해야 하나? 
//  일단 세부 조건을 두고, 인덱스끼리 안 겹칠때는 작으면 start를 올리고, 겹칠거 같으면 end를 올려야지
// sum 과 m의 비교에서
// sum > m: 정렬된 배열에서 m 값을 맞추기 위해 투 포인터로 할 수 있는 방법이 더는 없다. 
// 이 경우 포인터를 이동할 수록 가능한 값을 증가시킬 뿐이다. 그러니까, 동작을 끝내야 한다.
// sum == m: 답을 찾은 경우
// sum < m: 값을 더 증가시켜야 하는데, 이게 좀 더 정교하게 해야 하는 경우.
// 찾았다. start_index를 초기화시키는 절차가 없어서 문제다.

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            array[i] = sc.nextInt(); // what happens then?
        }
        Arrays.sort(array);

        int start_index = 0;
        int end_index = 0;
        int sum = array[start_index];
        int ans = 0;
        while(start_index < n && end_index < n){
            sum = array[start_index] + array[end_index];
            if(sum < m){
                if(start_index < end_index-1){
                    start_index++;
                }
                else
                    end_index++;
            }
            else if(sum == m){ // found one
                ans++;
                start_index = 0;
                end_index++;
            }
            else if (sum > m){
                break;
            }
        }
        System.out.println(ans);

    }
}   
```

## Phase2. Bottom up

# 재귀: 하노이의 탑

## Phase1. Top Down

```python
# 하노이 원판
# Phase1. 문제 읽기
# 한 번에 하나의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# Phase2. 문제 풀기
# n 20을 기점으로 출력 여부가 달라짐. 
# N 최대값은 100.
# 일단 방법은 알겠거든 그런데 리컬젼을 어떻게 해야 할지 모르겠다. 
# move_plate(i): i번째 원판을 옮긴다 쳐. 
# 그다음 재귀는? move_plate()
# 순서를 바꿔서 종료조건부터 생각해보자. 
# 원판 = [1,2,3]
# hanoi = [[1, 2, 3], [], []]
# 다음 = [[2, 3],[],[1]]
# ...
# = [[][][1, 2, 3]]
# 이렇다. 
# 종료조건은  len(hanoi[2])==3
# recursion할 때 들어가야 하는 정보는? 원판 번호, 다음 위치, 
# 다음 위치는 뭔데. 
# recursion. 결국 작은 문제를 해결하는 방식으로 큰 문제가 해결되는 건데. 
# Phase3.  문제는 풀겠다. 그런데 머리로는 아무것도 안 돌아간다. 더 n=4를 다시 풀어복.
# Phase4. 재귀 코드 템플릿을 작성해보기
# 모르겠다. 일단 25분 이상 생각했다.
# 자 이제 다시 생각해보자. recursion 에서 중요한 건 sub problem 정의하는 거다. 
# 사실 그림 이해하면 끝이긴 하다.

# 그러면 어떻게 하는데. 
global_n = int(input())
ans = 0
# n개의 원판을 start에서 end로 옮기는 경로.
def hanoi(n, start, end):
    global ans
    if n == 0: return
    # n번째 원판은 무조건 3번째 기둥으로 옮겨짐. 더 알 필요 없음. 
    # 지금 구하는게 경우의 수인가? 아니, 경로 산정인거지. 경로가 하나니까 산정할 필요가 없는 거고
    ans += 1
    print(start, end) if global_n <= 20 else None
    hanoi(n-1, start, 6-start-end)
    hanoi(n-1, 6-start-end, end)

hanoi(global_n, 1, 3)
print(ans)

```

## Phase2. Bottom Up

```python
def move(no: int, x: int, y: int) -> None:
	"""원반 no개를 기둥 x에서 기둥 y로 옮김"""
	if no > 1:
		move(no - 1, x, 6 - x - y)
	print(x, y)
	if no > 1:
		move(no - 1, 6 - x - y, y)

n = int(input())

move(n, 1, 3)
```

### 질문들

1. 조건문이 두개나 필요한 이유: 하노이 탑에서는 print 되는 순서가 중요함. 그래서 우선은 n-1개를 보조 기둥으로 옮기는 작업을 호출한 후 그것들을 옮기는 작업이 완료 됐을 때 지금 원판을 최종 위치로 옮기고, 나머지 원판들을 다시 보조 기둥에서 최종 위치로 옮기는 작업을 해 줘야 함.
# 재귀: N-queen

## Phase1. Top Down

### 아이디어: 재귀는 과거형이다. 정확히 말하면, 지금 문제를 푸는 시점은 과거의 문제들이 다 해결된 시점이다. 문제의 시제를 잘 생각해야 한다.

### 풀이: 실패

```python
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# 재귀 문제 푸는법
# 1. subproblem 정의
# 전혀 모르겠다. 
# n번째 퀸을 놓을 자리를 고민하고 있다. 지금은.
# 이미 해결했다. n-1개의 퀸을 놓는 문제는.
# n-1개의 퀸이 이미 놓여 있으므로 내가 할 일은 n번째 퀸을 놓을 수 있는 빈 자리를 고민하는 것이다.
# 빈자리에 전부다 놓을 수 있는가? 안 될 거 뭐 있나. 
# 

n = int(input())

def get_possible_places_pass1(already_placed):
    possible_places = []
    for x, y in already_placed:


def place(n, already_placed): 
    """n 번째 퀸을 놓는 위치를 placed에 추가해서 리턴."""
    # base condition 이따가 해 주고
    if n == 1: 
        already_placed.append([0, 0])
    # n-1 번째의 퀸을 놓을 위치를 '이미 추가된 것들 위치'에 추가해서 리턴해서 추가.
    already_placed.append(place(n-1), already_placed) 
    possible_places = get_possible_places(already_placed)
    return len(possible_places)
    
```

## Phase2. Bottom Up

### 문제를 다시 정리하기

> 무엇이 이해되지 않았는지 구체적으로 정리합니다.

sub problem 정의를 하지 못했다.

### 작은 문제로 디버깅

> 컴퓨터 대신 손으로 직접 실행해보는 것도 효과적입니다. 예제 입력을 작게 하여 코드가 어떻게 동작하는지 확인.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/005964d6-917a-4d21-bede-ff8ab6a4e978/IMG_9871.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=5ae48614c392a8ffbdc65d4b95a4993c070a45298f425977ef313cb9ee475d29&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a82a3eec-e72a-40bb-87cb-8327c5cc36b1/IMG_9872.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=9ffd331a40c80632cade968212fb990e68b7fb1e6d03423c484b0a4bc29c419d&X-Amz-SignedHeaders=host&x-id=GetObject)

n=5까지 그려봤으나 규칙 확인 실패

### 관련 개념 복습: 재귀 기초 개념

> 개념 부족으로 인한 풀이 실패.

관련 코드 다시 학습

재귀: 어떠한 이벤트에서 자기 자신을 포함하고 다시 자기 자신을 사용하여 정의되는 경우 재귀라고 함.

재귀적 정의의 예시: 자연수의 정의

- 1은 자연수입니다.
- 어떤 자연수의 바로 다음 수도 자연수입니다.
재귀적 정의의 응용: 팩토리얼 n!의 정의(n은 양의 정수)

- 0! = 1
- n > 0이면 n! = n x (n - 1)!
```python
# 양의 정수 n의 팩토리얼 구하기
def factorial(n: int) -> int:
	"""양의 정수 n의 팩토리얼 값을 재귀적으로 구함"""
	if n > 0:
		return n * factorial(n - 1)
	else:
		return 1
```

팩토리얼을 재귀적으로 구하는 과정.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/ef6a62d5-e03d-40cc-88e9-b4e6fb30c8d3/IMG_9873.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=78299544b4a28991e7008d49b76e39d26be6dc26e5c8ca59dc547177d47db4c2&X-Amz-SignedHeaders=host&x-id=GetObject)

(맨 마지막이 d)

각 단계에 대한 설명

a 함수 호출식 factorial(3)을 실행하면 factorial() 함수가 호출됨. 이 함수는 매개변수 n에 3을 전달받아 3*factorial(2)의 값을 반환합니다. 그런데 이 곱셈을 하려면 factorial(2)의 값을 구해야 함. 그래서 실제 인수로 2를 전달해서 함수 factorial(2)를 호출.

b 호출된 factorial() 함수는 매개변수 n에 2를 전달받음. 다시 2*factorial(1)을 실행하기 위해 함수 factorial(1)을 호출

c 호출된 factorial() 함수는 매개변수 n에 1을 전달받음. 1 * factorial(0)을 실행하기 위해 factorial(0)을 호출.

d 호출된 factorial()함수는 매개변수 n에 전달받은 값이 0이므로 1을 반환합니다. 이때 처음으로 return문이 실행되고 반환값 1을 c로 보냄

이제 다시 역순으로 올라감

c 반환된 값 1을 전달받은 factorial 함수는 1 * factorial(0), 즉 1 * 1 을 반환

b 반환된 값 1을 전달받은 factorial 함수는 2 * factorial(1), 즉 2*1을 반환

a 반환된 값 2를 전달받은 factorial 함수는 3*factorial(2) 즉, 3*2를 반환

이렇게 최종 factorial(3)값인 6을 얻음

- 직접 재귀와 간접 재귀
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a1fda402-9322-4b73-b569-596a90f192eb/IMG_9874.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=6ddbb3029f3f48249cd6cfd4bb7dcb644b4b7b2b15ce6de7fef35e7a7ef69de9&X-Amz-SignedHeaders=host&x-id=GetObject)

- 유클리드 호제법
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/899122bf-a705-49f5-94ca-91e8cedab38e/IMG_9875.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDTBG2H%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNDWuOfX5tX%2FMS%2Bdz692QFYaya6dJ%2Bbx5xg9WZnw5qFQIhAMLqId4xvR8o3Oqe4IKEOOny8A%2BxV%2BsLczBSbBvtfDI2Kv8DCBEQABoMNjM3NDIzMTgzODA1IgyYCLzI%2BuEGkrUzpnkq3AODlinANFzb2hPHZM9CAkzErRrL%2FEzB6XBlg8%2BV9j4pEIezNiLKp98y5KT12PkaNnIn0XJbTGv%2FkuGRMRR5sJQUd6YdngnWAIrsYn8V4mAhed7fjthlVC8ZgYCe%2FY49%2FY4ON%2FwU2dC8yovM0UQ%2FwIuV6%2B9oRyuLBbNiLm8o2KzhWlQ2LTCPQnlSywWYIDKvoNOJ%2BgqIU6WPsyP6WTNGT22zE3WgVLBkkk3OqI0GgbNCLOPhvi98KCaWDgik0YAMLeO5iaitd800IhXk6DtuHNG%2BT%2FHCl0RLg5NBHpkOU%2FKQ4H4Zs%2FaA8zWMw8sO8IQoOQrHUdoYDl%2BbJBg33Saa2jLojMG0SMETXi%2BUioSughRgi1eilCBpoRoFIR1feq5c1Z5Tx0FiZMFotb%2BeJXBWKQQu7E0OK4Hhxp8XlYq4jQ5xa463rRqUcfzNSCL%2BA52DKz8iuHrsCgsXYMruH1hlGjK0Enl2Ea2qkwwXMuRqQ31NM7ksvCVICoET4YUvrSlw7LdWhtNatNjcm88SsAJYtuDaEi7mAfWJFGdaz2HCg8mRShH9tFv9mqcPhK7VdplRFxTIldhLthb%2B912GksBk6qX8Zcj375BsUuU%2FjShNAoHHVTw%2BtBv0daLTq2R8lTCn4dS%2BBjqkAcUXYCg2FhAio8RZOiuTpU5Pk5WxK%2BpWmzseAHs%2FrnchsXTJleeMK6ZI6k5m0LzPfffRfgUccfcSmzskgPzi%2FgN6C3LWPKQNaXTmizTgc9YYYaRuIp%2Bww%2BR6m0erbusQHxi%2FOuNKVevX4jfZIg8Nw58AlAmNKYdZ6QHUPo5SkudfDEpJm61wznZ3EtxAl%2F%2FWTp8CsfIdU6NKpuQ7hHQA0H9KLuHa&X-Amz-Signature=8f1679a59e7cd6b3cecbf8b730841d9d67c5669d017923174e6972c19755bd0f&X-Amz-SignedHeaders=host&x-id=GetObject)

이 과정의 수학적 정의: 두 정수 x와 y의 최대 공약수를 gcd(x, y)로 표기할 때, x=az와 y=bz를 만족하는 정수 , a, b와 최대의 정수 z가 존재할 때 z는 gcd(x, y)라고 할 수 있다.

gcd(x, y)의 재귀적 정의(이때 재귀 매개 변수 규칙 상, x가 항상 크다)

- y가 0이면 → x
- y가 0이 아니면 → gcd(y, x%y)
구현된 코드

```python
# 유클리드 호제법으로 최대 공약수 구하기

def gcd(x: int, y: int) -> int:
	"""정숫값 x와 y의 최대 공약수를 반환"""
	if y == 0:
		return x
	else:
		return gcd(y, x % y)
```

### 관련 개념 복습: 재귀 알고리즘 2가지 분석 방법

> 복습 지시: 아래 코드를 가지고 상,하향식 분석 도식을 그리고, 출력 결과를 예상하세요.(상, 하향식 분석의 출력 결과 예상을 모두 하기 전에는 답 확인하지 마세요) → 복습 완료.

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

> recur()함수는 앞에서 다룬 facorial()함수나 gcd() 함수와 달리 함수 안에서 재귀 호출을 2번 실행. 이처럼 재귀 호출을 여러 번 실행하는 함수를 순수한 재귀라고 하는데, 실제 동작은 복잡합니다. 실행 결과처럼 매개변수 n에 4를 전달하면 recur() gkatnsms 1, 2, 3, 1, 4, 1, 2를 한 줄에 하나씩 출력합니다. 만약에 n이 3이나 5라면 어떤 결과를 출력할지는 간단히 알 수 없습니다.. 재귀 호출하는 recur() 함수를 top-down과 bottom-up 방법으로 분석해보겠습니다.

- top-downd
매개변수 n에 4를 전달하면 recur() 함수는 다음과 같은 순서로 실행합니다.

recur(4)의 실행 과정

1. recur(3)을 실행합니다.
1. 4를 출력합니다.
1. recur(2)를 실행합니다.
위의 과정 2에서 4가 출력되려면 recur(3)의 실행을 완료한 뒤이므로 먼저 과정 1에서 recur(3)이 무엇을 하는지 그림 5-5를 참고하여 알아보겠습니다. 각각의 상자는 recur() 함수의 동작을 나타냅니다. 전달받은 값이 0 이하면 recur()함수는 아무 일도 하지 않으므로 비어 있다는 의미로 상자 안에 -를 표시합니다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/61ada9d6-0300-477b-8faf-1933c1296dea/IMG_9876.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DITOMZI%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDanUt7YwGgjCtXdiCzU6REb8kLsDV9U62pXbWQmlelbAIhAIcOz60XpHtu4VFWoUQyHWGpnvB9J0qWOYadLi3aUReiKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7PtHmbRzaB%2BLhHzYq3APS4xfmtvT%2FtPB0C09yrQYEjDDAVUNhsaupkK8ILuwZlPSqDYX5gh7sguV9s1qhaJmFXfm5EJQYtKYSGlu74eRiw%2B88T0UFWIVo85x1nrU8bH99TSSRJy4Uc7RRoAfvpx%2BrXG1aVi8JdTlUVOeJXCaku4IE1RABgF6ffy3tRXW%2Fc%2ByKkZokFuT1cBsYNBYsA1rhtktIZqRkIdtGJM20lthmjfspP9YAsWLlQL6ZIVYYNj7uoZXxxZJx4opWKsctAiOiVukTQqBvi41hknqoIzmTyz%2Fu0pcvXDfxDACygyf7V1L0TeFYDVyIv1ljCRZDIsUPDHb10GprO2okz829k2XH%2BzxVlJSxTYbts8n1nsRnm3VYKf6bo1Tv1BTjhV%2Bl%2BLAHqFFflzrlCIU5En%2B6y2K57FjusUDJFyzpGAS67PtWO2wDM7WhTAvb%2FtDsz8WyqCn7gvyKDvmgQXNQWQF8CLHXeYEuaeLAlLoJB9huOrwuoXG7QIUSFkc1aB0ddO8j9zHG8uc%2BTYHh6woc20uhSen0RDTMwbc%2BHmDy1t6lQja8qugUK9UiFOuP4Lfcif12KEU53%2BGj%2BBzSvf0EjhOlO2rfQO%2B1%2Bsp5mtL1Ju2JxfZiIEH1VfTzzZJpc2zogDC4xNS%2BBjqkAWzmbvhuMKG0uZFTWmYapZLkJxwhl0uSsvNbUn1N%2F4R7ptclcOA5I0yWx1Ygu%2FYUPv7UsbTmN5bAtdUv%2FzhfR6Zd16Kbxjj05oZzgxC9SvKIcMVMHytapwPjULwVoFUPtyxjfCo96yC%2FIFSldlKl5Mh6EIHGOAIWniVqki0y%2BjCdMEK%2BZS13XXeLQdV9QcvpxPrG24AvwPpOulRgJvb1WyjJabjq&X-Amz-Signature=ef0d23241d68fa62c984127cfac1810eba7acf9f1beaa833246eedebfa192735&X-Amz-SignedHeaders=host&x-id=GetObject)

가장 위쪽에 위치한 상자의 함수 호출부터 시작하여 계단식으로 자세히 조사해 나가는 분석 방법을 하향식 분석이라 합니다. 그런데 그림에서 보다시피 recur(1), recur(2) 등 같은 함수가 여러번 호출되고 있습니다. 꼭대기부터 분석하면 이렇게 같은 함수를 여러 번 호출할 수 있으므로 하향식 방식이 반드시 효율적이라고 말할 수는 없습니다.

- bottom-up
하향식 분석과는 반대로 아래쪽부터 쌓아 올리며 분석하는 방법을 상향식 분석이라고 합니다. recur() 함수는 n이 양수일 때만 실행하므로 먼저 recur(1)이 어떻게 처리되는지 알아야 합니다. recur(1)은 다음과 같은 순서로 실행됩니다.

recur(1)의 실행 과정

1. recur(0)을 실행합니다.
1. 1을 출력합니다.
1. recur(-1)을 실행합니다.
이때, 1, 3 과정은 출력할 내용이 없으므로 결국 과정 2만 출력. 다음으로 recur(2) 실행과정

1. recur(1)을 실행합니다.
1. 2를 출력합니다.
1. recur(0)을 실행합니다.
recur(2)를 실행하면 과정 1에서 recur(1)은 1을 출력하지만 과정 3은 아무것도 출력하지 않음. 결국 recur(1)과 recur(2)의 과정을 거쳐 1, 2를 출력. 이 작업을 recur(4)까지 쌓아 올리며 설명한 내용이 아래 그림. 이 과정을 통하여 recur(4) 최종 출력 얻을 수 있음.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b1769365-105f-46de-b9a9-3de7d23c5e8a/IMG_9877.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DITOMZI%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDanUt7YwGgjCtXdiCzU6REb8kLsDV9U62pXbWQmlelbAIhAIcOz60XpHtu4VFWoUQyHWGpnvB9J0qWOYadLi3aUReiKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7PtHmbRzaB%2BLhHzYq3APS4xfmtvT%2FtPB0C09yrQYEjDDAVUNhsaupkK8ILuwZlPSqDYX5gh7sguV9s1qhaJmFXfm5EJQYtKYSGlu74eRiw%2B88T0UFWIVo85x1nrU8bH99TSSRJy4Uc7RRoAfvpx%2BrXG1aVi8JdTlUVOeJXCaku4IE1RABgF6ffy3tRXW%2Fc%2ByKkZokFuT1cBsYNBYsA1rhtktIZqRkIdtGJM20lthmjfspP9YAsWLlQL6ZIVYYNj7uoZXxxZJx4opWKsctAiOiVukTQqBvi41hknqoIzmTyz%2Fu0pcvXDfxDACygyf7V1L0TeFYDVyIv1ljCRZDIsUPDHb10GprO2okz829k2XH%2BzxVlJSxTYbts8n1nsRnm3VYKf6bo1Tv1BTjhV%2Bl%2BLAHqFFflzrlCIU5En%2B6y2K57FjusUDJFyzpGAS67PtWO2wDM7WhTAvb%2FtDsz8WyqCn7gvyKDvmgQXNQWQF8CLHXeYEuaeLAlLoJB9huOrwuoXG7QIUSFkc1aB0ddO8j9zHG8uc%2BTYHh6woc20uhSen0RDTMwbc%2BHmDy1t6lQja8qugUK9UiFOuP4Lfcif12KEU53%2BGj%2BBzSvf0EjhOlO2rfQO%2B1%2Bsp5mtL1Ju2JxfZiIEH1VfTzzZJpc2zogDC4xNS%2BBjqkAWzmbvhuMKG0uZFTWmYapZLkJxwhl0uSsvNbUn1N%2F4R7ptclcOA5I0yWx1Ygu%2FYUPv7UsbTmN5bAtdUv%2FzhfR6Zd16Kbxjj05oZzgxC9SvKIcMVMHytapwPjULwVoFUPtyxjfCo96yC%2FIFSldlKl5Mh6EIHGOAIWniVqki0y%2BjCdMEK%2BZS13XXeLQdV9QcvpxPrG24AvwPpOulRgJvb1WyjJabjq&X-Amz-Signature=0c52b9d20572cee7f66783bc79bc343acd619d0d7d6abb4500bbb89550dc6f62&X-Amz-SignedHeaders=host&x-id=GetObject)

> 만약 위의 재귀 호출을 거꾸로 출력하려면?

```python
def recur(n: int) -> int:
	"""순수한 재귀 함수 recur의 구현(거꾸로 출력)"""
	if n > 0:
		recur(n - 2)
		print(n)
		recur(n - 1)
```

위 코드의 호출 과정

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/0c1839b9-722b-4eaa-a55f-4bfea7bf1cd5/IMG_9878.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DITOMZI%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDanUt7YwGgjCtXdiCzU6REb8kLsDV9U62pXbWQmlelbAIhAIcOz60XpHtu4VFWoUQyHWGpnvB9J0qWOYadLi3aUReiKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7PtHmbRzaB%2BLhHzYq3APS4xfmtvT%2FtPB0C09yrQYEjDDAVUNhsaupkK8ILuwZlPSqDYX5gh7sguV9s1qhaJmFXfm5EJQYtKYSGlu74eRiw%2B88T0UFWIVo85x1nrU8bH99TSSRJy4Uc7RRoAfvpx%2BrXG1aVi8JdTlUVOeJXCaku4IE1RABgF6ffy3tRXW%2Fc%2ByKkZokFuT1cBsYNBYsA1rhtktIZqRkIdtGJM20lthmjfspP9YAsWLlQL6ZIVYYNj7uoZXxxZJx4opWKsctAiOiVukTQqBvi41hknqoIzmTyz%2Fu0pcvXDfxDACygyf7V1L0TeFYDVyIv1ljCRZDIsUPDHb10GprO2okz829k2XH%2BzxVlJSxTYbts8n1nsRnm3VYKf6bo1Tv1BTjhV%2Bl%2BLAHqFFflzrlCIU5En%2B6y2K57FjusUDJFyzpGAS67PtWO2wDM7WhTAvb%2FtDsz8WyqCn7gvyKDvmgQXNQWQF8CLHXeYEuaeLAlLoJB9huOrwuoXG7QIUSFkc1aB0ddO8j9zHG8uc%2BTYHh6woc20uhSen0RDTMwbc%2BHmDy1t6lQja8qugUK9UiFOuP4Lfcif12KEU53%2BGj%2BBzSvf0EjhOlO2rfQO%2B1%2Bsp5mtL1Ju2JxfZiIEH1VfTzzZJpc2zogDC4xNS%2BBjqkAWzmbvhuMKG0uZFTWmYapZLkJxwhl0uSsvNbUn1N%2F4R7ptclcOA5I0yWx1Ygu%2FYUPv7UsbTmN5bAtdUv%2FzhfR6Zd16Kbxjj05oZzgxC9SvKIcMVMHytapwPjULwVoFUPtyxjfCo96yC%2FIFSldlKl5Mh6EIHGOAIWniVqki0y%2BjCdMEK%2BZS13XXeLQdV9QcvpxPrG24AvwPpOulRgJvb1WyjJabjq&X-Amz-Signature=11c98efee2ca5a09b2f9b056d2adb089810dedc8fad1af19c99886be2c3bc436&X-Amz-SignedHeaders=host&x-id=GetObject)

### 관련 개념 복습: 재귀 알고리즘의 비재귀적 표현

> 복습 지시
일단 한번 쉐도잉 하세요.
두 번째 코드를 그림으로 그리세요.

꼬리 재귀를 제거하기: recur() 함수의 맨 끝에서 재귀 호출하는 꼬리 재귀 recur(n- 2)함수의 의미는 ‘인수로 n-2의 값을 전달하고 recur() 함수를 호출하는 것’입니다. 따라서 이 호출은 다음 동작으로 바꿀 수 있습니다.

> n의 값을 n-2로 업데이트하고 함수의 시작지점으로 돌아갑니다. 

```python
def recur(n: int) -> int:
	"""꼬리 재귀를 제거한 recur()함수"""
	while n > 0: # 2. 함수의 시작 지점으로 돌아간다.(모로 가도 서울로 가면 된다)
		recur(n - 1)
		print(n)
		n = n - 2 # 1. n을 n-2로 업데이트하고
```

재귀를 제거하기: 꼬리 재귀와 달리 맨 앞에서 재귀 호출하는 recur(n-1) 함수는 제거하기가 쉽지 않습니다. 왜냐하면 n값을 출력하기 전에 recur(n-1)을 실행해야 하기 떄문입니다. 예를 들어 n값이 4인 경우 재귀 호출 recur(3)의 처리가 완료될 때까지 4를 어딘가에 저장해야 합니다.다시 말해 재귀 호출하는 recur(n - 1)을 제거하려면 다음과 같이 간단하게 바꿀 수 는 없다.

> n값을 n - 1로 업데이트하고 함수의 시작 지점으로 돌아갑니다. X!!!!

왜냐하면 현재의 n 값을 임시로 저장할 필요가 있기 때문입니다. 또한 recur(n-1)의 처리를 완료하고 n값을 출력할 때 임시로 저장했던 n을 꺼내 그 값을 출력해야 합니다. 이러한 문제는 스택으로 해결 가능. 

```python
from stack import Stack

def recur(n: int) -> int:
	"""recursion 없는 recursion 함수."""
	s = Stack(n)
	
	while True:
		if n > 0:
			s.push(n)
			n = n - 1 # 1. n을 n-1로 업데이트하고
			continue # 2. 함수의 시작 지점으로 돌아갑니다.
		if not s.is_empty() # n이 0 이하가 됐을 때, 스택 상단의 값을 하나 팝 합니다.
			 n = s.pop() 
			 print(n) # 그 값을 출력하고
			 n = n - 2 # n을 n-2로 업데이트하고 함수의 처음으로 돌아갑니다.
			 continue
		break
```

그림

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/267dd9f6-51ff-4616-b454-cae7044a8d0b/IMG_9879.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DITOMZI%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDanUt7YwGgjCtXdiCzU6REb8kLsDV9U62pXbWQmlelbAIhAIcOz60XpHtu4VFWoUQyHWGpnvB9J0qWOYadLi3aUReiKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7PtHmbRzaB%2BLhHzYq3APS4xfmtvT%2FtPB0C09yrQYEjDDAVUNhsaupkK8ILuwZlPSqDYX5gh7sguV9s1qhaJmFXfm5EJQYtKYSGlu74eRiw%2B88T0UFWIVo85x1nrU8bH99TSSRJy4Uc7RRoAfvpx%2BrXG1aVi8JdTlUVOeJXCaku4IE1RABgF6ffy3tRXW%2Fc%2ByKkZokFuT1cBsYNBYsA1rhtktIZqRkIdtGJM20lthmjfspP9YAsWLlQL6ZIVYYNj7uoZXxxZJx4opWKsctAiOiVukTQqBvi41hknqoIzmTyz%2Fu0pcvXDfxDACygyf7V1L0TeFYDVyIv1ljCRZDIsUPDHb10GprO2okz829k2XH%2BzxVlJSxTYbts8n1nsRnm3VYKf6bo1Tv1BTjhV%2Bl%2BLAHqFFflzrlCIU5En%2B6y2K57FjusUDJFyzpGAS67PtWO2wDM7WhTAvb%2FtDsz8WyqCn7gvyKDvmgQXNQWQF8CLHXeYEuaeLAlLoJB9huOrwuoXG7QIUSFkc1aB0ddO8j9zHG8uc%2BTYHh6woc20uhSen0RDTMwbc%2BHmDy1t6lQja8qugUK9UiFOuP4Lfcif12KEU53%2BGj%2BBzSvf0EjhOlO2rfQO%2B1%2Bsp5mtL1Ju2JxfZiIEH1VfTzzZJpc2zogDC4xNS%2BBjqkAWzmbvhuMKG0uZFTWmYapZLkJxwhl0uSsvNbUn1N%2F4R7ptclcOA5I0yWx1Ygu%2FYUPv7UsbTmN5bAtdUv%2FzhfR6Zd16Kbxjj05oZzgxC9SvKIcMVMHytapwPjULwVoFUPtyxjfCo96yC%2FIFSldlKl5Mh6EIHGOAIWniVqki0y%2BjCdMEK%2BZS13XXeLQdV9QcvpxPrG24AvwPpOulRgJvb1WyjJabjq&X-Amz-Signature=e3322135da638d6b48ea34bcd1087df1828325a764ef5af2ba004b3883c2e924&X-Amz-SignedHeaders=host&x-id=GetObject)



자, 이제 도식적으로는 이해 할 만큼 한 거 같다. 

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
			s.push(n)
			n = n - 1
			continue
		if not s.is_empty():
			n = s.pop()
			print(n)
			n = n - 2
			continue
		break
```

### 다른 사람의 풀이를 분석

> 책 쉐도잉. 뭔 말인지 전혀 모르겠다. 
그림을 그리면서 정리. 

코드: i 열에 퀸을 하나 배치하는 작업

```python
# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

pos = [0] * 8 # 각 열에서 퀸의 위치를 출력

def put() -> None:
	for i in range(8):
		print(f'{pos[i]:2}', end='')
	print()
	
def set(i: int) -> None:
	for j in range(8):
		pos[i] = j # 퀸을 j 행에 배치
		if i == 7: # 모든 열에 퀸의 배치를 종료
			put()
		else:
			set(i+1) # 다음 열에 퀸을 배치

set(0) # 0 열에 퀸을 배치
```

코드: 위에서 조건을 추가하여, 각 열에 하나의 퀸만 놓도록 하는 코드

```python
pos = [0] * 8
flag  = [False] * 8

def put() -> None:
    """print queens placed on each column"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    for j in range(8):
        if not flag[j]: # if flag is true, set function does nothing.
            pos[i] = j
            if i == 7:
                put()
            else: 
                flag[j] = True
                set(i+1)
                flag[j] = False

set(0)
```

> 이처럼 필요하지 않은 분기를 없애서 불필요한 조합을 열거하지 않는 방법을 한정(bounding)이라고 합니다. 분기 작업과 한정 작업을 조합하여 문제를 풀이하는 방법을 분기한정(branching and bounding mehod)라고 합니다.

여기에 대각선 조건만 추가하면 퀸 문제 해결.

```python
pos = [0] * 8
flag_a  = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put() -> None:
    """print queens placed on each column"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    for j in range(8):
        if( not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + 7]
           ):
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)
```



대각선 플래그가 이해가 안 된다. 아래 그림을 참고

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/061efcc5-eb21-424e-a204-afe0e5f1e953/IMG_9881.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DITOMZI%2F20250315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250315T075001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDanUt7YwGgjCtXdiCzU6REb8kLsDV9U62pXbWQmlelbAIhAIcOz60XpHtu4VFWoUQyHWGpnvB9J0qWOYadLi3aUReiKv8DCBAQABoMNjM3NDIzMTgzODA1Igy7PtHmbRzaB%2BLhHzYq3APS4xfmtvT%2FtPB0C09yrQYEjDDAVUNhsaupkK8ILuwZlPSqDYX5gh7sguV9s1qhaJmFXfm5EJQYtKYSGlu74eRiw%2B88T0UFWIVo85x1nrU8bH99TSSRJy4Uc7RRoAfvpx%2BrXG1aVi8JdTlUVOeJXCaku4IE1RABgF6ffy3tRXW%2Fc%2ByKkZokFuT1cBsYNBYsA1rhtktIZqRkIdtGJM20lthmjfspP9YAsWLlQL6ZIVYYNj7uoZXxxZJx4opWKsctAiOiVukTQqBvi41hknqoIzmTyz%2Fu0pcvXDfxDACygyf7V1L0TeFYDVyIv1ljCRZDIsUPDHb10GprO2okz829k2XH%2BzxVlJSxTYbts8n1nsRnm3VYKf6bo1Tv1BTjhV%2Bl%2BLAHqFFflzrlCIU5En%2B6y2K57FjusUDJFyzpGAS67PtWO2wDM7WhTAvb%2FtDsz8WyqCn7gvyKDvmgQXNQWQF8CLHXeYEuaeLAlLoJB9huOrwuoXG7QIUSFkc1aB0ddO8j9zHG8uc%2BTYHh6woc20uhSen0RDTMwbc%2BHmDy1t6lQja8qugUK9UiFOuP4Lfcif12KEU53%2BGj%2BBzSvf0EjhOlO2rfQO%2B1%2Bsp5mtL1Ju2JxfZiIEH1VfTzzZJpc2zogDC4xNS%2BBjqkAWzmbvhuMKG0uZFTWmYapZLkJxwhl0uSsvNbUn1N%2F4R7ptclcOA5I0yWx1Ygu%2FYUPv7UsbTmN5bAtdUv%2FzhfR6Zd16Kbxjj05oZzgxC9SvKIcMVMHytapwPjULwVoFUPtyxjfCo96yC%2FIFSldlKl5Mh6EIHGOAIWniVqki0y%2BjCdMEK%2BZS13XXeLQdV9QcvpxPrG24AvwPpOulRgJvb1WyjJabjq&X-Amz-Signature=d6950bb2a872a5a8b67bbbc73deaacd9cd63b1540a6b2c418029a0a5be3fa1b8&X-Amz-SignedHeaders=host&x-id=GetObject)

> 쉐도잉, 필사, 그림 따라 그리기를 동원해서 n-queen 문제를 읽기는 했다. 여전히 잘 모르겠다. branching and bounding이 중요한 키워드인 것은 알겠다.
학교 수업 때 쓴 교제를 다시 볼까? 

근데 일단 어떻게 푸는지는 다 알지 않아? 코드를 직접 생각하면서 문제를 구성해보는 것도 의미가 있을 거 같은데? 음…글쎄 일단 그런가? 아니면 다음 문제 한번 보고 돌아와봐

# 재귀: Z

## Phase1. Top Down.

```python
# 문제 읽기
# 첫째 줄에 정수 N, r, c가 주어진다.
# N > 1인 경우, 배열을 크기가 2^N-1 × 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때 r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 문제 풀기
# 문제 정의 
# 그렇게 어려울 거 같지 않은데, 일단 재귀 지식에 입각해서 수도코드를 작성해보자.

# 함수: 재귀(?): 뭐 하는 함수인데? 현재 위치가 i,j일때 다음 방문하는 좌표를 구하는 함수? 이게 작은 재귀를 다 한 다음 큰 재귀를 해야 함.
# 재귀로 넘어가는 값이 그러니까 사각형이어야 하는 거지. 
# (r1, c1, r2, c2)이걸 넘겨서 이 값이 정사각형 한 변의 길이가 2인 점들이 되면 방문을 하고, 그게 다 끝났으면? 
# 큰 사각형 하나를 줬을 떄 작은 사각형들로 나눠서 재귀를 하고, 베이스 컨디션은 2인 정사각형.
# endpoint에서 다음 사각형 start point로 가야지. 그리고 이건 항상 (r1, c1), (r2, c2)로 정해져있다.
# 하노이 문제랑 좀 비슷하다. 대신 재귀 안에서 재귀를 네번 순서대로 해야 할 거 같은데, 그지? ㅇㅇ

class rect:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2
    def __str__(self):
        return f'{self.r1, self.c1, self.r2, self.c2}'

def get_rect(pos, T: rect):
    half_r = (T.r1 + T.r2)//2
    half_c = (T.c1 + T.c2)//2
    if pos == 'A':
        return rect(T.r1, T.c1, half_r, half_c)
    if pos == 'B':
        return rect(T.r1, half_c, half_r, T.c2)
    if pos == 'C':
        return rect(half_r, T.c1, T.r2, half_c)
    if pos == 'D':
        return rect(half_r, half_c, T.r2, T.c2)
    

def recur(T: rect): # 사각형 하나가 주어졌을 때, T에 대한 A, B, C, D 사각형을 구해서 재귀
    global grid, cnt
    if abs(T.r1 - T.r2) == 2:
        for i in range(T.r1, T.r2):
            for j in range(T.c1, T.c2):
                # print(i, j)
                grid[i][j] = cnt
                cnt += 1
        return
    A = get_rect(pos='A', T=T)
    B = get_rect(pos='B', T=T)
    C = get_rect(pos='C', T=T)
    D = get_rect(pos='D', T=T)
    recur(A)
    recur(B)
    recur(C)
    recur(D)

# initial T must contain correct r, c ponits.
n, r, c = tuple(map(int, input().split()))
n = 2**n
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = rect(0, 0, n, n)
recur(T=initial_rect)
print(grid[r][c])
# for g in grid:
#     print(g)
```

실행 시간: 3.785085 초

시간 초과 발생. 제한시간은 0.5초로 굉장히 짧다. 대신 메모리가 크고. 스택을 이용해서 재귀를 없애야 하나?

```python

from collections import deque

s = deque()

class rect:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1
        self.c1 = c1
        self.r2 = r2
        self.c2 = c2
    def __str__(self):
        return f'{self.r1, self.c1, self.r2, self.c2}'

def get_rect(pos: str, T: rect):
    half_r = (T.r1 + T.r2)//2
    half_c = (T.c1 + T.c2)//2
    if pos == 'A':
        return rect(T.r1, T.c1, half_r, half_c)
    if pos == 'B':
        return rect(T.r1, half_c, half_r, T.c2)
    if pos == 'C':
        return rect(half_r, T.c1, T.r2, half_c)
    if pos == 'D':
        return rect(half_r, half_c, T.r2, T.c2)
    
def recur(T: rect):
    global grid, cnt
    while True:
        if abs(T.r1 - T.r2) == 2:
            # 현재 업데이트된 사각형이 충분히 작다면 방문을 한 다음 종료.
            for i in range(T.r1, T.r2):
                for j in range(T.c1, T.c2):
                    grid[i][j] = cnt
                    cnt += 1
            T = s.popleft()
            continue
        if s: 
            s.appendleft(get_rect('D', T))
            s.appendleft(get_rect('C', T))
            s.appendleft(get_rect('B', T))
            s.appendleft(get_rect('A', T))
            T = s.popleft()
            continue
        break

# initial T must contain correct r, c ponits.
n, r, c = tuple(map(int, input().split()))
n = 2**n
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = rect(0, 0, n, n)
s.appendleft(initial_rect)
recur(T=initial_rect)
print(grid[r][c])
```

실행 시간: 0.357471 초(n=10)

스택으로 구현은 성공했다. 제한시간 0.5초에 대해서도 훨씬 빠르다. 그런데도 시간 초과가 발생한다. 그럼 어디서 더 성능을 개선할 수 있을까? 일단 시간이 n에 영향을 많이 받는다. n이 11만 돼도 시간이 2초에 가까워진다. 

내 생각에 자료구조 문제는 아닐 거 같고 이터레이션 타임을 줄여야 한다. i, j를 모두 기록해서 찾는 대신, 빠르게 목적지까지 찾아가는 방법도 있을 거 같다. 스마트하게 하자 스마트하게. 그리고 get_rect도 없애는게 훨씬 맞겠다. 일단 get_rect 제거.

```python
  cd /Users/johyeonho/jungle-backjoon ; /usr/bin/env /Users/johyeonho/jungle-backjoon/.venv/bin/python /Users/johyeonho/.vscode/extensions/ms-python.debugpy-2025.4.1-darwin-arm
64/bundled/libs/debugpy/adapter/../../debugpy/launcher 53384 -- /Users/johyeonho/jungle-backjoon/BOJ1074.py 
10 512 512
786432
실행 시간: 3.463909 초
 {Bach} 🌎   ~/jungle-backjoon   main ±
  cd /Users/johyeonho/jungle-backjoon ; /usr/bin/env /Users/johyeonho/jungle-backjoon/.venv/bin/python /Users/johyeonho/.vscode/extensions/ms-python.debugpy-2025.4.1-darwin-arm
64/bundled/libs/debugpy/adapter/../../debugpy/launcher 53416 -- /Users/johyeonho/jungle-backjoon/BOJ1074.py 
10 512 512
786432
실행 시간: 2.683325 초

```

rect 클래스를 제거하고 정보를 리스트로 넘기니 거의 1초가 줄어들긴 했다! 이제 이터레이션을 수정해서 순서를 알 필요가 없는 세부 사각형의 헤드에 진입한 경우 그냥 지나가도록 하자. 그 로직은 어떻게 만들지?

```python

from collections import deque
import time

start_time = time.time()  # 시작 시간 기록

s = deque()

def recur(T: list):
    global grid, cnt, r, c
    while True:
        if T[2] - T[0] == 2:
            # 아래 이터레이션 자체를 경우에 따라 스킵하려면? 
            if r in range(T[0], T[2]) and c in range(T[1], T[3]):
                for i in range(T[0], T[2]):
                    for j in range(T[1], T[3]):
                        grid[i][j] = cnt
                        cnt += 1
                break
            else: 
                print('pass')
                cnt += 4
            T = s.popleft()
            continue
        if s: 
            half_r = (T[0] + T[2])//2
            half_c = (T[1] + T[3])//2
            s.appendleft((half_r, half_c, T[2], T[3]))
            s.appendleft((half_r, T[1], T[2], half_c))
            s.appendleft((T[0], half_c, half_r, T[3]))
            s.appendleft((T[0], T[1], half_r, half_c))
            T = s.popleft()
            continue
        break

# initial T must contain correct r, c ponits.
n, r, c = tuple(map(int, input().split()))
n = 2**n
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = (0, 0, n, n)
s.appendleft(initial_rect)
recur(T=initial_rect)
print(grid[r][c])
```

그냥 어펜드를 시킬 때도, 그 순회하는 인덱스가 의미가 있을 것인지 없을 것인지 미리 판단해서, 필요 없으면 그냥 그대로 카운터만 올려버리면 안 되나

```python

from collections import deque
import time

start_time = time.time()  # 시작 시간 기록

s = deque()

def recur(T: list):
    global grid, cnt, r, c
    while True:
        edge = T[2] - T[0]
        if edge == 2:
            # 아래 이터레이션 자체를 경우에 따라 스킵하려면? 
            if r in range(T[0], T[2]) and c in range(T[1], T[3]):
                print('arrive')
                for i in range(T[0], T[2]):
                    for j in range(T[1], T[3]):
                        grid[i][j] = cnt
                        cnt += 1
                break
            else: 
                print('pass')
                cnt += 4
            T = s.popleft()
            continue
        if s: 
            half_r = (T[0] + T[2])//2
            half_c = (T[1] + T[3])//2

            D = (half_r, half_c, T[2], T[3])
            C = (half_r, T[1], T[2], half_c)
            B = (T[0], half_c, half_r, T[3])
            A = (T[0], T[1], half_r, half_c)

            s.appendleft(D)
            s.appendleft(C)
            s.appendleft(B)
            s.appendleft(A)
            T = s.popleft()
            flag = True
            while flag:
                edge2 = T[2] - T[0]
                if r in range(T[0], T[2]) and c in range(T[1], T[3]):
                    print('found: ', T)
                    flag = False
                else: # 없다면 버리고 다시 팝.
                    print("pass: ", T)
                    print('edge: ', edge2)
                    cnt += 2**edge2 
                    print("cnt update:")
                    T = s.popleft()
            continue
        break

# initial T must contain correct r, c ponits.
n, r, c = tuple(map(int, input().split()))
n = 2**n
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
cnt = 0
initial_rect = (0, 0, n, n)
s.appendleft(initial_rect)
recur(T=initial_rect)
print(grid[r][c])
```

딱 생각했던 구현. 하지만 여전히 시간 초과. 유의미한 차이가 없다. 그리드를 안 쓰고 카운터만 쓰면? 그래도 n^2는 변함 없음. 시간초과 날 거임. 

## Phase2. Bottom up

이 코드는 Z-모양으로 2차원 배열을 순회하는 문제(즉, Z-분할 정복)를 해결하는 방식인데, 현재 BFS 스타일의 큐(deque)와 루프를 사용하여 해결하고 있습니다.

하지만 시간 최적화가 필요한 몇 가지 문제가 있습니다.

🔥 개선할 수 있는 주요 부분

1.	불필요한 while 루프 제거 → 재귀 방식으로 개선

2.	deque의 활용 방식 변경 → 큐를 활용하는 방식이 최적화되지 않음

3.	불필요한 if 조건문 최소화

4.	배열 전체를 사용하지 않고 단순히 카운트만 유지하도록 변경

🚀 최적화된 코드

```plain text
def recur(n, x, y, cnt):
    """Z-분할 정복을 이용한 탐색 최적화"""
    if n == 2:  # Base case: 2x2 크기일 때 직접 채우기
        if x == r and y == c:
            print(cnt)
            exit()
        cnt += 1
        if x == r and y + 1 == c:
            print(cnt)
            exit()
        cnt += 1
        if x + 1 == r and y == c:
            print(cnt)
            exit()
        cnt += 1
        if x + 1 == r and y + 1 == c:
            print(cnt)
            exit()
        return

    half = n // 2  # 현재 크기의 절반
    if r < x + half and c < y + half:  # A (좌상)
        recur(half, x, y, cnt)
    elif r < x + half and c >= y + half:  # B (우상)
        recur(half, x, y + half, cnt + half * half)
    elif r >= x + half and c < y + half:  # C (좌하)
        recur(half, x + half, y, cnt + 2 * half * half)
    else:  # D (우하)
        recur(half, x + half, y + half, cnt + 3 * half * half)

# 입력 받기
n, r, c = map(int, input().split())
n = 2 ** n  # 2^n 크기의 배열
recur(n, 0, 0, 0)  # Z-모양 탐색 시작
```

🔥 최적화된 코드의 장점

✅ 1. deque와 반복문 제거 → 재귀로 개선

•	원래 코드에서는 큐(deque)를 사용하면서 불필요한 while 반복이 발생했습니다.

•	재귀 호출을 사용하면 큐를 사용할 필요가 없고, 불필요한 요소를 저장하지 않아 메모리 사용량도 줄어듭니다.

✅ 2. grid 배열을 없애고 카운트만 유지

•	원래 코드는 전체 배열을 만들고 cnt 값을 저장했는데, 이는 불필요한 메모리 낭비입니다.

•	정확한 위치에서만 cnt를 계산하면 배열을 만들 필요 없이 해결할 수 있습니다.

✅ 3. 불필요한 if 조건문 최소화

•	원래 코드에서는 불필요한 if r in range(...) and c in range(...) 같은 조건문이 많았습니다.

•	개선된 코드에서는 위치에 따라 한 번만 if-elif로 분기 처리하여 효율성을 높였습니다.

✅ 4. 시간 복잡도 개선

•	원래 코드의 최악의 경우 시간 복잡도: O(n^2) (큐에서 모든 영역을 검사)

•	개선된 코드의 시간 복잡도: O(log(n)^2) (분할 정복 사용)

🚀 결론

✅ 기존 코드의 문제점

•	큐(deque)를 사용하여 비효율적인 반복 수행

•	grid 배열을 유지하여 불필요한 메모리 사용

•	탐색 과정에서 if 문이 너무 많아 실행 속도 저하

✅ 개선된 코드의 장점

•	Z-분할 정복 사용 → 큐 제거 및 메모리 최적화

•	배열을 유지하지 않고 직접 cnt를 계산하여 공간 절약

•	**시간 복잡도 개선 (O(log(n)^2))**으로 더 빠름

이제 훨씬 효율적으로 수행시간을 줄일 수 있습니다! 🚀

# 정렬: 수 정렬하기 2

## Phase1. Top Down

https://www.acmicpc.net/problem/2751

N(1 ≤ N ≤ 1,000,000)

```python
import heapq

heap = []

n = int(input())

for i in range(n):
    d = int(input())
    heapq.heappush(heap, d)

while heap:
    print(heapq.heappop(heap))

```

시간초과.

## Phase2. Bottom Up

입력을 다음과 같이 변경해야 시간 안에 풀 수 있음. 시간초과는 해결됨.

```python
import heapq
import sys

heap = []

n = int(sys.stdin.readline().strip())  # 빠른 입력

for i in range(n):
    d = int(sys.stdin.readline().strip())  # 빠른 입력

    heapq.heappush(heap, d)

while heap:
    print(heapq.heappop(heap))

```

# 완전탐색: 차이를 최대로 만들기

https://www.acmicpc.net/problem/10819

## Phase1. Top Down

```python

n = int(input())
arr = list(map(int, input().split()))
max_val = 0

def update_max(new_val):
    global max_val
    if new_val > max_val: max_val = new_val

def pick(i, A):
    if(i == n): 
        update_max(calc(A))
        return
    for idx in range(n): 
        if arr[idx] not in A:
            pick(i + 1, [*A, arr[idx]])

def calc(A):
    tmp = 0
    for i in range(1, n):
        tmp += abs(A[i-1] - A[i])
    return tmp

pick(0,[])  
print(max_val)
```

눈으로 확인되는 문제는 없는데, 제출하면 오답으로 뜸. 문제가 되는 테스트 케이스가 있는 것으로 보임.

테스트케이스를 어떻게 찾지?

일단 값의 범위

n개의 정수로 이루어진 배열을 짝지었을 때 그 차의 절대값의 합이 최대가 되는 경우.

3 ≤ n ≤ 8

-100 ≤ d ≤ 100

```python

import sys
MAX_INT = sys.maxsize

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

max_val = -MAX_INT

def pick(i, A):
    global max_val
    if(i == n): 
        val = calc(A)
        max_val = val if val > max_val else max_val
        return
    for idx in range(n): 
        if arr[idx] not in A:
            pick(i + 1, [*A, arr[idx]])

def calc(A):
    tmp = 0
    for i in range(1, n):
        tmp += abs(A[i-1] - A[i]) # | A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
    return tmp

pick(0,[])  
print(max_val)
```

문제 발견!

수열이 전부 다른 값인줄 알았는데, 아니었다. 같은 값이 있으면 not in A 로직 때문에 추가가 안 된다.

## Phase2. Bottom Up



# 정렬: 단어 정렬

## Phase1. Top Down

https://www.acmicpc.net/problem/1181

```python
# # 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 
# # 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.


# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys

words = []
wordset = []
n = int(sys.stdin.readline().strip())
# input 
for _ in range(n):
    word = sys.stdin.readline().strip()
    if word not in wordset:
        words.append([word, len(word)])
        wordset.append(word)

words.sort(key=lambda x: (x[1], x[0]))

for word in words:
    print(word[0])
# 그래서 뭐 해야 하는데? 하나만 남기고 제거하는 걸 먼저 생각해야겠는데? 
# 하나만 남기고 제거 어떻게 해?
```

바로 해결. 따로 더 볼 내용은 없을 거 같음.


# 정렬: 수 정렬하기 3

https://www.acmicpc.net/problem/10989

난이도-중 

> n 개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램을 작성하시오
N(1 ≤ N ≤ 10,000,000)
둘째줄부터는 N줄에 거려서 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수다. 
각 수의 범위: 10000보다 작거나 같은 자연수. 

분석: 위의 수 정렬하기 2 문제와 비교했을 때 n이 10배 더 크다. 자연수라는 조건이 있으니까 기수정렬 쓰면 될 거 같은데, 사실 기수정렬이 기억이 안 난다.

아래 코드는 수 정렬하기 2에서 썼던 코드 그대로다. 이대로 제출하면 메모리 초과 에러가 난다. 기수정렬은 메모리를 더 쓰지 않나? 일단 

```python
import heapq
import sys

heap = []

n = int(sys.stdin.readline().strip())  # 빠른 입력

for i in range(n):
    d = int(sys.stdin.readline().strip())  # 빠른 입력

    heapq.heappush(heap, d)

while heap:
    print(heapq.heappop(heap))

```

