import sqlite3, sys, os, time
from tabulate import tabulate

def connect_db():
    return sqlite3.connect("db.sqlite3")

def add_data(item):
    with connect_db() as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO items (name, purchase_date, purchase_price, purchase_location) VALUES (?, ?, ?, ?)", [item])
        con.commit()
        print("Item added!")

def delete_data():
    print("Delete data")

def view_data():
    print("Get data")
    with connect_db() as con:
        cur = con.cursor()
        data = cur.execute("SELECT * FROM items")
        if data != None:
            table = []
            for row in data:
                id = row[0]
                name = row[1].title()
                date = row[2]
                price = row[3]
                # price_str = f"${float(price):.2f}"
                location = row[4].title()
                row = [id, name, price, date, location]
                table.append(row)
            print(tabulate(table, headers=["ID", "Item name", "Date", "Price", "Purchase Location"], tablefmt="rounded_grid"))
            # html_data = tabulate(table, headers=["ID", "Item name", "Price"], tablefmt="html")
            # export_html(html_data)
        else:
            print("No items in db")

def export_html():
    ...

def clear_history():
    print("Clear")

def get_input():
    while True:
        print("(v)iew, (a)dd, (d)elete, (c)lear, or (e)xit")
        action = input("What would you like to do? ").strip().lower()
        if action == "v":
            view_data()
        elif action == "a":
            try:
                print("Add an item")
                while True: 
                    while True:
                        name = input("Name: ").strip()
                        if name == "e":
                            print("Cancelling...")
                            break
                        elif name:
                            break
                    
                    while True:
                        date = input("Purchase date: ").strip()
                        if date == "e":
                            print("Cancelling...")
                            break
                        elif date:
                            break
                    while True:
                        price = input("Purchase price: ").strip()
                        if price == "e":
                            print("Cancelling...")
                            break
                        elif price:
                            break
                    while True:
                        location = input("Purchase location: ").strip()
                        if location == "e":
                            print("Cancelling...")
                            break
                        elif location:
                            break
                    # Handle validation, checking if value is "e"
                    item = (name, date, price, location)
                    add_data(item)

            except ValueError as e:
                print("Invalid input:", e)
        elif action == "d":
            delete_data()
        elif action == "c":
            clear_history()
        elif action == "e":
            sys.exit("Exiting...")

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