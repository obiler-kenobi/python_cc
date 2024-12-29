prompt = "Good day! Welcome to the movie theater!"
prompt += "\nThe price of the ticket will depend on your age! What is your age? "

active = True
while active:
    age = input(prompt)

    # book solution
    # if age == 'quit':
    #   break
    age = int(age)
    if age < 3:
        print("\nThe ticket for you is free!")
    elif age < 13:
        print("\nThe ticket for you is only $10.00")
    else:
        print("\nThe standard ticket is $15.00!")