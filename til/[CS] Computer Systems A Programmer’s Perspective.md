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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/74f81e5f-5768-470a-a83a-648292a7757f/Screenshot_2025-03-14_at_10.23.17_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAT7PZTM%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYr2JUeTGiZ3%2FGCecE1GKUu46XAyhGFcS%2BHmNNAxMQoAiBTWU9kn4yOLFDPfgXmzZw4M0aZRK1Yn4khQrpSsCbwNCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMNTN2KP8FJ9qdM%2F4qKtwDZJDU4bouUH9mDIhMKtK7UjauzXd6ESYB1HiktyNW5jTv6vpqMWinI40G719be4YBDWnecQ9Vi%2FiOYsV1hsnMTq%2FT5B5YTp3yTuNSL17XWx%2BNVQ1uKxHcyKohEjeL%2BerchmFsJoBsHQGtVgPJi2OZ6sqwUx0%2F2juNPjQ79IicFz6sZfs%2Fld3Mh7C03RNoQ4UuGOhcar0Mq7YUTMXKL1%2FJQYdDlu%2F4jmio3SP5wP6hf2haKSLRLutIYm0AWnqCjN7WEsmtXguRn0m3zVUcTA4%2FMZ6jF11qMXk67PeF%2FN02iFc5HyLnBUlAWXUoRcNQCXCo%2B5KwhCcU87BaadK9Nw8wfJlxmXtey26OmOPcuYY7bHEdb2c6E4RRgEwXziXat9gRgsGI%2BXmQmKxgLNDRtEwK2tkLKX9RO0wqX5dQaen88IxVeaCZ5DVkJZXljmkF%2BfgxoXy3y5k9%2F6YDyzmUNw1fjUAhzxuxib9bd7hOi%2FUhisSP6guXpHAlrmxVM0ZYldsbCNM8RM0I%2B%2B0051uTJOwm9Ti9zIBlAUJjiU5QC6Olxz5kQt5I27d2oBEfK7PBAQfLVRIh%2FYQuE9zQnvIUDzX0%2FBOn8jhfJnNgvDdviOL656zxQuusEFXX5Kot%2Fasw74HYvgY6pgFW6kBwLkdmgo1g2f9rKFkJj6pjg17btMPX68Fzq2EXLRuyK%2FI1Hv%2FtSdeMEAT4fLnEE%2BpcR0lqZWyZrFUU8NcMLCPgdCoSrV6ur0lWFtDwnPCEIhU0H%2B%2BUzlfjhQLoV5%2FPnC0hZuBvc9k%2Bhg6M8W6ruJG6tR9gr4KFaAABCnLmT0Cg3IPzsMixYneyzGw4ExmfSrgPfdEMWXLwzLJocOHbVRp%2Fl7En&X-Amz-Signature=87ef71f558cdfdda81984a57e2e79f7499cee8a460bd96c527539c0021df4a41&X-Amz-SignedHeaders=host&x-id=GetObject)

## 명제

- Files such as hello.c that consist exclusively of ASCII characters are known as text files.
# A Tour of Computer Systems: Programs Are Translated by Other Programs into Different Forms

> meaning Compilation System.



## 그림

