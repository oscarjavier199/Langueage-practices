#create a list with short messages, then print each message using a function

def print_message(short_messages):
    for message in short_messages:
        print(f"{message}")
    
short_messages = ['have a nice day', 'you can make this!', 'stay strong']
print_message(short_messages)