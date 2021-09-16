from random import randint

numbers = []

for i in range(0,100):
    numbers.append(randint(1,100))

numbers.sort()

print("The total is %s, and the average is %s" % (sum(numbers), sum(numbers)/10))

print("The smallest number is %s and the largest is %s" % (numbers[0], numbers[-1]))
