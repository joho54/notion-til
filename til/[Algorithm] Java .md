# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673WXNC2Q%2F20250306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250306T070943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDg8uZRRqHaN9YnbrGD7%2F5gRuPUV8hUgH7MddS8PmLRTQIgT08yTqA7YKsNs4HuJrf50d9UqTeSAZX9DKbd5ayu1g0q%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDIT3g5bIys6Xdk2XeCrcAwHNiQQwPqn%2FjILoCeVw8lBvhKXfHn74Tl%2F1mdpaU8p9TfgN3M%2B%2Bxpw3SfXkE2XLcDj2tGrAH9PqPckoYvYbhrOQ7XLCjppR5RDr%2F1F31EFYFA4W46K0yNSiQb7%2FwURhvwDCNlo18pq4UZA8Hx5kWnVxclIMWSZE7%2Fe7khWBL35HJm8f0UD23tAjsyRWqda9V5MoXKLyB7RhuoxRHSbgpnUX3DrHEoOILhwbWkxkO64q9l3Gr3Xvy8%2BThypLsYU2Qrgs3t1zzefGT3ykGmk91GCpZeMFdqsjI8g018UGhhNjjdldVGvsQFqEDUWNE2IP8g%2BgMWxXB4KOdr4j8qPGxTy4ppI4PTBlwHmdydQruzojzhkxy6DulsjHeS4fP%2F7cVEifuS1O2f5forW1SgW7fe6FSUs43DjXJqh4c0z61tPusT8zK8HD6Co4RceN36cZyNoElx4ZvobzaTTZ7397cioj7yKyzt5rVzn7W3KUy77UmUbyoY%2BkudX9z1MPKKiRjQ2gPCdvjwYOU5ZVm9cL9h%2Fx5xDFdKviV%2BsDl4Qnc5bGcArepQdMAqU9UBGzIXJEwdBFyz%2BeExwkBf07cpnp42NKhBvFpVZxsCOe2kUb4RQU1pUMRoOhkDmkKAP6MPf2pL4GOqUB3Nrthit62wSiBNMfv7EwLphIIKewd5LHiw%2BwH4335Ie%2Fpe%2FchC5yFv0WyAWAvu%2F9oobfVCp5nABR30X%2FTNPKDBPv01hONtsoiuW%2B9GwWC7lvDiiynTW07oxT3LXLcCS%2Fy7nby0QCCD4ZGGRjRFUD0UKKmNhOBEpGDPCSBLAAnwny4%2FFDXgQOdAjlPBXkJk5Hp3R2uIZf2PnSXRWPxnmZ2lpeV3Z1&X-Amz-Signature=7e4bbeb42cdf8695a57f0ffa34046dd2fda0dc475bf1cca5ee6698b3e794a2ac&X-Amz-SignedHeaders=host&x-id=GetObject)

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

