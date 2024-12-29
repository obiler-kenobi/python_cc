# NOTE: Looping through all key-value pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
 
# NOTE: To write a for loop for a dictionary, you create names for the
# two variables that will hold the key and value in each key-value pair
# You can choose any names you want for these two variables.

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# NOTE: The items() method return a sequence of key-value pairs when
# used on a dictionary.

# NOTE: Key-value pairs are specially good for dictionaries that stores
# same kind of information for many different keys. The example below is
# the best way to show this since the keys all refer to a person's name
# and all the values refer to their favorite language.

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python'
        }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}.")

# NOTE: This code shows that as the loop works through each key-value
# pair, the key is assigned to the variable name, and the value is 
# assigned to the variable language.

# NOTE: The keys() method is useful when you don't need to work with all
# value in a dictionary. The for loop below tells Python to pull all the
# keys from the dictionary and assign them one at a time to the variable
# name.

for name in favorite_languages.keys():
    print(name.title())

# NOTE: Looping through the keys is actually the default behavior when
# looping through a dictionary.

# This code would have exactly the same output as above
for name in favorite_languages:
    print(name.title())

# NOTE: You can choose to use the keys() method explicitly if it makes
# your code easier to read and understand, or it can also be omitted.

# NOTE: You can access the value associated with any key you care about
# inside the loop, by using the current key.

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# NOTE: The keys() isn't just for looping: it actually returns a
# sequence of all the keys, and the if statement simply checks if the
# 'value' is in the sequence.

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

# NOTE: Looping through a dictionary's keys in a particular order
# You can use the sorted() function to to get a copy of the keys in
# order.

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# NOTE: Looping through all value in the dictionary
# If you are primarily interested in looping through the values that a
# dictionary contains, you can use the values() method to return a
# sequence of values without any keys.

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# NOTE: To see each language chosen without repetition, we can use a set
# A set is a collection of in which each item must be unique. This is 
# useful for large number of polls gathered.

# NOTE: When you wrap a set() around a collection of values that contains
# duplicate items, Python identifies the unique items in the collection
# and builds a set from those items.

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# NOTE: You can build set directly using braces and separating the 
# elements by commas:

favorite_languages = {'python', 'c', 'python', 'rust'}
print(favorite_languages)

# NOTE: When you see braces with no key-value pairs, you're probably
# looking at a set. Unlike lists and dictionaries, sets do not retain
# items in a specific order
