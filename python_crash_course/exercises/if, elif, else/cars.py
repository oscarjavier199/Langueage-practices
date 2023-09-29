#using if, else statements to print in uppercase a specific term

#list of cars
cars = ['audi', 'bmw', 'porsche', 'toyota', 'maserati']

#for loop to iterate through the items in the list
for car in cars:
    if car == 'bmw':                #if statement to check if condition is True
        print(car.upper())
    else:                           #if condition is False print next line
        print(car.title())
