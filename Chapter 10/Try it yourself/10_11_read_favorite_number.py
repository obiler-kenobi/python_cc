from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's {favorite_number}!")
else:
    print("Sorry, I don't know what your favorite number is.")