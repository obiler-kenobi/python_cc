favorite_numbers = {
    'oliver': [13, 15, 6],
    'frances': [7, 10],
    'serj': [2, 5],
    'leslie': [5],
    'vince': [8, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")