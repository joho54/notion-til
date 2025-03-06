# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSKSEN6N%2F20250306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250306T071126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAad%2Fg8SboYHBslu9dqxPX%2BqskIfKrZ%2Bmcfqo4R9hSBgIhALOuxdSohru9rRRNm9VBjf5mbgVFVE6yZA9%2BAb2k8UrvKv8DCCcQABoMNjM3NDIzMTgzODA1Igw2stHUQXgxm7PYtQ8q3ANLqEDPJdctG1hoXBESdBmX%2F6y2SEhfryOQxBrZ2sk3VG6dV6j%2BPBiBXue7CLyuPpKCkVTWn9KhAbOg7d4zvZjO0Zlp%2BzZzD%2Fq1ZGvxORxoj%2FFr4SHWo2rBGBWS1i5Bdh4tY%2BIGI943079zzhMHLykCVbKHv8KeaVsjFAVXf%2B1Tdzgp2tl8UlZjJAXTkPHuqkOM3RQqIIOHfl20idbUZOQkQ9Fm0XIii%2BQBPrbpKdgsV2356khjfbVq%2F66ZghyLl3BcBQXbsI70hYY2wLIKvGew7bQorpo3seQbFwF%2FUC2JZO6Cjq2vPC%2BLBAUwj43VqiWlGIhp3BPNESGvboSvoEtQrERzXRo84hFqQ%2BfNuqCgG%2F9uUypVzkw93Ovl9BajuTk7mWdo7BRTH3iSFagNhP7vUJ6iZ28xXzSzfWECzx1iEh5w7U4V4rs3%2FOgelTuRvtTLSCdrE4BFys7UbVSSgVwh0wlIf%2B3GtceNMzoSVy4oEGOE85%2B5UHeWwTfo5k8wh1IpUIJf813RYqWVm6QtXGbY%2FFHoy0r2Ayr8cBpuOBmv5RG1fdKFp5bnQ01ho%2F%2B20dJkPJF45KdTFml4NHP2RtGEtrkZ%2F7w23akdWwTfwo9b83%2BT3aWqPqHekCEQtTCK96S%2BBjqkAT4tbqMb3J%2F0Tidpn1g%2FWeGfKJ8G%2BYcwVhDrAR04GF6rk12NyAc3Uo2xAwebNLf%2F0Tvvv2Hn0sdcjtnXrq3BOfxW0n8Tq24ZDH5fUkssNB0qq%2Fw9n3iliN%2BV7do9IX4AKB%2FAfWHVdGJgOzP2ApZAMIViQ9EpcDsb1jbbHZzNCFpcDo9QrWiW%2BpIJf4W6n90OILgw7a2OJ3Asd3yzbyxSn%2BI23bjk&X-Amz-Signature=d2444f95e5792514028934c2960cde48eb2984f7e699aa58d392bcd4de617020&X-Amz-SignedHeaders=host&x-id=GetObject)

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

