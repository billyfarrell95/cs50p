
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    def __str__(self):
        return f"Wizard name: {self.name} "

class Student(Wizard):
    def __init__(self, name, house):
        # super() is parent class, Wizard
        super().__init__(name)
        self.house = house
    def __str__(self):
        return super().__str__() + f"Student name: {self.name}, House: {self.house} "

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return super().__str__() + f"Professor name: {self.name}, Subject: {self.subject} "

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

print(wizard, end="\n")
print(student, end="\n")
print(professor, end="\n")
