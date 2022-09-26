# create a list
myList = ["jim", "bob", "jack", "anna"]

# read 2nd value in list
print(myList[1])

# add value to the end of the list
myList.append("jeff")

# change 4th value
myList[3] = "george"

# loop through list, printing each value
for i in range(len(myList)):
    print(myList[i])

# in python there are not arrays, only lists

# create a tuple
myTuple = (1, 4, 6, 7, 2)

# read 2nd value in tuple
print(myTuple[1])

# loop through tuple, printing each value
for i in range(len(myTuple)):
    print(myTuple[i])
