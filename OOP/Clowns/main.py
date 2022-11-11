import random

class Clown():
    def __init__(self, name, type, nose=None):
        self.name = name
        self.type = type
        if not nose:
            noseColours = ["Red", "White", "Brown", "Orange", "Green", "Blue", "Black"]
            nose = noseColours[random.randint(0,len(noseColours)-1)]
        self.nose = nose

    def setNose(self, colour):
        self.nose = colour

    def getInfo(self):
        return (self.name, self.type, self.nose)

    def perform(self, enthusiasm):
        if enthusiasm < 5 and self.type == "Sad":
            return f"{self.name} didn't perform their best :("
        elif enthusiasm < 5 and self.type == "Happy":
            return f"{self.name} didn't perform their best, but they were still smiling"
        elif enthusiasm < 5:
            return f"{self.name} tried their best"
        elif self.type == "Sad":
            return f"{self.name} had a good performance, but wasn't smiling"
        elif self.type == "Happy":
            return f"{self.name} had a good performace and had fun"
        else:
            return f"{self.name} had a good performance"

if __name__ == "__main__":
    clown1 = Clown("Jeff", "Happy")
    clown2 = Clown("Alex", "Sad", "Black")

    print(f"{clown1.getInfo() = }")
    print(f"{clown2.getInfo() = }")

    name, ctype, nose = clown1.getInfo()
    print(f"{name = }")
    print(f"{ctype = }")
    print(f"{nose = }")

    enthusiasm = random.randint(1,10)
    print(f"{enthusiasm = }")
    print(f"{clown1.perform(enthusiasm) = }")
    print(f"{clown2.perform(enthusiasm) = }")
