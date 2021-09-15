print("Welcome to the Average Calculator!\nAny numbers that you input will have the average calculated when you enter -1\n")

total = 0
count = 0
while True:
    userNumber = int(input("Number: "))
    if userNumber == -1:
        break
    total += userNumber
    count += 1

print()
print("The average of the numbers is " + str(total/count))
print("The total of the numbers is " + str(total))