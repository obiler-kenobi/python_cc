current_users = ['Oliver','john','FRANCES','Mace','kenobi','XyPhr']
new_users = ['Johny','OLIVER','XYPHR','Pulsar','conan']

#my solution; inefficient
#lower_current_users = []
#for current_user in current_users:
#    lower_current_users.append(current_user.lower())

#book solution using list comprehension; much cleaner and more efficient
lower_current_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"Sorry, the username ({new_user}) you entered is already in use! Please choose another username!")
    else:
        print("Username is available! Thank your for signing up!")