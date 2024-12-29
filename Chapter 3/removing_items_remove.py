#Removing an item can be according to its position or value
#remove() method can be used if only the value of an item is known
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#You can also put the value you want to remove in a variable so you can still use/access it even after removing it
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")