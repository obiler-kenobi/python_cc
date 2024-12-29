my_pizzas = ['cheese spinach','pepperoni','hawaiian']
friend_pizzas = my_pizzas[:] #no need to indicate the first and second parameter when copying the whole list

my_pizzas.append('all meat')
friend_pizzas.append('baked sushi')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())