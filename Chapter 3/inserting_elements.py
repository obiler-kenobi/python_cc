#Inserting elements in a list can be done ay any position in the list
motorcycles = ['honda','yamaha','suzuki']

#Using the insert method, you can specify the index of the new element and the value of the new item
#This method opens a space at position [index] and stores the value at that location. This operation shifts every other value one position to the right 
motorcycles.insert(0, 'ducati')

print(motorcycles)