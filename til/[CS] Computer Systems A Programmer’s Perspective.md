# [CS] Computer Systems A Programmer’s Perspective



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 버텀업 스타일 독서 정리. 

> #: 이름, 그림, 표, 명제

> 읽기 과정의 정의. 읽기는 무엇인가? 줄글을 어떻게 읽어야 하는가? 그때그때 체계를 세우자

# A Tour of Computer Systems: Information is Bits + Context

## 그림

### The hello program

```c
#include <stdio.h>
 
int main()
{
    printf("hello, world\n");
    return 0
}
```

## The ASCII text representation of hello.c 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/74f81e5f-5768-470a-a83a-648292a7757f/Screenshot_2025-03-14_at_10.23.17_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGWFQOUM%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9lgvg5msHG%2BATe0ixsZyeNVtebiGhOPLksMFPwoPE7wIhAPQs5Ek3EL1br1rmeqeiodfOlSi4pVXxCXH4%2BRC1vdqSKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyinTTCxcRqcRb6sjAq3AMoPx%2BnLCyqmS9z7Klpki6yCbbxonDQAf9ZdEpxxBlc6E9kJV%2BcwXCVYHofW%2B7Tp0R24H%2B0Qmcg6fVur2oKE5xXvqGDDfR88GLowsfsticA5QYd71SMVhsomwE1RtRqpyZq7u68%2FlJryrBtZQa2bE4kmpwgtqdnhK1dc1nfopnfosZmqWeXExR9JYL2y4Dzz0vEQtob9meX6ZTOgT3bnEwyB9zUUp4ha38hBxSUcjKKJRqr0DEvKmq74DpkslM%2FOvRYOfQRUXaoO90qw9V%2BAJW%2FtuUV6KcpRstt9soix99afK6KvQIGluXHiKNUOAm01G7vg52XhLhr1a8MVY2RN%2BgKFcRukGEFH7nUCMOwDN%2BCcEjSnfeQzvbtQyC1zLT7u4l3bY3x839ydqRfpKn9KyYLWnde5HxCE6%2FBMPTmOWJIsnQh0xAuYIJlreHW3j1oYPaxWoZ7v4vSyRgLGYyAfxKzm7OHY2NIlXzo57nr3xWGionz%2F0ZJzuXArS2OaQvqw%2B1%2Bp7V%2Bl8ZM2Ml8mKJZKuORVgax%2BhptsJxbr%2BdALwIx1e1VZMCUNDBBlPnPHr8HMMTOTzDO9YOeh0gB%2BsiMF2xj8JmU%2Bh4%2FLb0rIO%2BiapizRLSRGiIYg4fWsOaGCDCA79K%2BBjqkAYrYl3nAMyY%2FSyedC2tft80BkdpZP318UgWvyQ%2Fxy4g10V3%2FiZB9l522nANXCwzjwo5174e3%2BZFQ%2BwqDONUqd432CmdjdKFUDALxlfjrIUOKVqVJTtFpe%2B%2FdwqQR%2Fngm42QxlN45ZY1%2BTVzqlibZx6N1uI4sH1s8NV6AEEVfpKsxBuEdvFXuRAQkT5%2BG89rTXj6s5TWcF4oscBWSHLSqfQLtc9Kj&X-Amz-Signature=0f556e7880b4d1468e68955dde70e57ec9fb70c8f48288990e773831d210ca62&X-Amz-SignedHeaders=host&x-id=GetObject)

## 명제

- Files such as hello.c that consist exclusively of ASCII characters are known as text files.
# A Tour of Computer Systems: Programs Are Translated by Other Programs into Different Forms

> meaning Compilation System.



## 그림

