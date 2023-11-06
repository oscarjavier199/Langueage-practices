# *args practice

def sandwich_order(*items):
    """Functions takes an arbitrary number of args to create a sandwich order"""
    for item in items:
        print(f"{item}")


sandwich_order('\nOrder1:\npepperoni', 'extra cheese', 'mushrooms')
sandwich_order('\nOrder 2:\nCheese only!')
sandwich_order('\nOrder 3:\nPineanple and cheeeese, please', 'ham', 'onion', 'green pepper')


