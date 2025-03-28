from string import punctuation
def main():
    while True:
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")

def does_start_two_letters(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    else:
        return False

def validate_len(s):
    if (len(s) > 1 and len(s) < 7):
        return True
    else: 
        return False

def is_first_num_zero(s):
    for c in s:
        if c.isnumeric():
            if int(c) > 0:
                return True
                break
            else:
                return False
            
def has_nums_in_middle(s):
    for c in s:
        if c.isnumeric() and s[-1].isalpha():
            return False
        else:
            return True

def has_punct(s):
    for p in punctuation:
        if p in s:
            print("has punc")
            return False
            break
        else:
            return True

def is_valid(s):
    """
    Must start with 2 letters
    Max 6 chars
    Min 2 chars
    Numbers can't be used in middle
    First num used can't be 0
    No periods, spaces, or punctuation marks
    """
    is_valid_length = validate_len(s)
    if is_valid_length:
        start_two_letters = does_start_two_letters(s[:2])
        first_num_not_zero = is_first_num_zero(s)
        no_nums_in_middle = has_nums_in_middle(s[2:])
        no_punctuation = has_punct(s)
        if start_two_letters and first_num_not_zero and no_nums_in_middle and no_punctuation:
            return True

main()