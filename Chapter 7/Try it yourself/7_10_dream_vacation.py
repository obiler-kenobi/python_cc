# book solution
# name_prompt = "What's your name? "
# location_prompt = "Where is your dream vacation? "
# repeat_prompt = "Would you like others to take the poll?(yes/no) "

responses = {}

poll_active = True
while poll_active:
    name = input("What's your name? ")
    # name = input(name_prompt)
    dream_vacation = input(f"Hi {name.title()}! Where is your dream vacation? ")
    # location = input(location_prompt)

    responses[name] = dream_vacation
    # responses[name] = location

    repeat = input("Would you like others to take the poll?(yes/no) ")
    # repeat = input(repeat_prompt)

    # if repeat != 'yes': NOTE: this is a better solution
    #   break
    if repeat == 'no':
        poll_active = False

print("\n--- Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} really wanted to go to {vacation.title()}!")

