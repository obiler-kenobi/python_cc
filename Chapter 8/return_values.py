# NOTE: Functions can process data and then return a value or set of
# values which are called return value/s. 

# NOTE: The return statement takes a value from inside a function and 
# sends it back to the line that called the function

# NOTE: Returning a simple value

# formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# NOTE: When you call a function that return a value, you need to
# provide a variable that the return value can be assigned to

# NOTE: Sometimes it makes sense to make an argument optional, so that
# when using a function, people can choose to provide extra information
# only if they want to. To achieve that, we can use default values to 
# make an argument optional

# formatted_name.py updated with optional argument
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

# NOTE: Optional values allow functions to handle a wide range of use
# case while letting function calls remain as simple as possible

# NOTE: Returning a dictionary
# A function can return any kind of value you need it to, including more
# complicated data structures like lists and dictionaries

# person.py
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)

# person.py modified to add age in the dictionary
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age=27)
print(musician)

# NOTE: Using a function with a while loop

# greeter.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First Name: ")
#     l_name = input("Last Name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"Hello, {formatted_name}!")


# greeter.py modified to have a break statement for quitting the program
while True:
     print("\nPlease tell me your name:")
     print("(enter 'q' at any time to quit)")
     f_name = input("First Name: ")
     if f_name == 'q':
         break
     
     l_name = input("Last Name: ")
     if l_name == 'q':
         break

     formatted_name = get_formatted_name(f_name, l_name)
     print(f"Hello, {formatted_name}!")
