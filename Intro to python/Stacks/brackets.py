import stack

brackets = stack.Stack(10)
curlyBrackets = stack.Stack(10)
squareBrackets = stack.Stack(10)
triangleBrackets = stack.Stack(10)

userInput = input("Enter your string to check if the brackets are balanced: ")

for i in range(len(userInput)):
    if userInput[i] == "(":
        brackets.push("(")
    elif userInput[i] == ")":
        brackets.pop()
    elif userInput[i] == "{":
        curlyBrackets.push("{")
    elif userInput[i] == "}":
        curlyBrackets.pop()
    elif userInput[i] == "[":
        squareBrackets.push("[")
    elif userInput[i] == "]":
        squareBrackets.pop()
    elif userInput[i] == "<":
        triangleBrackets.push("<")
    elif userInput[i] == ">":
        triangleBrackets.pop()

if brackets.peak() == None and curlyBrackets.peak() == None and squareBrackets.peak() == None and triangleBrackets.peak() == None:
    print("The string has balanced brackets!")
else:
    print("The brackets are not balanced :(")