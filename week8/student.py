import emoji

# Lecture - 1:16
class Student:
    # Instantiate object
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} at {self.house}"
    
    # By convention, should take self even if it is unused
    def charm(self):
        match self.patronus:
            case "Stag":
                return emoji.emojize(":horse_face:")
            case "Otter":
                return emoji.emojize(":otter:")
            case "Jack Russell terrier":
                return emoji.emojize(":dog_face:")
            case _:
                return emoji.emojize(":magic_wand:")

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student)
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    # Constructor call
    return Student(name, house, patronus) 

if __name__ == "__main__":
    main()