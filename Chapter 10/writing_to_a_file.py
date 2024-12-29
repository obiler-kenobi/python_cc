# NOTE: Writing a single line
# Once you have a path defined, you can write to a file using the 
# write_text() method.

# write_message.py
from pathlib import Path

path = Path('programming.txt')
path.write_text('I love programming.')

# NOTE: The write_text() method takes a single argument: the string that 
# you want to write to the file.

# NOTE: Python can only write string to a text file. If you want to 
# store numerical data in a text file, you'll have to convert the data 
# to string format first using the str() function 

# NOTE: Writing multiple lines
# The write_text() method does a few things behing the scenes. If the 
# file that path points to doesn't exist, it creates that file. Also, 
# after writing the string to the file, it makes sure the file is closed 
# properly. To write more than one line to a file, you need to build a 
# string containing the entire contents of the file, and then call 
# write_text() with that string.

from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)

# NOTE:!! Be careful when calling write_text() on a path object. If the 
# file already exists, write_text() will erase the current contents of 
# the file and write new contents to the file.