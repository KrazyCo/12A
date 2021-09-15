print("Prime Number Output\n")
userNumber = int(input("Enter the number to go up to: "))
#Task 1 - ask the user for a number

#Task 2 - complete the for loop below
for number in range(1,userNumber+1):
    primeNumber = True
    
    for i in range(2, number):
        if number % i == 0:
            primeNumber = False
            break
    if primeNumber:
        print(number)