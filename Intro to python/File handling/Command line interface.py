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
    try:
        userSelection = userInput[0].upper()
        fileName = userInput[1]
        message = ' '.join(userInput[2:])
        # print(f"{userSelection = }")
        # print(f"{fileName = }")
        # print(f"{message = }")
    except:
        pass # only 1 arg in userinput

    if userSelection == "ADD":
        file = openFile(fileName, "a")
        if file:
            file.write(message)
            file.write("\n")
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
                # print(f"{line = }")
            if lineCount == 1:
                print(f"{fileName}.txt is empty")
            file.close()
            print()

    elif userSelection == "NEW":
        file = openFile(fileName, "w")
        file.close()
        print("Sucess\n")

    elif userSelection == "COUNT":
        file = openFile(fileName, "r")
        if file:
            charCount = 0
            line = file.readline()
            while line != "":
                charCount += len(str(line).strip())
                line = file.readline()
            print(f"There are {charCount} char(s) in {fileName}.txt\n")
            file.close()
    
    elif userSelection == "COUNTWORD":
        file = openFile(fileName, "r")
        if file:
            wordlist = []
            line = file.readline()
            while line != "":
                for i in range(len(line.strip().split())):
                    wordlist.append(line.strip().split()[i])
                line = file.readline()
            wordCount = wordlist.count(message)
            print(f"There are {wordCount} words that are \"{message}\" in {fileName}.txt\n")
            file.close()

    elif userSelection == "STOP":
        break

    else:
        print('''Syntax:
{selection} {file} {message if needed}
Options:
ADD, SHOW, NEW, STOP

''')

print("\nProgram stopped")
