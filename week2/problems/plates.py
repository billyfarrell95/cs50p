from string import punctuation
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def does_start_two_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

def validate_len(s):
    if (len(s) > 1 and len(s) < 7):
        return True

def is_first_num_zero(s):
    for c in s:
        if c.isnumeric():
            return c == '0' 
    return False 

def has_nums_in_middle(s):
    found_num = False
    for c in s:
        if c.isnumeric():
            found_num = True
        elif found_num and c.isalpha():
            return True 
    return False 

def has_punct(s):
    for p in punctuation:
        if p in s:
            return True
    return False

def is_valid(s):
    """
    Must start with 2 letters
    Max 6 chars
    Min 2 chars
    Numbers can't be used in middle
    First num used can't be 0
    No periods, spaces, or punctuation marks
    """
    if not does_start_two_letters(s[:2]):
        return False
    
    if not validate_len(s):
        return False
    
    if is_first_num_zero(s):
        return False

    if has_nums_in_middle(s[2:]):
        return False
    
    if has_punct(s):
        return False
    
    return True

main()

# PASS
# check50 --local cs50/problems/2022/python/plates