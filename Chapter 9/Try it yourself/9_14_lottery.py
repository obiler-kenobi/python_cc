from random import choice

winning_characters = [
                        1, 
                        15, 
                        34, 
                        19, 
                        13, 
                        8, 
                        5, 
                        25, 
                        7, 
                        6, 
                        'o', 
                        'j', 
                        'f', 
                        'm', 
                        'a'
                        ]

winning_ticket = []

# book solution
while len(winning_ticket) < 4:
    winning_character = choice(winning_characters)

    if winning_character not in winning_ticket:
        winning_ticket.append(winning_character)

print(f"The winner with the matching ticket of: {winning_ticket} wins the grand price!")

# my solution - bare solution
for num in range(4):
    winning_ticket.append(choice(winning_characters))

print(f"The winner with the matching ticket of: {winning_ticket} wins the grand price!")

