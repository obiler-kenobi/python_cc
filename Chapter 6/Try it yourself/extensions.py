users = {
    'aeinstein': {
        'first_name': 'albert',
        'last_name': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first_name': 'marie',
        'last_name': 'curie',
        'location': 'paris',
        },
    'ntesla': {
        'first_name': 'nikola',
        'last_name': 'tesla',
        'location': 'croatia',
        },
    'tedison': {
        'first_name': 'thomas',
        'last_name': 'edison',
        'location': 'united states',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location'].title()

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")