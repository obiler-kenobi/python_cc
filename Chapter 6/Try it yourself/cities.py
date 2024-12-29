cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_800_000,
        'fact': "Tokyo is home to the world’s busiest pedestrian crossing, Shibuya Crossing, where as many as 3,000 people cross at a time during peak hours.",
        },
    'shanghai': {
        'country': 'china',
        'population': 26_300_000,
        'fact': "Shanghai Tower, the tallest building in China, is the second-tallest in the world and has the world’s fastest elevators, reaching speeds of 20.5 meters per second.",
        },
    'mumbai': {
        'country': 'india',
        'population': 20_700_000,
        'fact': "Mumbai is home to Dharavi, one of the world’s largest slums, but also houses one of the most expensive residential buildings in the world, Antilia.",
        },
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']
    
    print(f"\nThe city of {city.title()} can be found in {country} with a total population of {population}! Did you know that {fact}")

