import pymysql

def lateListCheck():

    print("정상출석부와 대조 시작")

    absenceNum = 0

    # MySQL 데이터 처리
    # MySQL Connection 셋팅
    # conn = pymysql.connect(host='localhost', user='root', password='as097531',
    #                     db='autofacecheck', charset='utf8')

    ##### 다은이 DB
    conn = pymysql.connect(host='localhost', user='root', password='asd1234',
                        db='autofacecheck', charset='utf8')

    curs = conn.cursor()

    #전체 출석부 출력
    sql = "select * from stuList;"
    curs.execute(sql)
    stuList = curs.fetchall()

    for stu in stuList:

        stuId = stu[1]
        stuName = stu[2]

        nCheckSql = "select count(*) as cnt from checknormality where stuID = %s;"
        curs.execute(nCheckSql, stuId)
        existStuN = curs.fetchone()[0]

        #정상출석부에 수강생 없을 경우 실행
        if existStuN < 1:

            # 지각생 리스트에 있는지 확인(예외처리를 위함)
            aCheckSql = "select count(*) as cnt from checkabsence where stuID = %s;"
            curs.execute(aCheckSql, stuId)
            existStuA = curs.fetchone()[0]

            #기존 리스트에 없었으므로 디비에 반영
            if existStuA < 1:
                absenceInsertSql = "insert into checkabsence(stuId,stuName) values (%s, %s);"
                curs.execute(absenceInsertSql, (stuId, stuName))
                absenceNum += 1
                print("결석 인원 체크 : " + str(absenceNum) + "명")

            else:
                print("")

        else:
            print("결석 여부 체크 중입니다")

    aCheckSql = "select count(*) as cnt from checkabsence;"
    curs.execute(aCheckSql)
    absenceNum = curs.fetchone()[0]

    print("결석자는 총 " + str(absenceNum) + "명 입니다.")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    print("결석자 분류 시작")
    lateListCheck()