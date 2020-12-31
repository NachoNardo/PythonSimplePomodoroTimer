import sys
from PyQt5.QtWidgets import *

#Created to read the "config.txt" file and set the right amount of minutes,
#shortbreaks and long breaks
def readInfo():
    configInfo = open("config.txt", "r")
    period = int(configInfo.readline())

#Main Window with the main UI interactions
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 250)
        self.setWindowTitle("PSPT")
        self.UI()
        self.show()

    def UI(self):
        pass

#Starts the application after closing the console
def start():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())