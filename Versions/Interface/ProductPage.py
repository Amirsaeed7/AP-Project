# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Product_Name = QtWidgets.QLabel(self.centralwidget)
        self.Product_Name.setGeometry(QtCore.QRect(20, 100, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Product_Name.setFont(font)
        self.Product_Name.setText("")
        self.Product_Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Product_Name.setObjectName("Product_Name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 0, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 670, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 720, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Search_Box = QtWidgets.QTextEdit(self.centralwidget)
        self.Search_Box.setGeometry(QtCore.QRect(900, 120, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.Search_Box.setFont(font)
        self.Search_Box.setObjectName("Search_Box")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(819, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.Details = QtWidgets.QLabel(self.centralwidget)
        self.Details.setGeometry(QtCore.QRect(170, 180, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Details.setFont(font)
        self.Details.setAlignment(QtCore.Qt.AlignCenter)
        self.Details.setObjectName("Details")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(10, 250, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.RAM = QtWidgets.QLabel(self.centralwidget)
        self.RAM.setGeometry(QtCore.QRect(10, 300, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RAM.setFont(font)
        self.RAM.setObjectName("RAM")
        self.Storage = QtWidgets.QLabel(self.centralwidget)
        self.Storage.setGeometry(QtCore.QRect(10, 350, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Storage.setFont(font)
        self.Storage.setObjectName("Storage")
        self.Name_Label = QtWidgets.QLabel(self.centralwidget)
        self.Name_Label.setGeometry(QtCore.QRect(100, 250, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Name_Label.setFont(font)
        self.Name_Label.setText("")
        self.Name_Label.setObjectName("Name_Label")
        self.Camera = QtWidgets.QLabel(self.centralwidget)
        self.Camera.setGeometry(QtCore.QRect(10, 400, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Camera.setFont(font)
        self.Camera.setObjectName("Camera")
        self.RAM_Label = QtWidgets.QLabel(self.centralwidget)
        self.RAM_Label.setGeometry(QtCore.QRect(100, 300, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.RAM_Label.setFont(font)
        self.RAM_Label.setText("")
        self.RAM_Label.setObjectName("RAM_Label")
        self.Storage_Label = QtWidgets.QLabel(self.centralwidget)
        self.Storage_Label.setGeometry(QtCore.QRect(100, 350, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Storage_Label.setFont(font)
        self.Storage_Label.setText("")
        self.Storage_Label.setObjectName("Storage_Label")
        self.Camera_Label = QtWidgets.QLabel(self.centralwidget)
        self.Camera_Label.setGeometry(QtCore.QRect(100, 400, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Camera_Label.setFont(font)
        self.Camera_Label.setText("")
        self.Camera_Label.setObjectName("Camera_Label")
        self.SimCard = QtWidgets.QLabel(self.centralwidget)
        self.SimCard.setGeometry(QtCore.QRect(10, 450, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.SimCard.setFont(font)
        self.SimCard.setObjectName("SimCard")
        self.SimCard_Label = QtWidgets.QLabel(self.centralwidget)
        self.SimCard_Label.setGeometry(QtCore.QRect(100, 450, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.SimCard_Label.setFont(font)
        self.SimCard_Label.setText("")
        self.SimCard_Label.setObjectName("SimCard_Label")
        self.Battery = QtWidgets.QLabel(self.centralwidget)
        self.Battery.setGeometry(QtCore.QRect(10, 500, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Battery.setFont(font)
        self.Battery.setObjectName("Battery")
        self.Battery_Label = QtWidgets.QLabel(self.centralwidget)
        self.Battery_Label.setGeometry(QtCore.QRect(100, 500, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Battery_Label.setFont(font)
        self.Battery_Label.setText("")
        self.Battery_Label.setObjectName("Battery_Label")
        self.Size = QtWidgets.QLabel(self.centralwidget)
        self.Size.setGeometry(QtCore.QRect(10, 550, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Size.setFont(font)
        self.Size.setObjectName("Size")
        self.Weight = QtWidgets.QLabel(self.centralwidget)
        self.Weight.setGeometry(QtCore.QRect(10, 600, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Weight.setFont(font)
        self.Weight.setObjectName("Weight")
        self.Size_Label = QtWidgets.QLabel(self.centralwidget)
        self.Size_Label.setGeometry(QtCore.QRect(100, 550, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Size_Label.setFont(font)
        self.Size_Label.setText("")
        self.Size_Label.setObjectName("Size_Label")
        self.Weight_Label = QtWidgets.QLabel(self.centralwidget)
        self.Weight_Label.setGeometry(QtCore.QRect(100, 600, 450, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Weight_Label.setFont(font)
        self.Weight_Label.setText("")
        self.Weight_Label.setObjectName("Weight_Label")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(770, 170, 400, 300))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setBold(False)
        font.setWeight(50)
        self.Image.setFont(font)
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Prices = QtWidgets.QLabel(self.centralwidget)
        self.Prices.setGeometry(QtCore.QRect(590, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Prices.setFont(font)
        self.Prices.setObjectName("Prices")
        self.Digikala = QtWidgets.QLabel(self.centralwidget)
        self.Digikala.setGeometry(QtCore.QRect(590, 510, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Digikala.setFont(font)
        self.Digikala.setObjectName("Digikala")
        self.Mobile = QtWidgets.QLabel(self.centralwidget)
        self.Mobile.setGeometry(QtCore.QRect(590, 570, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Mobile.setFont(font)
        self.Mobile.setObjectName("Mobile")
        self.MeghdadIT = QtWidgets.QLabel(self.centralwidget)
        self.MeghdadIT.setGeometry(QtCore.QRect(590, 630, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MeghdadIT.setFont(font)
        self.MeghdadIT.setObjectName("MeghdadIT")
        self.Digikala_Label = QtWidgets.QLabel(self.centralwidget)
        self.Digikala_Label.setGeometry(QtCore.QRect(715, 510, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Digikala_Label.setFont(font)
        self.Digikala_Label.setText("")
        self.Digikala_Label.setObjectName("Digikala_Label")
        self.Mobile_Label = QtWidgets.QLabel(self.centralwidget)
        self.Mobile_Label.setGeometry(QtCore.QRect(715, 570, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Mobile_Label.setFont(font)
        self.Mobile_Label.setText("")
        self.Mobile_Label.setObjectName("Mobile_Label")
        self.MeghdadIT_Label = QtWidgets.QLabel(self.centralwidget)
        self.MeghdadIT_Label.setGeometry(QtCore.QRect(715, 630, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MeghdadIT_Label.setFont(font)
        self.MeghdadIT_Label.setText("")
        self.MeghdadIT_Label.setObjectName("MeghdadIT_Label")
        self.Update_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Update_Button.setGeometry(QtCore.QRect(580, 680, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Update_Button.setFont(font)
        self.Update_Button.setObjectName("Update_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCtegories = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(18)
        self.actionCtegories.setFont(font)
        self.actionCtegories.setObjectName("actionCtegories")
        self.actionProfile_Page = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(18)
        self.actionProfile_Page.setFont(font)
        self.actionProfile_Page.setObjectName("actionProfile_Page")
        self.actionLogin_Page = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(18)
        self.actionLogin_Page.setFont(font)
        self.actionLogin_Page.setObjectName("actionLogin_Page")
        self.actionFavorites = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(18)
        self.actionFavorites.setFont(font)
        self.actionFavorites.setObjectName("actionFavorites")
        self.menuMenu.addAction(self.actionCtegories)
        self.menuMenu.addAction(self.actionProfile_Page)
        self.menuMenu.addAction(self.actionLogin_Page)
        self.menuMenu.addAction(self.actionFavorites)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Runnn!"))
        self.label_3.setText(_translate("MainWindow", "Contact us via : @comfortablynumb7 on Telegram or 09908611517                                                                                          "))
        self.label_4.setText(_translate("MainWindow", "Company Address : Iran - Tehran - Narmak - IUST "))
        self.Search_Box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cooper Black\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.Details.setText(_translate("MainWindow", "Details"))
        self.Name.setText(_translate("MainWindow", "Name:"))
        self.RAM.setText(_translate("MainWindow", "RAM:"))
        self.Storage.setText(_translate("MainWindow", "Storage:"))
        self.Camera.setText(_translate("MainWindow", "Camera:"))
        self.SimCard.setText(_translate("MainWindow", "SimCard:"))
        self.Battery.setText(_translate("MainWindow", "Battery:"))
        self.Size.setText(_translate("MainWindow", "Size:"))
        self.Weight.setText(_translate("MainWindow", "Weight:"))
        self.Prices.setText(_translate("MainWindow", "Prices"))
        self.Digikala.setText(_translate("MainWindow", "DigiKala.com"))
        self.Mobile.setText(_translate("MainWindow", "Mobile.ir"))
        self.MeghdadIT.setText(_translate("MainWindow", "MeghdadIT.com"))
        self.Update_Button.setText(_translate("MainWindow", "Update"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionCtegories.setText(_translate("MainWindow", "Ctegories"))
        self.actionProfile_Page.setText(_translate("MainWindow", "Profile "))
        self.actionLogin_Page.setText(_translate("MainWindow", "Login "))
        self.actionFavorites.setText(_translate("MainWindow", "Favorites"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
