import re

def main():
    while True:
        email = input("What's your email? ").strip()
        if re.search(r"^.+@.+\.edu$", email):
            print("Valid")
        else:
            print("Invalid")
    

if __name__ == "__main__":
    main()