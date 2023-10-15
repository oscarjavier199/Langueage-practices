from pathlib import Path

def reading_files(path):

    files = ['cats.txt', 'dogs.txt']

    for file in files:
        path = Path(file)
        
        try:
            content = path.read_text(encoding='utf-8')
        except FileNotFoundError:
            pass
        else:
            print(f"Content of the file {path}: \n{content}\n")
    
reading_files(Path)