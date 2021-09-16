userNumber = int(input("Give me a number to find the factorial of: "))

total = userNumber

if userNumber != 0:
    for i in range(userNumber):
        if i != 0:
            total *= i
else:
    total = 1

print(total)