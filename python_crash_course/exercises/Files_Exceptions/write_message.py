from pathlib import Path

path = Path('programming.txt')

path.write_text('I love programming')

contents = f"I love programming.\n"
contents += f"I also love new games.\n"
contents += f"I also love working with data!\n"

path.write_text(contents)