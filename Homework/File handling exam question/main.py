# question 1

def readMessage(fileName):
    file = open(fileName, "r")
    message = file.read()
    file.close()
    return message

print(readMessage("file.txt"))


# question 2a

def getText(fileName):
    file = open(fileName, "r")
    message = file.read()
    file.close()
    return message

def fullStop(fileName):
    message = getText(fileName)
    for i in range(len(message)):
        if message[i] == ".":
            capitalNeeded = True
            count = 1
            while capitalNeeded:
                if ord(message[i+count]) => 97 and ord(message[i+count] =< 122:
                    print(message[i+count])
                    message[i+count] = message[i+count]
                    capitalNeeded = False