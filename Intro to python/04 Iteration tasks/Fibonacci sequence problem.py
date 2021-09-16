userNumber = int(input("How many numbers do you want? "))

count = 0
lastNumber = 0
currentNumber = 1

print("1")

while count != userNumber-1:
    fibonacciNumber = lastNumber + currentNumber
    print(fibonacciNumber)
    lastNumber = currentNumber
    currentNumber = fibonacciNumber
    count += 1