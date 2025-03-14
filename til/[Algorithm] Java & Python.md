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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=6268f9037bab267b8583ea3f5df2b13caa3f910b0a43a0c89d3600eb7fbcc1ad&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/005964d6-917a-4d21-bede-ff8ab6a4e978/IMG_9871.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=3283e221dc62d4c1dcbc6209c7067210e6c99189377fe0897d68b47f7aacc086&X-Amz-SignedHeaders=host&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a82a3eec-e72a-40bb-87cb-8327c5cc36b1/IMG_9872.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=5ac658b598981e978edd108d9a197742d048ee7bf1ddbb73fabc36ad81b4e622&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/ef6a62d5-e03d-40cc-88e9-b4e6fb30c8d3/IMG_9873.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=ca829d1eecf977342d1cb4931ae434795b9c1dfec608e74aeefc9b966dfc7b52&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a1fda402-9322-4b73-b569-596a90f192eb/IMG_9874.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=7e3f89cebc64ce6867f46705303f9b3fabf5ff843207e1470dd0deb923c13262&X-Amz-SignedHeaders=host&x-id=GetObject)

- 유클리드 호제법
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/899122bf-a705-49f5-94ca-91e8cedab38e/IMG_9875.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=048581d0af3fb896d355406cb9eb551142f76223e146d0e69e3cee32375ded54&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/61ada9d6-0300-477b-8faf-1933c1296dea/IMG_9876.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBSQGNNY%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsjjtZ6ayO1AVeKssSJOiCbVSRoSzUn5XUcweiUvOBMAiEAwxvUOD5b0iYkQl81cOrNXPfc86z7zqq%2Fx1O4jeFaeSIqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCC4v4IL4qSHtiAQUircA2bELN03MZv4S0lVdNClfBllX9CO256fLMrkfdZ%2BfRLHlcn%2Fcl%2FkOqY2l%2FtBtalPzBOk4cE7pFJVz0yuBXoDlctmbdDD0OymAnYC%2BdRf1JA2I%2F5vVgS%2BBrqk5Ptp6MmFcRqefekt6mOTLmS%2FyxyPCnGtUl6dOwvLp8vt0rh6gA5BV5Sza9mwZpMUr9CcwE8nGHZ71c%2B2B1o%2F1iibt5pUW%2FR8H85%2BpwLOnvsE2nvGZDV%2BVHqj1fAPjL5ohT1P8e2rxYyGqTSmQAOvOszKnPODMEiceRIv6XKG7hWzhM8ygyoh%2BcQ7kGqkCJT%2FBWfKEAmhHpc7PWf4Qu8rJJQi5VpaDCrAtly6imJqdRnnGRLm6DU6WdTNFHd1RSllghS4PvCekOOJm4BqDGySpe%2FbOizd8Tmeb1ZGKqlTljfu6dQnuuF5%2Bhf9u0nuf6A7pDUPTeyD5B4tf0XqGBM9xpVdzyXWaCjfEk8IvWChhXl73sSyZ1AIjwE9q0S1EsnMjx8W1XczSb22atumIdVszBxf5py8Uc6euOwaLMvwAbd6n685JzHycrRhpBZhu2iAm4OtMwyUYv9TKQVpVhyU7LilatFmFf6yYU%2FKMDkZ%2BHGAMK7olprg1DI8Tep6mcz81DTkMPXu0r4GOqUBKhpjhwUDoIJITFOyCb15A%2Fs4J18IpupMyDX7y73No%2F5ETZUjVnNXEA0Zh8X1Hgo6hnnUtTnFDROY5DLS6PwtNGNZ9AQFgALHEJbj2KrKKSz8OJ44z3EToyRzO4iumy8gUvAJjomIigLJ5PAxSb5DRWLte8NWz5qDO8Gj8aXzb2%2FUGuS0s6NW3y5h8sqW1Gw89A%2F7v5IueZBzQ8hAaTHG0qSgXHtm&X-Amz-Signature=bdec50795de188a131af7994408a7da2ebb614cc85629cd2131f0d60f8cc6003&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/b1769365-105f-46de-b9a9-3de7d23c5e8a/IMG_9877.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPE3XXUC%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5jPVzbGfIufq5kEoyPCBTdXZLyRKuMMHN684f4O6wUgIgSBcxNT8ycUf0m4lC65GEy%2FOq12b6vx2AG9mGNgmXTHUqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCuvD8BYT22%2FPagaqCrcAyU6yEkpU1aGPTBhScgWbWaY5ahqFjwINpnt%2F8YXpZcPbJnoub7WtXbkXjC%2BqjeWIA3Ow1svzUU7oI61pj46%2Fq6zDk6LR7NP%2B9SJaXWEKfb0G4HbKBIPQThi6nEKerKSdSo6nNMSHn8RxkguDxpBchlOWBDSdOMva1SuRV2qy0AS13uMhtMQi1%2FioHSvO2Rlen9xKn34pGbFO%2BNP6Rl3RFBwqOrxIjPyL1%2FCAB%2BiPWNx%2B1yPGe8UBktSjRkvlRTwqUfJb%2Fsr2G6eBmsPgCpM2jbHhKithAUtgo8YJAN1oKk4nIUJP6N8Va6xbWBEQoWV%2Bv1Pux3j87VHejR1gOzcmmPJssjQryX%2F%2BYlIbeRYO%2Bq%2FlTawEW256GAb7l4SRWivFN8IrP%2FK7pw%2BJKEPaLOTKcEPTtLKZAjDrl46AKKNtN22bhL3QzRIMllG2RT8L70jWZHR6Mc4PZX3G4KhpMGfVPJ1aRPjuWeDR02ebz%2FmFbccndVwJ46OogUQoiEDj%2FABWn7HQspJFw%2FJ7zuK91H9P0uS5gDjHrgMcSNwJ6mU6KoL%2B0gejpqXinvw4UaoBgPQa2dlk973XRA9jEtcw0M9HRAKlaOjsS3mFpRa8s97quzFlGbGGtN79YgaUN%2BsMPbu0r4GOqUBMOPn4Zpp%2Bl%2BpaHmWBthPsHMY9F5GiX14vbWXg986BtvYHpUWMXrwpiZT4mg6RWwe50dqPFXLXw0LYjSdIjTTimIVG456qNXY2GQ0wkEEs%2FHNJnbRlSOvbMTXt8VdKcxc%2BUI2FKXts8whTYr%2BDDghSNlpUbKTuMnH%2Fz3cEeWqNrryuBFLEUb%2B7%2FkoDUQEVfHtztULgzdO8AjgCRebpbbIbUttLgHw&X-Amz-Signature=0f30f3266be6534cc3c440c1f806ae13b5bc385e2f65ca5720b7f9cb744bf958&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/0c1839b9-722b-4eaa-a55f-4bfea7bf1cd5/IMG_9878.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPE3XXUC%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5jPVzbGfIufq5kEoyPCBTdXZLyRKuMMHN684f4O6wUgIgSBcxNT8ycUf0m4lC65GEy%2FOq12b6vx2AG9mGNgmXTHUqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCuvD8BYT22%2FPagaqCrcAyU6yEkpU1aGPTBhScgWbWaY5ahqFjwINpnt%2F8YXpZcPbJnoub7WtXbkXjC%2BqjeWIA3Ow1svzUU7oI61pj46%2Fq6zDk6LR7NP%2B9SJaXWEKfb0G4HbKBIPQThi6nEKerKSdSo6nNMSHn8RxkguDxpBchlOWBDSdOMva1SuRV2qy0AS13uMhtMQi1%2FioHSvO2Rlen9xKn34pGbFO%2BNP6Rl3RFBwqOrxIjPyL1%2FCAB%2BiPWNx%2B1yPGe8UBktSjRkvlRTwqUfJb%2Fsr2G6eBmsPgCpM2jbHhKithAUtgo8YJAN1oKk4nIUJP6N8Va6xbWBEQoWV%2Bv1Pux3j87VHejR1gOzcmmPJssjQryX%2F%2BYlIbeRYO%2Bq%2FlTawEW256GAb7l4SRWivFN8IrP%2FK7pw%2BJKEPaLOTKcEPTtLKZAjDrl46AKKNtN22bhL3QzRIMllG2RT8L70jWZHR6Mc4PZX3G4KhpMGfVPJ1aRPjuWeDR02ebz%2FmFbccndVwJ46OogUQoiEDj%2FABWn7HQspJFw%2FJ7zuK91H9P0uS5gDjHrgMcSNwJ6mU6KoL%2B0gejpqXinvw4UaoBgPQa2dlk973XRA9jEtcw0M9HRAKlaOjsS3mFpRa8s97quzFlGbGGtN79YgaUN%2BsMPbu0r4GOqUBMOPn4Zpp%2Bl%2BpaHmWBthPsHMY9F5GiX14vbWXg986BtvYHpUWMXrwpiZT4mg6RWwe50dqPFXLXw0LYjSdIjTTimIVG456qNXY2GQ0wkEEs%2FHNJnbRlSOvbMTXt8VdKcxc%2BUI2FKXts8whTYr%2BDDghSNlpUbKTuMnH%2Fz3cEeWqNrryuBFLEUb%2B7%2FkoDUQEVfHtztULgzdO8AjgCRebpbbIbUttLgHw&X-Amz-Signature=abe92963745917fcacd7965eb324a43a2927c7e410ed5fd72df9918356788a07&X-Amz-SignedHeaders=host&x-id=GetObject)

