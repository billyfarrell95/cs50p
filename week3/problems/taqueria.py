def main():
    total = 0
    while True:
        try:
            item = input("Item: ")
            item = item.title().strip()
            if item in menu:
                price = menu[item]
                total += price
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

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

if __name__ == "__main__":
    main()

# PASS
# check50 --local cs50/problems/2022/python/taqueria