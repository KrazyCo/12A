from random import randint

total = 0
minValue = 100
maxValue = 0

for i in range(0,100):
    number = randint(1,100)
    total += number
    if minValue > number:
        minValue = number
    if maxValue < number:
        maxValue = number

print("The total is %s, and the average is %s" % (total, total/100))

print("The smallest number is %s and the largest is %s" % (minValue, maxValue))
