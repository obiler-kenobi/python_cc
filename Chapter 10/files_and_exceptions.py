# NOTE: Reading from a file

# NOTE: Reading the ocntents of a file

# NOTE: pi_digits.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

# NOTE: To work with the contents of a file, we need to tell Python the 
# path to the file. A path is the exact location of a file or folder on 
# a system. Using the Path object, you can check that the file exists
# before working with it, read the file's contents, or write new data to 
# the file.

# NOTE: Removing the extra string returned by read_text() using rstrip()
contents = contents.rstrip()
print(contents)

path.read_text().rstrip()
print(contents)
# NOTE: This approach is called method chaining. It applies multiple
#  methods in an object in a single expression

# NOTE: Relative and Absolute File Paths
# NOTE: When you pass a simple filename to Path, Python looks in the 
# directory where the file that's currently being executed is stored 
# (the .py program). But the file you're currently being executed is
# also stored in the same working directory you are working on

# NOTE: To get Python to open files from a directory other than the one 
# where your program file is stored, you mneed to provide the correct 
# path

# NOTE: There are two main ways to specify paths in programming. 
# NOTE: A relative path: which tells Python to look for a given location
# relative to the directory where the currently running program file is 
# stored. We need to build a path that starts with the directory/
# location of the file and ends with the filename.
path = Path('text_files/filename.txt')

# NOTE: Absolute path: which tells Python the exact location of the file 
# in your computer, regardless of where the program that's being 
# executed is stored. This can be used if a relative path doesn't work.

path = Path('/home/oliver/python_crash_course/Chapter\ 10/text_files/filename.txt')

# NOTE: Using absolute paths, you can read files from any location on
# your system.

# NOTE: Accessing a file's lines
# When you're working with a file, you'll often want to examine each
# line of the file. You might be looking for certain information in the
# file, or you might want to modify the text in the file in some way.

# NOTE: You can use the splitlines() method to turn a long string into a 
# set of lines, and then use a for loop to examine each line from a 
# file, one at a time
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

# NOTE: Working with a File's Contents
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# NOTE: When Python reads from a text file, it interprets all text in
# the file as a string. If you read in a number and want to work with
# that value in a numerical context, you'll have to convert it to an
# integer using the int() function or a float using the float() function

# NOTE: Large Files: One Million Digits (changed to 100 decimal)
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# NOTE: Is your birthday contained in Pi?
# pi_birthday.py
path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# NOTE: Working with
