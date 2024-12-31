"""Test for city_function module."""
from city_functions import city_country

def test_city_country():
    """Test if 'Santiago, Chile' works."""
    city_country_result = city_country('santiago', 'chile')
    assert city_country_result == 'Santiago, Chile'