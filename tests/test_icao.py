import pytest
from pydantic import ValidationError

from src.models import Icao


def test_icao_is_alphanumeric():
    mroc = Icao(code="mroc")
    assert isinstance(mroc, Icao)

    mr42 = Icao(code="mr42")
    assert isinstance(mr42, Icao)

    mrpv = Icao(code="MRPV")
    assert isinstance(mrpv, Icao)


def test_icao_is_not_alphanumeric():
    bad_icaos = ["mro!", "/kd2", ".pro", "*m*m", "rrr."]

    for icao in bad_icaos:
        with pytest.raises(ValidationError):
            bad = Icao(code=icao)
            assert isinstance(bad, Icao)


def test_icao_incorrect_length():
    bad_icaos = ["h", "oo", "bad", "kklll"]

    for icao in bad_icaos:
        with pytest.raises(ValidationError):
            bad = Icao(code=icao)
            assert isinstance(bad, Icao)
