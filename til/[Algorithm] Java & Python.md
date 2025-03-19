# [Algorithm] Java & Python



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 

> Phase1은 문제 읽기, 조건 리스트업, 직접 풀어보기, 구현하기 

> 알고리즘 트러블 슈팅 템플릿: 입력값 범위 확인, 추측, 복잡도 분석



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

![](./images/Screenshot_2025-03-03_at_5.30.53_PM.png)

![](./images/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=6c97d6e4a9f19e99e22785a391844065859c2be74642427e02ec41a7120c6d34&X-Amz-SignedHeaders=host&x-id=GetObject)

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
이 문제의 경우 재귀 실행 스택을 이해하고 나니 한결 이해됨.

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

![](./images/IMG_9871.heic)

![](./images/IMG_9871.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=87ab67e9b8e7403f7a89fee840e6c1867a43796db57e356eedf28148a1f2db59&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9872.heic)

![](./images/IMG_9872.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=102c8b7b543592cdb3b580958f8337f24cab343b0d623edb5d515afc32299dca&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9873.heic)

![](./images/IMG_9873.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=88161fb7ee911424b09dfeb0c291896fa17972350ef045b297098d7f13aca4c4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![](./images/IMG_9874.heic)

![](./images/IMG_9874.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=239d3d25a5388949f1e559bc4c5c085da2da26a5038737b1f193d29cb4d18c8d&X-Amz-SignedHeaders=host&x-id=GetObject)

- 유클리드 호제법
![](./images/IMG_9875.heic)

![](./images/IMG_9875.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYQ537YQ%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC6U%2FJiu%2FW85zyhTpJSSOojn0DeFjg69tg46iPENic8MAIgNSIxNLsHv4CdMYIhn6IMLh%2F%2FjVJKtAIpFREOwcujHfIq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDM7GOtQmtj73ob73oSrcA10%2BAUUn1yR3MhOgBxh%2FSpsr%2B8J1SzfD3yf78Zf0y5q3SZbzax5FDBA%2F91iPbYefD%2FV7AnLarc7s3oUpsDGY%2BwWp91%2B9iROPGqodATu2tnNXxl%2FiuPNtwyuOBtNA6JCe1XwppAKokWmbcfMAfUD9cuZrvVYob2Gx5mG3ajFqtCx12qLp433N%2BUQMc%2B1i6TMniB0io%2FjbmpYNU%2FpAgxIHdgTHOCWBCeG4xigfaPr8hhjHADmYG5IPqjCrEGncfMmcPw7g0QYCeeBfk8bC2zyohpqf4fXkjW8NBwMtNVARJFgau%2FmmU6mE8iOMAK%2B4ubAJlw7oQor9eCUhW4q9hjMz2RsYKH3Da9kzOHNRK8ABRqIGmvdTIeQBYDuT1yyUN7odVJ9LWDrDjMvJcsLY82Ijbw2IPPJmhcx2LuG2bYkvmk7Mr7DM4M0OgGpJOP%2Bl3yyjYSynDhG5KDGQdfaa1MG3WIQ6ijePGQfIdls6X9rw3j8THg4owQR1c1tdL%2BcdtcOyl%2BigUYDaS5yyHm7S12Evg9wduBE4VWViEMZkX5YXBsOGNj1s5fxlRV0UCJ0PT6JfM%2BU7QX%2FGYUrWeoH0dI%2BvLS8R52Y%2BcOukLto9e94lNy22XQfsZDnhdkOrbxhuMOqx574GOqUBsf2HBrGAfn%2FJF3I5I9FXoI5s%2FiM5%2FVx2LqmltM1PnO%2BhKUjephjyUOyaVATfe%2FV2T5lSqIV%2FcVypXZKf3W0hH%2BT8RnkmObiJcGoXqnvvg7y0uhI0MYKl7l2kfk2Bdq8yLzzgbi82o%2BE1AyYabqsz1GDQv8q2oel9nlf8syabQUA3K74aHYVDzDI6icAU%2BbhTjRYcsf9gIMhyc48F3v4c%2FtnaQDtO&X-Amz-Signature=566635a15afb9d6d396ce01638feac8c20e744692e153735120aae7dd4fb0aa3&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9876.heic)

![](./images/IMG_9876.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=9ab79a176980c35cb255c37d54f5879a9eb9b39302aefbaf9a71d0f12aa51120&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9877.heic)

![](./images/IMG_9877.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=eb532c40f5c39b8de63a1a0dd328bd16d11444fc89fb0dcfe61aeac80a812395&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9878.heic)

![](./images/IMG_9878.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=e248e4ac76a0962628edc91446276ffea81b610051fcdf52041f9d5ecd8ab9d0&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](./images/IMG_9879.heic)

![](./images/IMG_9879.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=1f90f250c8d50c0946bb78e0e2e8a5e4290f940a0f87503671d4b240058dcf07&X-Amz-SignedHeaders=host&x-id=GetObject)



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

![](./images/IMG_9881.heic)

![](./images/IMG_9881.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=7e5344b40cbee86799c25af43b24f0964b23bd59b532385092e4ccd7ce0d9f6c&X-Amz-SignedHeaders=host&x-id=GetObject)

> 쉐도잉, 필사, 그림 따라 그리기를 동원해서 n-queen 문제를 읽기는 했다. 여전히 잘 모르겠다. branching and bounding이 중요한 키워드인 것은 알겠다.
학교 수업 때 쓴 교제를 다시 볼까? 

근데 일단 어떻게 푸는지는 다 알지 않아? 코드를 직접 생각하면서 문제를 구성해보는 것도 의미가 있을 거 같은데? 음…글쎄 일단 그런가? 아니면 다음 문제 한번 보고 돌아와봐

## Phase3. 역시 알고리즘은 직접 풀어야지

### 그림: 수도코드 및 풀이 내용

![](./images/IMG_9900.heic)

![](./images/IMG_9900.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=d1b2aaa7a7de4f955f91dd2cad9ffc1de5764bca68e0200797819e6e679b347e&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9901.heic)

![](./images/IMG_9901.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=5f2ab353d21584805159241ec3e759c37f563fac015fd26dcb8c4eb8417ea272&X-Amz-SignedHeaders=host&x-id=GetObject)

![](./images/IMG_9902.heic)

![](./images/IMG_9902.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYZ5MHJF%2F20250319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250319T003719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIAkbMwJZODRD1dpwrZ4hwr24%2F%2BFLqqIObmKycwpZAoFjAiAIWbSx26xAkLnB%2FDBcDc7R9oKEim4y%2F%2FaefS1dXeOxtyr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM8VgEvKIG7GnkDjVIKtwDC1%2F%2FC3yViaHPjiDXNpj8Br7KbQJvnu3YhgNQMNQtwXKU5pBYqqIFKC3mG8nKracTiyhY5DiHL5Mni9u4T4FPzXc8gTCaaBkxQlMhgm50tOBlElD7sWnTeYtJ7x9APHvn%2FR1CDT7g1BbMvivp5erdoM%2FPrc0k3L%2ByWGN1VtbOLcX8rTrJEZWLc5Td2GfT2nfdp7ldyKYVufkaH1ByrvyHGsDzvite%2FgLBZOjd7lSkV2cCRbu6xA6rQc4W4Bh4uYOnsH%2Fgltu%2BFTMwF10xztALFhEfBEzS%2FOY%2FxvVtvIyZHWt3tjWnVrYgiQv2SVPL6kx9AJ3yYyfzgS60ckSM1TdcbPghkqfw5zZVAdhAI9x4Cyq1KOyyBLneflWxFjabT9gC6sTdFrWzMSFkuyZO2v0BhgFWdnWSuDZKgioQXwUavMwCDuth%2FaJCbOQYCtyhF8cmn5q2wd2s5jfCCMm0K4QKUCkM%2BOmJeGzcKbDbZs5NyhCEQquhViY2xXZiB5JrjlO%2BDnxBy%2BbHaOvZB7cJUndaKyTqdmqCA%2F%2Be5SdqC3Qz%2FcX5vIIJAb0akebxNz7XHei6DWV046HlleT50dbrspb0%2FiWPnAV%2FkyS%2FL%2BvnPCUheVONgfiZ1Gnsb71a7v4w2rDnvgY6pgHfTcN%2B08J4QDSdT1AeomjM%2BbHQ%2BIp0Vwzf5DhSsTSoa%2F6iL8il8cjE%2FQGP2%2F6Dy7xxeQF04CnOIf3pkn1yqAV9OXpEdvDeeFLCwaP9RucKeV9CLxs%2Fg7EYEGa3SRz3pfqaJgGUc2fRigkizmgmGak3VqibCTRWMwR1mpQmXIJFDy8Q4pGVGR3B9zjt5plJKaYJ%2Brkb9yn2hiAVLehAN4Uzs83vjp4V&X-Amz-Signature=9083215f94952a3540c83acee291c69938de26a5219c9894dfed1fb5354675aa&X-Amz-SignedHeaders=host&x-id=GetObject)

### 코드:  2트

```python

import sys

n = int(sys.stdin.readline().strip())

flag_a = [False for _ in range(n)]
flag_b = [False for _ in range(2 * n - 1)]
flag_c = [False for _ in range(2 * n - 1)]

Queens = [None for _ in range(n)]
cnt = 0

def recur(i):
    global cnt
    for j in range(n):
        if (flag_a[j] == False
            and flag_b[i+j] == False
            and flag_c[n - 1 + i - j] == False
            ):
            Queens[i] = j
            if i == n:
                cnt += 1
                continue
            flag_a[j] = True
            flag_b[i+j] = True
            flag_c[n - 1 + i - j] = True
            recur(i + 1)
            flag_a[j] = False
            flag_b[i+j] = False
            flag_c[n - 1 + i - j] = False

recur(0)
print(cnt)
```

제대로 결과가 안 나오는데, 이거는 답 안 보고 디버깅 해야 할 필요가 있음. 중단점 ㄱㄱ

디버깅 결과 베이스 컨디션에서 인덱스와 사이즈를 잘못 비교한 문제였음 i == n을 i == n-1로 고쳐서 해결

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

그냥 어펜드를 시킬 때도, 그 순회하는 인덱스가 의미가 있을 것인지 없을 것인지 미리 판단해서, 필요 없으면 그냥 그대로 카운터만 올려버리면 안 되나. 일단 stack으로 풀면 풀린다고 함.

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

## Phase2. 힌트 풀이 및 정답 분석

카운터만 증가시켜라. 30분동안 고민해보고, 또 안 되면 그냥 GPT 답 보기

### 코드: 실패. 

```python
# 자 수도코드를 그럼 다시 칠까? 그냥 해.

import sys

def recur(n, i, j, cnt): # i 번째에 왔을 때 그 뭐냐 음. 
    global r, c
    offset_size = 2**(n-1) # 사각형의 사이즈 설정
    
    # if base condition
    # 현재 인덱스 정보는 i, j에 담겨 있음.
    if i  == r or i == r - 1:  
        if (i, j) == (r, c): return
        j += 1
        cnt += 1
        if (i, j) == (r, c): return
        i += 1
        j -= 1
        cnt += 1
        if (i, j) == (r, c): return
        j += 1
        cnt += 1
        if (i, j) == (r, c): return
    # 대충 조건은 이런 느낌일 거 같아.
    # 그럼 인덱스는 어떻게 가야 해? 인덱스가 갈 필요가 있나? 그냥 뻔하지 않나?  이 값이 계속 커지다가. 어차피 말야.
    recur(n-1, i, j, cnt + offset_size)

n, r, c = list(sys.stdin.readline().split()) # suppose n = 4
recur(n, 0, 0, 0)
```

> 이때 프로토콜이 뭐더라. 답안을 수도코드 정리 → 나의 수도코드 작성 → 코드 작성. 이렇게 하는 거였음.

기억을 더듬어 다시 구현했으나, 또 실패. 이걸 왜 못하는 거지?

```python
import sys
result = 0
def recur(n, i, j, cnt):
    # base condition
    # 알아서 잘 해보시고.
    global result
    if n == 1:
        if r == i and c == j:
            pass
        elif r == i and c == j + 1:
            cnt += 1
            result = cnt
        elif r == i + 1 and c == j:
            cnt += 2
            result = cnt
        elif r == i + 1 and c == j + 1:
            cnt += 3
            result = cnt
        print(f'done! {cnt}')
        result = cnt
        return cnt
    # r, c가 몇 사분면에 있는지 확인한 다음 포인터와 i, j 값을 적절히 업데이트
    edge = (2**(n))
    querter_size  = (2**(n))
    half = edge // 2
    print(f"edge {edge}, half {half}, i: {i}, j: {j} r: {r}, c: {c}")
    # r, c는 전체 사각형 기준 인덱스. 
    # 현재 사각형의 시작 인덱스는 i, j
    print(f'half point {i + half}, {j + half}')
    if (r < i + half) and (c < j + half): # r, c가 2^n 사각형의 1사분면에 있는지 여부.  
        print('first quarter')
        recur(n-1, i, j, cnt)
    elif (r < i + half) and (c >= j + half): # 2사분면
        print('second quarter')
        recur(n-1, i, j + half, cnt + querter_size) # 이거 맞아?
    elif (r >= i + half) and (c < j + half): # 3사분면
        print('third quarter')
        recur(n-1, i + half, j, cnt + querter_size*2)
    elif (r >= i + half) and (c >= j + half): # 4사분면
        print('fourth quarter')
        recur(n-1, i + half, j + half, cnt + querter_size * 3)

n, r, c = tuple(map(int, sys.stdin.readline().split()))
recur(n, 0, 0, 0)
print(result)
```

일단 정답코드를 참조하면, n을 아예 넓이로 바꿔버려서 생각하기 편하게 만들었다.

### 정답

```python
import sys

def recur(n, x, y, cnt):
    """Z-분할 정복을 이용한 탐색 최적화"""
    if n == 2:  # Base case: 2x2 크기일 때 직접 탐색
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

    half = n // 2  # 현재 크기의 절반 (사분면 크기)
    
    if r < x + half and c < y + half:  # 1️⃣ A (좌상) half는 분명히 넓이인데, 이것을 인덱스로 비교한다고?
        recur(half, x, y, cnt)
    elif r < x + half and c >= y + half:  # 2️⃣ B (우상)
        recur(half, x, y + half, cnt + half * half)
    elif r >= x + half and c < y + half:  # 3️⃣ C (좌하)
        recur(half, x + half, y, cnt + 2 * half * half)
    else:  # 4️⃣ D (우하)
        recur(half, x + half, y + half, cnt + 3 * half * half)

# 입력 받기
n, r, c = map(int, sys.stdin.readline().split())
n = 2 ** n  # 2^N 크기의 배열 -> 이게 사각형의 크기가 아니고, 한 변의 길이다. 
recur(n, 0, 0, 0)  # Z-모양 탐색 시작
```



```python
    if r < x + half and c < y + half:  
```

### 질문

half는 분명히 넓이인데, 이것을 인덱스로 비교한다고? 그게 아니에요 선생님. 문제를 똑바로 읽어 보세요. 사각형 넓이는 2^n x 2^n 이잖아요. 그런데 recur 함수를 초기 호출할 때 무슨 값을 줬어요? 2**n을 줬죠? 그러니까 한 변만 가지고 함수에서 다루는 거에요. 이 한 변을 2로 나눈 half는 당연히 한 변의 그거고. 그러니까 뭐야, 니가 잘못한 거야. 

어 그러면, n ** 4로 초기 정의를 바꾸면 내 값도 맞는거 아니에요?

그래도 되는데 어렵네. 이 문제를 통해 느낀점. 문제정의가 아주 중요하다. 

인덱스 설정이 너무 까다롭다. 그냥 패스.

### 다른 정답

```python
N, r, c = map(int, input().split())

answer = 0

def find_Area(N, r, c):
    global answer

    if N == 0:
        return
    
    size = 2**(N-1)  # 현재 분할 크기 (사분면의 한 변 길이)
    
    # 몇 번째 사분면인지 확인
    if r < size and c < size:  # 0번 사분면 (좌상단)
        num = 0
    elif r < size and c >= size:  # 1번 사분면 (우상단)
        num = 1
        c -= size  # 다음 좌표 변환
    elif r >= size and c < size:  # 2번 사분면 (좌하단)
        num = 2
        r -= size  # 다음 좌표 변환
    else:  # 3번 사분면 (우하단)
        num = 3
        r -= size
        c -= size

    answer += (size * size) * num  # 이전 방문 수 누적
    find_Area(N-1, r, c)  # 더 작은 크기로 재귀 호출

find_Area(N, r, c)
print(answer)
```

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

## Phase1. Top Down

난이도-중 

> n 개의 수가 주어졌을 때 이를 오름차순으로 정렬하는 프로그램을 작성하시오
N(1 ≤ N ≤ 10,000,000)
둘째줄부터는 N줄에 거려서 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수다. 
각 수의 범위: 10000보다 작거나 같은 자연수. 

분석: 위의 수 정렬하기 2 문제와 비교했을 때 n이 10배 더 크다. 자연수라는 조건이 있으니까 기수정렬 쓰면 될 거 같은데, 사실 기수정렬이 기억이 안 난다.

아래 코드는 수 정렬하기 2에서 썼던 코드 그대로다. 이대로 제출하면 메모리 초과 에러가 난다. 기수정렬은 메모리를 더 쓰지 않나? 일단 이건 30분 고민해봤자 진행될 그거는 아니니까 여기까지 보고 공부를 하는게 맞다고 생각한다.

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

## Phase2. Bottom Up

# 완전탐색: 외판원 순회 2

https://www.acmicpc.net/problem/10971

## Phase1

```python
# 문제 쉐도잉.
# 어 이거 그냥 BFS 아닌가. 
# 출발은 어디서? 아무데서. 이 부분에서 완전탐색을 해야함.
# 아 기억 안 나는데 일단 함수 세개가 필요함
# dfs로 풀어야 하나?  스택에다가 갈 지역을 집어넣고, 비용이 최소인 것을 차례로 올려보내서 한 지역에서 갈 수 있는 최소값을 구하면 되나? 
# i, j가 직관적이지가 않네.
# 그래프 쓰면 DFS를 쓸 수 있을 거 같은데 아직 머리에 개념이 잘 안 잡혀서 패스. n이 최대 10이므로 진짜 완전탐색 해도 될 거 같기도? 
# n by n이라 복잡도가 n^2^2처럼 느껴질수도 있지만, 1 -> 2 -> 3 -> ... -> n 이렇게 선형 순회하는 거라 n^2이면 충분할듯.

import sys
MAX_INT = sys.maxsize
min_cost = MAX_INT

def visit(i, cost):
    global min_cost
    if not False in visited: # base condition
        # 모두 방문했다면 비용 업데이트
        min_cost = min(min_cost, cost)
        return
    # 다음 마을 결정.
    for j in range(n):
        if i != j and visited[j] == False and costs[i][j] != 0: # 방문하지 않았다면
            visited[j] = True
            print(f'from: {i}, to: {j}, cost: {costs[i][j]}')
            visit(j, cost + costs[i][j])
            visited[j] = False

n = int(input())

visited = [
    False
    for _ in range(n)
]

costs = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

# 0 마을부터 차례로 방문
for i in range(n):
    for j in range(n):
        if costs[i][j] != 0:
            print(f'from: {i}, to: {j}, cost: {costs[i][j]}')
            visit(j, cost=costs[i][j])

print(min_cost)
```

몇 가지 조건을 놓쳤는지 확인해야 함

놓친게 있네. 문제 조건을 그냥 리스트업 해놓는게 좋겠다. 다시 돌아오는 조건을 못 봄.

```python

import sys
MAX_INT = sys.maxsize
min_cost = MAX_INT

def visit_to(i, cost, log: list): 
    global min_cost, home
    if not False in flag_visit: # 바닥조건 다시 생각하기. 갔던 마을로 다시 갈 수는 없으니까 결국 마지막 방문한 마을에서 원래 마을로 돌아오는 값을 더해야 함.
        if costs[i][home] != 0:
            min_cost = min(min_cost, cost+costs[i][home]) 
        return
    for j in range(n):
        if flag_visit[j] == False and costs[i][j] != 0: 
            flag_visit[j] = True
            visit_to(j, cost + costs[i][j], [*log, j])
            flag_visit[j] = False

n = int(input())

flag_visit = [
    False
    for _ in range(n)
]

costs = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

for i in range(n):
    flag_visit[i] = True
    home = i
    for j in range(n):
        if costs[i][j] != 0:
            flag_visit[j] = True
            visit_to(j, costs[i][j], [i, j]) 
            flag_visit[j] = False
    flag_visit[i] = False

print(min_cost)

```

풀긴 했는데 문제 조건을 잘못 이해해서 한참 걸렸다. 제발 문제 좀 똑바로 읽어주세요

# 정렬: 수 정렬하기 3

## Phase1. Top Down

주어지는 값의 범위가 1~100000으로 작기 때문에 도수 정렬을 활용해야 함. 특히 도수정렬 시 배열에 모든 값을 저장하면 메모리를 초과하기 때문에 바로바로 스트림을 출력해야 함.

```python
# 문제의 특징: 수의 개수가 10000000개.
# 수는 100000보다 작거나 같은 '자연수'
# int형은 4바이트
# 만약 int 최대값이 10000이라면,
# 도수정렬을 위한 배열 세 개를 생각했을 때
# A = original array . len = n, n*10000000 = 40,000,000 바이트, 40MB
# 즉 A를 입력받느라 별도의 배열을 만들면 메모리 초과가 발생할 것. 바로 F를 만들어서 작업해야 한다.
# F =  len = max value = 10000. 40,000 바이트, 40 키로바이트.
# S = A와 동일. 아, s에서 초과되는구나.
# t 작성하기
# a 입력 스트림이 없으면 이걸 못 하는데? 
# t = [0 for _ in range(n)] # t의 사이즈는 왜 n인가요? 결과값의 길이가 n이기 때문입니다. 이거 때문에 메모리 초과 나요
# max_d까지 이터레이션 하는 이유가 뭔가요? 입력 값의 최대값까지만 보고 배열을 갱신하면 되기 때문에 그 이후는 볼 필요가 없습니다.
# 왜 MAX_VAL로 초기화했나요? 최대 가능한 값으로 수열을 만들어줘야 하기 떄문입닏.

```



```python


import sys

MAX_VAL = 10_001

n = int(sys.stdin.readline().strip())
f = [0 for _ in range(MAX_VAL)] 
max_d = 0
for _ in range(n):
    d = int(sys.stdin.readline().strip())    
    max_d = max(max_d, d)
    f[d] += 1

cnt = 0
for i in range(max_d+1):     while f[i] > 0:
        print(i)
        f[i] -= 1
        cnt += 1

```

이 코드로 해결

# 완전탐색: 안전 영역

https://www.acmicpc.net/problem/2468

## Phase1. Top Down

### 코드

```python
# 최대 인덱스는 칼럼 값 - 1이면 충분하다. 즉 in range(max_column_val) 이러면 된다.
# 이건 또 그래프가 들어가있네. 그래프 탐색을 자연스럽게 쓸 수 있을듯.

import sys  
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, h):
    if in_range(x, y) and not visited[x][y] and grid[x][y] > h:
        return True
    return False

def move(x, y, h):
    global visited
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny, h):
            visited[nx][ny] = True
            move(nx, ny, h)

def simulate(h: int):
    global visited
    cnt = 0
    for i in range(n):
        for j in range(n):
            if can_go(i, j, h):
                visited[i][j] = True
                cnt += 1
                move(i, j, h)
    return cnt

max_area = -1

for i in range(1, max(max(grid))):
    max_area = max(simulate(i), max_area)
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max_area)
```

시간 초과 뜸. 알고리즘 문제 트러블 슈팅도 템플릿이 있어야겠다.

### 이슈: 시간초과

- 입력 범위 확인
  - n 범위: 2 이상 100 이하.
  - 높이 범위: 1 이상 100 이하.
- 추측
  - n값이 100이면 급격한 속도 저하가 있는 것 같음.
- 복잡도 분석.
  - n by n 그리드를 BFS할 때의 시간 복잡도: 최악의 경우 n^2
  - simulate 함수는 n by n 모든 영역에 대해 위의 BFS를 수행. 최악의 조합의 경우 n^2 * n^2 = n^4
  - 여기에 시뮬레이팅하는 경우, 최악의 경우 100번의 반복을 수행. 100 * n ^ 4
  - 많이 느리긴 해. h에 따른 BFS 작업이 반복적인데, 이걸 최적화할 수는 없을까?
  - 시뮬레이팅 시간 단위를 t라 할 때, t 상태에서는 t+1을 전혀 예측할 수 없다. 
  - 그럼 아무리 반복된다 해도 이걸 어떻게 써먹을 방법이 없는데. 
  - n^4가 문제인가? 
  - 최악의 경우 이렇게 10,000,000,000 나오는데, 이게 단위가 초도 아니고, 
  - 이게 DFS였구나. 하긴, 재귀를 하는 거니까. 큐를 쓰면 빨라진대.
- 10분 생각
  - 넓이 리스트가 있다 치고, 2 이상인 값이 없으면 더 볼 필요가 없음. 영역 개수가 줄어들기만 할게 확실하기 때문.
  - 아래에 그 조건을 추가했으나, 여전히 시간 초과. 포기.
```python
# 최대 인덱스는 칼럼 값 - 1이면 충분하다. 즉 in range(max_column_val) 이러면 된다.
# 이건 또 그래프가 들어가있네. 그래프 탐색을 자연스럽게 쓸 수 있을듯.

import sys  
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, h):
    if in_range(x, y) and not visited[x][y] and grid[x][y] > h:
        return True
    return False

def move(x, y, h):
    global visited, width
    width += 1
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny, h):
            visited[nx][ny] = True
            move(nx, ny, h)

width = 0

def simulate(h: int):
    global visited, width
    # 이거 뭐 하는 함수냐? 특정 높이에서 탐색하면서 영역 계산한 다음 리턴
    cnt = 0
    area_widths = []
    for i in range(n):
        for j in range(n):
            if can_go(i, j, h): # 갈 곳 없으면 알아서 재귀를 멈춘다니까.
                visited[i][j] = True
                cnt += 1
                # 한번 출발했을 때 영역 넓이를 계산해야함.
                move(i, j, h)
                area_widths.append(width)
            width = 0
    if (max(area_widths)) <= 2:
        return "END"
    return cnt

max_area = -1

for i in range(1, max(max(grid))):
    result = simulate(i)
    if result != "END":
        max_area = max(result, max_area)
    else: break
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max_area)

                
```

- 포기하고 물어보기
## Phase2. Bottom Up

```python
# 최대 인덱스는 칼럼 값 - 1이면 충분하다. 즉 in range(max_column_val) 이러면 된다.
# 이건 또 그래프가 들어가있네. 그래프 탐색을 자연스럽게 쓸 수 있을듯.

import sys  
from collections import deque

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, h):
    if in_range(x, y) and not visited[x][y] and grid[x][y] > h:
        return True
    return False

stack = deque()

def move(h):
    global visited, width, stack
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny, h):
                visited[nx][ny] = True
                # x, y를 nx, ny로 설정하고 함수의 처음으로 돌아갑니다.
                # nx, ny를 저장해줍니다.
                stack.append((nx, ny))



def simulate(h: int):
    global visited
    # 이거 뭐 하는 함수냐? 특정 높이에서 탐색하면서 영역 계산한 다음 리턴
    cnt = 0
    for i in range(n):
        for j in range(n):
            if can_go(i, j, h): # 갈 곳 없으면 알아서 재귀를 멈춘다니까.
                visited[i][j] = True
                cnt += 1
                # 한번 출발했을 때 영역 넓이를 계산해야함.
                stack.append((i, j))
                move(h)
    return cnt

# 지금 할 일: 재귀 형식의 DFS를 스택 형식으로 바꿔주기.

max_area = 0

for i in range(max(max(grid))+1):
    result = simulate(i)
    max_area = max(result, max_area)
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max_area)

                



```

스택으로 바꾸고 시간 문제는 해결. 그냥 함수 호출 오버헤드 문제가 해결 돼서 그런 거 같다.

그런데, 마지막 테스트 케이스에서 에러가 생긴다. 어디가 문제일까.

```python
for i in range(max(max(grid))+1):
```

이게 문제였다. 이러면 안 되는데 오랜만에 풀면서 기초적인 실수를 했다. 이 경우 배열의 앞 원소를 기준으로 nested 배열 중 최대 배열을 찾고, 그 다음 그 배열에서 최대값을 찾는다. 그냥 이거 쓰면 안 된다.

아무튼 스택으로 바꿔서 해결 완.

```python
# 최대 인덱스는 칼럼 값 - 1이면 충분하다. 즉 in range(max_column_val) 이러면 된다.
# 이건 또 그래프가 들어가있네. 그래프 탐색을 자연스럽게 쓸 수 있을듯.

import sys  
from collections import deque

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, h):
    if in_range(x, y) and not visited[x][y] and grid[x][y] > h:
        return True
    return False

stack = deque()

def move(h):
    global visited, width, stack
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny, h):
                visited[nx][ny] = True
                # x, y를 nx, ny로 설정하고 함수의 처음으로 돌아갑니다.
                # nx, ny를 저장해줍니다.
                stack.append((nx, ny))



def simulate(h: int):
    global visited
    # 이거 뭐 하는 함수냐? 특정 높이에서 탐색하면서 영역 계산한 다음 리턴
    cnt = 0
    for i in range(n):
        for j in range(n):
            if can_go(i, j, h): # 갈 곳 없으면 알아서 재귀를 멈춘다니까.
                visited[i][j] = True
                cnt += 1
                # 한번 출발했을 때 영역 넓이를 계산해야함.
                stack.append((i, j))
                move(h)
    return cnt

# 지금 할 일: 재귀 형식의 DFS를 스택 형식으로 바꿔주기.

max_area = 0

for i in range(-1, 101):
    result = simulate(i)
    max_area = max(result, max_area)
    visited = [[False for _ in range(n)] for _ in range(n)]

print(max_area)

                



```

# 재귀: LCS 2

https://www.acmicpc.net/problem/9252

## Phase1. Top Down 30 min, 실패. 

```python
# 이거 디피로 은근 쉽게 풀 수 있었는데.
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.1 초 (하단 참고)	256 MB	50622	19238	14787	38.535%
# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.


# 손으로 풀어보기.


import sys

# input
A = list(sys.stdin.readline().strip())
B = list(sys.stdin.readline().strip())

m, n = len(A), len(B)

dp = [[0 for _ in range(m)] for _ in range(n)]

# init dp
def init(A, B, m, n, dp):
    tmp = 0
    for i in range(m):
        if B[0] == A[i]: tmp = 1
        dp[0][i] = tmp

    tmp = 0
    for j in range(n):
        if A[0] == B[j]: tmp = 1
        dp[j][0] = tmp

init(A, B, m, n, dp)

string = ''
for i in range(1, m):
    for j in range(1, n):
        hit = dp[i-1][j-1] + 1 if A[i] == B[j] else 0
        # if hit != 0:
            # string += A[i] # 이 시점에서는 완성된 문자열을 알 방법이 없음. 완성된 테이블을 탐색해서 알아내야 함.
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], hit)


i, j = 0, 0
while True:
    dxs, dys = [0, 1], [1, 0]
    print(f'what the fuck')
    for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy

        if nx < m and ny < n and dp[i][j] < dp[nx][ny]: # 공통문자를 찾은 경우
            i, j = nx, ny # 업데이트
            print(f'i: {i}, j: {j}')
            string += A[i]
            print(f'adding {A[i]}')
        else: # 공통 문자를 찾지 못한 경우.
            print(f'nothing found on {i}, {j}')
            if i < m: 
                print(f'going to below')
                i += 1
            elif j < n:
                print(f'going to right')
                j += 1
            else:
                break
    if len(string) >= dp[m-1][n-1]: break

        # print(string)
    # 지금은 더 큰 값을 알고 있음.
# 이슈: 출력 문자열을 제대로 구할 수 없음
## Phase 1. 
### 환경: 파이썬
### 로그: CAYK (정상 출력: ACAK)
### 최근 변경 사항: 순회하면서 LCS 출력하는 while루프 작성
## Phase2-1
### 확인: 이거도 백 트래킹 해야 하나? 
### 시도: 
### 결과: 


for row in dp:
    print(row)

print(string)

```

LCS 길이는 구했지만, 그걸 출력하는 방법을 모르겠음. 이건 백 트래킹 할 때 다시 봐야 한다.

## Phase2. Bottom Up

계속 느끼는 거지만, 문제 풀 때는 긴장을 늦추면 안 된다. 이것도 그렇게 어려운게 아니고 직접 손으로 풀고 이해를 했으면 어렵지 않게 했을 것이다.

### Nested Phase 1. 손으로 풀어보기

손으로도 못 풀겠다.

2.	LCS 문자열 구하기 (Backtracking)

•	dp[m][n]부터 거꾸로 탐색하면서 문자열을 추출.

•	A[i] == B[j]이면 해당 문자는 LCS 문자열의 일부이므로 저장.

•	dp[i-1][j] > dp[i][j-1]이면 위쪽으로 이동, 아니면 왼쪽으로 이동.

