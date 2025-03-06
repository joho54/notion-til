# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3ABVWVU%2F20250306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250306T071511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2yMymRsKn%2FN5%2FpWVAyjsRij9BLSNBWkVnLvtWH3YRsAiAy9VYxj6XI34hdgfd30HIaxlrH5qkpHOSz%2Fzx8zcvqUCr%2FAwgnEAAaDDYzNzQyMzE4MzgwNSIM68zGMJpdHNhT0ypEKtwDUm1QWy4Xn8xsgA%2Bs%2F5woxlFBwIcmcq46gibtM6HTAR1wnlLWLnFwnS346RngqWVYZOEJ4pPEBiXEzGCSlL5OnPtW0JawQjUFFyLflCyVSfh6DfSkihh%2BcSiT4WyLs1xhOepqgdvm7AHrhkOLz5%2FHSjxBzzBV4H%2FbAD7Z4AvhmyZbWjpuZt%2FPjRdHndOALozIQjTln42fDnGHU3h4fegmPVAdwCS0CULnNOEA9FpqeBuuz6qBM4bKKBgiuDu2xFxpoc55Q5Y5AbNr%2BZvGVXe0h9PrVX4YMnGmxMfy%2Bev6YW4wkuLpyhBOucS%2B8bpMK5dy4sCUD%2FmOWPxAmbdMXTBR2wuTVvWAMDlcs1jOl9%2BeLPFP1o9VoH%2FyH1xvvQvLjQ54vI%2FPV0RH56rr98OZKhC3JSgO4vi2wiEnue8XP4bUDGZjT46UwetPGzdjQVxWyAs6p7oX7IuqICxx7GZ9skHstXKp8XuAM%2F9yjlcY7MgBXZPj7%2F7BNRUO37D0l6ZktS%2FYFP6OPOvkaHYpAHifPIGF8xWTxq7mrQnLH3gjL6xh4u6UdQ8935tQdIQwrhkO%2FVi7wtSm6Mn6ENeVPD%2Bd7y0X7PT7opVVuNoDfk9bwAm2D2A7rrKTZpV8C6jI80cwt%2FakvgY6pgGDeKrD%2FVFJoqHM1W5r1AHpbSKMF9TMeVKpa5w6QGXXixxtEiuLohBlb%2BEC0KnfAPHMOXDaSUn87HN3AfdVR%2BIvoQeb8VFcKVeS1E5h2feUVQufNTeoEhqhnikTrj0Mr3XhGLfXu%2B86CJWH%2BfMc6WbuC4ftt6WgfVbmlZCl%2BxPeRujVgQBLtkRi7c8MXb%2Fbd%2Fr3UzircxLhlzyLeOGaQAnr1Cn44JoJ&X-Amz-Signature=3453dad28eae7114c0d1bc950932d5d6a84458731544e4fad39bee971d84784a&X-Amz-SignedHeaders=host&x-id=GetObject)

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

