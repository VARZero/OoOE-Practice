virtualReg = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
# 가상 레지스터 매핑용 [실제 Reg, 시작pc, 소멸pc], 20개 존재 / RMT
Logic_VirtualBoard = {"sp": None, "status": None, "Back": None, 
    "r0": None, "r1": None, "r2": None, "r3": None, 
    "r4": None, "r5": None, "r6": None, "r7": None,
    "r8": None, "r9": None, "r10": None, "r11": None
} # 논리 레지스터가 가장 마지막에 어떤 가상 레지스터에 매핑되어 있는지 여부 저장

# Reservation Queue
RQalu = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # RQ add, sub
RQaluMul = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # RQ add, sub, mul, div
RQld = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # RQ load
RQst = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # RQ store
RQfp = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
RQbranch = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # RQ branch [pc, cycle]

ReoBu = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ] # Reorder buffer

opcodeFile = open("opcode.ocb", "r") # 명령어 파일
outCycleInfo = open("cycleInfo.txt","w") # 진행된 코드 파일

def decoderMC(Mcode):
    # 디코더, 머신코드를 인자로 받고 uCode를 리턴(mci-Machine Code Info)
    mci = list() # [pc, opcode, opcode의 종류, Rt, R1, R2]
    # Opcode의 종류: 0-ALU / 1-Load / 2-FP / 3-Store / 4-branch / 5-error
    
    mci[0] = Mcode.split() # pc
    mci[1] = Mcode.split() # opcode

    # opcode type
    if Mcode[0] == "add" or Mcode[0] == "sub" or Mcode[0] == "mul" or Mcode[0] == "div": mci[2] = 0
    elif Mcode[0] == "ld": mci[2] = 1
    elif Mcode[0] == "fsadd" or Mcode[0] == "fssub" or Mcode[0] == "fsmul" or Mcode[0] == "fsdiv": mci[2] = 2
    elif Mcode[0] == "st": mci[2] = 3
    elif Mcode[0] == "branch": mci[2] = 4
    else: mci[2] = 5
    
    mci[3] = code.split() # Rt
    mci[4] = code.split() # R1
    mci[5] = code.split() # R2

    return mci

def virtualRegMapping(uCode):
    # 레지스터 매핑 및 가상 레지스터 갯수 제한용, uCode를 인자로 받고 가상 레지스터가 매핑된 uCode를 리턴
    # 그러나, 매핑이 불가능 한 경우, 0을 리턴 (다시 호출 필요)

    vir_uCode = [uCode[0], uCode[1], uCode[2], 0, uCode[3], 0, uCode[4], 0, uCode[5]] # 레지스터가 가상인지 논리인지 저장

    
    # Opcode 종류에 따라 새로운 가상 레지스터를 매핑할지 존재하는 가상 레지스터를 매핑할지 확인
    if uCode[3] == "zero": # 일단 목적지 레지스터가 0이면 의미 없음.
        vir_uCode[3] = "zero"
    elif uCode[2] <= 2:
        # 비어있는 가상 레지스터 찾기
        i = 0
        for vreg in virtualReg:
            if vreg == []:
                break
            i += 1
            if i == virtualReg.count(): # 가상 레지스터의 유효공간이 꽉찬경우 매핑 불가능
                return 0

        # 매핑이 가능할때
        virtualReg[i] = [uCode[3], uCode[0], None]
        if Logic_VirtualBoard[uCode[3]] == None:
            # 한번도 해당 논리 레지스터가 매핑된 경우가 없다면
            Logic_VirtualBoard[uCode[3]] = i 
        elif Logic_VirtualBoard[uCode[3]] != None:
            # 한번이라도 해당 논리 레지스터가 매핑된 경우
            virtualReg[Logic_VirtualBoard[uCode[3]]][2] = uCode[0] # 소멸 등록 (소멸 자체는 function unit에서 진행)
            Logic_VirtualBoard[uCode[3]] = i
    
        vir_uCode[3] = 1
        vir_uCode[4] = i
    else:
        # 해당 논리 레지스터를 찾고 가상 레지스터를 기록 
        vir_uCode[2] = Logic_VirtualBoard[uCode[3]]

    # R1, R2가 연결되는 부분이 있는지 확인 및 지정 (0은 그냥 무시)
    if uCode[4] != "zero" or Logic_VirtualBoard[uCode[4]] != None:
        vir_uCode[5] = 1
        vir_uCode[6] = Logic_VirtualBoard[uCode[4]]
    if uCode[5] != "zero" or Logic_VirtualBoard[uCode[5]] != None:
        vir_uCode[7] = 1
        vir_uCode[8] = Logic_VirtualBoard[uCode[4]]

    return vir_uCode

def mappingRQ(vir_uCode):
    # RQ에 매핑하는 부분
    
    return 0