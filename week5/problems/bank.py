def main():
    greeting = input("What do you have to say? ")
    amount = value(greeting)
    print(f"${amount}")

def value(greeting):
    if (greeting.lower().strip().startswith("hello")):
        return 0
    elif (greeting.lower().strip().startswith("h")):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()