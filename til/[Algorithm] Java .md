# [Algorithm] Java 



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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3LWRABU%2F20250307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250307T141312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtEysTCqyTOYFGVa2kymCACgCx5MtGyImuDayYcDvL1wIgHsQZY11412kYJPMvDDuaydvd70UjyU8UN8MLHrZCt3Yq%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDAK2qsKtF7lZbiz69ircA3u3LKAYuQOGtZ5YZWEtHSNh4AEL77mTgRIPdbp%2BiWSFyELjaicgIK2fF9WYir1MXKUL%2BrRzC5z8BjEkAFzAPMAQYt2AUb3xoQW0ZUXWTSWIIRGawMp031EQXeEJyT9jv1bgyrtg0s5DXRaFvNkPvLWwLNx1hZINt5uWB1tXi9n9fxz75ipZPI%2FMrN1GTCWUU4uXhw1IKyRDMO4glhFk9mg323LrrJQj9SIhmUhXim1o3BOMw3q5doHcuyl%2Fmvpym1evDXrRmO2ae%2B2TiM10Cf2d9WOmpAio%2Fm3LVabUQ0HjPwnyV4tXg9yQAXoIPFDqPOyzO%2FfCRrVwN7sfBXdsxsajVqC%2FJ%2Ft60xJd7S8RO5LxGuCABvKSszrQfQP9dobxLxeatKn0yNgM7MataSb5NMLHET9Kf8IdMsVyGqp7zwN44%2By0tSotXy42DT4%2Fnbvrp1hyuNjD56tlQMbTdmnGaXbj4O79sOaM2NotFnEnyePqXXAW4lAbwmuMLAuJzZhBMC73s1Uae6mkfFzNOKqfykJGwX1J95qN0Puax1XDjkZFhjbkhw%2Bb8B3e412yeS%2F4wY3k%2BnbMiEzwVVmvIwng%2BiPhxku8UY8VwWuDvaN6MT374fNhCqc259GfMH2pMOLfq74GOqUB4jarB07EbwX64Nsx4%2BUjMzsfBcI7sDL1mGeoWExTabAnYx79VQEmySoZ1V9L6PSb8fPb3QTlptRsBelp9AumSCiNR5aTddw00ylNcYu2gFE8mY7Gjw7vGwa5XjgfKd2Gb5ABHH0gEPofyAKrEDxd7W1AbrREPI68%2BB0WqPq0lr7d5UybPtuFfdn4%2BmOHTUVpvaCHZHEaEZfiIOToJYA4%2Fgg5ylqT&X-Amz-Signature=aec9bf7c98684008e1869b5b55d4eb0e0c9e5f94516a51e6afcba5dc187559e7&X-Amz-SignedHeaders=host&x-id=GetObject)

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

