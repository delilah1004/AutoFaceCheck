# 출석 진행 과목 선택 창 UI 및 기능

from PyQt5 import QtCore, QtGui, QtWidgets
import auto_check
import auto_late_check
import static
import pymysql
import etc_module

class Ui_MainWindow_subject(object):
    def __init__(self):
        self.classList = []
        self.classCodeList = []
        self.staticData = static.staticVar

    def callClass(self):
        
        userID = self.staticData.profID
        print(userID)
        
        conn = pymysql.connect(host='localhost', user='root', password='asd1234',
                                db='autofacecheck', charset='utf8')


        # Connection 으로부터 Cursor 생성
        curs = conn.cursor()

        sqlSetClass = "SELECT * FROM profsubject WHERE profId = %s;"
        curs.execute(sqlSetClass, (userID))
        tmpClassList = curs.fetchall()
        
        conn.commit()
        conn.close()

        if(len(tmpClassList)>0):
            print("choose class")

            for c in tmpClassList:
                subject = c[1]
                subjectNum = c[0]
                self.classList.append(subject)
                self.classCodeList.append(subjectNum)

            print(self.classList)

        else:
            print("no class")


    def setupUi(self, MainWindow_subject):
        self.callClass()

        MainWindow_subject.setObjectName("MainWindow_subject")
        MainWindow_subject.resize(448, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow_subject)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 421, 251))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 101, 81))
        self.pushButton.setObjectName("pushButton")
        ###check 버튼 클릭 이벤트
        self.pushButton.clicked.connect(self.btn1_clicked)
        ###
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 140, 101, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        ###late 버튼 클릭 이벤트
        self.pushButton_2.clicked.connect(self.btn2_clicked)
        ###
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(60, 60, 301, 71))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItem("")
        for cb in self.classList:
            self.comboBox.addItem("")
        
        self.horizontalLayout.addWidget(self.comboBox)
        MainWindow_subject.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow_subject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_subject.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow_subject)
        self.statusbar.setObjectName("statusbar")
        MainWindow_subject.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_subject)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_subject)

    def retranslateUi(self, MainWindow_subject):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_subject.setWindowTitle(_translate("MainWindow_subject", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow_subject", "Subject List"))
        self.pushButton.setText(_translate("MainWindow_subject", "Check"))
        self.pushButton_2.setText(_translate("MainWindow_subject", "Late"))
        self.label.setText(_translate("MainWindow_subject", "Name"))
        self.comboBox.setItemText(0, _translate("MainWindow_subject", " - - - - - select - - - - - "))
        
        index = 0
        for cl in self.classList:
            index = index + 1
            self.comboBox.setItemText(index, _translate("MainWindow_subject", cl))

            if index == len(self.classList):
                break
    
    def btn1_clicked(self):
        comboBoxText = str(self.comboBox.currentText())
        
        # subject 선택 안됨
        if 'select' in comboBoxText:
            print("choose another class")

        else:
            classIndex = 0
            for c in self.classList:

                if comboBoxText == c:
                    break
                
                classIndex = classIndex + 1
            
            classCode = str(self.classCodeList[classIndex])
            etc_module.CreateTable(classCode)
            auto_check.checkNormalityStart()

    def btn2_clicked(self):
        auto_late_check.checkLateStart()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_subject = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_subject()
    ui.setupUi(MainWindow_subject)
    MainWindow_subject.show()
    sys.exit(app.exec_())