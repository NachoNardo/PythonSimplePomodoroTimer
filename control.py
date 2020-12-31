import time

#Created to read the "config.txt" file and set the right amount of minutes,
#shortbreaks and long breaks
def readInfo():
    configInfo = open("config.txt", "r")
    period = int(configInfo.readline())
    return period


#Start the pomodoro cicle using the "config.txt" for parameters
def StartCicle():
    parameters = readInfo() #Captures the informations for the cicle
    while(1):

