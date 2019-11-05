from datetime import datetime
import pymysql
import static

def CreateTable(classCode):
    # classCode = str(self.classCodeList[classIndex])
    staticData = static.staticVar

    now = datetime.now()
    mToday = now.strftime('%m%d')

    # 날짜, 문자열, 구분으로 스트링 저장
    staticData.checkTable = mToday+classCode+"normality"
    staticData.lateTable = mToday+classCode+"late"
    staticData.absenceTable = mToday+classCode+"absence"

    # 디비 연결
    conn = pymysql.connect(host='localhost', user='root', password='as097531',
                        db='autofacecheck', charset='utf8')

    curs = conn.cursor()

    # 테이블 있는지 확인
    sqlExistTable = "show tables like '" + staticData.checkTable + "';"
    curs.execute(sqlExistTable)
    existTable = len(curs.fetchall())

    # 테이블 없으면
    if existTable == 0:
        creatList = [staticData.checkTable, staticData.lateTable, staticData.absenceTable]
        commentList = ['출석 db 생성 완료', '지각 db 생성 완료', '결석 db 생성 완료']
        cIndex = 0

        #테이블 생성
        for creList in creatList:
            sqlCreate =  "CREATE TABLE " + creList + """
                    (
                    attendTime timestamp default now(),
                    stuId int NOT NULL,
                    stuName VARCHAR(45) NOT NULL
                    );"""
            curs.execute(sqlCreate)

            print(commentList[cIndex])

            cIndex = cIndex + 1

    conn.commit()
    conn.close()