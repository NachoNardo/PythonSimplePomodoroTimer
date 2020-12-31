import sys
import control
from PyQt5.QtWidgets import *

#Main Window with the main UI interactions


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 250)
        self.setWindowTitle("PSPT")
        self.UI()

    def UI(self):                             #Defining the widgets inside the window
        parameter = readInfo()
        timer = QLabel(""+parameter,self)
        timer.move(100, 50)
        self.show()

#Starts the application after closing the console


def start():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())