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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVJ5UDRL%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T003550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL3SzUuFkJMLZHMy%2F00PTQbxdHY9%2Fo9fhrLD7lGKiCiAIgMY8QOpd9oW6KVFlEofNI7w%2Fo%2FMwg6Z29kO4UzqXHO5wqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1tIpa0fNWbZzSMISrcA8BbGs0U25i5CRYguRCwv%2B0fBoiCJVn%2FWTkdTnncTYK3SzwNasK0CZLZiHHg1zl4f8ITDsu8mtKY%2Fci%2BcT5tGmmd7p2eBMZYaRqV0rS%2FtQFW91t0UGTJ9Oidf78ZY8%2Fo%2FQ1aomS0mPzoCzv1vZnHD%2FoUPgyTLZBWzAgz%2Bzmg16nSfRx5nGDDaJYeG3K0GtCJYYyMR%2FrIfSroiSKHWJGuF03E%2BhkbsIc5fe1UCac87%2BV%2Bm7PvOCcQhmc6z6e8b%2BJjjnCsO7xFHvwh3oDBOq3X3tA9FfpK9hwwlU%2FwnZH6a6Mmdo0pMfNhvffyFYEL8dt47uaY9i3ETJzUBhtfscUyLbiwuSCF3QqCNzS4SaQlzdKGP%2BA%2BJHagKZWJ6Vsq%2BV%2FcbQOzNp28dJ4iLISQGWqSrIOJrWVImz6G3xQqS8C2igC8O7mBUmLlAskk54a1BEczBk4i7c%2Fp%2FltyEWybGQelnD9jdLsWLD8bKzzaNyA5ndd2TOnHRCJtPuiMK3byHRLvHkIuIx0ydJVoXKKZRNqdGy9XbJO3TwFiKGoKdKEtMGM1h1pZoQWSzuw7fSbIDpMLzQPsqHHJdk25WLQR%2B1CLuLlCPhpb%2Brgfiy5do5odU%2BS962zuGf0NriFCB63MMI7uzb4GOqUBvb6O7PPjs2IvCvuZAAPcDhz9vnFx0WFVq%2FDa3IgRmjBMgyZ%2Fmum8yx7nBNPmmmOklK5NvUuVJYXHSwJIeNuIdOAFiVIC4iYH2WV6125680%2B7V24CjbHTIEi2ZY5xn9rr8RwE3%2FBrbjYlvQ78yIDQYFB%2FQ86Ku%2BaLL5oC8qaW9E4%2FjeT6bMjHxM5Q49%2BAnB%2Ff85WeudhDzFiDn2jEXKP5EFbbYmIO&X-Amz-Signature=70f4a27dd3034d8a7bc2a202c11901e5d7c998023f1e2a8f9f120c30199906a8&X-Amz-SignedHeaders=host&x-id=GetObject)

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

