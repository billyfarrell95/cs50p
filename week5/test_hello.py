from hello import hello

def test_default():
    assert hello("David") == "hello, David"

def test_argument():
    assert hello() == "hello, world"

def test_default_multiple():
    for name in ["John", "Bob", "George"]:
        assert hello(name) == f"hello, {name}"