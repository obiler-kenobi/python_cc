# NOTE: One advantage of functions is the way they separate blocks of
# code from your main program. You can go a step further by storing your
# functions in a separate file called a module and then importing that 
# module into your main program.

# NOTE: An import statement tells Python to make the code in a module
# available in the currently running program file.

# NOTE: Storing your functions in a separate file allows you to hide the
# details of your program's code and focus on it's higher-level logic.
# It also allows you to reuse functions in many different programs.

# NOTE: Importing entire module
# A module is a file ending in .py that contains the code you want to
# import into your program.

# NOTE: This is a sample file to show how to import functions from a
# module in the same directory

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE: When Python reads this file, the line import pizza tells Python 
# to open the file pizza.py and copy all the functions from it into this program

# NOTE: This approach in which you simply write import followed by the
# module name makes every function from the module available in your
# program

# NOTE: Importing specific functions
# You can also import a specific function from a module usinng the
# syntax: from module_name import function_name

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE: You can import as many functions as you want by separting each
# name with a comma: from module_name import function_0, function_1, ...make_pizza

# NOTE: With this syntax, you don't need to use the dot notation when
# call a function since the function was explicitly imported.


# NOTE: Using 'as' to give a function an alias
# If the name of a function you're importing might conflict with an
# existing name in your program, or if the function name is long, you
# can use a short, unique alias - an alternate name similar to a
# nickname for a function

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE: The import statement shown here renames the function. Anytime we
# call the function, we simply write the alias instead, and Python will
# run the code while avoiding any confusion with another name in your
# you might have written in your program

# NOTE: Syntax: from module_name import function as fn

# NOTE: Using as to give a module an alias
# You can also provide an alias for a module name which allows you to
# call the module's function more quickly

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# NOTE: The module pizza is given the alis p in the import statement,
# but all the module's functions retain their original names

# NOTE: Importing all functions in a module
# You can tell Python to import every function in a module by using the 
# asterisk (*) operator. The asterisk in the import statement tells
# Python to copy every function from the module into the program file.
# Because every function is imported, you can call each function by name
# without using the dot notation. However, it's best not to use this
# approach when you're working with larger modules that you didn't write
# If a module the module has a function name that matches an existing
# name in our projecct, you can get unexpected results.

# NOTE: The bet approach is to import the function you want, or import
# the entire module and use the dot notation which will make your code
# clearer and easy to read and understand

# NOTE: Syntax: from module_name import *

# NOTE: Styling functions
# Functions should have descriptive names, and these names should use
# lowercase letters and underscores. Descriptive names help you and
# others understand what your code is trying to do. Module names should 
# use these conventions as well

# NOTE: Every function should have a comment that explains concisely
# what the function does. This comment should appear immediately after
# the function definition and use the docstring format

# NOTE: If you specify a default value for a parameter, no spaces should
# be used on either side of the equal sign.
# ex. def function_name(parameter_0, parameter_1='default value')

# NOTE: The same convention should be used for keyword arguments

# NOTE: PEP 8 recommends that you limit lines of code to 79 characters.
# If a set of parameters causes a function's definition to be longer
# than 79 characters, press ENTER after the opening parenthesis and on
# the next line press the TABA key twice

# ex:
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...

# NOTE: If your pgoram or module has more than one function, you can
# separate each by two blank lines to make it easier to see where one
# function ends and the next one begins

# NOTE: All import statements should be written at the beginning of a
# file. The only exception is if you use comments at the beginning of
# your file to describe the overall program