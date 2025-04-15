import sqlite3, os, time, webbrowser, re, platform
from tabulate import tabulate
    
def connect_db():
    """
    Return db connection
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
    Deletes specified item from db if it exists
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
    except sqlite3.OperationalError as e:
        print(e)

def update_data(id):
    """
    Accepts id as an int
    Allows updating of item in db if it exists
    """
    try:
        with connect_db() as con:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM items WHERE rowid = ?", (id,))
            if data != None:
                data_list = format_data_as_list(data)
                print("You are updating:")
                print(format_rows_as_table(data_list))
                item = get_item_input("updating")
                if len(item) == 4:
                    try:
                        update_statement = "UPDATE items SET name=?, purchase_date=?, purchase_price=?, purchase_location=? WHERE rowid = ?"
                        name, date, price, location = item[0], item[1], item[2], item[3]
                        cur.execute(update_statement, (name, date, price, location, id))
                        print("Item updated:")
                        data = cur.execute("SELECT * FROM items WHERE rowid = ?", (id,))
                        data_list = format_data_as_list(data)
                        print(format_rows_as_table(data_list))
                    except sqlite3.OperationalError as e:
                        print(e)
                else:
                    print("ID not found")
    except sqlite3.OperationalError as e:
        print(e)

def format_rows_as_table(list):
    """
    Return data as formatted table using tabulate
    """
    return tabulate(list, headers=["ID", "Item name", "Date", "Price", "Purchase Location"], tablefmt="rounded_grid")

def format_data_as_list(data):
    """
    Returns db data in list
    """
    list = []
    for row in data:
        id, name, date, price, location = row[0], row[1], row[2], row[3], row[4]
        row = [id, name, date, price, location]
        list.append(row)
    return list

def view_data():
    """
    Prints db data in table
    """
    with connect_db() as con:
        try:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM items")
            if data != None:
                data_list = format_data_as_list(data)
                print(format_rows_as_table(data_list))
            else:
                print("No items in db")
        except sqlite3.OperationalError as e:
            print(e)

def export_data():
    """
    Formats db data as HTML
    """
    with connect_db() as con:
        try:
            cur = con.cursor()
            data = cur.execute("SELECT * FROM items")
            if data != None:
                table = format_data_as_list(data)
                html = tabulate(table, headers=["ID", "Item name", "Date", "Price", "Purchase Location"], tablefmt="html")
                create_html(html)
            else:
                print("No items in db")
        except sqlite3.OperationalError as e:
            print(e)

def create_html(html):
    """
    Writes the formatted HTML data from export_data to the output file
    Prompts user whether they would like to open output file
    """
    html = html.replace("<table>", "<table class='table'>")
    with open("output.html", "w") as file:
        file.write("<html>")
        file.write("<head>")
        file.write('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">')
        file.write("<title>Exported Data</title>")
        file.write("</head>")
        file.write("<body>")
        file.write(html)
        file.write("</body>")
        file.write("</html>")
        
    while True:
        open_file = input("output.html created. Open? (y/n) ").strip()
        if open_file.lower() == "y":
            try:
                print("Opening...")
                time.sleep(0.5)
                plat = platform.system()
                abs_path = os.path.abspath("output.html")
                if plat in ("Linux", "Darwin"):
                    webbrowser.open(f"file://{abs_path}", new=0)
                elif plat == "Windows":
                    webbrowser.open(abs_path, new=0)
                break
            except webbrowser.Error as e:
                print(e)
        elif open_file.lower() == "n":
            break
        else:
            print("Invalid input. Enter (y/n)")

def clear_history():
    """
    Clears user input history
    """
    print("Clearing...")
    plat = platform.system()
    time.sleep(0.5)
    if plat in ("Linux", "Darwin"):
        os.system("clear")
    elif plat == "Windows":
        os.system("cls")

def validate_date(str):
    """
    Return True if date matches regex for YYYY-MM-DD format
    """
    return bool(re.match(r"^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])$", str))

def search(str):
    """
    Finds item in db in which the name contains a match to the str param
    """
    with connect_db() as con:
        try:
            cur = con.cursor()
            query = "SELECT * FROM items WHERE name LIKE CONCAT('%', ?, '%')"
            cur.execute(query, (str,))
            rows = cur.fetchall()
            if rows:
                print("Found:")
                table = []
                for row in rows:
                    id, name, date, price, location = row[0], row[1], row[2], row[3], row[4]
                    row = [id, name, date, price, location]
                    table.append(row)
                print(format_rows_as_table(table))
            else:
                print(f"No items found for '{str}'")
        except sqlite3.OperationalError as e:
            print(e)

def get_item_input(action):
    """
    Handle getting user input for item
    Returns list with validated item input
    Used when adding or updating an item
    """
    canceled = False
    item = []
    fields = ["name", "date", "price", "location"]
    print("(c) to cancel operation")
    for field in fields:
        while True:
            if field == "name" or field == "location":
                input_val = input(f"{field}: ").strip().lower()
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
            print(f"Canceled {action} item.")
            break
    if input_val != "e" and len(item) == 4:
        return item

def get_input():
    """
    Handles getting user input and calling CRUD functions
    """
    while True:
        print("\n(v)iew, (a)dd, (d)elete, (u)pdate, (s)earch, (cl)ear, (ex)port or (e)xit", end="\n\n")
        action = input("What would you like to do? ").strip().lower()
        if action == "v":
            view_data()
        elif action == "a":
            item = get_item_input("adding")
            if item:
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
        elif action == "u":
            print("(c) to cancel operation")
            input_val = input("ID to update: ").strip()
            if input_val == "c":
                print("Canceled operation")
                continue 
            elif input_val:
                try:
                    id = int(input_val)
                    update_data(id)
                except ValueError:
                    print("ID must be a number")
            else:
                print("ID is required")
        elif action == "s":
            print("(c) to cancel operation")
            input_val = input("Search for item name: ").strip()
            if input_val == "c":
                print("Canceled operation")
                continue
            elif input_val:
                search(input_val)
            else:
                print("Search term required")
        elif action == "cl":
            clear_history()
        elif action == "ex":
            export_data()
        elif action == "e":
            print("Exiting...")
            break
        else:
            print("Invalid input")

def main():
    with connect_db() as con:
        try:
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
        except sqlite3.OperationalError as e:
            print(e)

if __name__ == "__main__":
    main()