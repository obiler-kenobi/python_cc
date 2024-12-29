# NOTE: Functions are named blocks of code designed to done specific
# job. Functions are used to avoid typing all the code for the same
# task again and again.

# greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# NOTE: The keyword def informs the Python that we are defining a
# function. This is the function definition which tells the Python the
# name of the function and what kind of information the function needs
# to do its job. The parentheses holds that information. Even if the
# function have no need of information to do its job, the parentheses
# are still required. The function then ends with a colon.

# NOTE: The comment below the function name is called a docstring.
# It can be used using triple quotes (""" """). This is often used to 
# describe what a function does. When Python generates documentation,
# it looks for a string immediately after the function's definition.

# NOTE: A function call tells Python to execute the code in the function
# To call a function, you write its name along with the necessary
# information in the parentheses.

# NOTE: Passing information to a function

# modified greeter.py
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user("oliver")

# NOTE: By adding 'username' in the parentheses, the function can now
# accept any value of username the user specify. The function now
# expects the user to provide a value for username each time it's called

# NOTE: Arguments and Parameters

# In the previous example, the defined greet_user() function required a
# value for the variable username. That variable is an example of a 
# parameter. Parameters are pieces of information the function needs to
# do its job. The value 'oliver' is an example of an argument.
# Arguments are pieces of information that's passed from a function 
# call to a function.

# NOTE: When we call the function, we place the value we want the
# function to work with in parentheses. In this case, the argument
# 'oliver' was passed to the function greet_user(), and the value was
# assigned to the parameter username.