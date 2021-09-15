rice = 1
total = 0

for i in range(64):
    total += rice
    rice += rice

print("Your total is", total)
