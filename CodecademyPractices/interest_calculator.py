# Simple program to calculate an interest rate

principal = 1000
rate = 1.0
numyears = 5
current_year = 1

while current_year <= numyears:
    principal = principal * (1 + rate)
    print(f"Year {current_year}. {principal:0.2f}")
    current_year += 1