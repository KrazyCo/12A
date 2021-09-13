from guizero import App, TextBox, Text, Box

app = App(title="Portfolio grade problem")

def calculate():
    pass

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

app.display()