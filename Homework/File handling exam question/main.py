# question 1

def readMessage(fileName):
    file = open(fileName, "r")
    message = file.read()
    file.close()
    return message

print(readMessage("file.txt"))


# question 2

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
                try:
                    message[i+count] # checking if out of range
                except:
                    capitalNeeded = False
                else:
                    if message[i+count] != "." and message[i+count] != " ":
                        message = message[:i+count] + message [i+count].upper() + message[i+count+1:]
                        capitalNeeded = False
                    else:
                        count += 1
    print(f"{message = }")
    file = open(fileName, "w")
    file.write(message)
    file.close()

fullStop("fullstop.txt")

# question 3

def contains(string1, string2):
    for i in range(len(string1)):
        if string1[i:i+len(string2)] == string2:
            return True
    return False

contains1 = contains("Hello", "Hell")
print(f"{contains1 = }")                        # contains in it
contains2 = contains("Why hello there", "hi")
print(f"{contains2 = }")                        # doesnt contain it
contains3 = contains("joe biden", "joe biden")
print(f"{contains3 = }")                        # identical