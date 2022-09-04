from cgitb import reset
from math import log, pi, sqrt
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from app_design import *

def rectangular(eps, h, freq):
    w = 3e8 / ((2 * freq) * sqrt((eps + 1)/2))
    eff = ((eps + 1) / 2) + ((eps - 1) / 2) * (1 + 12 * (h/w)) ** -0.5
    leff = 3e8 / ((2 * freq) * sqrt(eff))
    delta_l = 0.412 * h * (((eff + 0.3) * (w/h + 0.264)) / ((eff - 0.258) * (w/h + 0.8)))
    l = leff - 2 * delta_l
    
    w = w * 1e3
    l = l * 1e3
    return w, l

def circular(eps, h, freq):
    F = 8.791 * (1e9 / (freq * sqrt(eps)))
    r = F / sqrt((1 + ((2 * h) / (pi * eps * F)) * (log((pi * F) / (2 * h)) + 1.7726)))

    r = r * 10
    return r

def triangular(eps, h, freq):
    a = (2 * 3e8) / ((3 * freq) * sqrt(eps))

    a = a * 1e3
    return a


class Microstrip(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.labelError.setVisible(False)

        self.ui.comboDiel.addItem('mm')
        self.ui.comboDiel.addItem('mil')
        self.ui.comboFreq.addItem('GHz')
        self.ui.comboFreq.addItem('MHz')

        self.ui.radioRectangular.click()
        self.imageRectangular()
        self.ui.radioRectangular.clicked.connect(self.imageRectangular)
        self.ui.radioCircular.clicked.connect(self.imageCircular)
        self.ui.radioTriangular.clicked.connect(self.imageTriangular)

        self.ui.buttonCalculate.clicked.connect(self.calculate)
        self.ui.buttonReset.clicked.connect(self.reset)
        self.show()
    
    def imageRectangular(self):
        self.ui.imageRectangular.setHidden(False)
        self.ui.imageCircular.hide()
        self.ui.imageTriangular.hide()
    
    def imageCircular(self):
        self.ui.imageRectangular.hide()
        self.ui.imageCircular.setHidden(False)
        self.ui.imageTriangular.hide()
    
    def imageTriangular(self):
        self.ui.imageRectangular.hide()
        self.ui.imageCircular.hide()
        self.ui.imageTriangular.setHidden(False)

    def calculate(self):
        try:
            eps = float(self.ui.dielectricConstant.text())
            h = float(self.ui.dielectricHeight.text()) * 1e-3 if self.ui.comboDiel.currentText() == 'mm' else float(self.ui.dielectricHeight.text()) * 2.54e-5
            freq = float(self.ui.frequency.text()) * 1e9 if self.ui.comboFreq.currentText() == 'GHz' else float(self.ui.frequency.text()) * 1e6
        
            if self.ui.radioRectangular.isChecked() == True:
                result_w, result_l = rectangular(eps, h, freq)
                self.ui.resultWidth.setText("%.2f" % result_w)
                self.ui.resultLength.setText("%.2f" % result_l)

                self.ui.resultRadius.clear()
                self.ui.resultSide.clear()

            if self.ui.radioCircular.isChecked() == True:
                r = circular(eps, h, freq)
                self.ui.resultRadius.setText("%.2f" % r)

                self.ui.resultWidth.clear()
                self.ui.resultLength.clear()
                self.ui.resultSide.clear()

            if self.ui.radioTriangular.isChecked() == True:
                a = triangular(eps, h, freq)
                self.ui.resultSide.setText("%.2f" % a)

                self.ui.resultWidth.clear()
                self.ui.resultLength.clear()
                self.ui.resultRadius.clear()

            self.ui.labelError.setVisible(False)

        except:
            self.ui.labelError.setVisible(True)
            self.reset()

    def reset(self):
        self.ui.dielectricConstant.clear()
        self.ui.dielectricHeight.clear()
        self.ui.frequency.clear()
        self.ui.resultWidth.clear()
        self.ui.resultLength.clear()
        self.ui.resultRadius.clear()
        self.ui.resultSide.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Microstrip()
    w.show()
    sys.exit(app.exec_())