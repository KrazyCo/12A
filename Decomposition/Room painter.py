def widthInput():
    return int(input("Enter the width of the room in meters: "))

def lengthInput():
    return int(input("Enter the length of the room in meters: "))

def heightInput():
    return int(input("Enter the height of the room in meters: "))

def calculate(width, length, height):
    total = 0
    total += width * length
    total += width * height * 2
    total += length * height * 2
    return total

def output(area):
    print(f"The area of the room is {area} meters squared, so you need {area} liters of paint.")

width = widthInput()
length = lengthInput()
height = heightInput()

area = calculate(width, length, height)

output(area)