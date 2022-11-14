class Student():
    def __init__(self, name):
        self.name = name

    def praise(self):
        return f"Well done {self.name}, you've done really well!"

    def reassurance(self):
        return f"Keep going {self.name}, you're never gonna achive your goals!"

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()