import sys, csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 2:
        if sys.argv[1].strip().endswith(".csv"):
            f = sys.argv[1].strip()
            output = output_csv_as_table(f)
            print(output)
        else:
            print("Not a CSV file")
            sys.exit()
    elif len(sys.argv) > 2:
        print("To many command-line arguments")
        sys.exit()
    else:
        print("To few command-line arguments")
        sys.exit()

def output_csv_as_table(f_path):
    menu = []
    try:
        with open(f_path) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
            return tabulate(menu, tablefmt="grid")
    except FileNotFoundError:
        return "File does not exist"

if __name__ == "__main__":
    main()