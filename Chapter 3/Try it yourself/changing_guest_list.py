guests = ['oliver','john','arenas']
guests_cant_come = []

#1st solution
cant_make_it = 'arenas'
guests_cant_come.append(cant_make_it)
guests[-1] = 'redon'

name = guests[0].title()
print(f"Hello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

print(f"The guest that can't come is {guests_cant_come[0].title()}.")


#2nd solution
guests = ['oliver','john','arenas']
guests_cant_come = []
cant_make_it = guests.pop()
guests.append('redon')
guests_cant_come.append(cant_make_it)

name = guests[0].title()
print(f"\nHello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

print(f"The guest that can't come is {guests_cant_come[0].title()}.")

#3rd solution
guests = ['oliver','john','arenas']
cant_make_it = 'john'
guests_cant_come = []
guests.insert(1,'redon')
guests.remove(cant_make_it)
guests_cant_come.append(cant_make_it)

name = guests[0].title()
print(f"\nHello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

print(f"The guest that can't come is {guests_cant_come[0].title()}.")

#book solution
#I wasn't able to use this so it's a minus point for me
guests = ['oliver','john','arenas']

name = guests[0].title()
print(f"\nHello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

name = guests[1].title()
print(f"I'm afriad Mr. {name} won't be joining us for dinner.")

del(guests[1])
guests.insert(1, 'redon')

name = guests[0].title()
print(f"\nHello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

