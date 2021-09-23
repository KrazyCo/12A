print("Type \"stop\" to stop the program and calculate")

numbers = []

while True:
    number = input("Enter a number: ")
    if number.lower() == "stop":
        break
    numbers.append(int(number))

print("The lowest number is %s and the highest number is %s" % (min(numbers), max(numbers)))