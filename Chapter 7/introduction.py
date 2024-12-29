# NOTE: Using the input() function, you'll be able to accept user input
# that will allow the Python program to work with it.

# NOTE: Using Python's while loop, you'll be able to keep programs
# running as long as certain conditions remain true.

# NOTE: How the input() function works
# The input() function pauses the program and waits for the user to 
# enter some text. One Python receives the user's input, it assigns that
# input in a variable to make it convenient for the developer to work 
# with

# parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# NOTE: The input function takes one argument: the prompt that we want
# to display to the user, so they know what kind of information to enter

# NOTE: Writing clear prompts
# Each time the input() function is being used, a clear and easy-to-
# follow prompt that tells the user what kind of information being
# being looked for should be included

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# NOTE: Sometimes you'll want to write a prompt that's longer than one
# line. You can assign the prompt in a variable and pass that variable
# to the input() function.

prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# NOTE: The operator += takes the string that was assigned to prompt and
# adds the new string onto the end.

# NOTE: When input() function is used, Python interprets everything the 
# user enters as a string.

# NOTE: Using int() to Accept Numerical Input
age = input("How old are you? ")
# print(age >= 18) this produces an error because a string cannot be 
# compared to a numerical value
age = int(age)
print(age >= 18)

# NOTE: int() exmample 2
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# NOTE: When you use numerical input to do calculations and comparisons,
# be sure to convert the input value to a numerical representation first

# NOTE: The Modulo Operator
# The modulo (%) operator divides a number by another and returns the
# remainder

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

# NOTE: The modulo operator doesn't tell you how many times a number
# fits into another but tells you what the remainder is

# NOTE: Even or Odd example
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
