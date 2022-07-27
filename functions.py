import os.path
import pickle
import select
import sys
from datetime import *

# int임
# masksNum = data[0]      # 마스크 잔여량
# maskUser = data[1]      # 마스크 사용자수
# changeDue = data[2]     # 마스크 교체주기

# datetime 모듈의 time.datetime 객체임.
# lastChange = data[3]    # 과거에 교체한 날짜
# currentTime = data[4]   # 현재 날짜
# changeDate = data[5]    # 미래에 교체할 날짜


def readInput(timeOut):     # 시간제한이 있는 input함수

    i, o, e = select.select([sys.stdin], [], [], timeOut)

    if (i):
        return sys.stdin.readline().strip()
    else:
        return "nothing"


def updateData(data):       # 날짜 데이터를 업데이트합니다.

    masksNum = data[0]                  # 마스크 잔여량
    maskUser = data[1]                  # 마스크 사용자수
    changeDue = data[2]                 # 마스크 교체주기

    lastChange = data[3]                # 마지막으로 교체한 날짜
    currentTime = date.today()          # 현재 날짜

    while changeDate <= currentTime:    # 교체일이거나 교체일이 지났으면
        lastChange = changeDate         # 날짜 바꾸기
        masksNum -= maskUser            # 마스크 개수 줄이기
        changeDate += timedelta(days=changeDue)  # 앞으로 바꿀 날짜

    return [masksNum, maskUser, changeDue, lastChange, currentTime, changeDate]


def intInput():             # 정수를 입력받아 정수로 반환합니다.
    while True:
        num = input("> ")
        if num.isdigit():
            return int(num)
        else:
            print("정확한 정수값을 입력해주세요!")


def setting():              # 초기 설정값을 입력받아 반환합니다.
    print("현재 마스크 재고를 입력해주세요!")
    masks = intInput()
    print("마스크를 사용할 가족 구성원 수를 입력해주세요!")
    user = intInput()
    print("마스크를 며칠에 한 번씩 교체할지 입력해주세요!")
    changeDue = intInput()

    currentTime = date.today()

    lastChange = currentTime

    return [masks, user, changeDue, lastChange, currentTime]


def buyingMask():
    pass
    print("구매하신 마스크의 수량을 입력하세요!")
    num = intInput()
    print("넵 알겠습니다!")
    return num
