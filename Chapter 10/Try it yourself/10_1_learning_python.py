from pathlib import Path

path = Path('10_1_learning_python.txt')
contents = path.read_text()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)