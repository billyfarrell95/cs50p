import re

# Lecture 57:00
def main():
    while True:
        email = input("What's your email? ").strip()
        # \w = [a-zA-Z0-9_]
        if re.search(r"^\w+@\w+\.edu$", email):
            print("Valid")
        else:
            print("Invalid")
    

if __name__ == "__main__":
    main()