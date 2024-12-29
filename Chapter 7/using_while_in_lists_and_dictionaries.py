# NOTE: A for loop is effective for looping through a list, but you
# shoudn't modify a list inside a for looop because Python will have
# trouble keeping track of the items in the list. To modify a list as
# you work through it, use a while loop.

# NOTE: Using while loops with lists and dictionaries allows you to 
# collect store, and organize lots of input to examine and report later

# NOTE: Moving items from one list to another

# Example: moving unverified users to verified list

# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfimed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified users into the list of confirmed users.

while unconfimed_users: # This line remaines active as long as the list
                        # is not empty
    current_user = unconfimed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# NOTE: Removing all instances of Specific values from a list
# The remove() function works in the previous examples because the 
# values we're trying to remove only appeared once in the list.

# To remove all instance of a specific value, you can run a while loop
# until that value is no longer in the list

# Example: Removing all instances of 'cat' from the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# NOTE: Filling a Dictionary with User Input
# You can prompt for as much input as you need in each pass through
# with a while loop

# Example: polling program to capture paritipant name and response

responses = {}
# Set a flag to indicate the polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response  in the dictionary
    responses[name] = response # you can use a variable to set the key

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond?(yes/no)" )
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")