#IF STATEMENT SYNTAX
#if conditional_test: --any conditional test can be put in this line
#   do something      --any action can be put in the indented block

#if the conditional test evaluates to True, the Python code following
#the if statement will be executed. However, if it evaluates to False
#Python ignores the code.

age = 19
if age >= 18:
    print("You are old enough to vote!")

#All indented lines after an if statement will be executed if it passes
#the conditional test, but will be ignored the same way if the 
#conditional test fails.

#v2
age = 19
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")

#v3: Failing the test: No output will be shown
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")

#IF-ELSE STATEMENT SYNTAX
#Python's if-else syntax makes it possible to take one action when
#the conditional test passes and do other actions in all other cases.
#if conditional_test:
#   do something
#else:
#   do something else
age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#IF-ELIF-ELSE STATEMENT SYNTAX
#Python's if-elif-else syntax enables us to test more than two possible
#situations.
#if conditional_statement:
#   do something
#elif conditional_statement:
#   do another thing
#else:
#   do something elese      

#It's important to note that Python only executes one block of code in
#an if-elif-else statement chain. It runs each conditional tests and 
#once it passes, it will execute the code following it and skips the
#rest of the tests.

age = 19
if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYou admission cost is $25.")
else:
    print("\nYour admission cost is $40.")

#v2: cleaner and more efficient; this code is also easier to modify.
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"\nYour admission cost is ${price}.")

#Multiple elif blocks:  You can use as many elif blocks as you want
age = 66
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"\nYour admission cost is ${price}.")

##OMITTING THE ELSE BLOCK
#Python does not require an else block at the end of an if-elif chain
#(will test and check if it's also possible if if-else statement). 
#An else block is useful sometimes but other times, using an additional
#elif statement that catches a specific condition makes it much clearer

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65  :
    price = 20

print(f"\nYour admission cost is ${price}.")

#The else block is a catchall statement. It matches any condition that
#wasn't matched by a specific if or elif test, and that can sometimes
#include invalid or even malicious data. Note: If you have a specific
#final condition to test for, consider using a final elif block and omit
#the else block.

##TESTING MULTIPLE CONDITIONS
#It's also important sometimes to check all conditions of interest. In
#this case, we can use a series of if statements with no elif or else
#else blocks. This technique makes sense when more than one condition 
#could be True, and you want to take act on every condition that is True

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#In summary, if you want only one block of code to run, use an if-elif-
#else chain. If more than one block of code needs to run, use a series
#of independent if statements.