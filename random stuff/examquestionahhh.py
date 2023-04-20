def validateAnswer(answer, randomLetters):
    valid = True
    scoreCount = 0
    for i in range(len(answer)):
        letterValid = False
        for j in range(len(randomLetters)):
            if answer[i] == randomLetters[j]:
                letterValid = True
                randomLetters[j] = "!"
                scoreCount += 1
        if not letterValid:
            valid = False
    if valid:
        return scoreCount
    else:
        return 0


randomLetters = ["O", "P", "X", "C", "M", "U", "R", "E", "T", "N"]
print(f"{randomLetters = }")


print(validateAnswer("RETURN", randomLetters))
