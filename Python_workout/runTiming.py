def run_timing():
    
    '''calculates average running time'''
    
    welcome = f"\n\tEnter your running time in minutes and I'll give you the"
    welcome += f" average \n\t(Enter 0 to quit)\n"
    print(welcome)
    
    #list to store user's input
    times = []
    
    #loop to keep asking user for running time
    while True:  
        running_time = int(input("running time (minutes): "))
        times.append(running_time)
        
        # if user's input == 0 program stops
        try:
            if not running_time:
                average = sum(times) / len(times)
                print(f"\n\tAverage running time: {average:.2f}\n")
                break
        except ValueError:
            print("hey! that's not a valid number")

run_timing()