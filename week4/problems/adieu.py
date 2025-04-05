import sys

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            name = name.strip().title()
            names.append(name)
        except EOFError:
            adieu(names)
            sys.exit()

def adieu(list):
    length = len(list)
    adieu_str = "Adieu, adieu, to "
    if length == 1:
        print(f"\n{adieu_str}{list[0]}")
    elif length == 2:
        print(f"\n{adieu_str}{list[0]} and {list[1]}")
    else:
        m = adieu_str
        for name in list[:-1]:
            m += f"{name}, "
        m += f"and {list[-1]}"
        print(f"\n{m}")

main()

# PASS
# check50 --local cs50/problems/2022/python/adieu