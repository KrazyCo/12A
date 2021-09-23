nameOne = input("Input the first name of the first person: ")
nameTwo = input("Input the first name of the second person: ")

vowels = "aeiou"
consonents = "bcdfghjklmnpqrstvwxyz"
love = "love"
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
            if char.lower() == vowels[i]:
                vowelTotal += 1
    return vowelTotal

def consonantCounter(name):
    consonantTotal = 0
    for char in name:
        for i in range(len(consonents)):
            if char.lower() == consonents[i]:
                consonantTotal += 1
    return consonantTotal

def containsLove(name):
    for char in name:
        for i in range(len(love)):
            if char.lower() == love[i]:
                return True
    return False

if len(nameOne) == len(nameTwo):
    total += 20
    print("Length match")
if isVowel(nameOne[0]) and isVowel(nameTwo[0]):
    total += 10
    print("Vowels start")
elif not(isVowel(nameOne[0]) and isVowel(nameTwo[0])):
    total += 5
    print("Consentants start")

if vowelCounter(nameOne) == vowelCounter(nameTwo):
    total += 12
    print("Vowel amount")

if consonantCounter(nameOne) == consonantCounter(nameTwo):
    total += 12
    print("Consonants amount")

if containsLove(nameOne) and containsLove(nameTwo):
    total += 7
    print("Contains love")

print(total)