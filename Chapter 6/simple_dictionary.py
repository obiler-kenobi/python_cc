# NOTE: Python's dictionary allows us to connect pieces of related 
# information. It is similar to lists but allows us to connect pieces of information.

# Simple dictionary
alien_0 = {'color':'green', 'points': 5}

# access and prints the value of color and points of alien_0 dictionary
print(alien_0['color'])
print(alien_0['points'])

# NOTE: Working with dictionaries
# A dictionary in Python is a collection of key-value pairs. Each key
# is connected to a value, and you can use a key to acces the value
# associated with that key. A key's value can be a number, a string, a 
# list, or even another dictionary. Any object that you can create can 
# be used as a value in a dictionary.

# NOTE: A dictionary is wrapped in braces {} with a series of key-value 
# pairs.
# A key-value pair is a set of value associated with each other
# Every key is connected to its value by a colon, and individual
# key-value pairs are separated by commas.

# NOTE: Adding New Key-Value pairs
# Dictionaries are dynamic structures, and you can add new key-value 
# pairs to a dictionary at any time. You can do this by giving the name
# of the dictionary followed by the new key in brackets [] along with
# the new value.
alien_0 = {'color':'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# NOTE: Starting with an empty dictionary
# It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it. To start, define a
# dictionary with an empty set of braces and then add each key-value 
# pair on its own line

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# NOTE: Typically, you'll use empty dictionaries when storing user-
# supplied data in a dictionary or when writing a code that generates a 
# large number of key-value pairs automatically.

# NOTE: Modifying values in a dictionary
# To modify a value in a dictionary, give the name of the dictionary 
# with he key in square brackets and then the new value you want 
# associated with that key.

alien_0 = {'color':'green'}
print(f"\nThe alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

# Tracking the position of an alien example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

# alien_0['speed'] = 'fast' book sample; modifying the value to see the
# change in output

# Move alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_inrecement = 1
elif alien_0['speed'] == 'medium':
    x_inrecement = 2
else:
    # This must be a fast alien
    x_inrecement = 3

# The new position is the old position plush the increment.
alien_0['x_position'] = alien_0['x_position'] + x_inrecement

print(f"New position: {alien_0['x_position']}\n")

# Removing key-value pairs
# When you no longer need a piece of information that's stored in a
# dictionary, you can use the del statement to compeletely remove a key-
# value pair. del only needs the name of the dictionary and the key to
# be removed

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# NOTE: The delete key-value pair is removed permanently

# NOTE: A dictionary of Similar Objects
# You can use a dictionary to store one kind of information about many
# objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

language = favorite_languages['sarah'].title()
print(f"\nSarah's favorite language is {language}.")

# NOTE: Using get() to access dictionary values
# Using keys in square brackets to retrieve the value you're interested
# in from a dictionary might cause one potential problem; if the key you
# ask for doesn't exist, you'll get an error.

alien_0 = {'color': 'green', 'speed': 'slow'}
# Example of an error; commented out to run the program
# print(alien_0['points'])

# NOTE: For dictionaries specfically, you can use the get() method to 
# set a default value that will be returned if the requested key doesn't
# exist. The get() method requires a key as a first argument and a
# second optional argument, you can pass a value to be returned if the 
# key doesn't exist.

point_value = alien_0.get('points','No point value assigned.')
print(point_value)

# NOTE: If there's a chance the key you're asking for might not exist,
# consider using the get() method instead of the square bracket notation.
# If you leave out the second argument in the call to get() and the key 
# doesn't exist, Python will return None. This special value mean's "no 
# value exists". This is not an error but meant to indicate that absence 
# of a value.
