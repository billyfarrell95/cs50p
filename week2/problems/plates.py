def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    start_two_letter = (s[0].isalpha() and s[1].isalpha())
    valid_len = (len(s) > 1 and len(s) < 7)
    starts_zero = s.startswith("0")
    nums_in_middle = False
    for char in s:
        if char.isnumeric() and s[-1].isalpha():
            nums_in_middle = True
    if (start_two_letter and valid_len and not starts_zero and not nums_in_middle):
        return True
    else:
        return False



main()