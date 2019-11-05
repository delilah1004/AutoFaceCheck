import pymysql
import static

def lateListCheck():

    print("정상출석부와 대조 시작")

    staticData = static.staticVar

    # MySQL 데이터 처리
    # MySQL Connection 셋팅
    conn = pymysql.connect(host='localhost', user='root', password='as097531',
                        db='autofacecheck', charset='utf8')

    ##### 다은이 DB
    # conn = pymysql.connect(host='localhost', user='root', password='asd1234',
    #                     db='autofacecheck', charset='utf8')

    curs = conn.cursor()

    # 전체 출석부 출력
    sqlList = "select * from stuList;"
    curs.execute(sqlList)
    stuList = curs.fetchall()

    for stu in stuList:

        stuId = stu[1]
        stuName = stu[2]

        # 정상 출석부에 있는지 확인
        sqlCountN = "select count(*) as cnt from " + staticData.checkTable + " where stuID = %s;"
        curs.execute(sqlCountN, stuId)
        existStuN = curs.fetchone()[0]

        # 지각생 리스트에 있는지 확인
        sqlCountL = "select count(*) as cnt from " + staticData.lateTable + " where stuID = %s;"
        curs.execute(sqlCountL, stuId)
        existStuL = curs.fetchone()[0]

        # 결석자 명단에 있는지 확인
        sqlCountA = "select count(*) as cnt from " + staticData.absenceTable + " where stuId = %s;"
        curs.execute(sqlCountA, stuId)
        existStuA = curs.fetchone()[0]

        # 전체 출석부 명단에 있는 수강생과 정상 출석부 있는 사람들 비교, 정상 출석부에 없으면
        if existStuN < 1:

            # 지각자 명단, 결석자 명단에도 없음
            if existStuL < 1 and existStuA < 1:

                # 결석자 명단에 추가
                sqlInsertA = "insert into " + staticData.absenceTable + "(stuId,stuName) values (%s, %s);"
                curs.execute(sqlInsertA, (stuId, stuName))

                print("결석자 확인 중")

            # 어느하나라도 있으면 안됨
            else:
                print("지각자 명단 대조 중")

        else:
            continue

    absenceNumSql = "select count(*) as cnt from " + staticData.absenceTable +";"
    curs.execute(absenceNumSql)
    absenceNum = curs.fetchone()[0]
    print("결석자는 총 " + str(absenceNum) + "명 입니다.")

    conn.commit()
    conn.close()

def checkAbsenceStart():
    print("결석자 분류 시작")
    lateListCheck()