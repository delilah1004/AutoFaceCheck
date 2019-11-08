# 출석부 동적 생성 모듈

from datetime import datetime
import pymysql
import static

def CreateTable(classCode):
    
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

# 출석 반영 여부 정확도 향상 모듈
def CheckAccuracy(checkName):

    dicList = static.staticVar.checkDictionary
    
    # 이름이 있으면 값 1 추가
    if checkName in dicList:
        dicList[checkName] += 1 

    # 없으면 default 1 설정해주고 생성
    else:
        dicList[checkName] = 1




#######################################################################################
        # # knowns 디렉토리 모음
        # dirname = 'knowns'
        # self.fname = 'exp'

        # # jpg 담긴 폴더들
        # folders = os.listdir(dirname)

        # # 각 폴더들 참조
        # for folder in folders:
        #     files = os.listdir(folder)
        #     self.fname = folder
        #     print(files)

        #     for filename in files:
        #         name, ext = os.path.splitext(filename)
        #         name = self.fname

        #         if ext == '.jpg':
        #             self.known_face_names.append(name)
        #             pathname = os.path.join(folder, filename)
        #             img = face_recognition.load_image_file(pathname)
        #             face_encoding = face_recognition.face_encodings(img)[0]
        #             self.known_face_encodings.append(face_encoding)

        #######################################################################################