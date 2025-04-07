from jar import Jar
import pytest

def test_init():
    jar = Jar()
    with pytest.raises(ValueError):
        jar = Jar(-1)
    jar = Jar(0)
    jar = Jar(12)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(20)
    jar.deposit(1)
    jar.deposit(11)
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(12)
    jar.withdraw(1)
    jar.withdraw(5)
    jar.withdraw(4)
    with pytest.raises(ValueError):
        jar.withdraw(6)