#rental car
'''
car = input("What kind of rental car are you looking for? >>> ")
print(f"Let me see if I can find you a {car.title()}")
'''

#restaurant sitting
'''
people = int(input("How many people are in your dinner group? >>> "))
if people > 8:
    print("Sorry you'll have to wait for a table")
else:
    print("Sure! please follow me")
'''

#multiples of ten
'''
number = input("Please enter a number, I'll tell you if it's multiple of 10 >>> ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of ten 😊")
else:
    print(f"{number} is not multiple of 10 😒")
'''

#1 to 11
'''
number = 1
while number < 11:
    print(number)
    number += 1
'''

#parrot program
'''
prompt = ("\nTell me something and I'll repeat it back to you ")
prompt += ("\nEnter 'quit' to end the program >>> ")

message = ""

while message != "quit":
    message = input(prompt)
        
    if message != "quit":
        print(message)
'''

# using break
'''
prompt = ("\nEnter your favorite video game")
prompt += ("\nEnter 'game over' to end the program >>> ")

while True:
    game = input(prompt)
    if game == 'game over':
        break
    else:
        print(f"I also love {game.title()}")
'''

#using brake part. 2
'''
prompt = ("\nEnter a city you'd love to visit ")
prompt += ("\nEnter 'done' to exit the program >>> ")

while True:
    city = input(prompt)
    if city == 'done':
        break
    else:
        print(f"I'd also love to visit {city.title()}")
'''

#using continue in while loops
'''
number = 0

while number < 15:
    number += 1
    if number % 2 == 0:
        continue
    print(number)
'''

#using flag
'''
prompt = ("\nWhat is your favorite movie:")
prompt += ("\nEnter 'quit' to end the program >>> ")

movie_flag = True

while movie_flag:
    user_input = input(prompt)
    if user_input == "quit":
        movie_flag = False
        print("\n\t--- Program Terminated ---")
    else:
        print(f"\n\tNever heard of {user_input.title()}")
'''

#same previous program but using break:
'''
prompt = ("\nEnter your favorite TV series ")
prompt += ("\nEnter 'quit' to end the program >>> ")

while True:
    series = input(prompt)
    if series == 'quit':
        break
    else:
        print(f"\nI also like {series.title()}")
'''

#same previous program but using continue:
'''
prompt = ("\nEnter your favorite TV series ")
prompt += ("\nEnter 'quit' to end the program >>> ")

while True:
    series = input(prompt)
    if series != 'quit':
        print(f"\nI also like {series.title()}")
        continue
    else:
        break
'''

#another break:
'''
prompt = ("\nDo you like commics? (yes/no)")
prompt += ("\nEnter 'quit' to end the program >>> ")

while True:
    user_input = input(prompt)
    if user_input == 'quit':
        break
    elif user_input == 'yes':
        message_2 = input(f"what's your favorite one? >>> ")
        print(f"I also like {message_2.title()}")
        break
    elif user_input == 'no':
        print("I got you, comics are not for everyone 🧐")
        break
'''

#annother flag
'''
prompt = ("\nWhat's your favorite food? ")
prompt += ("\nEnter 'no hungry' to quit the program >>> ")

food_flag = True

while food_flag:
    message = input(prompt)
    if message == 'no hungry':
        food_flag = False
        print("\n\tI'm not hungry either, I am a computer! \n")
    else:
        print(f"\nI've never eaten {message}, because I'm a computer program 💻")
        food_flag = False
        print("\n\t--- Program Terminated ---")
'''

#another continue
'''
number = 5

while number < 15:
    number += 1
    if number % 3 != 0:
        continue    
    print(number)
'''

#pizza toppings:

'''
prompt = ("\n\tPlease enter the toppings you want in your pizza ")
prompt += ("\n\tEnter 'order' when you're done >>> ")

while True:
    message = input(prompt)
    if message == 'order':
        print("\n\tYour order will be ready in 15 minutes!\n")
        break
    else:
        print(f"\n\t{message.title()} is being added to your pizza")
'''
#movie tickets
'''
prompt = ("\n\tWhat is your age? >>> ")

while True:
    message = int(input(prompt))
    
    if message < 3:
        print("\n\tYour ticket is free!\n")
        break
    elif message < 12:
        print('\n\tYour ticket is $10\n')
        break
    else:
        print("\n\tYour ticket is $15\n")
        break
'''

