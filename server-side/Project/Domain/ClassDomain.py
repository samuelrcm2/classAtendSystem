from Models.Class import Class


class ClassDomain():
    self __init__(self, Class):
        self.classObject = Class(
            id=Class["id"],
            professorId=Class["professorId"],
            name=Class["name"],
            numberOfClasses=Class["numberOfClasses"])

    def update(self):
        self.classObject.update()

    def add(self):
        self.classObject.add()

    def delete(self):
        self.classObject.delete()
