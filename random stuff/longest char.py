def longest(stringInput):
    longest = 0
    temp = 0
    for i in range(len(stringInput)):
        if stringInput[i] == "C":
            temp += 1
        else:
            if temp > longest:
                longest = temp
            temp = 0
    if temp > longest:
        longest = temp
    return longest

print(longest("CCMCCCCCCCLLCCCCCC"))
