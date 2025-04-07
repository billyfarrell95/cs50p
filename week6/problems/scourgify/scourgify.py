import sys, csv

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].strip().endswith(".csv"):
            f = sys.argv[1].strip()
            o = sys.argv[2].strip()
            create_cleaned_file(f, o)
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) > 3:
        sys.exit("To many command-line arguments")
    else:
        sys.exit("To few command-line arguments")

def create_cleaned_file(f_path, o_name):
    new_data = []
    try:
        with open(f_path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                student = {
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"]
                }
                new_data.append(student)

    except FileNotFoundError:
        sys.exit("Input file does not exist")

    with open(f"{o_name}", "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in new_data:
            writer.writerow({"first": student["first"], "last": student['last'], "house": student["house"]})

if __name__ == "__main__":
    main()