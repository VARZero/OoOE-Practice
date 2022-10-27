#include <stdio.h>

/*  ###############################################################
	명령어의 처리 순서 구상
	---------------------------------------------------------------
	1. I.R을 통해 명령어가 들어옴
	2. I.R에서 명령어 4개를 추출 후 Decoder로 옮김
	3. Decoder에서 명령어 처리, Renamer로 옮김
	4-1. Renamer에서 Rt 레지스터를 가상 레지스터로 바꿈
	4-2. Renamer에서 R1, R2 레지스터가 종속성이 있는지 확인
	5. Renamer에서 종속성이 있는 레지스터를 연결되는 가상 레지스터로 변경
	6. Renamer에서 가상 레지스터로 변경된 명령어를 RUU에 저장
	############################################################### */

/* 최초로 들어오는 명령어의 구조, 코드의 이해를 돕기 위해 작성된 부분
struct instr_One{
	unsigned int addr; 32비트 / 해당 명령어의 주소 저장
	unsigned char opcode; 5비트 / 해당 명령어 opcode 저장 
	unsigned char func; 2비트 / 명령어 세부 내용 저장
	unsigned char rt; 5비트 / 목적지가 되는 레지스터 저장
	unsigned char r1; 5비트 / 인자1이 되는 레지스터 저장
	unsigned char r2; 5비트 / 인자2이 되는 레지스터 저장
	unsigned int imm; 25비트 / 인자로 정수나 오프셋, 주소등이 들어오는 경우 저장하는 공간
}
*/

struct EndDecoding{
	unsigned int addr;
	unsigned char ops; // opcode를 cpu 내부에서 처리하기 위해 쉬운 형태로 변경한 값을 저장
	bool ops-need-tRt; // Rt를 가상 레지스터로 바꿔야 하는가? 여부 저장
	bool func[2]; // 명령어 세부내용(자료형태만 배열로 변경)
	unsigned char rt; 
	unsigned char r1;
	unsigned char r2;
	unsigned int imm;
}

struct RUUdata{
	unsigned int addr;
	unsigned int RUUaddr; // RUU 내부에서의 주소
	unsigned int pre-BR-addr; // 필수 선행 명령어 주소 저장
	unsigned char ops;
	unsigned char func;
	unsigned char tRt; // 가상 레지스터
	unsigned char rRt; // 실제 레지스터
	unsigned int value; // rRt에 들어가야 하는 값 
	unsigned char tR1; // 종속성을 위해 변경된 레지스터1
	unsigned char tR2; // 종속성을 위해 변경된 레지스터2
	unsigned int imm;
}

RUUdata Renamer(){
	
}

int main(){
	
}
