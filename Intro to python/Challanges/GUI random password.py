from guizero import App, Text, CheckBox, TextBox, Box, PushButton
import string
import random

def calculate():
    try:
        int(charTextBox.value)
    except:
        print("char isnt int")
        return
    chars = []
    password = ""
    if lowercaseCheckBox.value == 1:
        for i in list(string.ascii_lowercase):
            chars.append(i)
    if uppercaseCheckBox.value == 1:
        for i in list(string.ascii_uppercase):
            chars.append(i)
    if digitsCheckBox.value == 1:
        for i in list(string.digits):
            chars.append(i)
    if symbolsCheckBox.value == 1:
        for i in list(string.punctuation):
            chars.append(i)

    if len(chars) == 0:
        print("char = 0")
        return

    for i in range(int(charTextBox.value)):
        password += str(chars[random.randint(0,len(chars)-1)])

    outputText.value = password
    

app = App(title="Password generator")

mainBox = Box(app, border=True)

mainBox1 = Box(mainBox)
charText = Text(mainBox1, align="left", text="Number of characters in password: ")
charTextBox = TextBox(mainBox1, command=calculate, align="left")

Text(mainBox, text="\nWhat to include in the password:")
lowercaseCheckBox = CheckBox(mainBox, command=calculate, text="Lowercase")
uppercaseCheckBox = CheckBox(mainBox, command=calculate, text="Uppercase")
digitsCheckBox = CheckBox(mainBox, command=calculate, text="Numbers")
symbolsCheckBox = CheckBox(mainBox, command=calculate, text="Symbols")
generateButton = PushButton(mainBox, command=calculate, text="Generate")

Text(mainBox)

outputBox = Box(mainBox, border=True, width="fill")
Text(outputBox, text="Your password is:")
outputText = TextBox(outputBox, width="fill")

app.display()