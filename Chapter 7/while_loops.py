# NOTE: Introducing while loops
# The while loop runs as long as, or while, a certain condition is true

# NOTE: The while loop in action
# Using a while loop to count up through a series of numbers
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# NOTE: the += operator is a shorthand for 
# current_number = current_number + 1

# NOTE: Letting the User choose when to quit

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

# The message variable was defined with empty string so Python has 
# somthing to check the first time it runs otherwise, it will not run
# the program since it has nothing to compare to
message = "" 
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# NOTE: Using a flag
# A flag is a variable that acts as a signal to the program. It is 
# defined to determine whether or not the entire program is active. It
# is commonly used when a program relies on many conditions to be true.
# As a result, the overall while statement needs to check only one 
# condition: whether the flag is currently true.

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# NOTE: Using break to exit a loop
# break can be used to exit a while loop immediately without running
# any remaining code in the loop, regardless of the results of any
# conditional test. You can use it to control which lines of code are 
# executed and which aren't, so the program only executes code that you
# want it to, when you want it to.

prompt = "\nPlease enter the name of a city you have visted: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
        city = input(prompt)

        if city == 'quit':
             break
        else:
             print(f"I'd love to go to {city.title()}!")

# NOTE: You can use break statement in any of Python's loops. For
# example, you could use break to quit a loop that's working through a
# list or a dictionary

# NOTE: Using continue in a loop
# Rather than breaking out of a loop entirely without executing the rest
# of its code, you can use the continue statement to return to the 
# beginning of the loop, based on the result of the conditional test.

current_number = 0
while current_number < 10:
     current_number += 1
     if current_number % 2 == 0:
          continue
     
     print(current_number)

# NOTE: Avoiding infinite loop
# Every while loop needs a way to stop running so it won't continue to
# run forever

x = 1
while x <= 5:
     print(x)
     # x += 1 : if this line was accidentally omittted

# The value of x will start at 1 but will never change and as a result
# the conditional test will always evaluate to True. If a program gets
# stuck in an infinite loop, press CTRL+C or just close the terminal
# window. To avoid writing infinite loops, test every while loop and
# make sure the loop stops when you expect it to. Make sure at least
# one part of the program can make the loop's condition False or cause
# it to reach a break statement