import re

def main():
    while True:
        email = input("What's your email? ").strip()
        # \w = [a-zA-Z0-9_]
        # ? = 0 or 1 repitition
        # * = 0 or more repititions
        if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
            print("Valid")
        else:
            print("Invalid")
    
if __name__ == "__main__":
    main()