TOTAL_COST = 0

def main():
    with open("taqueria.txt", "r", encoding="utf-8") as file:
        ascii_logo = file.read()
        print(ascii_logo)
    while True:
        try:
            item = input("What would you like to order? ")
            update_order(item)
        except EOFError:
            print("Thanks for ordering!")
            exit()

def update_order(item):
    global TOTAL_COST
    item = item.title().strip()
    if item in menu:
        price = menu[item]
        TOTAL_COST += price
        print(f"Total: ${TOTAL_COST:.2f}")
    else:
        print("Looks like that isn't on the menu.")

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()