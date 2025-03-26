def main():
    name = input("What's your name? ")
    message = hello(name)
    print(message)

def hello(to="world"):
    message = f"Hello, {to.title()}"
    return message

main()