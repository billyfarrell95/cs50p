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

def is_valid_len(s):
    if (len(s) > 1 and len(s) < 7):
        return True
    else: 
        return False

def has_valid_num_order(s):
    for c in s:
        if c.isnumeric():
            if int(c) > 0:
                return True
            else:
                return False
            
def has_valid_nums_pos(s):
    for c in s:
        if c.isnumeric() and s[-1].isalpha():
            return False
        else: 
            return True

def has_no_punc(s):
    no_punc = True
    for p in punctuation:
        if p in s:
            no_punc = False
            break
    return no_punc

def is_valid(s):
    """
    Must start with 2 letters
    Max 6 chars
    Min 2 chars
    Numbers can't be used in middle
    First num used can't be 0
    No periods, spaces, or punctuation marks
    """
    valid_len = is_valid_len(s)
    if valid_len:
        start_two_letters = does_start_two_letters(s[:2])
        valid_num_order = has_valid_num_order(s)
        valid_num_pos = has_valid_nums_pos(s[2:])
        has_no_punctuation = has_no_punc(s)
        if start_two_letters and valid_num_order and valid_num_pos and has_no_punctuation:
            return True
if __name__ == "__main__":
    main()