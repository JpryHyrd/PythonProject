from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    font = QtGui.QFont()
    font.setFamily("Segoe Print")
    font.setBold(True)
    font.setWeight(75)

    def __init__(self, gen="man"):
        self.gen = gen

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #312e2d;")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, -80, 1521, 1041))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/main-wooman.png"))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(620, -10, 16, 1161))
        self.line.setStyleSheet("color: #f1dbce;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: #f1dbce;\n"
"border: 3px solid #f1dbce;\n"
"border-radius: 30;\n"
"}\n"
"QPushButton:hover {\n"
"color: #c6594e;\n"
"border: 3px solid #c6594e;\n"
"border-radius: 30;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 300, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"color: #f1dbce;\n"
"border: 3px solid #f1dbce;\n"
"border-radius: 30;\n"
"}\n"
"QPushButton:hover {\n"
"color: #c6594e;\n"
"border: 3px solid #c6594e;\n"
"border-radius: 30;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #f1dbce;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setText("Вход")
        self.pushButton_2.setText("Регистрация")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.registration)


    def login(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #312e2d; \n"
"color: #312e2d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 370, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2 solid #f1dbce;\n"
"color: #f1dbce;\n"
"border-radius: 10;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #f1dbce;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #f1dbce;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 480, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2 solid #f1dbce;\n"
"color: #f1dbce;\n"
"border-radius: 10;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(660, 240, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: #f1dbce;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 1471, 671))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pictures/рамка.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 560, 121, 51))
        font = QtGui.QFont()
        self.label.setText("NAME")
        self.label_2.setText("PASSWORD")
        self.label_3.setText("Login")
        self.pushButton.setText("Log in")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border: 1px;\n"
"border-radius: 10;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #53504f;\n"
"color: white;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

    def registration(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        MainWindow.setStyleSheet("background-color: #312e2d; \n"
"color: #312e2d;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 210, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: #f1dbce;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 1471, 671))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pictures/рамка.png"))
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: #f1dbce;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(570, 320, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: 2 solid #f1dbce;\n"
"color: #f1dbce;\n"
"border-radius: 10;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 390, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #f1dbce;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 430, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border: 2 solid #f1dbce;\n"
"color: #f1dbce;\n"
"border-radius: 10;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 500, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("color: #f1dbce;")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(570, 540, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border: 2 solid #f1dbce;\n"
"color: #f1dbce;\n"
"border-radius: 10;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 620, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: white;\n"
"border: 1px;\n"
"border-radius: 10;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #53504f;\n"
"color: white;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.label_3.setText("Create new account")
        self.label.setText("NAME")
        self.label_2.setText("PASSWORD")
        self.label_5.setText("REPEAT PASSWORD")
        self.pushButton.setText("Sign up")
        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Money Keeper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
