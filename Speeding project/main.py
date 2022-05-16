def getInput():
    ageInput = 0
    while ageInput == 0:
        try:
            ageInput = int(input("Input the age of the car, enter 999 to end: "))
        except:
            print("You must input an integer")
    if ageInput == 999:
        return False
    speedInput = 0
    while speedInput == 0:
        try:
            speedInput = int(input("Input the speed of the car, enter 999 to end: "))
        except:
            print("You must input an integer")
    if speedInput == 999:
        return False
    return [ageInput, speedInput]

def percentages(data):
    speeding = 0
    for i in range(len(data)):
        if data[i][1] == True:
            speeding += 1
    percent = speeding/len(data)*100
    return percent



# data = [[5, True], [3, False], [7, True], [2, False], [9, False], [1, False], [6, False], [1, False], [2, True], [3, False], [10, True], [2, False], [7, True], [5, False]]
# print(percentages(data))

userInput = getInput()
if userInput:
    print(userInput)
else:
    print("User wants to end")