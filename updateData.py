from datetime import *

# masksNum = data[0]      # 마스크 잔여량
# maskUser = data[1]      # 마스크 사용자수
# changeDue = data[2]     # 마스크 교체주기

# lastChange = data[3]    # 마지막으로 교체한 날짜
# currentTime = data[4]   # 현재 날짜
# changeDate = data[5]    # 앞으로 교체할 날짜


def updateData(data):
    masksNum = data[0]              # 마스크 잔여량
    maskUser = data[1]              # 마스크 사용자수
    changeDue = data[2]             # 마스크 교체주기

    lastChange = data[3]            # 마지막으로 교체한 날짜
    currentTime = date.today()      # 현재 날짜
    changeDate = lastChange + timedelta(days=changeDue)

    if changeDate == currentTime:   # 교체일이면
        lastChange = currentTime    # 날짜 바꾸기
        masksNum = masksNum - maskUser

    return [masksNum, maskUser, changeDue, lastChange, currentTime, changeDate]