### 컴파일 시스템

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/6ecfdf9c-071d-425c-8048-a1fd54a82aa8/IMG_9865.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGWFQOUM%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9lgvg5msHG%2BATe0ixsZyeNVtebiGhOPLksMFPwoPE7wIhAPQs5Ek3EL1br1rmeqeiodfOlSi4pVXxCXH4%2BRC1vdqSKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyinTTCxcRqcRb6sjAq3AMoPx%2BnLCyqmS9z7Klpki6yCbbxonDQAf9ZdEpxxBlc6E9kJV%2BcwXCVYHofW%2B7Tp0R24H%2B0Qmcg6fVur2oKE5xXvqGDDfR88GLowsfsticA5QYd71SMVhsomwE1RtRqpyZq7u68%2FlJryrBtZQa2bE4kmpwgtqdnhK1dc1nfopnfosZmqWeXExR9JYL2y4Dzz0vEQtob9meX6ZTOgT3bnEwyB9zUUp4ha38hBxSUcjKKJRqr0DEvKmq74DpkslM%2FOvRYOfQRUXaoO90qw9V%2BAJW%2FtuUV6KcpRstt9soix99afK6KvQIGluXHiKNUOAm01G7vg52XhLhr1a8MVY2RN%2BgKFcRukGEFH7nUCMOwDN%2BCcEjSnfeQzvbtQyC1zLT7u4l3bY3x839ydqRfpKn9KyYLWnde5HxCE6%2FBMPTmOWJIsnQh0xAuYIJlreHW3j1oYPaxWoZ7v4vSyRgLGYyAfxKzm7OHY2NIlXzo57nr3xWGionz%2F0ZJzuXArS2OaQvqw%2B1%2Bp7V%2Bl8ZM2Ml8mKJZKuORVgax%2BhptsJxbr%2BdALwIx1e1VZMCUNDBBlPnPHr8HMMTOTzDO9YOeh0gB%2BsiMF2xj8JmU%2Bh4%2FLb0rIO%2BiapizRLSRGiIYg4fWsOaGCDCA79K%2BBjqkAYrYl3nAMyY%2FSyedC2tft80BkdpZP318UgWvyQ%2Fxy4g10V3%2FiZB9l522nANXCwzjwo5174e3%2BZFQ%2BwqDONUqd432CmdjdKFUDALxlfjrIUOKVqVJTtFpe%2B%2FdwqQR%2Fngm42QxlN45ZY1%2BTVzqlibZx6N1uI4sH1s8NV6AEEVfpKsxBuEdvFXuRAQkT5%2BG89rTXj6s5TWcF4oscBWSHLSqfQLtc9Kj&X-Amz-Signature=57cd17db462bb07d581b8b86ea8835a4571ffef9cd55e3978af6c06e5d1b3936&X-Amz-SignedHeaders=host&x-id=GetObject)

## 명제들

- On a Unix system, the translation from source file to object file is performed by a compiler driver
- Four phases of the compilation system
  - Preprocessor
  - Compiler
  - Assembler
  - Linker
- Preprocessing: 
## 코드

### assembly language of the main method(printing hello)

```c
main:
	subq $8, %rsp
	movl $ .LCO, %edi
	call puts
	movl $0, %eax
	addq %8, %rsp
	ret
```

# A Tour of Computer Systems: It Pays to Understand How Compilation Systems Work

## 명제

- Understanding compilation system pays on…
  - Optimizing program performance.
  - Understanding link-time errors. 
  - Avoiding security holes.
# A Tour of Computer Systems: Processors Read and Interpret Instructions Stored in Memory

## 그림

