# 시작하면 메뉴가 떠야 함.

# 메뉴는 다음과 같음
#     마스크 상황
#     마스크 구매하기
#     설정
#     나가기
# 각각의 기능은 함수로 나누고 메인함수에 모아보기.
# 너무 큰 파일은 그냥 나눠서 한 다음 임포트해서 쓰자. 

def startMenu():
    print("*"*50)
    print("어서오세요! 마스크 종합관리 시스템입니다.")
    print()
    print("1. 시작하기")
    print("2. 로드")

def printMainMenu():
    print("*"*50)
    print("원하시는 기능을 선택해주세요!")
    print()
    print("1. 현재 당신의 마스크 상황")
    print("2. 마스크 구매하기")
    print("3. 설정")
    print("4. 나가기")
    print()
    print("*"*50)

def mainSelection():
    SelectNum = input("> ")
    if SelectNum == "1":
        # 현재 마스크 상황
        pass
    elif SelectNum == "2":
        # 마스크 구매하기
        pass
    elif SelectNum == "3":
        # 설정
        pass
    elif SelectNum == "4":
        # 나가기
        return "quit"
    else:
        print("선택지의 숫자를 입력해주세요!")

    return "continue"

def main():
    
    printMainMenu()
    while mainSelection() == "continue":
        printMainMenu()
    
main()