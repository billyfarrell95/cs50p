def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow", n)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

main()

# i = 0
# while i < 3:
#     print("meow, while", i)
#     i += 1

# for i in [0, 1, 2]:
#     print("meow, list")

# for i in range(3):
#     print("meow, range")

# convention if i isn't needed as a var
# for _ in range(3):
#     print("meow, range convention")

# print("meow in print\n" * 3, end="")