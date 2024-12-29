major_rivers = { 
    'amazon': 'brazil',
    'nile': 'egypt',
    'yangtze': 'china',
    'mississippi': 'united states',
    'ganges': 'india',
    }

for river, country in major_rivers.items():
    print(f"\nThe {river.title()} River runs through {country.title()}.")

print("\nThe top 5 major rivers in the world are:")
for river in major_rivers.keys():
    print(river.title())

print("\nThe countries where major rivers in the world are located:")
for country in major_rivers.values():
    print(country.title())