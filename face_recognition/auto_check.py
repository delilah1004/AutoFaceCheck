# 자동 출석 체크 모듈

import face_recognition
import cv2
import camera
import os
import numpy as np
import pymysql
import auto_absence_check
import time
import threading
import static
import etc_module

class FaceRecog():
    def __init__(self):

        # 모듈 선언
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []
        self.staticData = static.staticVar
        self.etc_module = etc_module

        # 해당 경로에 있는 이미지로 학습 시작
        dirname = 'knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        # 변수 초기화
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def dbConnect(self, userInfo):
            
            # MySQL 데이터 처리
            # MySQL Connection 셋팅
            conn = pymysql.connect(host='localhost', user='root', password='as097531',
                                db='autofacecheck', charset='utf8')

            ##### 다은이 DB
            # conn = pymysql.connect(host='localhost', user='root', password='asd1234',
            #                     db='autofacecheck', charset='utf8')

            # conn = pymysql.connect(host='localhost', user='root', password='ghwns4825',
            #                     db='autofacecheck', charset='utf8')



            # Connection 으로부터 Cursor 생성
            curs = conn.cursor()

            # 얼굴 인식 후 전체 출석부에 있는 얼굴인지 테스트 한다.
            sqlCount = "select count(*) as cnt from stuList where stuID = %s;"
            curs.execute(sqlCount, int(userInfo))
            existStu = curs.fetchone()[0]

            # 전체 출석부에 있으면 실행
            if existStu > 0:

                # 해당 학번 학생의 이름이 무엇인지 전체 출석부에서 확인
                sqlList = "select * from stuList where stuId = %s;"
                curs.execute(sqlList, int(userInfo))
                stuName = curs.fetchone()[2]

                print(stuName + " 은 해당 강의 수강생 입니다")

                # 정상 출석부에 있는지 확인
                sqlCountN = "select count(*) as cnt from " + self.staticData.checkTable + " where stuId = %s"
                curs.execute(sqlCountN, int(userInfo))
                existStuN = curs.fetchone()[0]

                # 출석자 명단에 없으면
                if existStuN < 1:

                    # 결석자 명단에 있는지 확인
                    sqlCheckA = "select count(*) as cnt from " + self.staticData.absenceTable + " where stuID = %s;"
                    curs.execute(sqlCheckA, int(userInfo))
                    existStuA = curs.fetchone()[0]

                    # 지각자 명단에 있는지 확인
                    sqlCountL = "select count(*) as cnt from " + self.staticData.lateTable + " where stuId = %s;"
                    curs.execute(sqlCountL, int(userInfo))
                    existStuL = curs.fetchone()[0]

                    # 결석자, 지각자 명단 둘 다 없으면
                    if existStuA < 1 and existStuL < 1:

                        # 정상 출석부에 반영
                        sqlInsertN = "insert into " + self.staticData.checkTable + "(stuId,stuName) values (%s, %s)"
                        curs.execute(sqlInsertN, (int(userInfo), stuName))

                        print(stuName + "은 정상 출석부에 반영되었습니다")
                    
                    # 지각 명단에 있으면
                    elif existStuA < 1 and existStuL > 0:

                        print(stuName + " 은 지각자 입니다")

                        
                    # 결석자 명단에 있으면
                    elif existStuA > 0 and existStuL < 1:

                        print(stuName + " 은 결석자 입니다")

                    else:

                        print("중복 입력 에러 입니다. DB를 확인해주세요")

                # 출석자 명단에 있으면
                else:
                    print(stuName + "은 이미 정상 출석 되어있습니다")

            else:
                print("해당 강의를 수강하지 않는 학생이 있습니다.")

            conn.commit()
            conn.close()

    # 인식 시 프레임 생성
    def get_frame(self):
        frame = self.camera.get_frame()
        
        # 이미지 리사이즈
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if self.process_this_frame:
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:

                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # 인식 못하면 unknown
                name = "Unknown"
                if min_value < 0.6:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # text, frame 커스텀
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # 인천대 db에 없는 사람일 경우
            if name == "Unknown":

                print("인천대학교 학생이 아닙니다")
            
            # 교수님일 경우
            elif 'pro' in name:
                continue

            #인천대 db에 있는 사람일 경우
            else:
                self.etc_module.CheckAccuracy(name)

        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

class TimeCheck():
    def __init__(self):
        self.runningCheck = True

    def timer(self):
        print("타이머 시작")
        threading.Timer(15, self.runningStop).start()
    
    def runningStop(self):
        self.runningCheck = False
        return self.runningCheck


def checkNormalityStart():

    print("출석체크를 시작 합니다")

    face_recog = FaceRecog()
    print(face_recog.known_face_names)

    time_check = TimeCheck()
    time_check.timer()

    while time_check.runningCheck:
        frame = face_recog.get_frame()

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF

        # 출석체크가 다 끝나지 않았는데 중간에 종료 시킬때
        if key == ord("q"):
            auto_absence_check.checkAbsenceStart()
            break
    
    for checkId, checkNum in static.staticVar.checkDictionary.items():
        if checkNum > 5:
            print(str(checkId) + " : " + str(checkNum))
            face_recog.dbConnect(checkId)
    
    static.staticVar.checkDictionary = {}

    auto_absence_check.checkAbsenceStart()
    cv2.destroyAllWindows()
    print('finish')