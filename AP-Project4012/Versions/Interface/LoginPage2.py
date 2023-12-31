# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.HomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomeButton.setGeometry(QtCore.QRect(80, 10, 131, 70))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.HomeButton.setFont(font)
        self.HomeButton.setObjectName("HomeButton")
        self.ProfileButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProfileButton.setGeometry(QtCore.QRect(80, 80, 131, 70))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.ProfileButton.setFont(font)
        self.ProfileButton.setObjectName("ProfileButton")
        self.PageTitle = QtWidgets.QLabel(self.centralwidget)
        self.PageTitle.setGeometry(QtCore.QRect(-20, 160, 315, 70))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.PageTitle.setFont(font)
        self.PageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.PageTitle.setObjectName("PageTitle")
        self.SearchBox = QtWidgets.QTextEdit(self.centralwidget)
        self.SearchBox.setGeometry(QtCore.QRect(450, 180, 321, 35))
        self.SearchBox.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.SearchBox.setTabChangesFocus(False)
        self.SearchBox.setObjectName("SearchBox")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(770, 180, 70, 35))
        self.SearchButton.setObjectName("SearchButton")
        self.NameInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameInputLabel.setGeometry(QtCore.QRect(60, 320, 231, 100))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.NameInputLabel.setFont(font)
        self.NameInputLabel.setObjectName("NameInputLabel")
        self.NameInput = QtWidgets.QTextEdit(self.centralwidget)
        self.NameInput.setGeometry(QtCore.QRect(310, 310, 310, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NameInput.setFont(font)
        self.NameInput.setObjectName("NameInput")
        self.PasswordInputLabel = QtWidgets.QLabel(self.centralwidget)
        self.PasswordInputLabel.setGeometry(QtCore.QRect(60, 400, 210, 100))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.PasswordInputLabel.setFont(font)
        self.PasswordInputLabel.setObjectName("PasswordInputLabel")
        self.PasswordInput = QtWidgets.QTextEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(310, 410, 310, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setObjectName("PasswordInput")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(50, 520, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setObjectName("SubmitButton")
        self.SignInButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignInButton.setGeometry(QtCore.QRect(260, 520, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SignInButton.setFont(font)
        self.SignInButton.setCheckable(False)
        self.SignInButton.setChecked(False)
        self.SignInButton.setAutoRepeat(False)
        self.SignInButton.setAutoDefault(False)
        self.SignInButton.setDefault(False)
        self.SignInButton.setFlat(False)
        self.SignInButton.setProperty("Wrap", False)
        self.SignInButton.setObjectName("SignInButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, -50, 381, 231))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 640, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 670, 411, 16))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.ProfileButton.setText(_translate("MainWindow", "Profile"))
        self.PageTitle.setText(_translate("MainWindow", "Login"))
        self.SearchBox.setPlaceholderText(_translate("MainWindow", "Search Here"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.NameInputLabel.setText(_translate("MainWindow", "Username or Email:"))
        self.PasswordInputLabel.setText(_translate("MainWindow", "Password:"))
        self.SubmitButton.setText(_translate("MainWindow", "Submit"))
        self.SignInButton.setText(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "Runnn!"))
        self.label_2.setText(_translate("MainWindow", "Contact us via : @comfortablynumb7 on Telegram or 09908611517"))
        self.label_3.setText(_translate("MainWindow", "Company Address : Iran - Tehran - Narmak - IUST"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
