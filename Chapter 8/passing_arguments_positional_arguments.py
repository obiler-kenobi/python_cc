# NOTE: Since a function definition can have multiple parameters, a
# function call may need multiple arguments.

# NOTE: There are many ways to pass arguments to functions.
# Positional arguments: which need to be in the same order the
# parameters were written;
# Keyword arguments: where each argument consists of a variable name and
# a value;
# And lists and dectionaries of value

# NOTE: Positional Arguments
# Python must match each argument in the function call with a parameter
# in the function definition. Values matched up this way are called 
# positional arguments.

# pets.py

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# NOTE: Multiple Function Calls
# You can call a function as many times as needed('

describe_pet('dog','willie')

# NOTE: Order Matters in Positional Arguments
# You can get unexpeted results if you mix up the order of the arguments
# in a function call when using positional arguments.

describe_pet('harry','hamster')