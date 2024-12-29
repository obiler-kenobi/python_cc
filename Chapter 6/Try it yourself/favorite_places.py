favorite_places = {
    'oliver': ['baguio','baler','palawan'],
    'frances': ['rizal', 'makati', 'boracay'],
    'john': ['marinduque', 'capiz', 'siquijor'],
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
