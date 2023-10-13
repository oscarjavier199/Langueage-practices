from pathlib import Path
import json

path = Path('username.json')
content = path.read_text()
stored_name = json.loads(content)
print(f"Welcome back {stored_name}")