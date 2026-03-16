# Control flow and Boolean logic
marks = 85
attendance_percentage = 90

# using and, or in if statements
if marks >= 80 and attendance_percentage >= 80:
    print("Excellent! You get an A+ and a scholarship.")
elif marks >= 60 or attendance_percentage == 100:
    print("Good job! You passed.")
else:
    print("You need to improve.")
    
# using not operator
is_raining = False
if not is_raining:
    print("Let's play Football!")