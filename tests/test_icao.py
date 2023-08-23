from src.models import Icao

def test_icao_is_alphanumeric():
    icao = Icao(code="mroc")
    icao = Icao(code="mr42")
    icao = Icao(code="MRPV")