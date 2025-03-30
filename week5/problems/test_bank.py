from bank import value

def test_value_zero():
    assert value("Hello") == 0
    assert value(" HELLO") == 0
    assert value("Hello, how are you? ") == 0

def test_value_twenty():
    assert value("How are you?") == 20
    assert value(" HOW'S IT GOING?") == 20
    assert value("Hey") == 20

def test_value_hundred():
    assert value("What's up?") == 100
    assert value("") == 100
    assert value(" ") == 100