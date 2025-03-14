# [C] 토이프로젝트: 단어 맞추기 게임



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



> GPT 에게 바로 물어보지 말고, 코딩도장에서 관련 자료를 찾아서 오픈 북 형태로 실습 진행.



# 명세

C 언어 초보자를 위한 간단한 “단어 맞추기 게임” 프로젝트를 추천합니다.

🛠 프로젝트: 단어 맞추기 게임 (Word Guess Game)

설명

•	프로그램이 랜덤한 단어를 고릅니다.

•	사용자가 한 글자씩 입력하여 단어를 맞춰야 합니다.

•	제한된 횟수 내에 맞추지 못하면 게임 오버!

•	맞춘 글자는 화면에 표시되고, 틀린 글자는 카운트됩니다.

📌 구현 기능

1.	랜덤 단어 선택: 미리 정의된 단어 리스트에서 하나를 랜덤 선택.

2.	사용자 입력 처리: 한 글자씩 입력받고 맞는지 체크.

3.	화면 출력: 맞춘 글자는 보이고, 아직 못 맞춘 글자는 _로 표시.

4.	기회 제한: 정해진 횟수(예: 6회) 안에 못 맞추면 게임 오버.

5.	게임 종료 조건: 단어를 모두 맞추면 승리 메시지 출력.

📜 예제 실행 화면

```plain text
단어 맞추기 게임 시작! (단어 길이: 5)
_ _ _ _ _
입력하세요: a
틀렸습니다! 남은 기회: 5
_ _ _ _ _
입력하세요: e
맞았습니다!
_ e _ _ _
입력하세요: l
맞았습니다!
_ e l l _
입력하세요: o
축하합니다! 단어를 맞췄습니다: hello 🎉
```

📌 사용해야 할 C 언어 개념

✅ char 배열과 문자열

✅ rand()를 활용한 랜덤 단어 선택

✅ scanf()를 사용한 사용자 입력

✅ for와 while 루프

✅ if-else 조건문

이 프로젝트를 하면 배열, 문자열, 반복문, 조건문을 자연스럽게 익힐 수 있어요.

어떻게 시작할지 막막하면 기본 틀을 잡아줄 수도 있어요! 🚀



# 목표: 단어 배열을 생성하기.

```c
	char words[10][20] = {
		{"Hello"},
		{"Hebrew"},
		{"English"},
		{"Obama"},
		{"Folks"},
		{"I'll be back"},
		{"Be quiet"},
		{"Always"},
		{"Donald Trump"},
		{"Putin will send tea"}
	};
```

이렇게 하면 됨. c언어의 경우 배열 길이가 겹치면 그냥 덮어 써버린다.

# 목표: 0~9 사이의 랜덤 숫자를 생성해서 단어 선택

```c
#include <time.h>
#include <stdlib.h>
....
srand(time(NULL)); // 난수 시드 초기화
int random = 0; // 정수형 변수 선언
int r = rand()%10;      // Returns a pseudo-random integer between 0 and RAND_MAX.
```

# 목표: char 입력받기

```c
    while(true){
        char c1;
        printf("문자를 입력하세요: ");
        scanf("%c", &c1);    // 문자를 입력받아서 변수에 저장
        
        printf("%c\n",  c1);
    }
```

### % 기호: 형식 지정자(Format Specifier)

•	%는 입력 형식을 지정하는 기호로, scanf()가 입력받을 데이터의 타입을 해석하는 기준이 된다.

•	%c: 한 글자(char) 입력을 의미한다.

### & 기호: 주소 연산자(Address-of Operator)

•	&는 변수의 메모리 주소를 가져오는 연산자다.

•	scanf()는 입력된 데이터를 변수에 저장해야 하는데, 이를 위해 변수의 주소를 전달해야 한다.

📌 왜 주소를 전달해야 할까?

•	scanf()는 함수 내부에서 입력된 값을 변수에 저장하는데, 값 자체가 아니라 주소를 알아야 해당 변수의 메모리 공간을 변경할 수 있기 때문이다.

### 추가: *(포인터 연산자, Dereference Operator & Pointer Declaration)

1. 포인터 선언 (Pointer Declaration)

•	*는 포인터 변수를 선언할 때 사용한다.

•	포인터는 특정 타입의 변수 주소를 저장하는 변수이다.

🚀 즉, &는 주소를 얻고, *는 주소에 저장된 값을 가져온다!

# 목표: 맞춘 글자는 보이고, 아직 못 맞춘 글자는 _로 표시.

어떻게? 일단 under bar를 글자 수 만큼 출력하는 방법을 모르겠다. 문자열의 길이는 어떻게 알 수 있는가?

```c
#include <string.h>
//
strlen(char_var)
```

일단은 이렇게 하면 된다. 

전체 코드

