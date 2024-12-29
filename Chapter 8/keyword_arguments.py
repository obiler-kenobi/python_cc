# NOTE: Keyword arguments is a name-value pair that you pass to a
# function. You directly associate the name and the value within the
# argument. Keyword arguments free you from having to worry about 
# correctly ordering your arguments in the function call, and they
# clarify the role of each value in the function call

# pets.py
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# NOTE: When you use keyword arguments, be sure to use the exact names
# of the paramenters in the function definition

# NOTE: Default values
# When writing functions, you can define a defaul value for each
# parameter. When you define a default value, you can exclude the
# corresponding argument you'd usually write in the function call

# pets.py 
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# NOTE: The order of the parameters in the function definition had to be
# changed. Because the default value makes it unecessary to specify a
# type of animal as an argument, the only argument left in the function
# call is the pet's name. Python still interprets this as a positional
# argument, so if the function is called with just a pet's name, that
# argument will match up with the first parameter listed in the
# function's definition. 

# NOTE: When you use default values, any parameter with a default value
# needs to be listed after all the parameters what don't have default
# values. This allows Python to continue interpreting positional
# arguments correctly

# NOTE: Equivalent Function Calls
# Because positional arguments, keyword arguments, and default values
# can all be used together, you'll often have several equivalent ways
# to call a function

# Example
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# NOTE: Avoiding Argument Errors
# Unmatched arguments occur when you provide fewer or more arguments
# than a function needs to do its work.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()