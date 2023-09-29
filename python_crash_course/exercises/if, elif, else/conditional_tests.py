#series of conditional tests describing each test and my prediction for the 
#result of each test.

pizza = 'mushrooms'
print("Is pizza == 'pepperoni?' I predict False")
print(pizza == 'pepperoni')

movie = 'narnia'
print("Is movie == 'Harry Potter? I predict False")
print(movie == 'Harry Potter')

car = 'porsche'
print("is car == 'mazda'? I predict False")
print(car == 'mazda')

motorcycle = 'BMW'
print("is motorcycle == 'ninja'? I predict False")
print(motorcycle == 'ninja'.lower())

phone = 'iphone'
print("is phone == 'samsung'? I predict False")
print(phone == 'samsung'.lower())

laptop = 'asus'
print("is laptop == 'asus'? I predict True")
print(laptop == 'Asus'.lower())

country = 'norway'
print("is country == 'oslo'? I predict True")
print(country == 'Norway'.lower())

city = 'munich'
print("is city == 'munich'? I predict True")
print(city == 'Munich'.lower())

sport = 'tennis'
print("is sport == 'tennis'? I predict true")
print(sport == 'Tennis'.lower())

food = 'steak'
print("is food == 'steak'? I predict True")
print(food == 'Steak'.lower())

hero = 'Batman'.lower()
print("is hero != 'Batman'? I predict False")
print(hero != 'batman')

hero_2 = 'superman'.lower()
print("is hero_2 == 'Wonder Woman'? I predict False")
print(hero_2 == 'Wonder Woman')

car_2 = 'bmw'
print("is car_2 == 'BMW'? I predict True")
print(car_2 == 'BMW'.lower())

number_1 = 21
print("is number_1 >= '21'? I predict True")
print(number_1 >= 21)

number_2 = 10
print("is number_2 <= '5'? I predict False")
print(number_2 <= 5)

number_3 = 888
print("is number_3 > '555'? I predict True")
print(number_3 > 555)

number_4 = 11111111
print("is number_4 < '585858'? I predict False")
print(number_4 < 585858)

age_1 = 55
age_2 = 60
print("is age_1 and age_2 <= 100? I predict False")
print(age_1 and age_2 >= 100)

age_3 = 10
age_4 = 15
print("is age_3 <= 15 or age_4 >= 2? I predict True")
print(age_3 <= 15 or age_4 >= 2)

user_names = ['oscar', 'charlie', 'elena', 'damon', 'dr.house']
print("is 'dr. house in the list user_names? I predict True")
print('dr.house' in user_names)

user_names_2 = ['dexter', 'charlie', 'stephan', 'caroline', 'logan']
print("is dracula999 NOT in the list user_names_2? i predict True")
print('dracula999' not in user_names_2)
