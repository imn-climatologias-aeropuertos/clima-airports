
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
    bad_icaos = ["mro!", "/kd2", "1234", ".pro"]
    
    for icao in bad_icaos:
        with pytest.raises(ValidationError) as exc_info:
            bad = Icao(code=icao)
            assert isinstance(bad, Icao)