from Models.Student import Student


class StudentDomain():
    self __init__(self, Student):
        self.student = Student(
            id=Student["id"],
            cpf=Student["cpf"],
            firstName=Student["firstName"],
            lastName=Student["lastName"],
            birthDate=Student["birthDate"])

    def update(self):
        self.student.update()

    def add(self):
        self.student.add()

    def delete(self):
        self.student.delete()
