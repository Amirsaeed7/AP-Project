# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductMobilePageFinal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(991, 841)
        self.Battery = QtWidgets.QLabel(Dialog)
        self.Battery.setGeometry(QtCore.QRect(40, 510, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Battery.setFont(font)
        self.Battery.setObjectName("Battery")
        self.Size = QtWidgets.QLabel(Dialog)
        self.Size.setGeometry(QtCore.QRect(40, 560, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Size.setFont(font)
        self.Size.setObjectName("Size")
        self.Prices = QtWidgets.QLabel(Dialog)
        self.Prices.setGeometry(QtCore.QRect(400, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Prices.setFont(font)
        self.Prices.setObjectName("Prices")
        self.Details = QtWidgets.QLabel(Dialog)
        self.Details.setGeometry(QtCore.QRect(40, 200, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.Details.setFont(font)
        self.Details.setAlignment(QtCore.Qt.AlignCenter)
        self.Details.setObjectName("Details")
        self.Camera = QtWidgets.QLabel(Dialog)
        self.Camera.setGeometry(QtCore.QRect(40, 410, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Camera.setFont(font)
        self.Camera.setObjectName("Camera")
        self.SimCard = QtWidgets.QLabel(Dialog)
        self.SimCard.setGeometry(QtCore.QRect(40, 460, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SimCard.setFont(font)
        self.SimCard.setObjectName("SimCard")
        self.RAM_Label = QtWidgets.QLabel(Dialog)
        self.RAM_Label.setGeometry(QtCore.QRect(140, 310, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RAM_Label.setFont(font)
        self.RAM_Label.setText("")
        self.RAM_Label.setObjectName("RAM_Label")
        self.Digikala_Label = QtWidgets.QLabel(Dialog)
        self.Digikala_Label.setGeometry(QtCore.QRect(540, 260, 311, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Digikala_Label.setFont(font)
        self.Digikala_Label.setText("")
        self.Digikala_Label.setObjectName("Digikala_Label")
        self.Storage_Label = QtWidgets.QLabel(Dialog)
        self.Storage_Label.setGeometry(QtCore.QRect(140, 360, 211, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Storage_Label.setFont(font)
        self.Storage_Label.setText("")
        self.Storage_Label.setObjectName("Storage_Label")
        self.Storage = QtWidgets.QLabel(Dialog)
        self.Storage.setGeometry(QtCore.QRect(40, 360, 91, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Storage.setFont(font)
        self.Storage.setObjectName("Storage")
        self.SearchBox = QtWidgets.QTextEdit(Dialog)
        self.SearchBox.setGeometry(QtCore.QRect(590, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.SearchBox.setFont(font)
        self.SearchBox.setObjectName("SearchBox")
        self.Battery_Label = QtWidgets.QLabel(Dialog)
        self.Battery_Label.setGeometry(QtCore.QRect(140, 510, 211, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Battery_Label.setFont(font)
        self.Battery_Label.setText("")
        self.Battery_Label.setObjectName("Battery_Label")
        self.Weight_Label = QtWidgets.QLabel(Dialog)
        self.Weight_Label.setGeometry(QtCore.QRect(130, 610, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Weight_Label.setFont(font)
        self.Weight_Label.setText("")
        self.Weight_Label.setObjectName("Weight_Label")
        self.Mobile_Label = QtWidgets.QLabel(Dialog)
        self.Mobile_Label.setGeometry(QtCore.QRect(540, 310, 311, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Mobile_Label.setFont(font)
        self.Mobile_Label.setText("")
        self.Mobile_Label.setObjectName("Mobile_Label")
        self.Image = QtWidgets.QLabel(Dialog)
        self.Image.setGeometry(QtCore.QRect(570, 430, 391, 311))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Image.setFont(font)
        self.Image.setObjectName("Image")
        self.MeghdadIT_Label = QtWidgets.QLabel(Dialog)
        self.MeghdadIT_Label.setGeometry(QtCore.QRect(550, 370, 291, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MeghdadIT_Label.setFont(font)
        self.MeghdadIT_Label.setText("")
        self.MeghdadIT_Label.setObjectName("MeghdadIT_Label")
        self.SimCard_Label = QtWidgets.QLabel(Dialog)
        self.SimCard_Label.setGeometry(QtCore.QRect(140, 460, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SimCard_Label.setFont(font)
        self.SimCard_Label.setText("")
        self.SimCard_Label.setObjectName("SimCard_Label")
        self.MeghdadIT = QtWidgets.QLabel(Dialog)
        self.MeghdadIT.setGeometry(QtCore.QRect(400, 370, 171, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.MeghdadIT.setFont(font)
        self.MeghdadIT.setObjectName("MeghdadIT")
        self.Name = QtWidgets.QLabel(Dialog)
        self.Name.setGeometry(QtCore.QRect(40, 260, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 381, 121))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 800, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Weight = QtWidgets.QLabel(Dialog)
        self.Weight.setGeometry(QtCore.QRect(40, 610, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Weight.setFont(font)
        self.Weight.setObjectName("Weight")
        self.Name_Label = QtWidgets.QLabel(Dialog)
        self.Name_Label.setGeometry(QtCore.QRect(140, 260, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Name_Label.setFont(font)
        self.Name_Label.setText("")
        self.Name_Label.setObjectName("Name_Label")
        self.Digikala = QtWidgets.QLabel(Dialog)
        self.Digikala.setGeometry(QtCore.QRect(400, 270, 151, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Digikala.setFont(font)
        self.Digikala.setObjectName("Digikala")
        self.Mobile = QtWidgets.QLabel(Dialog)
        self.Mobile.setGeometry(QtCore.QRect(400, 320, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Mobile.setFont(font)
        self.Mobile.setObjectName("Mobile")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 750, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.SearchButton = QtWidgets.QPushButton(Dialog)
        self.SearchButton.setGeometry(QtCore.QRect(900, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.Update_Button = QtWidgets.QPushButton(Dialog)
        self.Update_Button.setGeometry(QtCore.QRect(390, 660, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Update_Button.setFont(font)
        self.Update_Button.setObjectName("Update_Button")
        self.RAM = QtWidgets.QLabel(Dialog)
        self.RAM.setGeometry(QtCore.QRect(40, 310, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RAM.setFont(font)
        self.RAM.setObjectName("RAM")
        self.Camera_Label = QtWidgets.QLabel(Dialog)
        self.Camera_Label.setGeometry(QtCore.QRect(140, 410, 211, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Camera_Label.setFont(font)
        self.Camera_Label.setText("")
        self.Camera_Label.setObjectName("Camera_Label")
        self.Size_Label = QtWidgets.QLabel(Dialog)
        self.Size_Label.setGeometry(QtCore.QRect(130, 560, 241, 40))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Size_Label.setFont(font)
        self.Size_Label.setText("")
        self.Size_Label.setObjectName("Size_Label")
        self.BackButton = QtWidgets.QPushButton(Dialog)
        self.BackButton.setGeometry(QtCore.QRect(780, 20, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.ProfileButton = QtWidgets.QPushButton(Dialog)
        self.ProfileButton.setGeometry(QtCore.QRect(50, 100, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.ProfileButton.setFont(font)
        self.ProfileButton.setObjectName("ProfileButton")
        self.HomeButton = QtWidgets.QPushButton(Dialog)
        self.HomeButton.setGeometry(QtCore.QRect(50, 30, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(14)
        self.HomeButton.setFont(font)
        self.HomeButton.setObjectName("HomeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Battery.setText(_translate("Dialog", "Battery:"))
        self.Size.setText(_translate("Dialog", "Size:"))
        self.Prices.setText(_translate("Dialog", "Prices"))
        self.Details.setText(_translate("Dialog", "Details"))
        self.Camera.setText(_translate("Dialog", "Camera:"))
        self.SimCard.setText(_translate("Dialog", "SimCard:"))
        self.Storage.setText(_translate("Dialog", "Storage:"))
        self.SearchBox.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cooper Black\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.SearchBox.setPlaceholderText(_translate("Dialog", "Search Here"))
        self.Image.setText(_translate("Dialog", "MOBILE PAGE"))
        self.MeghdadIT.setText(_translate("Dialog", "MeghdadIT.com"))
        self.Name.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Runnn!"))
        self.label_4.setText(_translate("Dialog", "Company Address : Iran - Tehran - Narmak - IUST "))
        self.Weight.setText(_translate("Dialog", "Weight:"))
        self.Digikala.setText(_translate("Dialog", "DigiKala.com"))
        self.Mobile.setText(_translate("Dialog", "Mobile.ir"))
        self.label_3.setText(_translate("Dialog", "Contact us via : @comfortablynumb7 on Telegram or 09908611517                                                                                          "))
        self.SearchButton.setText(_translate("Dialog", "Search"))
        self.Update_Button.setText(_translate("Dialog", "Update"))
        self.RAM.setText(_translate("Dialog", "RAM:"))
        self.BackButton.setText(_translate("Dialog", "Back"))
        self.ProfileButton.setText(_translate("Dialog", "Profile"))
        self.HomeButton.setText(_translate("Dialog", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())