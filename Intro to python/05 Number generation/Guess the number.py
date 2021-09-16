from random import randint
import random

randomNumber = randint(1,100)
counter = 0

print("The computer has picked a number between 1 and 100, you have to guess it!")

while True:
    userGuess = int(input("Enter your guess: "))
    counter += 1
    if userGuess == randomNumber:
        break
    elif userGuess > randomNumber:
        print("The number is lower than you guessed!\n")
    elif userGuess < randomNumber:
        print("The number is higher than you guessed!\n")

print("\nWell done, you guessed the number correctly!\nYou did this in %s guesses!" % counter)