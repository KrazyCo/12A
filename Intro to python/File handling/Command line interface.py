def openFile(name, mode):
    try:
        name = name+".txt"
        myFile = open(name, mode)
        return myFile
    except:
        print("Error: unable to open", name)
        return False


print('''
File editor:
Syntax:
{selection} {file} {message if needed}
Options:
ADD, SHOW, NEW, STOP

''')

while True:
    userInput = input("files> ").split()
    userSelection = userInput[0].upper()
    fileName = userInput[1]
    message = ' '.join(userInput[2:])
    # print(f"{userSelection = }")
    # print(f"{fileName = }")
    # print(f"{message = }")

    if userSelection == "ADD":
        file = openFile(fileName, "a")
        if file:
            file.write(message)
            file.close()
            print("Sucess\n")
    elif userSelection == "SHOW":
        file = openFile(fileName, "r")
        if file:
            lineCount = 1
            line = file.readline()
            while line != "":
                print(f"Line {lineCount}: {line.strip()}")
                line = file.readline()
                lineCount += 1
            if lineCount == 1:
                print(f"{fileName}.txt is empty")
            file.close()
            print()

    elif userSelection == "NEW":
        file = openFile(fileName, "w")
        file.close()
        print("Sucess\n")

    elif userSelection == "STOP":
        break

    else:
        print('''Syntax:
{selection} {file} {message if needed}
Options:
ADD, SHOW, NEW, STOP

''')

print("\nProgram stopped")
