import stack

stringStack = stack.Stack(50)

userInput = str(input("Enter your string: "))

for i in range(len(userInput)):
    stringStack.push(userInput[i])

for i in range(len(userInput)):
    print(stringStack.pop())