# 시작하면 메뉴가 떠야 함.

# 메뉴는 다음과 같음
#     마스크 상황
#     마스크 구매하기
#     설정
#     나가기
# 각각의 기능은 함수로 나누고 메인함수에 모아보기.
# 너무 큰 파일은 그냥 나눠서 한 다음 임포트해서 쓰자.

from turtle import delay
from module.start import *
from module.ReadInput import *
from datetime import *

data = [
    # 전부 int임

    # masksNum = data[0]      # 마스크 잔여량
    # maskUser = data[1]      # 마스크 사용자수
    # changeDue = data[2]     # 마스크 교체주기
    # currentTime = data[3]   # 현재 시간
    # lastChange = data[4]    # 마지막으로 교체한 날짜
]


def startMenu():
    print("*"*50)
    print("어서오세요! 마스크 종합관리 시스템입니다.")
    print("숫자를 입력해주세요!")
    print()
    print("1. 시작하기")
    print("2. 로드")
    print()
    print("*"*50)


def startSelect():
    global data
    SelectNum = input("> ")
    if SelectNum == "1":
        # 시작하기. 각종 기본 변수들 세팅.
        data = setting()

    elif SelectNum == "2":
        # 로드. 기본 변수들 값을 받아옴.
        load()

    else:
        print("선택지의 숫자를 입력해주세요!")


def maskStatus():
    global data
    masksNum = data[0]      # 마스크 잔여량
    maskUser = data[1]      # 마스크 사용자수
    changeDue = data[2]     # 마스크 교체주기
    currentTime = data[3]   # 현재 시간
    lastChange = data[4]    # 마지막으로 교체한 날짜
    changeDate = currentTime + timedelta(days=changeDue)

    print("<{}>".format(currentTime))
    print("현재 마스크 재고:\t", masksNum)
    print("마스크 사용자수:\t", maskUser)
    print("마지막으로 마스크를 바꾼 날짜:\t", lastChange)
    print("다음 마스크 교체날짜:\t", changeDate)
    print("마스크 교체 주기:\t {}일".format(changeDue))


def printMainMenu():
    print("*"*50)
    print("이 화면은 60초마다 업데이트됩니다.")
    maskStatus()
    print("*"*50)
    print("원하시는 기능을 선택해주세요!")
    print()
    print("1. 마스크 구매하기")
    print("2. 설정")
    print("3. 나가기")
    print()
    print("*"*50)


def mainSelection(SelectNum):
    global data

    if SelectNum == "1":
        # 마스크 구매
        pass
    elif SelectNum == "2":
        # 설정
        maskStatus()
        data = setting()
    elif SelectNum == "3":
        # 나가기
        print(data)
        return "quit"
    else:
        print("선택지의 숫자를 입력해주세요!")


def main():
    startMenu()
    startSelect()

    while True:

        printMainMenu()
        SelectNum = readInput(60)
        if SelectNum != "nothing":
            if mainSelection(SelectNum) == "quit":
                break
        data[3] = date.today()


main()


# 완전 메인 화면 따로 하나 만들고 선택지로 가는 화면을 따로 만든다.
# 지금 상황 화면을 메인 화면으로 정해두자.
# 시간 관련 코드
#     masksNum = data[0]      # 마스크 잔여량
#     maskUser = data[1]      # 마스크 사용자수
#     changeDue = data[2]     # 마스크 교체주기
#     currentTime = data[3]   # 현재 시간

# 그러니까, 오늘 날짜로부터 data[2] 만큼의 일수가 지나면 알림을 띠우면 됨.
# 즉 그만큼의 일수가 지났는지를 판단할 수 있어야 함.
# "마스크 교체일입니다." 텍스트를 메인에 띄우는 게 좋을듯.
# 전체를 루프로 묶고 한바퀴 돌 때마다 시간을 체크한다. + 저장한다.
