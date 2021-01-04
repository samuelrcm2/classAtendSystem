from Models.StudentAttendance import StudentAttendance


class StudentAttendanceDomain():
    self __init__(self, studentAttendance):
        self.studentAttendance = StudentAttendance(
            id=studentAttendance["id"],
            studentId=studentAttendance["studentId"],
            classId=studentAttendance["classId"],
            date=studentAttendance["date"],
            status=studentAttendance["status"])

    def getAll(self):
        return self.studentAttendance.getAll()

    def update(self):
        self.studentAttendance.update()

    def add(self):
        self.studentAttendance.add()
