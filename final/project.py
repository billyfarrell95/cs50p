import sqlite3, sys, os, time
from tabulate import tabulate

def connect_db():
    return sqlite3.connect("db.sqlite3")

def add_data():
    print("Add data")

def delete_data():
    print("Delete data")

def view_data():
    print("Get data")

def export_html():
    ...

def print_msg(msg):
    print(msg)

def clear_history():
    print("Clear")

def get_input():
    while True:
        print_msg("(v)iew, (a)dd, (d)elete, (c)lear, or (e)xit")
        action = input("What would you like to do? ").strip().lower()
        if action == "v":
            view_data()
        elif action == "a":
            add_data()
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