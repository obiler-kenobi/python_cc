"""Analyzing winnie the pooh"""
from pathlib import Path

path = Path('pooh.txt')
content = path.read_text()
print(content.count('the'))
print(content.lower().count('the'))
print(content.lower().count('the '))

# NOTE: Converting the string to lowercase using lower() catches all appearances of the word you're looking for.

# Book solution created a function
def count_common_words(filename, word):
    path = Path(filename)
    try:
        content = path.read_text()
    except FileNotFoundError:
        print("File {path} not found.")
    else:
        print(content.lower().count(word))

file = 'pooh.txt'
count_common_words(file,'the')