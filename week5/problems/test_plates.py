from plates import (
    does_start_two_letters,
    is_valid_len,
    has_valid_num_order,
    has_valid_nums_pos,
    has_no_punc
)

def test_does_start_two_letter():
    assert does_start_two_letters("ABC123") == True
    assert does_start_two_letters("ab1234") == True
    assert does_start_two_letters("12abcd") == False
    assert does_start_two_letters("12ABCD") == False

def test_validate_len():
    assert is_valid_len("abc123") == True
    assert is_valid_len("ab") == True
    assert is_valid_len("abc1234") == False
    assert is_valid_len("a") == False
    assert is_valid_len("") == False

def test_is_first_num_zero():
    assert has_valid_num_order("abc123") == True
    assert has_valid_num_order("abc012") == False

def test_has_nums_in_middle():
    assert has_valid_nums_pos("ab12cd") == True
    assert has_valid_nums_pos("ab1d") == True

def test_has_punct():
    assert has_no_punc("ab^&as") == False
    assert has_no_punc("abc&d3") == False
    assert has_no_punc("ab2@") == False
    assert has_no_punc("abc123") == True