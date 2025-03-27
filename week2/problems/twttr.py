def main():
    value = input("Input: ")
    shortened = remove_vowels(value)
    print(shortened)

def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    no_vowels = string
    for vowel in vowels:
        if vowel in string.lower():
            no_vowels = no_vowels.replace(vowel, "")
    return no_vowels

main()