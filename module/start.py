from datetime import *


def intInput():
    while True:
        num = input("> ")
        if num.isdigit():
            return int(num)
        else:
            print("정확한 정수값을 입력해주세요!")


def setting():
    print("현재 마스크 재고를 입력해주세요!")
    masks = intInput()
    print("마스크를 사용할 가족 구성원 수를 입력해주세요!")
    user = intInput()
    print("마스크를 며칠에 한 번씩 교체할지 입력해주세요!")
    changeDue = intInput()

    currentTime = date.today()

    lastChange = currentTime

    return [masks, user, changeDue, currentTime, lastChange]


def load():
    pass
