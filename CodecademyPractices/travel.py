# program shows how to use a return value later in the program

current_budget = 3500.75
print(f"Initial Budget ${current_budget}")
shirt_expense = 9


def print_remaining_budget(budget):
    """Prints message"""
    print(f"Your remaining budget after expenses is $ {str(budget)}")


def deduct_expense(budget, expense):
    """Returns budget minus expenses"""
    return budget - expense


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
