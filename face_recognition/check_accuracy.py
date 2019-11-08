# 출석 반영 여부 정확도 향상 모듈

import static

def CheckAccuracy(checkName):

    dicList = static.staticVar.checkDictionary
    
    # 이름이 있으면 값 1 추가
    if checkName in dicList:
        dicList[checkName] += 1 

    # 없으면 default 1 설정해주고 생성
    else:
        dicList[checkName] = 1