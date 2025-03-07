# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJRPXOQV%2F20250307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250307T070528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BslCfuUPBmo%2BxYTcTh88qfsYx2%2BtiPugTPsUQwhsPkAiEAsULkA0sPYXRcrhKHiC9EVNsODfUyua7yfEW%2FYvEWCgwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDExEZoqalNBp7MCvgircA3pe3vOdaILngj7doXJi23%2FDEW%2FSjogcJrRzvhIe8A6slnsY88eKecB%2BE48ZJeTuhMBuTYRnrTCbp7XBa5%2F7IRBObYDATLSJI3kTSAvGzx8mw5CxgWCkvxUhwuWP564gZf9EEP%2FIysCJVSDFAjdeoOzCHGFXHkwBFMLms3PwmLQx7PmGmKLhQDyzSHOiz9L3sbhTUpuVvuHBqLYZwDjmvoX8E%2F%2F5LZm%2FsMg1KUZyhJ0J7OgtjDXQd6RjTtIedtd%2F3iYWlSTXDipwwbLJOXSWswf%2BJtOUcxOEIqBZe6nAZ1ynaugorriT%2FCc63HOSRlPinWgQiBhxymn9OXThg%2Fk5s7qIkhkas%2FpWlOxU%2BSpNrYKvDEZKUb2iHm2rUAIvTBTtLOMEllatIyf5Q2g3j1jNbVB0GMeOil79ZmTxspplAdwlP6DNVEMxnS2f%2FHQVSysr5zVSdZzW%2Bl88IKFQ2vxMUPrdlsK8nqCtLPMipbG63d%2BY8FzVIZRhpvtAE1hu1Z2PMZzNxxMANNZUEtX7cEhaXP6ky3AxjBarvCnUF51hfayT0iT2i4cLEQFlQ2pCVGjYC%2FBWuOhz1YxGOIe%2F1w4AF8muGibT2WP2o9BPXG6yYfznDPavWNfZ2lkHmdE0MIinqr4GOqUBSUtwvevYvzuMLWEx%2BYAOgHY7SWm6hKTRoYKN3pl6hsUq%2F%2FUmDdT%2BmXj%2Bqsj%2B%2Fy9e9aStL0kk8Op0oQ8xgjtExieQJmLJu0DYFv%2BC8cGDDzS2l2x8IH4cBnS%2F47xF%2FwchnNxgeEpOrlmemrBkVUx7GeRQrKxIVlY0bFkLae%2BhSB1xwPrXBHrZGrmv9y1HJ6QlcsktUNeNTxqJn%2BOmmjD4mG8tR90L&X-Amz-Signature=272f42d03afac29eec4a0d20573db56217df9500e54377185dd8396dd4379597&X-Amz-SignedHeaders=host&x-id=GetObject)

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