```c
#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h> // rand() 함수 포함 라이브러리
#include <time.h>
#include <stdbool.h>    // bool, true, false가 정의된 헤더 파일
#include <string.h>


int main()
{    
    srand(time(NULL));

	char words[10][20] = {
		{"hello"},
		{"hebrew"},
		{"english"},
		{"japan"},
		{"folks"},
		{"holiday"},
		{"france"},
		{"always"},
		{"donald"},
		{"russia"}
	};
    int random = 0;

    random = rand()%10;
    long char_len = strlen(words[random]);
    printf("%d\n", random);
    printf("%s\n", words[random]);
    printf("%zu\n", char_len);

    while(true){
        char c1;
        printf("문자를 입력하세요: ");
        scanf(" %c", &c1);    // 문자를 입력받아서 변수에 저장
        // printf("%c\n",  c1);
        bool flag = false;
        // iterate on each 
        for(int i = 0; i < 10; i++){
            if (words[random][i] == c1){
                flag = true;
            }
        };
        if(flag){
            printf("correct!\n");
        }
        else{
            printf("wrong!\n");
        }
    }
};
```

그렇다면, 일단 boolean 타입의 배열을 정의해서 그에 따라 순회하며 reveal the characters according to iterated boolean variables.



# 이슈: strlen 컴파일 에러

## Phase1. 

### 환경

macOS, arm64, C

### 로그

```c
main.c:31:20: warning: format specifies type 'int' but the argument has type 'unsigned long' [-Wformat]
31 |     printf("%d\n", strlen(words[random]));
|             ~~     ^~~~~~~~~~~~~~~~~~~~~
|             %lu
1 warning generated.
```

### 최근 변경사항

아래 코드 작성.

```c
printf("%d\n", strlen(words[random])); 
```

## Phase2-1. 해결

### 확인

로그를 통해 확인할 수 있다시피 strlen의 반환 타입은 unsigned long. 이를 포매팅하는 예약어는 %zu.

### 시도

```c
printf("%zu\n", strlen(words[random]));
```

### 결과분석

제대로 출력 됨.

# 이슈: 문자열 하나를 처리하고 반복문이 다음 텀으로 넘어가버림. 

One iteration should process only one char.

에러는 아니고 그냥 논리를 완성해야 하는 부분. 

일단, getchar이나 scanf는 다 캐릭터 하나하나를 처리한다. 그럼 그렇게 안 하려면? 

아래와 같은 코드로 변경하면 된다.

```c

				char input_word[MAX_WORD_LEN];
        printf("문자를 입력하세요: ");
        scanf(" %s", input_word);    // 문자를 입력받아서 변수에 저장(입력값 포매팅에 공백이 필요.)
        bool flag = false;
        for(int i = 0; i < char_len; i++){
            // should be nested loop
            long input_len = strlen(input_word);
            for(int j = 0; j < input_len; j ++){
                if (words[random][i] == input_word[j]){
                    flags[i] = true;
                }
            }
        };
```

# 완성

```c
#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h> // rand() 함수 포함 라이브러리
#include <time.h>
#include <stdbool.h> // bool, true, false가 정의된 헤더 파일
#include <string.h>
#define MAX_TRIAL 5
#define MAX_WORD_LEN 20

int main()
{
    srand(time(NULL));

    char words[10][MAX_WORD_LEN] = {
        {"hello"},
        {"hebrew"},
        {"english"},
        {"japan"},
        {"folks"},
        {"holiday"},
        {"france"},
        {"always"},
        {"donald"},
        {"russia"}};
    // all set by false.
    bool flags[MAX_WORD_LEN];
    int random = 0;
    int trial = 1;
    random = rand() % 10;
    long char_len = strlen(words[random]);
    printf("%d\n", random);
    printf("%s\n", words[random]);
    printf("5번만에 단어를 맞춰 보세요\n");

    while (true)
    {
        char input_word[MAX_WORD_LEN];
        bool flag = false;
        int correct_sum = 0;
        
        printf("문자를 입력하세요: ");
        scanf(" %s", input_word); // 문자를 입력받아서 변수에 저장(입력값 포매팅에 공백이 필요.)
        for (int i = 0; i < char_len; i++)
        {
            // should be nested loop
            long input_len = strlen(input_word);
            for (int j = 0; j < input_len; j++)
            {
                if (words[random][i] == input_word[j])
                {
                    flags[i] = true;
                    // if this condition has been ran multiple times as much as the length of the character,
                    // user got the answer
                    correct_sum++;
                }
            }
        };
        for (int i = 0; i < char_len; i++)
        {
            if (flags[i])
                printf("%c", words[random][i]);
            else
                printf("_");
        }
        printf("\n");
        // game stop logic
        // user can win even the max trial hit at the final loop.
        trial++;
        if (correct_sum >= char_len){
            printf("정답입니다!\n");
            break;

        }
        if (trial > MAX_TRIAL)
        {
            printf("제한 횟수 초과!\n");
            break;
        }
    }
};
```

