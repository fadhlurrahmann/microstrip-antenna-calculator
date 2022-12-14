import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(461, 362) # fix window size
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("")
        Dialog.setWindowIcon(QtGui.QIcon(self.resource_path("assets/microstrip.ico"))) # add icon on title bar
        self.imageTriangular = QtWidgets.QLabel(Dialog)
        self.imageTriangular.setGeometry(QtCore.QRect(250, 0, 191, 191))
        self.imageTriangular.setText("")
        self.imageTriangular.setPixmap(QtGui.QPixmap(self.resource_path("assets/triangular.PNG")))
        self.imageTriangular.setObjectName("imageTriangular")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(-260, 200, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.imageRectangular = QtWidgets.QLabel(Dialog)
        self.imageRectangular.setGeometry(QtCore.QRect(250, 10, 191, 171))
        self.imageRectangular.setText("")
        self.imageRectangular.setPixmap(QtGui.QPixmap(self.resource_path("assets/rectangular.png")))
        self.imageRectangular.setObjectName("imageRectangular")
        self.imageCircular = QtWidgets.QLabel(Dialog)
        self.imageCircular.setGeometry(QtCore.QRect(250, 10, 191, 171))
        self.imageCircular.setText("")
        self.imageCircular.setPixmap(QtGui.QPixmap(self.resource_path("assets/circular.PNG")))
        self.imageCircular.setObjectName("imageCircular")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.buttonCalculate = QtWidgets.QPushButton(self.groupBox)
        self.buttonCalculate.setGeometry(QtCore.QRect(20, 310, 91, 23))
        self.buttonCalculate.setObjectName("buttonCalculate")
        self.radioCircular = QtWidgets.QRadioButton(self.groupBox)
        self.radioCircular.setGeometry(QtCore.QRect(20, 239, 67, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioCircular.setFont(font)
        self.radioCircular.setObjectName("radioCircular")
        self.dielectricHeight = QtWidgets.QLineEdit(self.groupBox)
        self.dielectricHeight.setGeometry(QtCore.QRect(20, 120, 133, 20))
        self.dielectricHeight.setObjectName("dielectricHeight")
        self.frequency = QtWidgets.QLineEdit(self.groupBox)
        self.frequency.setGeometry(QtCore.QRect(20, 168, 133, 20))
        self.frequency.setObjectName("frequency")
        self.dielectricConstant = QtWidgets.QLineEdit(self.groupBox)
        self.dielectricConstant.setGeometry(QtCore.QRect(20, 46, 133, 20))
        self.dielectricConstant.setStyleSheet("")
        self.dielectricConstant.setObjectName("dielectricConstant")
        self.buttonReset = QtWidgets.QPushButton(self.groupBox)
        self.buttonReset.setGeometry(QtCore.QRect(130, 310, 81, 23))
        self.buttonReset.setObjectName("buttonReset")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 146, 116, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 24, 106, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioTriangular = QtWidgets.QRadioButton(self.groupBox)
        self.radioTriangular.setGeometry(QtCore.QRect(20, 265, 82, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioTriangular.setFont(font)
        self.radioTriangular.setObjectName("radioTriangular")
        self.comboFreq = QtWidgets.QComboBox(self.groupBox)
        self.comboFreq.setGeometry(QtCore.QRect(160, 168, 51, 20))
        self.comboFreq.setObjectName("comboFreq")
        self.comboDiel = QtWidgets.QComboBox(self.groupBox)
        self.comboDiel.setGeometry(QtCore.QRect(160, 120, 51, 20))
        self.comboDiel.setObjectName("comboDiel")
        self.radioRectangular = QtWidgets.QRadioButton(self.groupBox)
        self.radioRectangular.setGeometry(QtCore.QRect(20, 213, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioRectangular.setFont(font)
        self.radioRectangular.setObjectName("radioRectangular")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 98, 96, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelError = QtWidgets.QLabel(self.groupBox)
        self.labelError.setGeometry(QtCore.QRect(20, 330, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setWordWrap(False)
        self.labelError.setObjectName("labelError")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(230, 200, 231, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(74, 52, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 52, 42, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.resultWidth = QtWidgets.QLineEdit(self.groupBox_2)
        self.resultWidth.setEnabled(False)
        self.resultWidth.setGeometry(QtCore.QRect(84, 18, 125, 20))
        self.resultWidth.setObjectName("resultWidth")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(74, 120, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(74, 86, 16, 16))
        self.label_10.setObjectName("label_10")
        self.resultRadius = QtWidgets.QLineEdit(self.groupBox_2)
        self.resultRadius.setEnabled(False)
        self.resultRadius.setGeometry(QtCore.QRect(84, 86, 125, 20))
        self.resultRadius.setObjectName("resultRadius")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 18, 48, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.resultLength = QtWidgets.QLineEdit(self.groupBox_2)
        self.resultLength.setEnabled(False)
        self.resultLength.setGeometry(QtCore.QRect(84, 52, 125, 20))
        self.resultLength.setObjectName("resultLength")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 43, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(74, 18, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 86, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.resultSide = QtWidgets.QLineEdit(self.groupBox_2)
        self.resultSide.setEnabled(False)
        self.resultSide.setGeometry(QtCore.QRect(84, 120, 125, 20))
        self.resultSide.setObjectName("resultSide")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.dielectricConstant, self.dielectricHeight)
        Dialog.setTabOrder(self.dielectricHeight, self.frequency)
        Dialog.setTabOrder(self.frequency, self.radioRectangular)
        Dialog.setTabOrder(self.radioRectangular, self.radioCircular)
        Dialog.setTabOrder(self.radioCircular, self.radioTriangular)
        Dialog.setTabOrder(self.radioTriangular, self.buttonCalculate)
        Dialog.setTabOrder(self.buttonCalculate, self.buttonReset)
        Dialog.setTabOrder(self.buttonReset, self.resultWidth)
        Dialog.setTabOrder(self.resultWidth, self.resultLength)
        Dialog.setTabOrder(self.resultLength, self.resultRadius)
        Dialog.setTabOrder(self.resultRadius, self.resultSide)
        Dialog.setTabOrder(self.resultSide, self.comboFreq)
        Dialog.setTabOrder(self.comboFreq, self.comboDiel)
        Dialog.setTabOrder(self.comboDiel, self.comboBox)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Microstrip Antenna Calculator"))
        self.buttonCalculate.setText(_translate("Dialog", "Calculate"))
        self.radioCircular.setText(_translate("Dialog", "Circular"))
        self.buttonReset.setText(_translate("Dialog", "Reset"))
        self.label_3.setText(_translate("Dialog", "Resonant Frequency"))
        self.label.setText(_translate("Dialog", "Dielectric Constant"))
        self.radioTriangular.setText(_translate("Dialog", "Triangular"))
        self.radioRectangular.setText(_translate("Dialog", "Rectangular"))
        self.label_2.setText(_translate("Dialog", "Dielectric Height "))
        self.labelError.setText(_translate("Dialog", "Input must be in numeric!!!"))
        self.label_9.setText(_translate("Dialog", ":"))
        self.label_5.setText(_translate("Dialog", "L (mm)"))
        self.label_11.setText(_translate("Dialog", ":"))
        self.label_10.setText(_translate("Dialog", ":"))
        self.label_4.setText(_translate("Dialog", "W (mm)"))
        self.label_8.setText(_translate("Dialog", "a (mm)"))
        self.label_6.setText(_translate("Dialog", ":"))
        self.label_7.setText(_translate("Dialog", "r (mm)"))

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)