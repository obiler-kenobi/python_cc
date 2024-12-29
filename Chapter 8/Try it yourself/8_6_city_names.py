def city_country(city, country):
    """Displays a city and its country of origin"""
    place = f"{city}, {country}"
    return place.title()

manila = city_country('manila', 'philippines')
print(manila)

tokyo = city_country('tokyo','japan')
print(tokyo)

beijing = city_country('beijing','china')
print(beijing)