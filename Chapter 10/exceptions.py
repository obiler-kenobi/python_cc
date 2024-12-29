# NOTE: Exceptions
# Python uses special objects called exceptions to manage errors that
# arise during a program's execution. If you write code that handles the
# exception, the program will continue running.
# If you don't handle the exception, the program will halt and show a
# traceback, which includes a report of the exception that was raised.

# Exceptions are handled with try-except blocks. It asks Python to do
# something, but also tells it what to do if an exception is raised.

# NOTE: Handling the ZeroDivisionError Exception
# division_calculator.py
# print(5/0)

# ZeroDivisionError is an example of an exception object. Python creates
# this kind of object in response to a situation where it can't do what
# it was asked to do.

# NOTE: Using try-except Blocks
# When you think an error may occur, you can write a try-except block to
# handle the exception that might be raised.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# NOTE: If the code in the try block works, Python skips over the except
# block. If the code in the try block causes an error, Python looks for 
# except block whose error matches the one that was raised, and runs the
# code in that block.

# NOTE: Using Exception to Prevent Crashes
# Handling errors correctly is especially important when the program has
# more work to do after the error occurs.

# division_calculator.py
print("Give me two numbbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# NOTE: The else Block
# Any code that depends on the try block executing successfully goes in
# the else block.

# division_calculator.py V2
print("Give me two numbbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

# NOTE: The only code that should go in a try block are codes that might
# cause an exception to be raised. Sometimes you'll have additional code
# that should run only if the try block was successful: this code goes
# in the else block. The except block tells Python what to do in case a
# certain exception arises when it tries to run the code in the try
# block.

# NOTE: Handling the FileNotFoundError Exception
# You can handle common issues when working with files like missing
# files, different location, misspelled filename, or non-existence of 
# a file using try-except block.

# alice.py w/ error
# from pathlib import Path

# path = Path('alice.txt')
# contents = path.read_text(encoding='utf-8')

# NOTE: The encoding argument is needed when your system's default 
# encoding doesn't match the encoding of the file that's being read.
# This is most likely to happen when reading from a file that wasn't
# created on your system.

# alice.py v2
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

# NOTE: Analyzing Text

# alice.py v3
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate numbber of words in the file:
    words = contents.split()
    # NOTE: The string method split() by default splits a string 
    # wherever it finds any whitespace.
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# NOTE: Working with Multiple Files
# word_count.py
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)

# NOTE: It's a good habit to keep comments up to date when you're
# modifying a program.

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# NOTE: Failing Silently
# You don't need to report every exception you catch. Sometimes, you'll
# want the program to fail silently when an exception occurs and
# continue on as if nothing happend.

# Python has a pass statement that tells it to do nothing in a block.
# word_count.py v2
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Updated the code to make the program fail silently
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)

# NOTE: It's a good habit to keep comments up to date when you're
# modifying a program.

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

# NOTE: The pass statement also acts as a placeholder. It's a reminder
# that you're choosing to do nothing at a specific point in your
# program's execution and that you might want to do something there
# later.
