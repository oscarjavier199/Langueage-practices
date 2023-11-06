def trip_planner_welcome():
    name = input("Enter your name please: ")
    print(f"Welcome to tripplanner v1.0 {name.title()}\n")


trip_planner_welcome()


def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time


estimate = estimated_time_rounded(8.5)


def destination_setup(origin, destination, estimated_time, mode_of_transport='Car'):
    print(f"Your trip starts off in {origin}")
    print(f"And you are traveling to {destination}")
    print(f"You will be traveling by {mode_of_transport}")
    print(f"It will take approximately {str(estimated_time)} hours")


destination_setup("Germany", "Norway", estimate)


# Write your dog_years function here:
def dog_years(name, age):
    return f"{name}, you are {age * 7} years old in dog years"


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))


# should print "Baby, you are 0 years old in dog years"


def square_root(num):
    return num ** 0.5


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))


# should print 10

# Write your average function here:
def average(num1, num2):
    avrg = num1 + num2
    return avrg / 2

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
"""
def need_evacuation(floor_no):
  flag = fire_alarm
  if flag == True:
    print("Evacuate floor " + str(floor_no) + " now!")
  else:
    print("This is a drill!")
fire_alarm = True
floor = 5
need_evacuation(floor)
print(flag)
"""

PROMPT = "Your value is "
def report_number(number):
  print(PROMPT + str(number))

report_number(100)

def buy_food(price1, price2, amount1, amount2):
  total1 = price1*amount1
  total2 = price2*amount2
  return total1, total2

print(buy_food(7.99, 6.40, 4, 5))