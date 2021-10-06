class Students:
    studentList = ["Darin Greg", "Amelia Anaya", "Brand Diggory", "Jervis Leith", "Layla Nickolas"]

    def addStudent(self, student):
        self.studentList.append(student)

    def getStudents(self):
        return self.studentList

    def updateStudent(self, toReplace, replaceWith):
        if toReplace.isnumeric():
            