def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0", name)
trip_planner_welcome("oskar")

def estimated_time_rounded(estimated_time):
  rounded_time =round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(5.55)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in", origin)
  print("And you are traveling to", destination)
  print("You will be traveling by", mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")
destination_setup("Oslo", "Copenhagen", estimate, "Car")

# program will print the information of a travel between two cities and the 
# estimated time to go from one city to the next one