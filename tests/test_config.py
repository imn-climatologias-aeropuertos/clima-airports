from src.config import MONTHS


def test_months():
    assert MONTHS[1].name == "febrero"

    expected_days_as_str = [f"{day}" for day in range(1, 32)]
    assert MONTHS[4].days_as_str == expected_days_as_str

    expected_days_as_int = [int(day) for day in expected_days_as_str]
    assert MONTHS[4].days_as_int == expected_days_as_int

    assert MONTHS[11].index == 12
