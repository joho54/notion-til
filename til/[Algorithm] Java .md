# [Algorithm] Java 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



# 투포인터: 연속된 자연수의 합 구하기

## 문제 분석하기

n의 최대값이 10,000,000이므로 O(nlogn) 알고리즘 쓰면 제한시간 초과하므로 O(n) 복잡도를 사용해야 함. 이런 경우 자주 사용하는 방법이 투 포인터

## 손으로 플어보기

### 투 포인터 이동 원칙

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/05bfa4fe-a087-4a4e-84ea-04165d656134/Screenshot_2025-03-03_at_5.30.53_PM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EX3JUH3%2F20250305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250305T042444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICeVmtY6pOilDHVnv6DjEgL0RMRkwU5aJD71LL%2F%2FGSq2AiAP2Y8JFmxv%2BflUmSyXotrPDHnSza7vf9Atvgp3PmSGLCqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOOQvQGusg5F6FQKrKtwDh3sFdN49L94lrF0Tqk%2Fd30i5iSt1U1chUN5m%2BWPTG%2BPsdwd660N99us1koE6Rrcs1LUZACqkDevWr0600xurTcRWyMq23B8C95no5fyXNCYd14nDkQs4dVN7Vz8uA5vTSMA8C1UxFSrge7%2B87jxEjIdYEm7N%2Fypaqbv9ErJ2OYwbo78Fi1oxXLqomO4O%2FZY21prLSGcP%2BlM%2FdccEfOAN1fclrxufWo1jsrfSEBii5ZLxQe17vWGN0FFOflEuesJEkQJi3dBWJ285SGCp44nXZUbsZVUMfdBoHzjSGrQ2sn5uONJQn2YAezXmE%2Fn7KrExbrHAUZo7QuIwlcibrvvkrwXcRtw0iowrQQbJTJJdwWk0VsTBHl8AMF7qkyu4GnKXGCDea%2B8eXxFrhBeTsccTC9zeKIDVEl4pROij8D%2F5qpibIK7d9GGiRo%2FLdXTmZlBkUcR6dgMlY%2BYTRAXTQpofYforbcDfFbSlsJH9GpMYf1uXfz5KbBbhenxlcopB%2BFZicw%2FLSZZR%2BlmODua4fHJd1qqMkRVQdy4mYpsVBlRBhe%2BH1Xpk%2BXEjwfXGryyXO7bCum2NmjswAJKeP8fO4VdYVg4nwBmKQ7kMWjogeXbrT3dk1ulitPgLFLepi48w14mfvgY6pgEj3eO%2FJ%2BlSzkf38M40pFyyUgDAuptY8mhfuxcTldC6J%2BJG%2FO0WVVJMTSFgWFi2b1tKB0QgcVeDoCUwLPiv5hFCWcXXcvB%2BV4N1hLdAp6lK%2BqRB49p07VazjMsHk4972Mce0HweI%2FK0vmteYTnw7U%2BzYh5YdEtfdQyVjKhiUXJfQmAikOI%2FQjsMi8Mig7DZ8rqZUL7o3i5Qog%2FemXPN%2FHiRZFwaK9rI&X-Amz-Signature=cc77c221419f0e8e75eb2e2f2b6f6443ab1e5106dd5c591abb51239a263619f3&X-Amz-SignedHeaders=host&x-id=GetObject)

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

