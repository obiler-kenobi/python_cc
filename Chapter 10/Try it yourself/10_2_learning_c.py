from pathlib import Path

path = Path('10_1_learning_python.txt')
contents = path.read_text()
lines = contents.replace('Python', 'C').splitlines()
for line in lines:
    # book solution
    # line = line.replace('Python', 'C')
    print(line)