from professor import Professor
from enrol import Enrol

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professors = []
        self.enrollments = []

        if isinstance(professor,Professor):
            self.professors.append(professor)
        elif isinstance(professor,list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Error("Invalid Professor ...")
            self.professors = professor
        else:
            raise Error("Invalid Professor ...")

    def add_professor(self,professor):
        if not isinstance(professor,Professor):
            raise Error("Invalid Professor ...")
        self.professors.append(professor)

    def add_enrolment(self, enrol):
        if not isinstance(enrol,Enrol):
            raise Error("Invalid Enrol ...")
        self.enrollments.append(enrol)

        if len(enrollments) == self.max:
            raise Error("Cannot Enrol, course is already full...")
        self.enrollments.append(enrol)

    def is_cancelled(self):
        return len(self.enrollments) < self.max

