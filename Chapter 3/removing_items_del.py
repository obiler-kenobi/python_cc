#Removing an item can be according to its position or value

#Removing an item using the del statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#del statement can be used when the position of the element to be removed is known
#This operation shifts every other value one position to the left
del motorcycles[0]
print(motorcycles)