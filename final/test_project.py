from project import validate_date

def test_validate_date():
    assert validate_date("2025-05-12") == True
    assert validate_date("2025-6-12") == True
    assert validate_date("2025-06-1") == True
    assert validate_date("2025-6-01") == True
    assert validate_date("2025-05-32") == False
    assert validate_date("2025-13-12") == False
    assert validate_date("2025/06/12") == False
    assert validate_date("April 14, 2025") == False
    assert validate_date("") == False