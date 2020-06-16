from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5 import Qt
from ProbablyNoTea import Ui_MainWindow as MainUI
import sys

class App(QtWidgets.QMainWindow, MainUI):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        
        self.combo_asked_param.currentIndexChanged.connect(self.asked_param_changed)

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

    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    program = App()
    program.show()
    sys.exit(app.exec_()) 