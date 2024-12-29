# NOTE: Nesting is when you want to store multiple dictionaries in a 
# list, or a list of items as a value in a dictionary. You can nest
# dictionaries inside a list, a list of items inside a dictionary, or 
# even a dictionary inside another dictionary.

# NOTE: A list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# NOTE: A more practical example would involve more than three aliens

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Changing the aliens to yellow; 10 points; medium speed;
for alien in aliens[:3]:
    if(alien['color'] == 'green'):
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif(alien['color'] == 'yellow'):
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"\nTotal number of aliens: {len(aliens)}")

# NOTE: A list in a dictionary
# Rather than putting a dictionary in a list, it's sometimes useful to
# put a list inside a dictionary.

# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }

# Summarize the order
print(f"Your ordered a {pizza['crust']}-crust pizza with the "
      "following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# NOTE: You can nest a list inside a dictionary anytime you want more 
# than one value to be associated with a key.

favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['rust','go'],
    'phil': ['python','haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# NOTE: You should not nest lists and dictionary too deeply. If you're
# nesting items much deeper than what you see in the preceding examples, 
# or if you're working with someone else's code with significant levels
# of nesting, there's most likely a simpler way to solve the problem

# NOTE: A dictionary in a dictionary
# You can nest a dicitionary inside another dictionary, but your code
# can get complicated quickly when you do.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# NOTE: The structure of each user's dictionary is identical. Although
# not required by Python, this structure makes nested dictionaries
# easier to work with.