import validators

def main():
    while True:
        email = input("What your email address? ")
        print("Valid") if validators.email(email) else print("Invalid")

if __name__ == "__main__":
    main()