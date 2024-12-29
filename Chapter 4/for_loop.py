#Printing out the name of magicians using for loop
#Using plural names for list and singular names for the elements of the list will
#help identify if a section of code is working with a single element
#or the entire list
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

#Printing out a message for each magician in the list
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    #Adding an additional message for each magician (element) in the list
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Printing out a summary of the for loop must be done by writing a line/block of code that are not indented
print(f"Thank you, everyone. That was a great magic show!")