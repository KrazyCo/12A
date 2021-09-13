from guizero import App, TextBox, Text, Box, PushButton

app = App(title="Portfolio grade problem")

def calculate():
    grades = [2, 4, 13, 22, 31, 41, 54, 67, 80]
    total = int(aTextBox.value) + int(dTextBox.value) + int(iTextBox.value) + int(eTextBox.value)
    if int(total) < 2:
        grade = "U"
        toNextGrade = 2 - total
    for i in range(len(grades)):
        if int(total) < grades[i]:
            grade = str(i)
            toNextGrade = grades[i] - total
            break
    outputText.value = "Your total mark was %s\n\nYou achived grade %s, and you needed\n%s more marks to achive the next grade." % (str(total), grade, toNextGrade)

inputBox = Box(app, align="top", border=True)
aBox = Box(inputBox, align="left", border=True)
dBox = Box(inputBox, align="left", border=True)
iBox = Box(inputBox, align="left", border=True)
eBox = Box(inputBox, align="left", border=True)

aText = Text(aBox, text="Analysis mark")
dText = Text(dBox, text="Design mark")
iText = Text(iBox, text="Implementation mark")
eText = Text(eBox, text="Evaluation mark")

aTextBox = TextBox(aBox)
dTextBox = TextBox(dBox)
iTextBox = TextBox(iBox)
eTextBox = TextBox(eBox)

submitButton = PushButton(app, text="Calculate", command=calculate)
outputText = Text(app)

app.display()