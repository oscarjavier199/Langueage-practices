def tittle_decorator(print_name_function):
    def wrapper():
        print("Student:")
        print_name_function()
    return wrapper

@tittle_decorator
def print_my_name():
    print("Oskar")
    
print_my_name()