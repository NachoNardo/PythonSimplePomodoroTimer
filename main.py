import time

configInfo = open("config.txt", "r")

period = int(configInfo.readline())

while(1):
    time.sleep(1)
    print(period)
    period -= 1
    if(period<=0):
        break

print("Finish")