### 컴파일 시스템

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/6ecfdf9c-071d-425c-8048-a1fd54a82aa8/IMG_9865.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAT7PZTM%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYr2JUeTGiZ3%2FGCecE1GKUu46XAyhGFcS%2BHmNNAxMQoAiBTWU9kn4yOLFDPfgXmzZw4M0aZRK1Yn4khQrpSsCbwNCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMNTN2KP8FJ9qdM%2F4qKtwDZJDU4bouUH9mDIhMKtK7UjauzXd6ESYB1HiktyNW5jTv6vpqMWinI40G719be4YBDWnecQ9Vi%2FiOYsV1hsnMTq%2FT5B5YTp3yTuNSL17XWx%2BNVQ1uKxHcyKohEjeL%2BerchmFsJoBsHQGtVgPJi2OZ6sqwUx0%2F2juNPjQ79IicFz6sZfs%2Fld3Mh7C03RNoQ4UuGOhcar0Mq7YUTMXKL1%2FJQYdDlu%2F4jmio3SP5wP6hf2haKSLRLutIYm0AWnqCjN7WEsmtXguRn0m3zVUcTA4%2FMZ6jF11qMXk67PeF%2FN02iFc5HyLnBUlAWXUoRcNQCXCo%2B5KwhCcU87BaadK9Nw8wfJlxmXtey26OmOPcuYY7bHEdb2c6E4RRgEwXziXat9gRgsGI%2BXmQmKxgLNDRtEwK2tkLKX9RO0wqX5dQaen88IxVeaCZ5DVkJZXljmkF%2BfgxoXy3y5k9%2F6YDyzmUNw1fjUAhzxuxib9bd7hOi%2FUhisSP6guXpHAlrmxVM0ZYldsbCNM8RM0I%2B%2B0051uTJOwm9Ti9zIBlAUJjiU5QC6Olxz5kQt5I27d2oBEfK7PBAQfLVRIh%2FYQuE9zQnvIUDzX0%2FBOn8jhfJnNgvDdviOL656zxQuusEFXX5Kot%2Fasw74HYvgY6pgFW6kBwLkdmgo1g2f9rKFkJj6pjg17btMPX68Fzq2EXLRuyK%2FI1Hv%2FtSdeMEAT4fLnEE%2BpcR0lqZWyZrFUU8NcMLCPgdCoSrV6ur0lWFtDwnPCEIhU0H%2B%2BUzlfjhQLoV5%2FPnC0hZuBvc9k%2Bhg6M8W6ruJG6tR9gr4KFaAABCnLmT0Cg3IPzsMixYneyzGw4ExmfSrgPfdEMWXLwzLJocOHbVRp%2Fl7En&X-Amz-Signature=1acb69425f62565e6eb4720ec4723903de3a9b89a12eed05b72673bb1b7730c7&X-Amz-SignedHeaders=host&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/a79cc0c1-f77b-45c6-af98-ce249dc64875/a0333935-3357-4f86-b41b-ddcfdf361333/IMG_9867.heic?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAT7PZTM%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T031204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYr2JUeTGiZ3%2FGCecE1GKUu46XAyhGFcS%2BHmNNAxMQoAiBTWU9kn4yOLFDPfgXmzZw4M0aZRK1Yn4khQrpSsCbwNCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMNTN2KP8FJ9qdM%2F4qKtwDZJDU4bouUH9mDIhMKtK7UjauzXd6ESYB1HiktyNW5jTv6vpqMWinI40G719be4YBDWnecQ9Vi%2FiOYsV1hsnMTq%2FT5B5YTp3yTuNSL17XWx%2BNVQ1uKxHcyKohEjeL%2BerchmFsJoBsHQGtVgPJi2OZ6sqwUx0%2F2juNPjQ79IicFz6sZfs%2Fld3Mh7C03RNoQ4UuGOhcar0Mq7YUTMXKL1%2FJQYdDlu%2F4jmio3SP5wP6hf2haKSLRLutIYm0AWnqCjN7WEsmtXguRn0m3zVUcTA4%2FMZ6jF11qMXk67PeF%2FN02iFc5HyLnBUlAWXUoRcNQCXCo%2B5KwhCcU87BaadK9Nw8wfJlxmXtey26OmOPcuYY7bHEdb2c6E4RRgEwXziXat9gRgsGI%2BXmQmKxgLNDRtEwK2tkLKX9RO0wqX5dQaen88IxVeaCZ5DVkJZXljmkF%2BfgxoXy3y5k9%2F6YDyzmUNw1fjUAhzxuxib9bd7hOi%2FUhisSP6guXpHAlrmxVM0ZYldsbCNM8RM0I%2B%2B0051uTJOwm9Ti9zIBlAUJjiU5QC6Olxz5kQt5I27d2oBEfK7PBAQfLVRIh%2FYQuE9zQnvIUDzX0%2FBOn8jhfJnNgvDdviOL656zxQuusEFXX5Kot%2Fasw74HYvgY6pgFW6kBwLkdmgo1g2f9rKFkJj6pjg17btMPX68Fzq2EXLRuyK%2FI1Hv%2FtSdeMEAT4fLnEE%2BpcR0lqZWyZrFUU8NcMLCPgdCoSrV6ur0lWFtDwnPCEIhU0H%2B%2BUzlfjhQLoV5%2FPnC0hZuBvc9k%2Bhg6M8W6ruJG6tR9gr4KFaAABCnLmT0Cg3IPzsMixYneyzGw4ExmfSrgPfdEMWXLwzLJocOHbVRp%2Fl7En&X-Amz-Signature=40bc9d2f1d539247f6f53378ef60b8533412b6893ee4a30b73111a5e47de6fbd&X-Amz-SignedHeaders=host&x-id=GetObject)

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



