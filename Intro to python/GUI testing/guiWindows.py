from guizero import App, Window, Text, PushButton

def openWindow():
    window.show(wait=True)

def closeWindow():
    window.hide()

app = App(title="Main window")
window = Window(app, title="Second window")
window.hide()

text = Text(window, text="This will be on the second window")

openButton = PushButton(app, text="Open window", command=openWindow)
closeButton = PushButton(window, text="Close window", command=closeWindow)

app.display()