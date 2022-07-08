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

    return {masks, user, changeDue}


def load():
    pass


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
    SelectNum = input("> ")
    if SelectNum == "1":
        setting()
    elif SelectNum == "2":
        load()
