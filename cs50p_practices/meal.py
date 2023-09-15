def main():
    what_time = input("What time is it? \n") #awk user for the current time.
    time = convert(what_time) #here we call convert, that has already converted to float the given time by user 
    
    #if- else- elif statement to determine the range of hours.
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
        print("Dinner Time")
    else:
        exit

#convert given time to float
def convert(time):
    hours, minutes = time.split(":") #split will separate the time given by user by the : hours will be at the right and minutes at the left
    new_minutes = float(minutes) / 60 #here we take the minutes as float and divide then by 60, 1 hour= to 60 minutes.
    return float(hours) + new_minutes #return the float value of hours plus the converted minutes (new_minutes)


if __name__ == "__main__":
    main()
