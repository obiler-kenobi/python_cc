# NOTE: Whatever the focus of your program is, you'll store the 
# information users
# provide in data structures such as lists and dictionaries. When users 
# close a program, you'll almost always want to save the information 
# they entered. A simple way to do this involves storing your data using 
# the json module.

# NOTE: The json module allows you to convert simple Python data 
# structures into JSON-formatted strings, and then load the data from 
# that file the next time the program runs. You can also use json to 
# share data between different python program or with people who work in 
# many other programming languages.

# NOTE: The JSON (JavaScript Object Notation) format was originally 
# developed for JavaScript. However, it has since become a common format 
# used by many languages including Python.

# NOTE: Using json.dumps() and json.loads()
# The json.dumps() generate a string containing the JSON representation
# of the data we're working with.
# The json.loads() reads the data in JSON format. This function takes in
# a JSON-formatted string and returns a Python object.

# number_writer.py
#from pathlib import Path
#import json

#numbers = [2, 3, 5, 7, 11, 13]

#path = Path('number.json')
#contents = json.dumps(numbers)
#path.write_text(contents)

# number_reader.py
from pathlib import Path
import json

path = Path('number.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

# NOTE: Saving and Reading user-generated data
# Saving data with json is useful specially when working with user-
# generated data to store the user's information so that you won't lose
# it when the program stops running.

# remember_me.py
#from pathlib import Path
#import json

#username = input("What is your name? ")

#path = Path('username.json')
#contents = json.dumps(username)
#path.write_text(contents)

#print(f"We'll remember you when you come back, {username}!")

# greet_user.py
#from pathlib import Path
#import json

#path = Path('username.json')
#contents = path.read_text()
#username = json.loads(contents)

#print(f"Welcome back, {username}!")

# remember_my.py v2
from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")

# NOTE: The exist() method from pathlib returns True if a file or folder
# exists and False if it doesn't.
