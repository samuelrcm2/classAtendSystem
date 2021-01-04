from enum import Enum, unique


@unique
class AttendanceStatus(Enum):
    Undefined = 'Undefined'
    Present = 'Present'
    Abdsent = 'Abdsent'
