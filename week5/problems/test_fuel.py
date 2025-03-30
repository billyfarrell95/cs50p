from fuel import (
    convert,
    gauge
)

def test_convert():
    assert convert("1/2") == "50%"
    assert convert("0/0") == None
    assert convert("1/1") == "F"
    assert convert("0/1") == "E"
    assert convert("7/8") == "88%"

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"