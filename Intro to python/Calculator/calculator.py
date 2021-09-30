userInput = input("Calculation: ")
output = 0

# bracketSplit1 = userInput.split("(")
# bracketSplit2 = []
# for i in bracketSplit1:
#     for x in i.split(")"):
#         bracketSplit2.append(x)

splitUserInputMultiply = userInput.split("*")

for num in splitUserInputMultiply:
    output *= int(num)

print(output)

# abandonded