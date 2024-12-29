values = list(range(1,11))
cubes = []

for value in values:
    cube = value ** 3
    cubes.append(cube)

    #print(cube) ; my solution

print(f"The first three items are {cubes[0:3]}")
#print(f"The first three items are {cubes[:3]})
print(f"Three items from middle of the list are {cubes[4:7]}")
print(f"The last three items in the list are {cubes[-3:]}")