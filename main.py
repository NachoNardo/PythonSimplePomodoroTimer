import time

period = 25

while(1):
    time.sleep(1)
    print(period)
    period -= 1
    if(period<=0):
        break

print("Finish")