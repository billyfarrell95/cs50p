import sqlite3, os, time, webbrowser
from tabulate import tabulate

def connect_db():
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

def get_input():
    """
    Handles getting user input and calling CRUD functions
    """
    while True:
        print("(v)iew, (a)dd, (d)elete, (c)lear, or (e)xit")
        action = input("What would you like to do? ").strip().lower()
        
        if action == "v":
            view_data()
        elif action == "a":
            item = []
            fields = ["Name", "Purchase date", "Purchase price", "Purchase location"]
            for field in fields:
                while True:
                    input_val = input(f"{field}: ").strip()
                    if input_val == "e":
                        print("Cancelling...")
                        break 
                    elif input_val:
                        item.append(input_val)
                        break
                    else:
                        print(f"{field} required")
                if input_val == "e":
                    break

            if input_val != "e" and len(item) == 4:
                add_data(item)
            elif input_val == "e":
                continue 

        elif action == "d":
            while True:
                input_val = input("ID to delete: ").strip()
                if input_val == "e":
                    print("Cancelling...")
                    break 
                elif input_val:
                    try:
                        id = int(input_val)
                        delete_data(id)
                        break
                    except ValueError:
                        print("ID must be a number")
                else:
                    print("ID is required")
            if input_val == "e":
                break
        elif action == "c":
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