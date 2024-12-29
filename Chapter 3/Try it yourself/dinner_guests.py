guests = ['oliver','john','arenas']
guests_cant_come = []
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

name = guests[0].title()
print(f"Hello {name}, we found a bigger table!")

name = guests[1].title()
print(f"{name}!!, we found a bigger table!")

name = guests[2].title()
print(f"Well, Mr. {name}, we found a bigger table.")

guests.insert(0, 'frances')
guests.insert(2, 'mae')
guests.append('atterado')

name = guests[0].title()
print(f"Hello {name}, would you like to have some dinner with me?")

name = guests[1].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[2].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

name = guests[3].title()
print(f"Hello {name}, would you like to have some dinner with me?")

name = guests[4].title()
print(f"{name}!!, let's go! I'm starving!!")

name = guests[5].title()
print(f"Well, Mr. {name}, we'll be happy if you could join us for dinner.")

print("\nApologies everyone but it seems I can only invite 2 people for dinner.")

popped_guest = guests.pop()
print(f"Apologies {popped_guest.title()}, I'm sorry but the table I ordered won't arrive on time and I won't be able to invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Apologies {popped_guest.title()}, I'm sorry but the table I ordered won't arrive on time and I won't be able to invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Apologies {popped_guest.title()}, I'm sorry but the table I ordered won't arrive on time and I won't be able to invite you to dinner anymore.")

popped_guest = guests.pop()
print(f"Apologies {popped_guest.title()}, I'm sorry but the table I ordered won't arrive on time and I won't be able to invite you to dinner anymore.")

name = guests[0].title()
print(f"Hello {name}, you're still invited for dinner!")

name = guests[1].title()
print(f"Hello {name}, you're still invited for dinner!")

#getting the number of guests invited
print(f"Because of the table, I was only able to invite {len(guests)} guests.")

del guests[0]
del guests[0]

print(guests)

