import random

def main():
    level = get_level()
    answered = 0
    while answered < 10:
        tries = 0
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        while tries < 3:
            try:
                answer = int(input(f"{n1} + {n2} = "))
                if answer == (n1 + n2):
                    print("Correct!")
                    break
                else:
                    tries += 1
                    if tries < 3:
                        print("Incorrect, try again")
                    else:
                        print(f"The answer is: {n1 + n2}")
            except ValueError:
                print("Invalid input, please enter a number")
        answered += 1

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            level = int(level)
            return level


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)



if __name__ == "__main__":
    main()