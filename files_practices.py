from pathlib import Path
import json

def write_to_json(path):
    path = Path('my_books.json')

    book_line = """
In respect of her art generally, Mr. Goldwin Smith has truly observed
that “metaphor has been exhausted in depicting the perfection of it,
combined with the narrowness of her field;” and he has justly added that
we need not go beyond her own comparison to the art of a miniature
painter."""


    content = json.dumps(book_line)

    path.write_text(content)


def read_json_file(path):
    
    path = Path('my_books.json')
    try:
        content = path.read_text()
        book = json.loads(content)
    except FileNotFoundError:
        print("sorry File doesn't exist in current directory")
    else:
        print(book)

read_json_file(Path)