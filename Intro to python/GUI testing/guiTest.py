from guizero import App, Text, PushButton

def changeMessage():
    message.value = "You pressed the button"

app = App(title="Title")

message = Text(app, text="This is some text")

button = PushButton(app, text="press me", command=changeMessage)

app.display()