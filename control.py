import time
import os

#Created to read the "config.txt" file and set the right amount of minutes,
#shortbreaks and long breaks
def readInfo():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'config.txt')
    configInfo = open(my_file, 'r')
    period = int(configInfo.readline())
    configInfo.close()
    return period


#Start the pomodoro cicle using the "config.txt" for parameters
def StartCicle():
    parameters = readInfo() #Captures the informations for the cicle
    while(1):
        break

