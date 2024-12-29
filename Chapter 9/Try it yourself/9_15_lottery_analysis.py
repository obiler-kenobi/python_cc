from random import choice

winning_numbers = [
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
my_ticket = ['f', 7, 'o', 6]
tries = 0
winner = False

def winning_ticket(winning_numbers):
    winning_ticket = []
    while len(winning_ticket) < 4:
        winning_character = choice(winning_numbers)

        if winning_character not in winning_ticket:
            winning_ticket.append(winning_character)

    return winning_ticket

def check_ticket(winning_ticket, my_ticket):
    if winning_ticket == my_ticket:
        return True
    else:
        return False
    
while winner == False:
    ticket = winning_ticket(winning_numbers)
    winner = check_ticket(ticket, my_ticket)
    tries += 1

print(f"Number of tries: {tries}")





