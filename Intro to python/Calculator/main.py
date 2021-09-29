from guizero import App, Box, Text, TextBox, PushButton

def num1():
    textInput.value += "1"
    print("1")
def num2():
    textInput.value += "2"
    print("2")
def num3():
    textInput.value += "3"
    print("3")
def num4():
    textInput.value += "4"
    print("4")
def num5():
    textInput.value += "5"
    print("5")
def num6():
    textInput.value += "6"
    print("6")
def num7():
    textInput.value += "7"
    print("7")
def num8():
    textInput.value += "8"
    print("8")
def num9():
    textInput.value += "9"
    print("9")

app = App(title="Calculator")

textInput = TextBox(app)

numbersBox = Box(app)
numbers1Box = Box(numbersBox)
numbers2Box = Box(numbersBox)
numbers3Box = Box(numbersBox)
num7 = PushButton(numbers1Box, text="7", align="left", command=num7)
num8 = PushButton(numbers1Box, text="8", align="left", command=num8)
num9 = PushButton(numbers1Box, text="9", align="left", command=num9)
num4 = PushButton(numbers2Box, text="4", align="left", command=num4)
num5 = PushButton(numbers2Box, text="5", align="left", command=num5)
num6 = PushButton(numbers2Box, text="6", align="left", command=num6)
num1 = PushButton(numbers3Box, text="1", align="left", command=num1)
num2 = PushButton(numbers3Box, text="2", align="left", command=num2)
num3 = PushButton(numbers3Box, text="3", align="left", command=num3)

app.display()