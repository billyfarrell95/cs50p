from ip import validate

def test_validate_invalid():
    assert validate("") == False
    assert validate(" ") == False
    assert validate("521.512.512.512") == False
    assert validate("0.0.123.256") == False
    assert validate("127.0.0.1.1") == False

def test_validate_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True