### 일반적인 컴퓨터 시스템의 하드웨어 구성

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a0333935-3357-4f86-b41b-ddcfdf361333/IMG_9867.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGWFQOUM%2F20250314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250314T235228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9lgvg5msHG%2BATe0ixsZyeNVtebiGhOPLksMFPwoPE7wIhAPQs5Ek3EL1br1rmeqeiodfOlSi4pVXxCXH4%2BRC1vdqSKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyinTTCxcRqcRb6sjAq3AMoPx%2BnLCyqmS9z7Klpki6yCbbxonDQAf9ZdEpxxBlc6E9kJV%2BcwXCVYHofW%2B7Tp0R24H%2B0Qmcg6fVur2oKE5xXvqGDDfR88GLowsfsticA5QYd71SMVhsomwE1RtRqpyZq7u68%2FlJryrBtZQa2bE4kmpwgtqdnhK1dc1nfopnfosZmqWeXExR9JYL2y4Dzz0vEQtob9meX6ZTOgT3bnEwyB9zUUp4ha38hBxSUcjKKJRqr0DEvKmq74DpkslM%2FOvRYOfQRUXaoO90qw9V%2BAJW%2FtuUV6KcpRstt9soix99afK6KvQIGluXHiKNUOAm01G7vg52XhLhr1a8MVY2RN%2BgKFcRukGEFH7nUCMOwDN%2BCcEjSnfeQzvbtQyC1zLT7u4l3bY3x839ydqRfpKn9KyYLWnde5HxCE6%2FBMPTmOWJIsnQh0xAuYIJlreHW3j1oYPaxWoZ7v4vSyRgLGYyAfxKzm7OHY2NIlXzo57nr3xWGionz%2F0ZJzuXArS2OaQvqw%2B1%2Bp7V%2Bl8ZM2Ml8mKJZKuORVgax%2BhptsJxbr%2BdALwIx1e1VZMCUNDBBlPnPHr8HMMTOTzDO9YOeh0gB%2BsiMF2xj8JmU%2Bh4%2FLb0rIO%2BiapizRLSRGiIYg4fWsOaGCDCA79K%2BBjqkAYrYl3nAMyY%2FSyedC2tft80BkdpZP318UgWvyQ%2Fxy4g10V3%2FiZB9l522nANXCwzjwo5174e3%2BZFQ%2BwqDONUqd432CmdjdKFUDALxlfjrIUOKVqVJTtFpe%2B%2FdwqQR%2Fngm42QxlN45ZY1%2BTVzqlibZx6N1uI4sH1s8NV6AEEVfpKsxBuEdvFXuRAQkT5%2BG89rTXj6s5TWcF4oscBWSHLSqfQLtc9Kj&X-Amz-Signature=22fa6137b047a0bb28cdfc769138ed512c02195e9c586669f1d337c7f469091d&X-Amz-SignedHeaders=host&x-id=GetObject)

## 명제

### 공부법

1. 쭉 읽기.
1. 각 요소별로 이름, 역할 정리. 아 모르겠다.


# 이슈: 실습을 위한 도커 우분투 실행 중, 컨테이너를 실행하면 바로 중지되는 현상

## Phase1.

### 환경: macOS, ARM, docker, container image: ubuntu:latest

### 로그: 따로 없음. 컨테이너가 바로 중지됨

### ㄷ최근 변경 사항: ubuntu 이미지로 컨테이너 생성

## Phase2-1

### 확인: 컨테이너가 계속 유지되도록 하려면, 아래와 같이 bash를 유지해줍니다.

```c
docker run -dit --name myubuntu ubuntu bash
```

-d: 백그라운드 실행 옵션

bash: 이 명령어를 통해 쉘로 접속해야 프로세스가 유지되면서 컨테이너가 살아 있음

위 두 조합을 쓰면 백그라운드에서 배쉬 실행중인 도커 컨테이너가 만들어짐. 일단 이렇게 해결할 수 있을것.

그렇다면 궁금증: 이미 종료된 우분투 컨테이너는 어떻게 다시 접속할 수 있어?

> 컨테이너의 기본 프로세스가 bash가 아니라면 접속 즉시 종료될 수 있습니다.
이럴 땐 컨테이너를 새로 만들어 bash를 유지하도록 해야 합니다.

그냥 버려야 한다. 

### 시도: 

```c
$ docker run -dit --name myubuntu ubuntu bash
$ docker exec -it myubuntu bash
```

### 결과분석: 

잘 됨.

주의사항! bash 가 메인 프로세스로 실행 될 때 exit으로 종료하면 다시 접속할 방법이 없다. 그냥 실습할 때마다 새로 만드는게 낫다.



