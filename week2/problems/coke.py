def main():
    cost = 50
    inserted = 0
    while True:
        coin = int(input("Insert Coin: "))
        if (coin == 5 or coin == 10 or coin == 25):
            inserted += coin
            if (inserted >= cost):
                print("Change Owed: ", inserted - cost)
                break
            else:
                print("Amount Due: ", cost - inserted)

main()

# check50 --local cs50/problems/2022/python/coke