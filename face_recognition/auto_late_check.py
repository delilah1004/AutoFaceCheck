# face_recog.py

import face_recognition
import cv2
import camera
import os
import numpy as np
import pymysql

class FaceRecog():
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.camera = camera.VideoCamera()

        self.known_face_encodings = []
        self.known_face_names = []

        # Load sample pictures and learn how to recognize it.
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

        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def __del__(self):
        del self.camera

    def dbConnect(self, userInfo):
            
            # MySQL 데이터 처리
            # MySQL Connection 셋팅
            # conn = pymysql.connect(host='localhost', user='root', password='as097531',
            #                     db='autofacecheck', charset='utf8')

            #### 다은이 DB
            conn = pymysql.connect(host='localhost', user='root', password='asd1234',
                                db='autofacecheck', charset='utf8')



            # Connection 으로부터 Cursor 생성
            curs = conn.cursor()

            # 얼굴 인식 후 전체 출석부에 있는 얼굴인지 테스트 한다.
            # existStu 0이면 없는 사람, 1이면 있는 사람이다.
            sqlCount = "select count(*) as cnt from stuList where stuID = %s;"
            curs.execute(sqlCount, int(userInfo))
            existStu = curs.fetchone()[0]

            # existStu > 0 -> 전체 출석부에 이름이 있으면 실행
            if existStu > 0:
                # 해당 학번 학생의 이름이 무엇인지 전체 출석부에서 확인
                sqlList = "select * from stuList where stuId = %s;"
                curs.execute(sqlList, int(userInfo))
                stuName = curs.fetchone()[2]

                print(stuName + " 은 해당 강의 수강생 입니다")

                #############결석 출석부 absenceList에 있는지 확인
                sqlCountA = "select count(*) as cnt from checkabsence where stuId = %s;"
                curs.execute(sqlCountA, int(userInfo))
                alreadyExist = curs.fetchone()[0]

                # absenceList -> 결석 출석 출석부에 이름이 있으면 지각자로 처리 시작
                if alreadyExist > 0:

                    print(stuName + " 은 지각생 입니다")

                    # 예외처리 -> 에러 방지용
                    lateCheckSql = "select count(*) as cnt from checklate where stuId = %s;"
                    curs.execute(lateCheckSql, int(userInfo))
                    alreadyExistL = curs.fetchone()[0]

                    #지각자 명부에 안적혀 있을 경우
                    if alreadyExistL < 1:
                        absenceDeleteSql = "delete from checkabsence where stuName = %s;"
                        curs.execute(absenceDeleteSql, stuName)

                        lateInsertSql = "insert into checklate(stuId,stuName) values (%s, %s);"
                        curs.execute(lateInsertSql, (int(userInfo), stuName))

                        print(stuName + "은 지각으로 변경되었습니다")

                    else:
                        print("에러 방지")

                # 결석 출석부에 없으므로 정상 출석부에 있는 학생임
                else:
                    print(stuName + "은 정상 출석 상태 입니다")
                # className = "check"
                # checkType = "Normality"
                # tableName = className + checkType
                # createSql = """create table `autoFaceCheck`.`%s` (
                #     `attendTime` timestamp default now(),
	            #     `stuId` int NOT NULL,
                #     `stuName` VARCHAR(45) NOT NULL
                # );"""
                # curs.execute(createSql, tableName)
                # 정상 출석부에 이름을 추가


            
            else:

                print("해당 강의를 수강하지 않는 학생이 있습니다.")

            conn.commit()
            conn.close()

    def get_frame(self):
        # Grab a single frame of video
        frame = self.camera.get_frame()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                min_value = min(distances)

                # tolerance: How much distance between faces to consider it a match. Lower is more strict.
                # 0.6 is typical best performance.
                name = "Unknown"
                if min_value < 0.6:
                    index = np.argmin(distances)
                    name = self.known_face_names[index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            if name != "Unknown":
                print("인천대학교 학생 입니다")
                self.dbConnect(name)
            
            else:
                print("인천대학교 학생이 아닙니다")

        return frame

    def get_jpg_bytes(self):
        frame = self.get_frame()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()

def checkLateStart():

    print("지각체크를 시작 합니다")

    face_recog = FaceRecog()
    print(face_recog.known_face_names)
    while True:
        frame = face_recog.get_frame()

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    print('finish')