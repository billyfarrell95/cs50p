import sys

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].strip().endswith(".py"):
            f = sys.argv[1].strip()
            print(count_lines(f))
        else:
            print("Not a Python file")
            sys.exit()
    elif len(sys.argv) > 2:
        print("To many command-line arguments")
        sys.exit()
    else:
        print("To few command-line arguments")
        sys.exit()

def count_lines(f_path):
    num = 0
    try:
        with open(f_path) as file:
            for line in file:
                if line.strip() and not line.strip().startswith("#"):
                    num += 1
            return f"Number of lines in '{file.name}': {num}"
    except FileNotFoundError:
        return "File does not exist"

if __name__ == "__main__":
    main()