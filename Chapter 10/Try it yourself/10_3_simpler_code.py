from pathlib import Path

path = Path('10_1_learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)