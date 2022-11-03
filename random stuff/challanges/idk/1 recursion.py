def printNumbers(a,b):
    print(a)
    if a < b:
        printNumbers(a+1,b)

printNumbers(5,10)