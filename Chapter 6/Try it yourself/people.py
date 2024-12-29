# commented out is the book solution

# people = []

habibi = {
    'first_name': 'frances mae',
    'last_name': 'aterrado',
    'age': 21,
    'city': 'pasay city',
    }
# people.append(habibi)

oliver = {
    'first_name': 'oliver john',
    'last_name': 'arenas',
    'age': 29,
    'city': 'makati city',
    }
# people.append(oliver)

michael = {
    'first_name': 'michael',
    'last_name': 'jackson',
    'age': 50,
    'city': 'new york city',
    }
# people.append(michael)

people = [habibi, oliver, michael]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']

    print(f"\nHi! I'm {full_name.title()}. I'm {age} years old and I live in {city.title()}!")