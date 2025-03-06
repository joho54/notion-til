# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJT7HSO5%2F20250306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250306T070509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZNmIwEFQ2IPIFSzVtC%2FMkOQXOgaNbQn3CSU9ZzvLj%2FAiBkPXXuF6QZMtTzeP6kxeUp9FO46KRvKpUsvwY9ClVASCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIMIIR%2BmeLY%2BAY2WBDpKtwDAiDNNv6cd8jKswizLa4QbagfYtxVVZEbFPUkYqC51Q8KBPhCDJx0ZtmIiwBZRHHkAwyutC57hJkeEETPpXGXbtBz47S4T6VYuWTtp2xljcfCQ3ZCYG%2FYqy3zngJwYFlUoa3WpsNdst%2FO1e4WHbrllEhF2cQWaQrHarJPLbV6izEn4XinKXmHEpuhYxayHhrIO5wVk6nsoq%2B10FTC%2FhMvibHPT%2BaLoHcHFBvkUUjJV0ZXQiezeItrF9y0%2FzSZyc%2FIosexAiIOFqBccuhvu1l09V%2FkSrN%2BNb9E6aWzWtLQ1bSkUhYQFMOM4TxvMo8vm9GMLtkwuqKgrzPiEkHinfq3TBd3nsQR16ztAhs1qLBzrMMND8fnrp0Vluq7Pp7xZ8PN2BGYxrrF4DdW67XB%2FfS5ezmsVObWkXoWDxKHUTfUwZyAMlQMIg%2BW1T7qoj9P447WyG1A6Te4q0wvwfYoRSKpyAoG4KE%2BaE2Ny9LlVp4%2FZjSKa8xBdpRAb0%2F%2FOKBhPsgVY6BfSZyZXbMwFR5cV2iCMjbSs%2Bh35TCqXG4NdTvS%2BZrtjYIRmFGX4FigzBK%2B80vyrzOEQ2FVUczz8f0rFgOQ0NAoaLBhf6lIzJtTeMS4yviOiGWrPgXlixCAneMw9%2FakvgY6pgFRnnOD8GEMQjP8UMiGVONKiNCmBy2oiy7JgdZgH%2BTciorQ%2BtS9Wu1%2FHYFOJmioz0AvJG3OsK%2FCLSIZgwGPuX84Mht7WrKmwDuFt6O4NTPk07Gw7GL6hSJRRV8nCCJMwHTZzPt6rIftVIXPER5j6HE%2BiNVk1pOmBfsfjgHY1oc4KIU6uKGX%2FrlLN6vgdFOASVXYWFV2O28YvunsZ%2Bj16kEhdD5Vp6MJ&X-Amz-Signature=b8472237894f8f6efada68f12873b6b88f23b2c4b5647f8ec5d4a727bc0692d5&X-Amz-SignedHeaders=host&x-id=GetObject)

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

