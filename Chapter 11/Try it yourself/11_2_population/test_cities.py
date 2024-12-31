"""Test for city_function module."""
from city_functions import city_country

def test_city_country():
    """Test if 'Santiago, Chile' works."""
    city_country_result = city_country('santiago', 'chile')
    assert city_country_result == 'Santiago, Chile'

def test_city_country_population():
    """Test if 'Santiago, Chile - population 5000000' works."""
    city_country_result = city_country('santiago', 'chile', 5000000)
    assert city_country_result == 'Santiago, Chile - population 5000000'