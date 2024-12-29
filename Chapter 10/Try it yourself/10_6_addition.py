"""Program that computes two number input from the user"""
from pathlib import Path

print("Enter two numbers to be added together.\n")

first_num = input("Input first number: ")
second_num = input("Input secong number: ")

try:
    first_num = int(first_num)
    second_num = int(second_num)
except ValueError:
    print("Please enter a valid number.")
else:
    print(f"The sum of the numbers you've entered is {first_num + second_num} ")

# Book solution
"""
    try:
        first_num = input("Input first number: ")
        first_num = int(first_num)

        second_num = input("Input second number: ")
        second_num = int(second_num)
    except ValueError:
        print("Please enter a valid number.")
    else:
        print(f"The sum of the numbers you've entered is {first_num + second_num}.") """