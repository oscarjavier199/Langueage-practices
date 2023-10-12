from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

print(f"\n\tFile content: \n\n{content.replace('Python', 'C')}\n")

file_list = ''

for line in content.splitlines():
    file_list += line
    print(line)
