from random import randint

numbers = []

for i in range(0,10):
    number = randint(1,10)
    numbers.append(number)
    print(number)

print("The total is %s, and the average is %s" % (sum(numbers), sum(numbers)/10))