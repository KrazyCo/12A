names = [["Alex BREW", 10], ["Wil BROOKS", -1], ["Andreas KRISTENSEN", 9], ["Musashi LOWE", 1], ["Alesandro NOEL", 0], ["Matvey OSIPOV", 3], ["Aidan ROLFE", 4], ["Luke SOUTHALL", 5], ["Felix STONE", 7], ["Conor STRICKLAND", 8], ["Arun SURMAN", 2]]
startPointer = 6

def printList(linkedList, currentPointer):
    currentPointer = startPointer
    while currentPointer != -1:
        print(linkedList[currentPointer][0])
        currentPointer = linkedList[currentPointer][1]

def findItem(toFind, linkedList, currentPointer):
    while currentPointer != -1:
        if toFind == linkedList[currentPointer][0]: return True
        currentPointer = names[currentPointer][1]
    return False

print("Find items:")
print(findItem("Conor STRICKLAND", names, startPointer))
print(findItem("Conor Strickland", names, startPointer))


def addToEnd(data, linkedList, currentPointer):
    lastPointer = -1
    while currentPointer != -1:
        lastPointer = currentPointer
        currentPointer = linkedList[currentPointer][1]
    linkedList.append([data, -1])
    linkedList[lastPointer][1] = len(linkedList)-1
    return(linkedList)

print("\nAdd to end")
print(names)
print(addToEnd("Joe BIDEN", names, startPointer))
print(addToEnd("Jill BIDEN", names, startPointer))


def addToStart(data, linkedList, currentPointer):
    linkedList.append([data, currentPointer])
    return len(linkedList)-1

print("\nAdd to start")
print(names)
print(addToStart("Bernie SANDERS", names, startPointer))
print(names)


def removeItem(data, linkedList, currentPointer):
    lastPointer = -1
    while currentPointer != -1:
        if data == linkedList[currentPointer][0]: break
        lastPointer = currentPointer
        currentPointer = names[currentPointer][1]
    if currentPointer == -1: return False
    linkedList[lastPointer][1] = linkedList[currentPointer][1]
    return True

print("\nRemove item")
print(names)
print(removeItem("Jill Biden", names, startPointer))
print(names)
print(removeItem("Jill BIDEN", names, startPointer))
print(names)


def addInOrder(data, linkedList, currentPointer):
    lastPointer = -1
    while currentPointer != -1:
        if data < linkedList[currentPointer][0]: break
        lastPointer = currentPointer
        currentPointer = names[currentPointer][1]
    linkedList.append([data, currentPointer])
    linkedList[lastPointer][1] = len(linkedList)-1

cleanNames = [["Alex BREW", 10], ["Wil BROOKS", -1], ["Andreas KRISTENSEN", 9], ["Musashi LOWE", 1], ["Alesandro NOEL", 0], ["Matvey OSIPOV", 3], ["Aidan ROLFE", 4], ["Luke SOUTHALL", 5], ["Felix STONE", 7], ["Conor STRICKLAND", 8], ["Arun SURMAN", 2]]
print("\nAdd in order")
print(cleanNames)
print(startPointer)
printList(cleanNames, startPointer)
addInOrder("Ben JAMES", cleanNames, startPointer)
print(cleanNames)
printList(cleanNames, startPointer)