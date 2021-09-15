numbers = []

for number in range(0,1000):
    primeNumber = True
    
    for i in range(2, number):
        if number % i == 0:
            primeNumber = False
            break
    if primeNumber:
        numbers.append(number)

# fixing having 0 and 1 in the list
numbers.remove(0)
numbers.remove(1)

print(round(sum(numbers)/len(numbers),0))