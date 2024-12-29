# NOTE: Sometimes you won't ahead of time how many arguments a function
# needs to accept. However, Python allows a function to collect an
# arbitrary number of arguments from the calling statement

# pizza.py
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# NOTE: the asterisk (*) in the parameter names tells Python to make a 
# tuple called toppings, containing all the values this function
# receives. Python packs the arguments into a tuple, even if the 
# function receives only one value

# pizza.py w/ loop
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# NOTE: Mixing positional and arbitrary arguments
# If you want a function to accept several different kinds of arguments,
# the parameter that accepts and arbitrary number of arguments must be
# placed last in the function definition. Python matches positional and
# keyword arguments first and then collects any remaining arguments in
# the final parameter

# pizza.py positional w/ arbitrary
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE: You'll often see the generic parameter name *args, which
# collects arbitrary positional arguments like this

# NOTE: Using arbitrary keyword arguments
# Sometimes you'll want to accept an arbitrary number of arguments, but
# you won't know ahead of time what kind of information will be passed
# to the function. In this case, you can write functions that accept as
# many key-value pairs as the calling statement provides

# user_profile.py
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# NOTE: The definition of build_profile() expects a first and last name,
# and then it allows the user to pass in as many name-value pairs as
# they want. The double asterisks (**) before the parameter user_info
# cause Python to create a dictionary called user_info containing all
# extra name-value pairs the function receives. Within the function, you
# can access the key-value pairs in user_info just as you would for any 
# dictionary

# NOTE: You can mix positional, keyword, and arbitrary values in many
# different ways when writing your own functions

# NOTE: You'll often see the parameter name **kwargs used to collect
# nonspecific keyword arguments