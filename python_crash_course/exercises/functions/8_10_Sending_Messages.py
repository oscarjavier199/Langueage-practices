# start with exercise 8_9_Messages.py and create a function to print the
# sent messages

#first function pops items from a list, appends them to new list and prints message
def print_message(short_messages, sent_messages):
    while short_messages:
        message = short_messages.pop()
        print(f"Sending your message ({message})...")
        sent_messages.append(message)
        
#second function only prints the sent messages
def sent_message(sent_messages):
    print("\nSent messages:\n")
    for messages in sent_messages:
        print(f"{messages}")
    
short_messages = ['have a nice day', 'you can make this!', 'stay strong']
sent_messages = []

#passes a copy of original list preserving it's contents
print_message(short_messages[:], sent_messages)
sent_message(sent_messages)


print('*' * 25)
print(f"Initial List: {short_messages}")
print(f"Final List: {sent_messages}")