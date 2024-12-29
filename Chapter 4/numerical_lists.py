#range() function can be used to print a series of number
#range() fnction causes Python to start counting at the first value you give it, and it stops
#when it reaches the second value you provided
#note: range follows the off-by-one behavior. ex: range(1,5) will result to 1 -> 2 -> 3 -> 4
for value in range(1,5): #to print the values 1 - 5, you should use range(1,6)
    print(value)

#range() can also accept only one argument, and it will start the sequence at 0
print("\n")

for value in range(6):
    print(value)

#range() function can be used with list() function to create a list of numbers
#You just need to wrap the list() function around a call to the range() function
print("\n")

numbers = list(range(1,6))
print(numbers)

#range() function also have the ability to skip/step numbers on a given range
#If you pass a third argument to range() function, that value is being used as a step size when
#generating numbers
print("\n")

even_numbers = list(range(2,11,2))
print(even_numbers)

#using range() function and list() function to create a list of the first 
#10 square numbers (square of integers from 1 - 10)
print("\n")

squares = []
for value in range(1,11):
    #square = value ** 2 #the ** represents the exponents
    #squares.append(square)

    squares.append(value**2)

print(squares)

#simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#min() function gets the smallest number in a list
print(f"\n{min(digits)}")

#max() function gets the largest number in a list
print(f"\n{max(digits)}")

#sum() function get the sum of all the numbers in a list
print(f"\n{sum(digits)}")

#list comprehension allows you to generate a list in just one line of code
#it combines for loop and the creation of new elements in one line
squares = [value**2 for value in range(1,11)]
print(f"\n{squares}")