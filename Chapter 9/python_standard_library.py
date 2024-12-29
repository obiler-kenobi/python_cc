# NOTE: The Python standard library is a set of modules included with 
# every Python installation. You can use any function or class in the 
# standard library by including a simple import statement at the top of 
# your file.

# NOTE. Random module

# NOTE: randint() function takes two integer arguments and returns a 
# randomly selected integer between (and including) those numbers.

from random import randint
print(randint(1,6))

# NOTE choice() function takes in a list or tuple and returns a randomly 
# chosen element.

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# NOTE: The random module shouldn't be used when building 
# security-related applications.

# NOTE: You can also download modules from external sources.