#check whether a value is in a list
#'in' allows us to find out if a particular value is already in a list.
#It tells Python to check if the existence of a value is in the list.
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#checking whether a value is NOT in a list
#we use the combined keywords of 'not' and 'in' = 'not in'
#if the value is not in the list, Python returns True
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")