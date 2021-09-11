from guizero import App, Text, TextBox, PushButton

def count():
    characterCount.value = len(enteredText.value)

app = App(title="Widgets")

# create widgets here

# message = Text(app, text="Enter your name")
# name = TextBox(app)

enteredText = TextBox(app, command=count)
characterCount = Text(app)

app.display()