#movie tickets 2
'''
prompt = ("\n\tWhat is your age? >>> ")

message_active = True

while message_active:
    message = int(input(prompt))
    
    if message < 3:
        print("\n\tYour ticket is free!\n")
        message_active = False
    elif message < 12:
        print('\n\tYour ticket is $10\n')
        message_active = False
    else:
        print("\n\tYour ticket is $15\n")
        message_active = False
'''   
#pizza toppings using break when the user enters a 'quit value'
'''
prompt = ("\nPlease enter the toppings you want in your pizza")
prompt += ("\nEnter 'quit' when you're done >>> ")

while True:
    user_toppings = input(prompt)
    if user_toppings == 'quit':
        break
    else:
        print(f"\n{user_toppings} is being added to your pizza")
'''

#movie ticket using conditional statements:
'''
prompt = ("What is your age? >>> ")

age = ''

while age == '':
    age = int(input(prompt))
    if age < 3:
        print("free")
    elif age < 15:
        print("$15")
    else:
        print("$50")
'''

#conditional statement while loop
'''
prompt = ("\n\twho is your favorite super hero? (Superman / Batman / none / myself) >>> ")

hero = ''

while hero  == '':
    hero = input(prompt)
    if hero == 'superman':
        print("\n\tThe man of steel is the best!")
    elif hero == 'batman':
        print("\n\tI am the night I am Vengance!")
    elif hero == 'none':
        print("\n\tI mean, at least think about Jhon Wick or someone else...")
    elif hero == "myself":
        print("\n\tThat's great!")
    else:
        print(f"\n\tNever heard of {hero}, sorry")
        
print("\n\thave a nice day!")
'''

#moving elemetns from one list to another using while loops
'''
uncompleted_books = ["gone girl", "12 rules of life", "The Brothers Karamazov"]
completed_books = []

print(f"\n\tBooks to read: {uncompleted_books}")
print("\n\t...")
print("\n\tTwo years later... Books are completed")


while uncompleted_books:
    un_books = uncompleted_books.pop()
    print(f"\nAdding {un_books} to completed_books...")
    completed_books.append(un_books)
    
print("..." * 25)
    
for completed_book in completed_books:
    print(f"\n{completed_book.title()} was fun to read")
print(f"\nNew list of completed Books: {completed_books}")
'''

#moving items from one list to another using while:
'''
pending_classes = ['maths', 'physics', 'geometry', 'biology']
taking_classes = []
print(f"\n\tClasses you have to take this year: {pending_classes}")

while pending_classes:
    classes = pending_classes.pop()
    taking_classes.append(classes)

print(f"\n\tOkay, I already enrolled myself in: {taking_classes}")
'''

#removing all repeated instances from a list using while loops:
'''
movies = ['harry potter', 'narnia', 'jhon wick', 'saw', 'harry potter', 
          'harry potter', 'hellboy']
print(f"Old movies list: {movies}")

while 'harry potter' in movies:
    movies.remove('harry potter')
print(f"new movies list:", movies)

'''

#while loops in dictionaries:
'''
book_poll = {}

loop_active = True

while loop_active:
    name = input("\nWhat's your name? >>> ")
    book = input(f"\nWhat's your favorite Book {name}? >>> ")
    
    book_poll[name] = book
    
    share = input("would you like to share the poll with someone else: (yes/no) >>> ")
    
    if share == 'yes':
        continue
    else:
        print(f"\nThank you for taking the poll {name}")
        loop_active = False
for name_key, book_value in book_poll.items():
    print(f"\nResults of the poll: \n {book_poll}")
'''

#exercise 7-8. Deli
'''
sandwich_orders = ['American', 'BLT', 'peanut butter and jelly', 
                   'cheese', 'turkey', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"{order.title()} sandwich is being made...")
    finished_sandwiches.append(order)
    
print("\nThis sandwiches were made:")

for sandwich in finished_sandwiches:
    print(f"*{sandwich}")
'''

#exercise 7-9. No Pastrami
'''
sandwich_orders = ['pastrami','American', 'BLT', 'pastrami','peanut butter and jelly', 
                   'cheese', 'turkey', 'tuna', 'pastrami']
finished_sandwiches = []

print("Sorry! we ran out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"{order.title()} sandwich is being made...")
    finished_sandwiches.append(order)
    
print("\nThis sandwiches were made:")

for sandwich in finished_sandwiches:
    print(f"*{sandwich}")
'''

