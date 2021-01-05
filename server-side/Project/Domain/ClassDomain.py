from Models.Class import Class


class ClassDomain():
    def __init__(self, Class):
        self.classObject = Class(
            id=Class["id"],
            professorId=Class["professorId"],
            name=Class["name"],
            numberOfClasses=Class["numberOfClasses"])

    def getAll(self):
        return self.classObject.getAll()

    def getByClassId(self, classId):
        return self.classObject.getByClassId(classId)

    def update(self):
        self.classObject.update()

    def add(self):
        self.classObject.add()

    def delete(self):
        self.classObject.delete()
