#Removing an item can be according to its position or value
#pop() method removes the last item in a list but lets you work with that item after removing it
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

#Using pop() method to use the last item in the list
motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcyle I owned was a {last_owned.title()}.")

#pop() method can be used to remove an item from any position in a list by including the index of the item in the parentheses
motorcycles = ['honda','yamaha','suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")