def percentages(data):
    speeding = 0
    for i in range(len(data)):
        if data[i][1] == True:
            speeding += 1
    percent = speeding/len(data)*100
    return percent

data = [[5, True], [3, False], [7, True], [2, False], [9, False], [1, False], [6, False], [1, False], [2, True], [3, False], [10, True], [2, False], [7, True], [5, False]]
print(percentages(data))