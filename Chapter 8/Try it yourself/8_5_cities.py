def describe_city(city, country='Philippines'):
    """Describe a city"""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('reykjavik','iceland')
describe_city('cebu')
describe_city(city='puerto princesa')