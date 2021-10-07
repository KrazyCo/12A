import random

# print("##@-: [R] [G] [B] [W]") layout for terminal view

length = 4
codes = []
colours = ["R", "G", "B", "W"]

for i in range(length): # todo: make sure 1 colour is only used once
    randomNum = random.randint(0, len(colours))
    print(randomNum)
    codes.append(colours[randomNum])
    colours.pop(randomNum)
