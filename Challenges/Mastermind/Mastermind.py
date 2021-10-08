import random

# i hate how this is coded but i dont want to fix it
# changed colours to letters quite late, stuck with it for var names

# config variables
guesses = 10
colours = ["A", "B", "C", "D", "E"]

guessCount = 0
oldGuesses = []
oldcorrectColours = []
oldcorrectPositions = []
lettersString = ""

def correctGuessPosition(guess, number, codes):
    if guess == codes[number]:
        return True
    else:
        return False
    
def correctGuessColour(guess, codes):
    for code in codes:
        if guess == code:
            return True
    return False

for letter in colours:
    lettersString += f"{letter}, "
lettersString = lettersString[:-2]

print(f'''Welcome to the MasterMind Challenge!
Your mission is to guess the letters that the computer has chosen!
The letters that they could be are:
{lettersString} (each letter is only used once)

You have {guesses} chances to guess the right letters

After you have guessed, the computer will tell you how many letters you
got in the right position with the right colour (shown by a @ in the sidebar) and how 
many letters you got correct, but in the wrong place (shown by a # in the sidebar)

Once you have correctly guessed all the colours in the right position,
the number of guesses you took will be shown

Good luck!


MasterMind game started...''')

# shuffling colours
random.shuffle(colours)
codes = colours[:4]
# print(f"codes are: {codes} (comment ln54 to remove)")

for i in range(guesses):
        print("----: [-] [-] [-] [-]")

gameWon = False

while True:
    print(f"Guess {guessCount+1}:")
    correctColours = 0
    correctPositions = 0
    userGuess = []
    while len(userGuess) < 4:
        userGuess = input("Enter your guess of the letters: ").upper().split(" ")
    userGuess = userGuess[:4]
    # print(f"userGuess: {userGuess}")
    for i in range(len(userGuess)):
        if correctGuessPosition(userGuess[i], i, codes):
            correctPositions += 1
        elif correctGuessColour(userGuess[i], codes):
            correctColours += 1
    # print(f"correctColours: {correctColours}")
    # print(f"correctPositions: {correctPositions}")
    oldGuesses.insert(0, userGuess)
    oldcorrectColours.insert(0, correctColours)
    oldcorrectPositions.insert(0, correctPositions)
    guessCount += 1
    for i in range(guesses-guessCount):
        print("----: [-] [-] [-] [-]")
    for i in range(guessCount):
        feedback = ""
        for b in range(oldcorrectPositions[i]):
            feedback += "@"
        for b in range(oldcorrectColours[i]):
            feedback += "#"
        for b in range(4-len(feedback)):
            feedback += "-"
        print(f"{feedback}: [{oldGuesses[i][0]}] [{oldGuesses[i][1]}] [{oldGuesses[i][2]}] [{oldGuesses[i][3]}]")
    if correctPositions == 4:
        gameWon = True
        break 
    if guessCount == guesses:
        break

if gameWon:
    print(f"Congratulations, you guessed the letters in {guessCount} guesses!")
else:
    codeString = ""
    for code in codes:
        codeString += f"{code}, "
    codeString = codeString[:-2]
    print(f'''Uh oh, you ran out of guesses!
The correct code was {codeString}''')
