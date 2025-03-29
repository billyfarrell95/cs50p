import random, sys

def main():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if not level > 0:
                pass
            else:
                gen_rand(level)
        except ValueError as e:
            pass

def gen_rand(n):
    rand_n = random.randint(1, n)
    guess(rand_n)

def guess(n):
    while True:
        try:
            guess = input("Guess: ")
            guess = int(guess)
            if guess > 0:
                if guess < n:
                    print("Too small!")
                elif guess > n:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()
        except ValueError:
            pass

main()