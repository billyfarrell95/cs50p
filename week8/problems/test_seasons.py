from seasons import minutes_since_date
import datetime

def test_minutes_since_date():
    assert minutes_since_date(datetime.datetime(2025, 4, 6), datetime.datetime(2024, 4, 6)) == 525600
    assert minutes_since_date(datetime.datetime(2025, 4, 6), datetime.datetime(2023, 4, 6)) == 1052640