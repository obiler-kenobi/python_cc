#checking for special items
#original code
requested_topppings = ['mushroom','green peppers','extra cheese']

for requested_topping in requested_topppings:
    print(f"Added {requested_topping}.")

print("\nFinished making your pizza!\n")

#code without the green peppers using if statement
requested_topppings = ['mushroom','green peppers','extra cheese']

for requested_topping in requested_topppings:
    if requested_topping == 'green peppers':
        print(f"Sorry, we're out of {requested_topping} right now.")
    else:
        print(f"Added {requested_topping}.")

print("\nFinished making your pizza!")

#checking that a list is not empty
requested_topping = []

#When the name of a list is used in a if statement, Python returns True
#if there's at least one item stored in the list, and False if the list
#is empty
if requested_topping:
    for requested_topping in requested_topppings:
        print(f"Added {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

#Using multiple lists
#You can use lists and if statements to make sure the input makes sense
#before you act on it

#The 'available_toppings list can be made into a tuple if it does not
#change
available_toppings = ['mushrooms','olives','green peppers','pepperoni',
                      'pineapple','extra cheese']
requested_topppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_topppings:
    if requested_topping in available_toppings:
        print(f"Added {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
    
print("\nFinished making your pizza!")