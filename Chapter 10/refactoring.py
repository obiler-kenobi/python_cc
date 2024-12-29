# Refactoring is the process of breaking up your code into a series of
# functions that have specific jobs. It makes your code cleaner, easier
# to understand, and easier to extend.

# remember_me.py v3
#from pathlib import Path
#import json

#def greet_user():
#    """Greet the user by name."""
#    path = Path('username.json')
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        print(f"Welcome back, {username}!")
#    else:
#        username = input("What is your name? ")
#        contents = json.dumps(username)
#        path.write(contents)
#        print(f"We'll remember you when you come back, {username}!")

#greet_user()

# remember_me.py v4
# from pathlib import Path
# import json

#def get_stored_username(path):
#    """Get stored username if available."""
#    if path.exists():
#        contents = path.read_text()
#        username = json.loads(contents)
#        return username
#    else:
#        return None

#def greet_user():
#    """Greet the user by name."""
#    path = Path('username.json')
#    username = get_stored_username(path)
#    if username:
#        print(f"Welcome back, {username}!")
#    else:
#        username = input("What is your name? ")
#        contents = json.dumps(username)
#        path.write_text(contents)
#        print(f"We'll remember you when you come back, {username}!")
    
#greet_user()

# NOTE: A good practice is to ensure that a function should either
# return the value you're expecting, or it should return None.

# remember_me.py v5
from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")
    
greet_user()

# NOTE: Each function in this final version has a single, clear purpose.
