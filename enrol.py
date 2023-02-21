from course import Course
from student import Student

class Enroll:
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise Error("Invalid Student . . .")
        if not isinstance(course, Course):
            raise Error("Invalid Course . . .")

        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self,grade):
        self.grade = grade
