"""
we can use
comparision operators: ==,>=, <=, !=
logical operators: and, or, not
short hand notations
"""

# simple conditional statement example

"""
score = int(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")
"""


#Match case(as like switch case in other programming languages)

"""
def get_day_name(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"

day_number = int(input("Enter a day number (1-7): "))
print(get_day_name(day_number))
"""


#Short hand if else
"""
a = 2
b = 330
print("A") if a > b else print("B")
"""

#You can also have multiple else statements on the same line:
"""
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
"""

# **Note: if statements cant be empty you can use pass instead
"""
a = 33
b = 200

if b > a:
  pass
"""