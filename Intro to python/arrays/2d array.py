def createArray(rows, columns):
    array = []

    for i in range(rows):
        tempArray = []
        for b in range(columns):
            tempArray.append(i+b)
        array.append(tempArray)

    return array

def printArray(array):
    print(array)
    print("\n")

def printRows(array):
    for row in array:
        print(row)
    print("\n")

def printFormattedArray(array):
    highestLen = 0
    for row in array:
        for value in row:
            if len(str(value)) > highestLen:
                highestLen = len(str(value))
    

    for row in array:
        toPrint = ""
        for value in row:
            toPrint += str(value)
            for i in range(highestLen - len(str(value)) + 1):
                toPrint += " "
        print(toPrint)

array = createArray(50,50)
printArray(array)
printRows(array)
printFormattedArray(array)