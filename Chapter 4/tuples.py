#Tuples are lists of items that cannot be changed or immutable
#Instead of using brackets[] we use parentheses() to 'define' the elements of the Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Python return a type error when we try to change the value of the elements of
#Tuple
#dimensions[0] = 250

#Tuples can be defined with one element but a trailing comma needs
#to be included. Although it doesn't make sense to build a tuple with
#one element, this can happen when tuples are generated automatically
my_tuple = (3,)

#Looping through a tuple is the same with lists
for dimension in dimensions:
    print(dimension)

#Although tuples can't be modified, it is possible to assign a new value
#to a variable the represents  a tuple. If we want to change the 
#elements of the tuple, we could redefine the entire tuple:
#python doesn't raise any errors because reassigning a variable is valid
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)