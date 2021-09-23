nameOne = input("Input the first name of the first person: ")
nameTwo = input("Input the first name of the second person: ")

vowels = "aeiou"
consonents = "bcdfghjklmnpqrstvwxyz"
total = 0

def isVowel(char):
    for vowel in vowels:
        if vowel == char.lower():
            return True
    return False

def vowelCounter(name):
    vowelTotal = 0
    for char in name:
        for i in range(len(vowels)):
            if char == vowels[i]:
                vowelTotal += 1
    return vowelTotal

def consonantCounter(name):
    consonantTotal = 0
    for char in name:
        for i in range(len(consonents)):
            if char == consonents[i]:
                consonantTotal += 1
    return consonantTotal

if len(nameOne) == len(nameTwo):
    total += 20
    print("Length match")
if isVowel(nameOne[0]) and isVowel(nameTwo[0]):
    total += 10
    print("Vowels")
elif not(isVowel(nameOne[0]) and isVowel(nameTwo[0])):
    total += 5
    print("Consentants")

if vowelCounter(nameOne) == vowelCounter(nameTwo):
    total += 12
    print("Vowel amount")

if consonantCounter(nameOne) == consonantCounter(nameTwo):
    total += 12
    print("Consonants amount")