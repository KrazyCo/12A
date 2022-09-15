import random
import time
import sys

maxNum = 49

# sortList = [3,6,1,4,2]

numbers = range(1, maxNum+1)
sortList = []
for number in numbers:
    sortList.append(number)
random.shuffle(sortList)

swapped = True
passNum = 0

while swapped:
    swapped = False
    passNum+=1
    for i in range(maxNum-1):
        if sortList[i] > sortList[i+1]:
            temp = sortList[i]
            sortList[i] = sortList[i+1]
            sortList[i+1] = temp
            swapped = True
            # print(sortList)
            textToPrint = ""
            for e in range(maxNum):
                if e == i or e == i+1:
                    textToPrint+="_"+str(sortList[e])+"_ "
                else:
                    textToPrint+=" "+str(sortList[e])+"  "
            sys.stdout.write("\r"+textToPrint)
            # sys.stdout.write("\n")
            sys.stdout.flush()
            time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()