from pathlib import Path
import json

path = Path('favorite_number.json')

def get_stored_favorite_number(path):
    """Get the users stored favorite number if available"""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None

def get_new_favorite_number(path):
    """Prompt user to enter their favorite number."""
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def show_favorite_number():
    """Show the user their favorite number."""
    path = Path('favorite_number.json')
    favorite_number = get_stored_favorite_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        favorite_number = get_new_favorite_number(path)
        print(f"Your favorite number is {favorite_number}! I'll remember it!")

show_favorite_number()

# Book solution
# from pathlib import Path
# import json

# path = Path('favorite_number.json')
# try:
#    contents = path.read_text()
# except FileNotFoundError:
#     number = input("What's your favorite number? ")
#     contents = json.dumps(number)
#     path.write_text(contents)
#     print("Thanks, I'll remember that.")
# else:
#     number = json.loads(contents)
#     print(f"I know your favorite number! It's {number}.")