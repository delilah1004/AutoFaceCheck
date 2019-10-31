# AutoFaceCheck Program

# Description
````````````````````````
  - Introduce : Recognize face with camera Automatically to make attendance check
  - Language : Python 3.6
  - DB : MySQL
  - Modules : face_recognition, flask, openCV, PyMySQL
  - Tools : qtpy5, designer, JSP, Anaconda
````````````````````````

# Preparations
````````````````````````
  - https://www.anaconda.com/distribution (Install Anaconda)
  - conda update conda
  - pip install --upgrade pip
  - conda create -n py36 python=3.6 anaconda
  - source activate py36
  - pip install opencv-python
  - pip install opencv-contrib-python
  - pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl (Must run where 'dlib-19.8.1-cp36-cp36m-win_amd64.whl' file is located)
  - pip install face_recognition
  - pip install flask
  - python login.py (Must run where 'login.py' file is located)
````````````````````````

# Files & Folder
````````````````````````
  - camera.py -> For camera test
  - login.py -> Login UI
  - subject.py -> Choose Class, Bt attendence check, Bt late check
  - auto_check -> Auto Attendence Check Module
  - auto_absence_check -> Auto Absence Check Module
  - auto_late_check -> Auto Late Check Module
  - templates folder -> Student & Professor photos
  - AutoFaceCheck/autofacecheck/WebContent/checklist -> JSP File for print results
````````````````````````
