#create a list
consoles = ['nes','playstation 1','family computer', 'gameboy', 'gameboy advance','gameboy sp','ds','playstation 3','switch','3ds','playstation 5']
print(f"These are all the consoles I had growing up until now: {consoles}")

#access an element
print(f"\nThe most memorable consoles for me are the {consoles[5].title()} and {consoles[1].title()} since I've played these two most of my childhood.")

#access last element of a list
print(f"\nThe latest console I have right now is the {consoles[-1].title()}.")

#modify list
consoles[-3] = 'nintendo switch'
print(f"I renamed the 'switch' to {consoles[-3].title()} so that it will not be confusing for those not familiar with the console.")

#adding elements to list using append()
consoles.append('steamdeck')
consoles.append('nintendo switch 2')
print(f"\nI added a new items in the list: {consoles}. I added one since I'm planning to buy this soon.")

#adding elements to list using insert()
consoles.insert(7, 'playstation 2')
consoles.insert(9, 'playstation 4')
print(f"\nI added Playstion 2 and Playstation 4 in the list because I wanted those before: {consoles}")

#remove an element of a list using del
del consoles[-1]
print(f"\nI removed Nintendo Switch 2 in {consoles} since it's not a priority for me right now.") 

#remove an element of a list using pop
popped_console = consoles.pop()
print(f"\nI also removed {popped_console.title()} from my list for now but it will be the next console I'll be buying when I have enough money.")
print(consoles)

#remove an element using pop with index
popped_console = consoles.pop(7)
print(f"\nI had to remove {popped_console.title()} in {consoles} but it may get back in the list soon once I had enough to collect the consoles I like.")

#removing an element by providing a value using remove()
removed_console = 'playstation 4'
consoles.remove(removed_console)
print(f"\n{removed_console.title()} was also removed from the list: {consoles} since I already have a {consoles[-1].title()}.")

#temporarily sort the list using sorted and reverse it using sorted(reverse=True)
print(f"\nNow to sort the consoles list temporarily: {sorted(consoles)}")
print(f"\nAnd now temporarily reversing the order: {sorted(consoles, reverse=True)}")

#permanently sort the list using sort and reverse it
print(f"\nYou know what, I like it better if the list is sorted alphabetically:")
consoles.sort()
print(consoles)

print(f"\nBut what if I reversed it?")
consoles.sort(reverse=True)
print(consoles)

#reverse the list
print(f"\nAnd reverse it again hehe:")
consoles.reverse()
print(consoles)

#get the length of the list
print(f"\nAll in all, I had owned {len(consoles)} consoles in my life.")