### 관련 개념 복습: 재귀 알고리즘의 비재귀적 표현

꼬리 재귀를 제거하기: recur() 함수의 맨 끝에서 재귀 호출하는 꼬리 재귀 recur(n- 2)함수의 의미는 ‘인수로 n-2의 값을 전달하고 recur() 함수를 호출하는 것’입니다. 따라서 이 호출은 다음 동작으로 바꿀 수 있습니다.

> n의 값을 n-2로 업데이트하고 함수의 시작지점으로 돌아갑니다. 

```python
def recur(n: int) -> int:
	"""꼬리 재귀를 제거한 recur()함수"""
	while n > 0:
		recur(n - 1)
		print(n)
		n = n - 2
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
			n = n - 1
			continue
		if not s.is_empty() 
			 n = s.pop()
			 print(n)
			 n = n - 2
			 continue
		break
```

그림

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/267dd9f6-51ff-4616-b454-cae7044a8d0b/IMG_9879.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPE3XXUC%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC5jPVzbGfIufq5kEoyPCBTdXZLyRKuMMHN684f4O6wUgIgSBcxNT8ycUf0m4lC65GEy%2FOq12b6vx2AG9mGNgmXTHUqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCuvD8BYT22%2FPagaqCrcAyU6yEkpU1aGPTBhScgWbWaY5ahqFjwINpnt%2F8YXpZcPbJnoub7WtXbkXjC%2BqjeWIA3Ow1svzUU7oI61pj46%2Fq6zDk6LR7NP%2B9SJaXWEKfb0G4HbKBIPQThi6nEKerKSdSo6nNMSHn8RxkguDxpBchlOWBDSdOMva1SuRV2qy0AS13uMhtMQi1%2FioHSvO2Rlen9xKn34pGbFO%2BNP6Rl3RFBwqOrxIjPyL1%2FCAB%2BiPWNx%2B1yPGe8UBktSjRkvlRTwqUfJb%2Fsr2G6eBmsPgCpM2jbHhKithAUtgo8YJAN1oKk4nIUJP6N8Va6xbWBEQoWV%2Bv1Pux3j87VHejR1gOzcmmPJssjQryX%2F%2BYlIbeRYO%2Bq%2FlTawEW256GAb7l4SRWivFN8IrP%2FK7pw%2BJKEPaLOTKcEPTtLKZAjDrl46AKKNtN22bhL3QzRIMllG2RT8L70jWZHR6Mc4PZX3G4KhpMGfVPJ1aRPjuWeDR02ebz%2FmFbccndVwJ46OogUQoiEDj%2FABWn7HQspJFw%2FJ7zuK91H9P0uS5gDjHrgMcSNwJ6mU6KoL%2B0gejpqXinvw4UaoBgPQa2dlk973XRA9jEtcw0M9HRAKlaOjsS3mFpRa8s97quzFlGbGGtN79YgaUN%2BsMPbu0r4GOqUBMOPn4Zpp%2Bl%2BpaHmWBthPsHMY9F5GiX14vbWXg986BtvYHpUWMXrwpiZT4mg6RWwe50dqPFXLXw0LYjSdIjTTimIVG456qNXY2GQ0wkEEs%2FHNJnbRlSOvbMTXt8VdKcxc%2BUI2FKXts8whTYr%2BDDghSNlpUbKTuMnH%2Fz3cEeWqNrryuBFLEUb%2B7%2FkoDUQEVfHtztULgzdO8AjgCRebpbbIbUttLgHw&X-Amz-Signature=3a9fb80a69d132114ee941c221c782fdaa8feed0b9f86de81fdecd3bdfb969de&X-Amz-SignedHeaders=host&x-id=GetObject)



오케이 이까지 다 정리하긴 했는데 무슨 소린지 하나도 모르겠다. 다음으로 할 일: 각 코드에 관한 상향식/하향식 분석을 그림으로 그리기. 근데 이거는 더 이상 머리가 안 돌아가니까 내일 합시다.



# 완전탐색: 차이를 최대로 만들기

```python

```

