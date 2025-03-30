def main():
    value = input("Input: ")
    shortened = shorten(value)
    print(shortened)


def shorten(string):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = string
    for vowel in vowels:
        if vowel in string.lower():
            no_vowels = no_vowels.replace(vowel, "")
    return no_vowels


if __name__ == "__main__":
    main()