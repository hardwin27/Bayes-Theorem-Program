from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from ProbablyNoTea import Ui_MainWindow as MainUI
import sys

class App(QtWidgets.QMainWindow, MainUI):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        
        self.combo_asked_param.currentIndexChanged.connect(self.asked_param_changed)
        self.btn_calc.clicked.connect(self.calculate)      

    def asked_param_changed(self, index):
        if index == 0:
            self.lbl_param_1.setText("-")
            self.lbl_param_2.setText("-")
            self.lbl_param_3.setText("-")
        elif index == 1:
            self.lbl_param_1.setText("P(B)")
            self.lbl_param_2.setText("P(A|B)")
            self.lbl_param_3.setText("P(B|A)")
        elif index == 2:
            self.lbl_param_1.setText("P(A)")
            self.lbl_param_2.setText("P(A|B)")
            self.lbl_param_3.setText("P(B|A)")
        elif index == 3:
            self.lbl_param_1.setText("P(A)")
            self.lbl_param_2.setText("P(B)")
            self.lbl_param_3.setText("P(B|A)")
        elif index == 4:
            self.lbl_param_1.setText("P(A)")
            self.lbl_param_2.setText("P(B)")
            self.lbl_param_3.setText("P(A|B)")

    def calculate(self):
        asked_param = self.combo_asked_param.currentText()
        result = 0.0
        try:
            param1 = float(self.line_param_1.document().toPlainText()) 
            param2 = float(self.line_param_2.document().toPlainText())
            param3 = float(self.line_param_3.document().toPlainText())
            if asked_param == "-":
                self.lbl_result.setText("Error: Asked parameter not slected yet")
            else:
                if asked_param == "P(A)":
                    #result = P(A|B) * P(B) / P(B|A)
                    result = param2 * param1 / param3
                elif asked_param == "P(B)":
                    #result = P(B|A) * P(A) / P(A|B)
                    result = param3 * param1 / param2
                elif asked_param == "P(A|B)":
                    #result = P(B|A) * P(A) / P(B)
                    result = param3 * param1 / param2
                elif asked_param == "P(B|A)":
                    #result = P(A|B) * P(B) / P(A)
                    result = param3 * param2 / param1

                self.lbl_result.setText(str(result))
        except ValueError:
            self.lbl_result.setText("Error: Some input not valid")
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = App()
    program.show()
    sys.exit(app.exec_()) 