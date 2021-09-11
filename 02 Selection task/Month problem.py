year = int(input("Enter your year: "))
month = int(input("Enter the number of your month in %s: " % year))
month -= 1

months = [(["January", 31]), (["Febuary (error)", 0]), (["March", 31]), (["April", 30]), (["May", 31]), (["June", 30]), (["July", 31]), (["August", 31]), (["September", 30]), (["October", 31]), (["November", 30]), (["December", 31])]

if year%4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if month == 1:
    if isLeapYear:
        outputMonth = ["Febuary", 29]
    else:
        outputMonth = ["Febuary", 28]
else:
    outputMonth = months[month]

print("%s has %s days in it" % (outputMonth[0], outputMonth[1]))