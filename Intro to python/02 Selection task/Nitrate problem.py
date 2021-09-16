nitrateLevel = float(input("Enter the nitrate level (between 0 and 50): "))

if nitrateLevel > 50:
    print("Error: Nitrate level too high")
elif nitrateLevel > 10:
    print("Dose 3ml")
elif nitrateLevel > 2.5:
    print("Dose 2ml")
elif nitrateLevel > 1:
    print("Dose 1ml")
else:
    print("Dose 0.5ml")