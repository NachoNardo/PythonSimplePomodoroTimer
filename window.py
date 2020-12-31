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
        parameter = control.readInfo()
        timer = QLabel(str(parameter),self)
        startButton = QPushButton("Start",self)
        stopButton = QPushButton("Stop",self)
        timer.move(100, 50)
        startButton.move(150, 50)
        stopButton.move(150, 100)
        self.show()
        startButton.clicked.connect(self.start)
        stopButton.clicked.connect(self.stop)

    def start(self):
        print("1")
        pass
    def stop(self):
        print("1")
        pass
#Starts the application after closing the console


def run():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())