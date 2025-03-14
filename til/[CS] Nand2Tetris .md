# [CS] Nand2Tetris 



> 개념과 이슈 트래킹을 조합해서 “복기 가능한” 자료를 만들도록 합니다.

> 이슈 트래킹 작성 원칙: Phase1(환경, 로그, 최근 변경사항), Phase2(확인, 시도, 결과분석) 형식으로 정리하세요. (Phase2는 최대 3회까지 반복하고 해결 안 되면 아예 처음부터 시작(불가능할 경우 도움 요청))

> 실습은 천천히, 하지만 robust하게 하세요. 



> 이 프로젝트의 경우 책에 있는 ‘구현’ 부분에서 하나씩 처리하자.

> 내일 테스트부터 하시면 됩니다. (겁나 게으르네)

# 목표: 분기 명령 테스트

## 작은 목표: BasicLoop 코드로 테스트

### VMTranslator 테스트 대상 코드

```c
    def writeLabel(self, label: str):
        asm_tmp = ''
        comment = f"// {label}\n"
        asm_tmp += f"({label})\n"
        self.result.extend([comment, asm_tmp])

    def writeGoto(self, label: str):
        asm_tmp = ''
        comment = f"// goto {label}\n"
        asm_tmp += f"@{label}\n"
        asm_tmp += f"0; JMP\n" # jump of no-condition
        self.result.extend([comment, asm_tmp])
```

