#sort() method changes the order of the list permanently
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#Using reverse=True inside the sort() method will reverse the order of the items in a list
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#sorted() method is used to present the list in sorted order but maintain the original order of the list
cars = ['bmw','audi','toyota','subaru']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

#reverse=True can also be used in sorted as an additional parameter
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

#reverse() method is used to only reverse (and not sort!) the original order of a list
#This method reverse the list in chronological order
#This method also changes the order permanently  
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)