"""Read cats and dogs from a file and catch exception error"""
from pathlib import Path

files = ['cats.txt','dogs.txt']
for file in files:
    path = Path(file)
    try:
        content = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(content)