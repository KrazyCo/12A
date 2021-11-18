def countChar(text, char):
    charCount = 0
    for i in range(len(text)):
        if text[i].upper() == char.upper():
            charCount += 1
    return charCount

def countString(text, string):
    stringCount = 0
    for i in range(len(text)):
        if text[i:i+(len(string))].upper() == string.upper():
            stringCount += 1
    return stringCount

def subString(text, start, numberOfChars):
    return text[start:start+numberOfChars]

def countSubStringInFile(fileName, subString):
    file = open(fileName, "r")
    fileContents = file.read()
    file.close()
    stringCount = 0
    for i in range(len(fileContents)):
        if fileContents[i:i+(len(subString))].upper() == subString.upper():
            stringCount += 1
    return stringCount


print(countChar("hello this is a string (wow)", "i"))
print(countString("the this is the best the string ever", "the"))
print(subString("ay nah thats crazy look this is a string", 3, 3))
print(countSubStringInFile("beemovie.txt", "bee"))