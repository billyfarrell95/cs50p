import emoji

class Student:
    # Instantiate object
    def __init__(self, name, house, patronus):
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

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter method
    @property
    def house(self):
        return self._house
    
    # Setter method
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    # @classmethod: can call method without instantiating the object
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)

def main():
    student = Student.get()
    # student.house = "Cannot be reassigned because of getter/setter"
    # student._house = "Can be reassigned, but shouldn't"
    print("Expecto Patronum!")
    print(student)
    print(student.charm())

if __name__ == "__main__":
    main()