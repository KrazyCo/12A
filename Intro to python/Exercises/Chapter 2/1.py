proverb = "A picture's worth a thousand words"
proverbImage = "An image is worth a thousand words"

for i in range(len(proverb)):
    if proverb[i] == "o":
        firstO = i
        break

proverbUpper = proverb.upper()

proverbLen = len(proverb)

print(f"{proverb = }")
print(f"{proverbImage = }")
print(f"{firstO = }")
print(f"{proverbUpper = }")
print(f"{proverbLen = }")