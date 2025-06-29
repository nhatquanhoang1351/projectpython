from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 80, 121, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setToolTipDuration(0)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./icon/logoeaut.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 330, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 390, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.username_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(270, 330, 241, 31))
        self.username_input.setObjectName("username_input")
        
        self.password_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(270, 390, 241, 31))
        self.password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  
        self.password_input.setObjectName("password_input")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 450, 131, 31))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Đăng nhập"))
        self.label_3.setText(_translate("MainWindow", "Tài khoản"))
        self.label_4.setText(_translate("MainWindow", "Mật khẩu"))
        self.pushButton.setText(_translate("MainWindow", "Đăng nhập"))


class LoginWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, on_login_success):
        super().__init__()
        self.setupUi(self)
        self.on_login_success = on_login_success  
        self.pushButton.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin":
            self.on_login_success() 
            self.close()  
        else:
            QMessageBox.warning(self, "Lỗi", "Tài khoản hoặc mật khẩu không đúng")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    def on_login_success():
        print("Đăng nhập thành công!")

    login_window = LoginWindow(on_login_success)
    login_window.show()
    sys.exit(app.exec())