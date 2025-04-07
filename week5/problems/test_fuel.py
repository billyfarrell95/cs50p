from fuel import (
    convert,
    gauge
)
import pytest

def test_convert():
    assert convert("1/3") == 33
    assert convert("1/2") == 50
    assert convert("2/3") == 67
    assert convert("7/12") == 58
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("100/100") == 100
    assert convert("99/100") == 99

    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ValueError):
        convert("10/3")

    with pytest.raises(ValueError):
        convert("1.25/7")

    with pytest.raises(ValueError):
        convert("2-3")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"