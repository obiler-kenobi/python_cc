from pathlib import Path

path = Path('guest_book.txt')
active = True
guests = ''
while active:
    name = input("Hi, welcome! Under what name will the reservation be? ")
    if name != 'stop':
        guests += name + "\n"
    else:
        active = False

path.write_text(guests)

# book solution
# prompt = "\nHi, what's your name? "
# prompt += "\nEnter 'quit' if you're the last guest. "

# guest_names = []
# while True:
#     name = input(prompt)
#     if name == 'quit':
#         break

#     print(f"Thanks {name}, we'll add you to the guest book.")
#     guest_names.append(name)

# Build a string where "\n" is added after each name.
# file_string = ''
# for name in guest_names:
#     file_string += f"{name}\n"

# path.write_text(file_string)