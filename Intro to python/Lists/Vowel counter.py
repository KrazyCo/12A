userinput = input("Enter a sentance for the vowels to be counted: ")

vowels = ["a", "e", "i", "o", "u"]
vowelCounter = [0,0,0,0,0]

for char in userinput:
    for i in range(len(vowels)):
        if char == vowels[i]:
            vowelCounter[i] += 1

print('''There are:
%s a's
%s e's
%s i's
%s o's
%s u's''' % (vowelCounter[0], vowelCounter[1], vowelCounter[1], vowelCounter[1], vowelCounter[1]))