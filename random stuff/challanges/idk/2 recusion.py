def addNumbers(a,b):
    if a == b:
        return a
    else:
        return a + addNumbers(a+1,b)

print(addNumbers(5,10))