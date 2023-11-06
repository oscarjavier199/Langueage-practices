# Program shows how higher-order functions work when a function is an argument
# program will print a message after the specified amount of seconds
import time


def after(seconds, function):
    time.sleep(seconds)
    function()


def greeting():
    print("Hello!")


after(10, greeting)
