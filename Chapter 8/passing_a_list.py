# NOTE: You'll find it useful to pass a list to a function, whether it's
# a list of names, numbers, or more complex objects, such as
# dictionaries. When you pass a list to a function, the function gets a
# direct access to the contents of the list

# greet_users.py

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# NOTE: When you pass a list to a function, the function can modify the
# list. Any changes to the list inside the function's body are permanent

# printing_models.py (w/o functions)

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed.")
for completed_model in completed_models:
    print(completed_model)

# printing_models.py (reorganized to functions)
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

# NOTE: This program is easier to to extend than the version without
# functions. This technique is more efficient than having to update
# code separately in several places in the program. This example also
# demonstrates the idea that every function should have one specific
# job.

# NOTE: Remember that you can always call a function from another
# function which will be helpful when splitting complex task into a 
# series of steps

# NOTE: Preventing a function from modifying a list

# printing_models.py (passing a copy of a list to avoid mofications)
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# NOTE: The slice notation "[:]" makes a copy of the list to send to the
# function. This is to avoid emptying the list of unprinted designs
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

# NOTE: Even though you can preserve the content of a list by passing a
# copy of it to your functions, you should pass the original list to
# functions unless you have a specific reason to pass a copy. It's more
# efficient for a function to work with an existing list, because this
# avoids using the time and memory needed to make a separate copy. This
# is especially true when working with large lists

