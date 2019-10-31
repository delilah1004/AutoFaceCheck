# AutoFaceCheck Program

# Description
````````````````````````
  - 내용 : 카메라로 얼굴 인식 후 자동으로 출석 체크를 해주는 프로그램
  - 언어 : Python 3.6
  - DB : MySQL
  - Module : face_recognition, flask, openCV, PyMySQL
  - 기타 툴 : qtpy5, designer, JSP, Anaconda
````````````````````````
# 사전 준비 사항
````````````````````````
  - https://www.anaconda.com/distribution (아나콘다 설치)
  - conda update conda
  - pip install --upgrade pip
  - conda create -n py36 python=3.6 anaconda
  - source activate py36
  - pip install opencv-python
  - pip install opencv-contrib-python
  - pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl (반드시 해당 파일이 있는 위치에서 실행)
  - pip install face_recognition
  - pip install flask
  - python login.py (반드시 해당 파일이 있는 위치에서 실행)
````````````````````````

# 파일 설명
````````````````````````
  - camera.py -> 카메라 테스트용
  - login.py -> 로그인 UI
  - subject.py -> 강의 선택, 출석체크 버튼, 지각체크 버튼 UI
  - auto_check -> 자동 출석체크
  - auto_absence_check -> 결석자 체크
  - auto_late_check -> 지각자 체크
  - templates folder -> 수강생, 교수님 사진 등록
  - AutoFaceCheck/autofacecheck/WebContent/checklist -> 결과를 웹에서 보여줄 JSP 파일
````````````````````````
