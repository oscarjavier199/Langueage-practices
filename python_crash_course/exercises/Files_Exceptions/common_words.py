from pathlib import Path

def count_words(path):
    
    books = [
        'anna_karenina.txt', 'don_quixote.txt', 'pride_and_prejudice.txt', 
        'The_beast_of_boredom.txt'
    ]
    
    for book in books:
        path = Path(book)
        
        try:
            contents = path.read_text().lower().count('happy')
        except:
            print("{path} is not in current directory")
        else:
            print(f"'Happy' in {path}: {contents}")

count_words(Path)