#dream vacation
'''
dream_vacation = {}

while True:
    name = input("\nWhat's your name? >>> ")
    vacation = input(f"\nWhat's your dream vacation {name} >>> ")
    dream_vacation[name] = vacation
    
    new_poll = input(f"\n{name}, would you like to send this poll to a friend? (yes/no) >>> ")
    
    if new_poll == 'yes':
        continue
    else:
        break
    
print("\n\tResult of the poll:")
for name_key, vacation_value in dream_vacation.items():
    print(f"\n{name_key}'s dream vacation is {vacation_value} ")
'''

#same previous exercise but using a flag:
'''
dream_vacation = {}

poll_active = True

while poll_active:
    name = input("\nWhat's your name? >>> ")
    vacation = input(f"\nWhat's your dream vacation {name} >>> ")
    dream_vacation[name] = vacation
    
    new_poll = input(f"\n{name}, would you like to send this poll to a friend? (yes/no) >>> ")
    
    if new_poll == 'yes':
        continue
    else:
        poll_active = False
    
print("\n\tResult of the poll:")
for name_key, vacation_value in dream_vacation.items():
    print(f"\n{name_key}'s dream vacation is {vacation_value} ")
'''

#another while in lists exercise:
#move values from countries to explore
#to explored_countries after 2 years
'''
cities_to_explore = ['munich', 'oslo', 'paris', 'copenaghen', 'zurich', 
                        'sydney', 'petersburg']
visited_cities = []

print(f"\nI'd love to go to this cities! {cities_to_explore}")

while cities_to_explore:
    after_2_years = cities_to_explore.pop()
    visited_cities.append(after_2_years)

print(f"\nAfter 2 years I've been to this cities... ")
for city in visited_cities:
    print(f"-{city}")
'''

#another while in lists
#remove books
'''
reading_list = ['harry potter', 'the children of hurin', 'dune', 'the witcher']
finished_books = []

print(f"\nI really want to read this books... {reading_list}...someday\n")

while reading_list:
    books = reading_list.pop()
    finished_books.append(books)
    
print("Finally! after 1 year, I've read: ")
for book in finished_books:
    print(f"{book}")
'''

# yet another while loop in lists:
# remove from todo list and add to completed:
'''
to_do = ['study some more', 'dinner', 'homework', 'meet with mom/dad', 
         'study', 'shower']
completed = [] 

to_do.reverse()
print(f"\nThis is my to-do list for today: {to_do}")
to_do.reverse()

while to_do:
    completed_task = to_do.pop()
    completed.append(completed_task)
    
print(f"\n--- Really Loooong day ---😴🥱")
print("\nBut I'm done with: ")

for task in completed:
    print(f"-{task}")
'''

#while loops and dictionaries:
'''
video_games = {}

game_over = True

while game_over:
    name = input("\nWhat's your name? >>> ")
    game = input(f"\nNice to meet you {name.title()}, What's your favorite video game? >>> ")
    video_games[name] = game
    
    print(f"\nI also like {game.title()}")
    console = input(f"\nDo you play on Xbox or PlayStation? >>> ").lower()
    
    if console == 'xbox':
        print("\n**I tough you had some good taste 🤣**")
        game_over = False
        print(f"\n--- Thank you for taking the poll {name.title()} ---")
        
    elif console == 'playstation':
        print("\n** Finally someone with good taste! 😁 **")
        game_over = False
        print("\n\t--- Thank you for taking the poll ---")
        
print("\n\t\t--- POLL RESULTS --- ")
for name_k, game_v in video_games.items():
    print(f"\n\t{name_k.title()}, likes to play {game_v.title()} on {console.title()}")
'''
    
#continue statement 

while True:
    name = input("\nwho are you? >>> ")
    if name != "oscar".lower():
        print("\n\t-- Sorry, don't know you -- try again --")
        continue
    elif name == 'oscar'.lower():
        password = input("\npassword please: >>> (it's a superhero) >>> ")
        print(password)
        if password == 'Batman'.lower():
            print(f"\n\tAccess Granted, Welcome Back Master {name.title()}")
        break
