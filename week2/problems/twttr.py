def main():
    value = input("Input: ").strip()
    shortened = remove_vowels(value)
    print(shortened)

def remove_vowels(string):
    vowels = "aeiouAEIOU"
    no_vowels = string
    for vowel in vowels:
        if vowel in string:
            no_vowels = no_vowels.replace(vowel, "")
    return no_vowels

main()

# PASS
# check50 --local cs50/problems/2022/python/twttr