from pathlib import Path

def count_words(path):
    
    '''function counts the word of a given file'''
        
filenames = [
        'anna_karenina.txt', 'pride_and_prejudice.txt', 'don_quixote.txt', 
        'The_beast_of_boredom.txt'
    ]

for filename in filenames:
    path = Path(filename)

    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, The file '{path}' Does not exist in current directory.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file '{path}' has approximately {num_words} words.")

count_words(Path)
