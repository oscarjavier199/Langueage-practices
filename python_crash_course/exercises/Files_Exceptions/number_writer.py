from pathlib import Path
import json

numbers = [2, 5, 6, 324, 76, 879, 98, 1]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)