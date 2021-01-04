from Models.Professor import Professor


class ProfessorDomain():
    self __init__(self, Professor):
        self.Professor = Professor(
            id=Professor["id"],
            cpf=Professor["cpf"],
            firstName=Professor["firstName"],
            lastName=Professor["lastName"],
            birthDate=Professor["birthDate"])

    def update(self):
        self.Professor.update()

    def add(self):
        self.Professor.add()

    def delete(self):
        self.Professor.delete()
