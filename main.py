import pickle
import os
from datetime import *

from functions import *

data = [
    # 전부 int임

    # masksNum = data[0]      # 마스크 잔여량
    # maskUser = data[1]      # 마스크 사용자수
    # changeDue = data[2]     # 마스크 교체주기

    # lastChange = data[3]    # 과거에 교체한 날짜
    # currentTime = data[4]   # 현재 날짜
    # changeDate = data[5]    # 미래에 교체할 날짜
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


def printMainMenu():
    print("*"*50)
    print("이 화면은 60초마다 업데이트됩니다.")
    maskStatus()
    print("*"*50)
    print("원하시는 기능을 선택해주세요!")
    print()
    print("1. 마스크를 더 구매했다면?")
    print("2. 설정")
    print("3. 나가기")
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
        if load() == "noData":
            data = setting()
    else:
        print("선택지의 숫자를 입력해주세요!")


def mainSelection(SelectNum):
    global data

    if SelectNum == "1":
        # 마스크 구매
        data[0] += buyingMask()
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


def maskStatus():
    global data
    masksNum = data[0]      # 마스크 잔여량
    maskUser = data[1]      # 마스크 사용자수
    changeDue = data[2]     # 마스크 교체주기

    lastChange = data[3]    # 과거 교체한 날짜
    currentTime = data[4]   # 현재 날짜
    changeDate = data[5]    # 미래 교체할 날짜

    print("<{}>".format(currentTime))
    if currentTime == lastChange:
        print("<!!!! 오늘은 마스크 바꾸는 날입니다 !!!!>")
    print((masksNum // maskUser) * changeDue)
    if (masksNum // maskUser) * changeDue <= 7:
        print("<!!!! {}일 뒤 마스크가 바닥납니다 !!!!>".format(
            (masksNum // maskUser) * changeDue))
    print("현재 마스크 재고:\t {}개".format(masksNum))
    print("마스크 사용자수:\t {}명".format(maskUser))

    print("마지막으로 마스크를 바꾼 날짜:\t", lastChange)
    print("다음 마스크 교체날짜:\t\t", changeDate)
    print("마스크 교체 주기:\t {}일".format(changeDue))


def load():
    global data

    # if not os.path.isfile("maskData.txt"):
    #     print("아직 저장된 데이터가 없습니다!")
    #     return "noData"

    with open("maskData.dat", "rb") as file:
        data = pickle.load(file)
    print("마지막 데이터를 로드했습니다!")


def main():
    global data
    startMenu()
    startSelect()

    while True:
        data = updateData(data)

        with open("maskData.dat", "wb") as file:
            pickle.dump(data, file)

        printMainMenu()

        SelectNum = readInput(60)
        if SelectNum != "nothing":
            if mainSelection(SelectNum) == "quit":
                break


main()
