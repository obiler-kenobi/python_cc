#Example of list and printing the whole list
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#Another example but accessing and printing only the element of a list
print(bicycles[0])

#Using a method on an element of a list
print(bicycles[0].title())

#The index of a list always starts at 0
##Accessing the 2nd element
print(bicycles[1])
##Accessing the 4th element
print(bicycles[3])

#The last element can be accessed using [-1] index and the 2nd to the last [-2] and so on and so forth 
##Accessing the last element
print(bicycles[-1])
##Accessing the 3rd last element
print(bicycles[-3])

#Using f-string on individual values from a list
message = f"My first ever bicycle was a {bicycles[0].title()}."
print(message)