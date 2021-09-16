userInput = input("Give me a sentance to work with: ")

output = ""
vowels = ["a", "e", "i", "o", "u"]
vowelCount = 0
consonantCount = 0

for char in reversed(userInput):
    output += char
    vowel = False
    for i in vowels:
        if char == i:
            vowel = True
    if char == " ":
        pass
    elif vowel:
        vowelCount += 1
    else:
        consonantCount += 1

print(output)
print("There were %s vowels and %s consonants" % (vowelCount, consonantCount))