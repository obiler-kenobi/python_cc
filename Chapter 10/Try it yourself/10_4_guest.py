from pathlib import Path

path = Path('guest.txt')

name = input("Hi! What's your name? ")

path.write_text(name)
print(f"Thank you, {name.title()}")