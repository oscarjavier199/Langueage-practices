from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print_dice = f"{randint(1, self.sides)}"
        print(print_dice)

print("\n6-sided Die:")
dice_game_6 = Die(6)
dice_game_6.roll_die()

print("\n10-sided Die:")
dice_game_10 = Die(10)
dice_game_10.roll_die()

print("\n20-sided Die:")
dice_game_20 = Die(20)
dice_game_20.roll_die()

