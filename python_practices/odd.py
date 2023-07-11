from datetime import datetime
import imp

# This program will tell us if the current minute is odd or not
# it will also wait a random number of seconds from 1
# to 60 and will print the information 5 times.

import random
import time

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
    21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(54):
    
    right_this_minute = datetime.today().minute
    
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1,60)
    time.sleep (wait_time)
    
    
        