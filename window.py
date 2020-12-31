import sys
from PyQt5.QtWidgets import *
from threading import Thread
import time
import os

#Thread used for running the cycle
class Cycle(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        parameters = readAllInfo()
        pass

#Main Window with the main UI interactions
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 250)
        self.setWindowTitle("PSPT")
        self.UI()

    def UI(self):                             #Defining the widgets inside the window
        parameter = readPeriod()
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
        cycle = Cycle(1)
        cycle.run()
        pass

    def stop(self):
        parameter = readPeriod()
        cycle = Cycle(1)
        cycle.killed = True
        print("2")
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






