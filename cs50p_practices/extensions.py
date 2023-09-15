#program will ask user for a file name, user is expected to type (filename).(file type)
#the program will return the media type

def main():
    file()
    
def file():
    
    file_name = input("File name: ")
    
    if file_name.endswith(".gif") or file_name.endswith(".GIF"):
        print("image/gif")
    elif file_name.endswith(".jpg") or file_name.endswith(".JPG"):
        print("image/.jpg")
    elif file_name.endswith(".jpeg") or file_name.endswith(".JPEG"):
        print("image/jpeg")
    elif file_name.endswith(".png") or file_name.endswith(".PNG"):
        print("image/png")
    elif file_name.endswith(".pdf") or file_name.endswith(".PDF"):
        print("application/pdf")
    elif file_name.endswith(".txt") or file_name.endswith(".TXT"):
        print("text/plain")
    elif file_name.endswith(".zip") or file_name.endswith(".ZIP"):
        print("application/zip")
    else:
        print("application/octet-stream")
        
if __name__ == "__main__":
    main()