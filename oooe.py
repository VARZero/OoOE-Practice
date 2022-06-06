virtualReg = {}
# 가상 레지스터 매핑용 {실제 Reg, 시작pc, 소멸pc, 사용하는 총 횟수, 사용된 횟수}, 20개 존재

# Reservation Queue
RQalu = [] # RQ add, sub
RQaluMul = [] # RQ add, sub, mul, div
RQld = [] # RQ load
RQst = [] # RQ store
RQfp = []
RQbranch = [] # RQ branch [pc, cycle]

RB = [] # Reorder buffer

opcodeFile = open("opcode.ocb", "r") # 명령어 파일
outCycleInfo = open("cycleInfo.txt","w") # 진행된 코드 파일

def virtualRegMapping(opcode):
    # 레지스터 매핑 및 가상 레지스터 갯수 제한용
    if opcode[0] =
    return outop

def mappingRQ(opcode):
    # RQ에 매핑하는 부분