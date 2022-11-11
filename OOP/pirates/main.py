class Sidekick():
    def __init__(self, name, film, person, type="Animal", speak=False):
        self.name = name
        self.film = film
        self.person = person
        self.type = type
        self.speak = speak
    
    def getDetails(self):
        return (self.name, self.film, self.person, self.type, self.speak)
    
    def setSpeak(self, speak):
        if not self.speak == speak:
            self.speak = speak
            if speak:
                print("You can now speak")
            else:
                print("You can now no longer speak")

if __name__ == "__main__":
    olaf = Sidekick("Olaf", "Frozen, Frozen 2", "Anna, Elsa", "Snowman")
    name, film, person, stype, speak = olaf.getDetails()
    print(f"{name = }")
    print(f"{film = }")
    print(f"{person = }")
    print(f"{stype = }")
    print(f"{speak = }")
    olaf.setSpeak(True)
    *_, speak = olaf.getDetails()
    print(f"{speak = }")

    print()
    tim = Sidekick("Timothy Q. Mouse", "Dumbo", "Dumbo", "Mouse")
    name, film, person, stype, speak = tim.getDetails()
    print(f"{name = }")
    print(f"{film = }")
    print(f"{person = }")
    print(f"{stype = }")
    print(f"{speak = }")

    print()
    pumbaa = Sidekick("Pumbaa", "The Lion King", "Timon", "Hog")
    name, film, person, stype, speak = pumbaa.getDetails()
    print(f"{name = }")
    print(f"{film = }")
    print(f"{person = }")
    print(f"{stype = }")
    print(f"{speak = }")