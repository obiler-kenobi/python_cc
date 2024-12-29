programming_terms = {
    'none': 'A special value meant to indicate the absence of a value.',
    'floats': 'Any number with decimal points.',
    'method': 'An action that Python can perform on a piece of data.',
    'lists': 'Allows you to store sets of information in one place, whether you have just a few items or millions of items.',
    'looping': 'Allows you to take the same action, or set of actions, with every item in a list.',
    'set': 'A collection in which each item must be unique.',
    'min': 'A function that lets you get the smallest number in a list.',
    'sum': 'A function that gets the sum of all the numbers in a list.',
    'tuples': 'Lists of items that cannot be changed or immutable.',
    'if': 'Statements that allows you to examine the current state of a program and respond appropriately to that state.',
    }

for term, definition in programming_terms.items():
    print(f'{term.title()}:\n{definition}\n')

