from person import Person
from enrol import Enrol

class Student(Person):
    def __init__(self, first,last,dob,phone, address, international = False):
        super().__init__(self,first,last,dob,phone,address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enrol):
        if not isinstance(enrol,Enrol):
            raise Error("Invalid Enrol ...")

        self.enrolled.append(enrol)

    def isPart_time(self):
        return len(self.enrolled) <= 3

    def isProbation(self):
        pass
