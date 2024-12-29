#slice function lets you work with a specific group of items in a list
#The parameters inside the slice function is the index of the first and 
#last elements you want to work with; however, as with the range() function
#Python stops one item before the second index specified
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#getting the 2nd - 4th items in a list
print(players[1:4])

#if the first index is omitted, the slice will always start at the beginning of the list
print(players[:4])

#omitting the 2nd parameter however, will always include all elements from the first parameter through
#the end of the list
print(players[2:])

#using a negative index as the first parameter will slice the list from the end of the list
#this example prints the last three (3) players in the list
print(players[-3:])

#like in range() function, including a third parameter [integer value] will tell the python
#how many items to skip
print(players[0::2])

#slice can be used in a for loop
print("Here are the top three players of my team:\n")
for player in players[:3]:
    print(player.title())

#you can copy a whole list using the slice function
my_foods = ['pizza', 'falafel', 'carrot cake']
#to copy a list, you can make a slice that includes the entire original list by omitting the first and 2nd index;
#you can also add parameters inside the slice function to only copy a range of items in the list
friend_foods = my_foods[:]

print(f"My favorite food are: {my_foods}")
print(f"\nMy friend's favorite food are: {friend_foods}")

#these appends are here to show that the items in my_foods are copied in the friend_foods
#and that they are a separate list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f"\nMy favorite food are: {my_foods}")
print(f"\nMy friend's favorite food are: {friend_foods}")

#if friend_foods is set to equal to my_foods, it will not produce two separate lists
#friends_foods = my_foods tells Python to associate the new variable with the list 
#that is already associated with the original variable, so now both variables point to the same list

#self research note: this happens to lists because they are mutable objects and can be changed 
#even after they are created. Meaning, both the variable my_foods_two and friends_foods_two points to a
#the same list (mutable object) that's why both the variable affects the same list

my_foods_two = ['pizza', 'falafel', 'carrot cake']
friend_foods_two = my_foods_two

my_foods_two.append('cannoli')
friend_foods_two.append('ice cream')

print(f"\nMy favorite food are: {my_foods_two}")
print(f"\nMy friend's favorite food are: {friend_foods_two}")