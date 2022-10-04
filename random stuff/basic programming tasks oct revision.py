while True:
    userInput = input("input a number or quit to exit: ")
    if userInput == "quit":
        break
    if userInput.isnumeric():
        print(int(userInput)*int(userInput))

for i in range(1,11):
    print(i*i)