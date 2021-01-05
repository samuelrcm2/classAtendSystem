from Models.StudentClass import StudentClass


class StudentClassDomain():
    def __init__(self, studentClass):
        self.studentClass = StudentClass(
            id=studentClass["id"],
            studentId=studentClass["studentId"],
            classId=studentClass["classId"])

    def update(self):
        self.studentClass.update()

    def add(self):
        self.studentClass.add()

    def delete(self):
        self.studentClass.delete()
