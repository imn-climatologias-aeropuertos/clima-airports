import pytest
from pydantic import ValidationError

from src.models import Station, Icao


def test_valid():
    icao = Icao(code="MROC")
    name = "International Airport Juan Santamaría"
    op_hours = [h for h in range(0, 24)]

    mroc = Station(name=name, icao=icao, op_hours=op_hours)
    assert isinstance(mroc, Station)


def test_invalid_names():
    icao = Icao(code="MROC")
    bad_names = [
        "InternationalAirportJuanSantamaría",
        "AK ANCHORAGE/ARTCC",
        "International Airport Tobías Bolaños!",
    ]
    op_hours = [h for h in range(0, 24)]

    for name in bad_names:
        with pytest.raises(ValidationError):
            mroc = Station(name=name, icao=icao, op_hours=op_hours)
            assert isinstance(mroc, Station)


def test_invalid_operation_hours_range():
    icao = Icao(code="MROC")
    name = "International Airport Juan Santamaría"
    bad_op_hour_ranges = [
        [h for h in range(-1, 13)],
        [h for h in range(12, 25)],
        [h for h in range(100, 150)],
        [h for h in range(-5, 0)],
    ]

    for hrange in bad_op_hour_ranges:
        with pytest.raises(ValidationError):
            mroc = Station(name=name, icao=icao, op_hours=hrange)
            assert isinstance(mroc, Station)
