# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PRIXQIT%2F20250307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250307T092139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFZpJPrEihNJlT33Up%2BxHDYMI1O0H%2FkiDUaxkw6lK8xzAiEA1xlosxP%2F2WOqgMZVqM1l7zwnlTnaI98gO2nn4Wyn1GMq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDGD7faPYhrOTh0M4%2FyrcAw1Y9%2F6C9%2Fc0YJkCSmvROMewMN1NX0pZVUsnNRX1QODrKsPfjPMxZASS%2FSbF46u9elaLYJJPjPEhk%2FDnfTThtMLNpXZmuPmZOKthfPJXB1OUqHAh3RmqFosZQLkPAybtOCyYkyVy8%2FUcZ%2FgB0pY1uHMbrwLlEZ71WHLXR%2BtsgXi0pBzyO3b5vtY8BcYiFhuFBdeejYsERgDYou%2BG1Xf2gcLu2KStGKXt7s0aYI3os1Px6nTviBPKQ8jOqDdl4MHTW1CuDi6Ghseh4kmooNJQ5zCxOamMWO6n%2FpxBu4532b3bFS4H2l4OEeXJBHdMZaYVExvUHZDlzb%2B3Oj7XAHT42LmYl6uhcH22Cx%2FLiBOkKAmT8Mkt%2F5fXpkayi%2FL4Vj1BzsfXj5YgU5c470yRwvaAZjcnIyBBwfKtKNjtmJGUiJcmZlvF82ZrcPajWijR6GULgAjBLSEbwjcGPUve7JA9FPiISnGV%2FURxsrjAeaSoNlVo%2BX128qbq3yTSD0OfBOyXmlb%2FOdcw0MBakf4ekENvt09bVgUl%2BjownYMI9c%2FFzfe9IXXN40lswgFZQjmme1fqVoeL40RJj6oS265%2FauHOtBjuhs4aRZMjs0UtGZKtRcGNl%2B3EwKjWdej2%2Fa94MIHnqr4GOqUBub%2Fr5yY01R40G1xlsZo0zb995WRsWfrsePXQr0PdB46SRc46VroGO2diuBSLZ0jMAujZ7KIeOJRTtniKMvNSzLAvHI1C4peL6jTPF%2F%2Fbdc1nGJ2gii%2BwBQJP2%2F79qcWhQOjRQWvdmJZRl7KzD7oieWlWTyiD%2FP7LXuJHV%2B3xnR2zqiF4t6XIf%2BF279F4gitRI7uDcQnWHwsfV83izJfzuAQ0NVQf&X-Amz-Signature=ac594656e0b14fdd4df38d80ff817d5c0cc6c38114d344cea6ce405a51a702fa&X-Amz-SignedHeaders=host&x-id=GetObject)

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

