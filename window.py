import sys
from PyQt5.QtWidgets import *
from threading import Thread
import time
import os

#Main Window with the main UI interactions
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 250)
        self.setWindowTitle("PSPT")
        self.UI()
        state = False

    def UI(self):                             #Defining the widgets inside the window
        period = readPeriod()
        timer = QLabel(str(period),self)
        startButton = QPushButton("Start",self)
        stopButton = QPushButton("Stop",self)
        timer.move(100, 50)
        startButton.move(150, 50)
        stopButton.move(150, 100)
        self.show()
        startButton.clicked.connect(self.start)
        stopButton.clicked.connect(self.stop)

    #Starts the pomodoro Cycle
    def start(self):
        parameters = []
        parameters = readAllInfo()
        state = True
        while(state):
            self.timer.setText(str(parameters[0]))
            time.sleep(1)
            parameters[0] -= 1
            if (parameters[0]<=0):
                state = False
        pass

    def stop(self):
        state = False
        pass

#Starts the application after closing the console
def run():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

#Created to read the "config.txt" file and set the right amount of minutes,
#shortbreaks and long breaks
def readPeriod():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'config.txt')
    configInfo = open(my_file, 'r')
    period = int(configInfo.readline())
    configInfo.close()
    return period

def readAllInfo():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'config.txt')
    configInfo = open(my_file, 'r')
    period = [int(configInfo.readline())]
    period.append(int(configInfo.readline()))
    period.append(int(configInfo.readline()))
    configInfo.close()
    return period






