startNum = int(input("Starting number: "))
endNum = int(input("Ending number: "))

for number in range(startNum,endNum+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)