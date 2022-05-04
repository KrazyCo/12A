import stack

stringStack = stack.Stack(50)

userInput = str(input("Enter your string: "))

for i in range(len(userInput)):
    stringStack.push(userInput[i])

outputString = ""
for i in range(len(userInput)):
    outputString += stringStack.pop()

print(outputString)