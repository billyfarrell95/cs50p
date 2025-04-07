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
            sys.exit(1)
    elif len(sys.argv) > 2:
        print("To many command-line arguments")
        sys.exit(1)
    else:
        print("To few command-line arguments")
        sys.exit(1)

def output_csv_as_table(f_path):
    try:
        with open(f_path) as file:
            reader = csv.DictReader(file)
            return tabulate(reader, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()