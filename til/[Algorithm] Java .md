# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVTVYJJD%2F20250306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250306T021147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwnxE6umapA7%2B%2FE%2BYrTG3vSTxsWaS9cFQ5zYa1u7P00AIgZeft03v9rMjkKcT%2BH%2BBlrEFiL%2F6m3ZyUfCHykTeai50q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDEdkxfdohm%2FSpMT2lircA2DbLEPCuIOzGLo3t0zMArrMwTq0J2JVX528%2BR0KvMWgLYJHQAxFy61Qb%2BTC0X4RNt9o1VDOkMfd16%2FgtUjKnJmQ6o7VRlokzTKYSCrks4LKciX1od%2BvzoMlzSLzwKTQUxhPA82QuESD5SdQoyG7DzlLoGlnbkMFKHmj0K3Kw8LhRv9NxbS%2FZJUdKEvQbDWmqVnwlTx05HTcrsrATknmZK5rTOYV9ZljtbYZ0UuuBH5gnQdxHJm6C1F1ualg%2B1SoUjNsmMntIoG0ldfRz3%2BPObV%2Fk44DXed8DzHEAqkErUobxO%2Fw5gS9Ecunn9ZCHccikqOiCccx%2B2BI1cay2%2BqCmsSkLhnYcGNUasjRiZQ0YoOjU5rsXcJam7RWyWuXYeUQJlUr9R%2By5HpBuv7FVCgRjrhbXD7ptd2%2BpyEjRVgtOjhrg2NNRaqupiCprH4dnWCCimcu%2Fot7VxZbBuY6TyN1gFhxPpvNApCIPw%2BDlVxeIMYGzJ9REiZyLMaEG8kSyJvMC07OGlfrcO1rm7Oqi8aJBZjjc%2BcwjAe5TBtPejA%2FzIpzCu4sO4iDsmANcGHI63Vx4APa5v96J61v6Jwo84mjEtgYExTIKba8fi%2BFQj6MHNoA2j%2B02HM9C0uN7l76MK3no74GOqUB6aykZs%2Bs7ENWESRqWDrhyZqyKsHd0DcNViU7mx0NTqL3PnU4FN2mAUSF566olZ2EuKnJFGoc9iKjom51SchMb0dQ0IxcszMUas18TbaRWreBc5AXIZPWac%2Fer1pByuVZ51tCKp3Ge0jR78B0Qinl8%2BT0P%2B4Tz82Qt%2Bmdl3NtbOVm4meG%2Bc1PPGryWI8BUyxQ2XQZ8mqn0aSOGkTC86WdTb57eN%2FB&X-Amz-Signature=fbf6af7a4e6f126ff71486917c80ea8b36be9c625c6d3134490977386ddd4c47&X-Amz-SignedHeaders=host&x-id=GetObject)

- sum > N: sum = sum - start_index; start_index++
- sum < N: end_index++; sum = sum + end_index;
- sum == N: end_index++; sum = sum + end_index; count++;
## 슈도코드

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

## 코드 구현

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

