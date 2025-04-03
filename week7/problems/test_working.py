from working import convert
import pytest

def test_convert_valid():
    assert convert("9am to 5pm") == "9:00 to 17:00"
    assert convert("9 AM to 5 PM") == "9:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 8:00"

def test_convert_invalid():
    invalid = [" ", "9 AM - 5 PM", "09:00 AM - 17:00 PM"]
    for item in invalid:
        with pytest.raises(ValueError) as excinfo:
            convert(item)
        assert str(excinfo.value) == "Invalid"