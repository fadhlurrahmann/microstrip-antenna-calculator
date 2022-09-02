# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 353)
        self.dielectricConstant = QtWidgets.QLineEdit(Dialog)
        self.dielectricConstant.setGeometry(QtCore.QRect(40, 50, 113, 20))
        self.dielectricConstant.setObjectName("dielectricConstant")
        self.dielectricHeight = QtWidgets.QLineEdit(Dialog)
        self.dielectricHeight.setGeometry(QtCore.QRect(40, 110, 113, 21))
        self.dielectricHeight.setObjectName("dielectricHeight")
        self.frequency = QtWidgets.QLineEdit(Dialog)
        self.frequency.setGeometry(QtCore.QRect(40, 160, 113, 21))
        self.frequency.setObjectName("frequency")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.buttonCalculate = QtWidgets.QPushButton(Dialog)
        self.buttonCalculate.setGeometry(QtCore.QRect(40, 290, 71, 31))
        self.buttonCalculate.setObjectName("buttonCalculate")
        self.buttonReset = QtWidgets.QPushButton(Dialog)
        self.buttonReset.setGeometry(QtCore.QRect(130, 290, 71, 31))
        self.buttonReset.setObjectName("buttonReset")
        self.resultWidth = QtWidgets.QLineEdit(Dialog)
        self.resultWidth.setEnabled(False)
        self.resultWidth.setGeometry(QtCore.QRect(330, 220, 81, 20))
        self.resultWidth.setObjectName("resultWidth")
        self.resultLength = QtWidgets.QLineEdit(Dialog)
        self.resultLength.setEnabled(False)
        self.resultLength.setGeometry(QtCore.QRect(330, 250, 81, 20))
        self.resultLength.setObjectName("resultLength")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 220, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 250, 61, 16))
        self.label_5.setObjectName("label_5")
        self.radioRectangular = QtWidgets.QRadioButton(Dialog)
        self.radioRectangular.setGeometry(QtCore.QRect(40, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioRectangular.setFont(font)
        self.radioRectangular.setObjectName("radioRectangular")
        self.radioCircular = QtWidgets.QRadioButton(Dialog)
        self.radioCircular.setGeometry(QtCore.QRect(40, 220, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioCircular.setFont(font)
        self.radioCircular.setObjectName("radioCircular")
        self.radioTriangular = QtWidgets.QRadioButton(Dialog)
        self.radioTriangular.setGeometry(QtCore.QRect(40, 250, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioTriangular.setFont(font)
        self.radioTriangular.setObjectName("radioTriangular")
        self.imageTriangular = QtWidgets.QLabel(Dialog)
        self.imageTriangular.setGeometry(QtCore.QRect(260, 10, 191, 191))
        self.imageTriangular.setText("")
        self.imageTriangular.setPixmap(QtGui.QPixmap("assets/triangular.PNG"))
        self.imageTriangular.setObjectName("imageTriangular")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(-260, 200, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.resultRadius = QtWidgets.QLineEdit(Dialog)
        self.resultRadius.setEnabled(False)
        self.resultRadius.setGeometry(QtCore.QRect(330, 280, 81, 20))
        self.resultRadius.setObjectName("resultRadius")
        self.resultSide = QtWidgets.QLineEdit(Dialog)
        self.resultSide.setEnabled(False)
        self.resultSide.setGeometry(QtCore.QRect(330, 310, 81, 20))
        self.resultSide.setObjectName("resultSide")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(270, 280, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(270, 310, 61, 16))
        self.label_8.setObjectName("label_8")
        self.imageRectangular = QtWidgets.QLabel(Dialog)
        self.imageRectangular.setGeometry(QtCore.QRect(260, 20, 191, 171))
        self.imageRectangular.setText("")
        self.imageRectangular.setPixmap(QtGui.QPixmap("assets/rectangular.png"))
        self.imageRectangular.setObjectName("imageRectangular")
        self.comboDiel = QtWidgets.QComboBox(Dialog)
        self.comboDiel.setGeometry(QtCore.QRect(150, 110, 41, 22))
        self.comboDiel.setObjectName("comboDiel")
        self.comboFreq = QtWidgets.QComboBox(Dialog)
        self.comboFreq.setGeometry(QtCore.QRect(150, 160, 41, 22))
        self.comboFreq.setObjectName("comboFreq")
        self.imageCircular = QtWidgets.QLabel(Dialog)
        self.imageCircular.setGeometry(QtCore.QRect(260, 20, 191, 171))
        self.imageCircular.setText("")
        self.imageCircular.setPixmap(QtGui.QPixmap("assets/circular.PNG"))
        self.imageCircular.setObjectName("imageCircular")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Microstrip Antenna Calculator"))
        self.label.setText(_translate("Dialog", "Dielectric Constant"))
        self.label_2.setText(_translate("Dialog", "Dielectric Height "))
        self.label_3.setText(_translate("Dialog", "Resonant Frequency"))
        self.buttonCalculate.setText(_translate("Dialog", "Calculate"))
        self.buttonReset.setText(_translate("Dialog", "Reset"))
        self.label_4.setText(_translate("Dialog", "W (mm)   :"))
        self.label_5.setText(_translate("Dialog", "L (mm)     :"))
        self.radioRectangular.setText(_translate("Dialog", "Rectangular"))
        self.radioCircular.setText(_translate("Dialog", "Circular"))
        self.radioTriangular.setText(_translate("Dialog", "Triangular"))
        self.label_7.setText(_translate("Dialog", "radius (r) :"))
        self.label_8.setText(_translate("Dialog", "side (a)   :"))