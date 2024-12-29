favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

people = ['oliver','frances','jen','john rey','vince','sarah','apollo','john vincent','leslie','phil','edward']

for person in people:
    if person in favorite_languages.keys():
        print(f"Hi, {person.title()}! Thank you for your response in the poll.")
    else:
        print(f"Hey, {person.title()}! Answer the poll right now!")
