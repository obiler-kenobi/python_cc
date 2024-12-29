from pathlib import Path
import json

path = Path('favorite_number.json')

favorite_number = input("What is your favorite number? ")
contents = json.dumps(favorite_number)
path.write_text(contents)
print(f"Your favorite number is {favorite_number} and I'll remember it!")
