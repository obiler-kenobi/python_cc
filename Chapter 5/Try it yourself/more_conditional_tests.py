color = 'black'
print("Is the color in the variable black?")
print(color == 'black')
print("Is the color in the variable red?")
print(color == 'red')

mood = 'empty'
print("\nAre you not happy?")
print(mood != 'happy')
print("Do you not feel empty?")
print(mood != 'empty')

username = "Oliver"
print("\nThe username Oliver is not avaiable!")
print(username.lower() == 'oliver')
print("The username Olivers is not available!")
print(username.lower() == 'olivers')

age = 29
print("\nI am already 29 years old!")
print(age == 29)
print("Am I already 30?")
print(age == 30)

empty = 0
print("\nIs 0 not empty?")
print(empty != 0)
print("Is 1 not empty?")
print(empty != 1)

price = 2_000
print("\nIs the price more than 1,000")
print(price > 1_000)
print("Is the price more than 3,000")
print(price > 3_000)

pokemon = 4
print("\nDo you have less than 6 pokemon in your hand?")
print(pokemon < 6)
print("Do you have less than 4 pokemon in your hand?")
print(pokemon < 4)

my_grade = 75
print("\nDid you pass the subject?")
print(my_grade >= 75)
my_grade = 89
print("Did you pass the subject?")
print(my_grade >= 75)
my_grade = 70
print("Did you pass the subject?")
print(my_grade >= 75)

discount = 1_000
print("\nDid you pay less than the discount? (Paid 900)")
print(900 <= discount)
print("Did you pay the discount? (Paid 1000)")
print(1000 <= discount)
print("Did you pay less than the discount? (Paid 1500)")
print(1500 <= discount)

written = 'pass'
technical = 'pass'
print("\nDid you pass the interview?")
print(written == 'pass' and technical == 'pass')
written = 'pass'
technical = 'fail'
print("Did you pass the interview?")
print(written == 'pass' and technical == 'pass')

person_1 = 'president'
person_2 = 'manager'
print("\nIs any person authorized to sign?")
print(person_1  == 'president' or person_2 == 'vice-president')
person_1 = 'employee'
person_2 = 'manager'
print("Is any person authorized to sign?")
print(person_1  == 'president' or person_2 == 'vice-president')

consoles = ['ps1','ps2','ps3','ps4','ps5']
print(f"\n{'ps1' in consoles}")
print('xbox' in consoles)

consoles = ['ps1','ps2','ps3','ps4','ps5']
print(f"\n{'ps1' not in consoles}")
print('xbox' not in consoles)