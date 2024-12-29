pets = []

# NOTE: In book solution, there's no need to use _<number> in the 
# variable of the pet dictionary. It will work the same if the variable 
# used is pet = {...}. Additional NOTE: keys can have spaces in the
# dictionary

pet_1 = {
    'kind': 'cat',
    'owner': 'oliver',
    }
pets.append(pet_1)

pet_2 = {
    'kind': 'dog',
    'owner': 'frances',
    }
pets.append(pet_2)

pet_3 = {
    'kind': 'otter',
    'owner': 'john',
    }
pets.append(pet_3)

pet_4 = {
    'kind': 'penguin',
    'owner': 'mae',
    }
pets.append(pet_4)

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']

    print(f"\n\tType of pet: {kind.title()} \n\tOwner: {owner.title()}")

# BOOK SOLUTION
# Make an empty list to store the pets in.
# pets = []

# Make individual pets, and store each one in the list.
# pet = {
#    'animal type': 'python',
#    'name': 'john',
#    'owner': 'guido',
#    'weight': 43,
#    'eats': 'bugs',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'chicken',
#     'name': 'clarence',
#     'owner': 'tiffany',
#     'weight': 2,
#     'eats': 'seeds',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'dog',
#     'name': 'peso',
#     'owner': 'eric',
#    'weight': 37,
#     'eats': 'shoes',
# }
# pets.append(pet)

# Display information about each pet.
# for pet in pets:
#     print(f"\nHere's what I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")