# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# 버튼 클릭시 넘어가는 창 참조
from subject import Ui_MainWindow_subject
# login 버튼 누르면 subject 창으로 넘어가기
import pymysql
import static

class Ui_MainWindow_login(object):
    def dbConnect(self):

            idd = int(float(self.lineEdit_user.text()))
            # idd = str(self.lineEdit_user.text())
            pww = str(self.lineEdit_password.text())

            # MySQL 데이터 처리
            # MySQL Connection 셋팅
            # conn = pymysql.connect(host='localhost', user='root', password='ghwns4825',
            #                     db='autofacecheck', charset='utf8')

            ##### 다은이 DB
            # conn = pymysql.connect(host='localhost', user='root', password='asd1234',
            #                     db='autofacecheck', charset='utf8')

            conn = pymysql.connect(host='localhost', user='root', password='asd1234',
                                db='autofacecheck', charset='utf8')


            # Connection 으로부터 Cursor 생성
            curs = conn.cursor()


            # print(idd)
            # print(pww)
            # print(str(type(idd)))
            # print(str(type(pww)))

            # sqlCount = "select count(*) as cnt from stuList where stuID = %s;"
            # curs.execute(sqlCount, int(userInfo))
            # existStu = curs.fetchone()[0]
            sqlLogin = "SELECT * FROM proflist WHERE profId = %s AND profPW = %s ;"
            curs.execute(sqlLogin, (idd, pww))
            # print(len(curs.fetchall()))
            if(len(curs.fetchall())>0):
                print("user found")
                static.staticVar.profID = idd
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow_subject()
                self.ui.setupUi(self.window)
                MainWindow_login.hide()
                self.window.show()
            else:
                print("user not found")

    
    def openWindow(self):
        self.dbConnect()
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_MainWindow_subject()
        # self.ui.setupUi(self.window)
        # MainWindow_login.hide()
        # self.window.show()

    def setupUi(self, MainWindow_login):

        MainWindow_login.setObjectName("MainWindow_login")
        MainWindow_login.resize(448, 313)
        MainWindow_login.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow_login)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 421, 261))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)

        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.groupBox.setObjectName("groupBox")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_3.setGeometry(QtCore.QRect(40, 60, 341, 161))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setHandleWidth(30)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_user = QtWidgets.QLabel(self.splitter)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_user.setFont(font)
        self.label_user.setObjectName("label_user")
        self.lineEdit_user = QtWidgets.QLineEdit(self.splitter)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_password = QtWidgets.QLabel(self.splitter_2)

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.lineEdit_password = QtWidgets.QLineEdit(self.splitter_2)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.splitter_2)
        self.pushButton_login = QtWidgets.QPushButton(self.splitter_3)

        font = QtGui.QFont()
        font.setPointSize(16)

        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")

        #버튼 클릭 이벤트 연결
        self.pushButton_login.clicked.connect(self.dbConnect)
        MainWindow_login.setCentralWidget(self.centralwidget)

        # 메뉴바 UI
        self.menubar = QtWidgets.QMenuBar(MainWindow_login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 21))
        self.menubar.setObjectName("menubar")

        MainWindow_login.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow_login)
        self.statusbar.setObjectName("statusbar")

        MainWindow_login.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_login)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_login)

    def retranslateUi(self, MainWindow_login):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_login.setWindowTitle(_translate("MainWindow_login", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow_login", "Auto Face Check"))
        self.label_user.setText(_translate("MainWindow_login", "User              "))
        self.label_password.setText(_translate("MainWindow_login", "Password     "))
        self.pushButton_login.setText(_translate("MainWindow_login", "LOGIN"))

    # def pushButton_login(event=None):
    #     dbConnect(self, userInfo)
    #     if lineEdit_user.get() != "" and lineEdit_password.get() != "":
    #         curs.execute("SELECT * FROM `test` WHERE `id` = ? AND `pw` = ?", (lineEdit_user.get(), lineEdit_password.get()))
    #         if curs.fetchone() is not None:
    #             lineEdit_user.set("")
    #             lineEdit_password.set("")
    #             self.pushButton_login.clicked.connect(self.openWindow)
    #     curs.close()


    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_login = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_login()
    ui.setupUi(MainWindow_login)
    MainWindow_login.show()
    sys.exit(app.exec_())
