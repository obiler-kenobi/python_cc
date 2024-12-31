def city_country(city_name, country_name, population=0):
    """Get the city, country, and population from users."""
    if population:
        city_country = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        city_country = f"{city_name.title()}, {country_name.title()}"
    return city_country

# Book solution:
# def city_country(city, country, population=0):
#     """Return a string representing a city-country pair."""
#     output_string = f"{city.title()}, {country.title()}"
#     if population:
#         output_string += f" - population {population}"
#     return output_string