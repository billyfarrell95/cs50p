import sqlite3, os, time, webbrowser, re
from tabulate import tabulate

def connect_db():
    """
    Return db connection
    Create if it doesn't exist
    """
    return sqlite3.connect("db.sqlite3")

def add_data(item):
    """
    Accepts a tuple or list
    Adds item to db
    """
    with connect_db() as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO items (name, purchase_date, purchase_price, purchase_location) VALUES (?, ?, ?, ?)", [item])
        con.commit()
        print("Item added!")

def delete_data(id):
    """
    Accepts id as an int
    Deletes specified item from db
    """
    try:
        with connect_db() as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM items WHERE rowid = ?", (id,))
            row = cur.fetchone() or None
            if not row == None:
                cur.execute(f"DELETE FROM items WHERE rowid={id}")
                con.commit()
                print("Item deleted")
            else:
                print("ID not found")
    except:
        print("Error deleting item")

def view_data():
    """
    Prints db data in table
    Sends formatted data to be exported as html
    """
    with connect_db() as con:
        cur = con.cursor()
        data = cur.execute("SELECT * FROM items")
        if data != None:
            table = []
            for row in data:
                id, name, date, price, location = row[0], row[1].title(), row[2], row[3], row[4].title()
                row = [id, name, date, price, location]
                table.append(row)
            print(tabulate(table, headers=["ID", "Item name", "Date", "Price", "Purchase Location"], tablefmt="rounded_grid"))
            html = tabulate(table, headers=["ID", "Item name", "Date", "Price", "Purchase Location"], tablefmt="html")
            export_html(html)
        else:
            print("No items in db")

def export_html(html_data):
    """
    Creates/updates html file with db data
    """
    with open("output.html", "w") as file:
        file.write("<html>")
        file.write("<head>")
        file.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">')
        file.write("<title>Exported Data</title>")
        file.write("</head>")
        file.write("<body>")
        file.write(html_data)
        file.write("</body>")
        file.write("</html>")
    webbrowser.open("output.html", new=0)

def clear_history():
    """
    Clears user input history
    """
    print("Clearing...")
    time.sleep(0.5)
    try:
        os.system("cls")
    except:
        pass

    try:
        os.system("clear")
    except:
        pass

def validate_date(str):
    """
    Return True if date matches YYYY-MM-DD format
    """
    return re.match(r"^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$", str)

def get_input():
    """
    Handles getting user input and calling CRUD functions
    """
    while True:
        print("(v)iew, (a)dd, (d)elete, (cl)ear, or (e)xit")
        action = input("What would you like to do? ").strip().lower()
        canceled = False
        if action == "v":
            view_data()
        elif action == "a":
            item = []
            fields = ["name", "date", "price", "location"]
            print("(c) to cancel operation")
            for field in fields:
                while True:
                    if field == "name" or field == "location":
                        input_val = input(f"{field}: ").strip()
                        if input_val == "c":
                            canceled = True
                            break 
                        elif input_val:
                            item.append(input_val)
                            break
                        else:
                            print(f"{field} required")
                    if field == "date":
                        input_val = input(f"{field}: ").strip()
                        if input_val == "c":
                            canceled = True
                            break 
                        elif validate_date(input_val):
                            item.append(input_val)
                            break
                        else:
                            print(f"{field} required. YYYY-MM-DD")
                    if field == "price":
                        input_val = input(f"{field}: ").strip()
                        if input_val == "c":
                            canceled = True
                            break 
                        elif input_val:
                            try:
                                item.append(float(input_val))
                                break
                            except ValueError:
                                print(f"{field} required. Enter a number, e.g. 120 or 120.25")
                if canceled:
                    print("Canceled adding item.")
                    break

            if input_val != "e" and len(item) == 4:
                add_data(item)

        elif action == "d":
            print("(c) to cancel operation")
            input_val = input("ID to delete: ").strip()
            if input_val == "c":
                print("Canceled operation")
                continue 
            elif input_val:
                try:
                    id = int(input_val)
                    delete_data(id)
                except ValueError:
                    print("ID must be a number")
            else:
                print("ID is required")

        elif action == "cl":
            clear_history()
        elif action == "e":
            print("Exiting...")
            break
        else:
            print("Invalid input")

def main():
    with connect_db() as con:
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            purchase_date TEXT,
            purchase_price TEXT,
            purchase_location TEXT
        )
        ''')
        get_input()

if __name__ == "__main__":
    main()