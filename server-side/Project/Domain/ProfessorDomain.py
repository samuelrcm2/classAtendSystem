from Models.Professor import Professor


class ProfessorDomain():
    self __init__(self, Professor):
        self.professor = Professor(
            id=Professor["id"],
            cpf=Professor["cpf"],
            firstName=Professor["firstName"],
            lastName=Professor["lastName"],
            birthDate=Professor["birthDate"])

    def getAll(self):
        return self.professor.getAll()

    def update(self):
        self.professor.update()

    def add(self):
        self.professor.add()

    def delete(self):
        self.professor.delete()
