#program will give a grade from F to A to a student according to the score given by user

score = int(input("Score: ")) #score variable

#grades from A to F according to score
"""""
if score >= 90 and score <= 100:
    print("Your grade: A, congrats!")
elif score >= 80 and score < 90:
    print("Your grade: B")
elif score >= 70 and score < 80:
    print("Your grade: C")
elif score >= 60 and score < 70:
    print("Your grade: D")
else:
    print("Your grade: F")
"""
    
#cleaner code
if score >= 90:
    print("Your grade: A, congrats!")
elif score >= 80:
    print("Your grade: B")
elif score >= 70:
    print("Your grade: C")
elif score >= 60:
    print("Your grade: D")
else:
    print("Your grade: F")