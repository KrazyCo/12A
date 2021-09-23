from random import randint

moneyTotal = 100
betCost = 10

print("You start off with £%s, every bet costs £%s" % (moneyTotal, betCost))

for i in range(10):
    userInput = int(input("Game %s, pick a number between 0 and 30")) 