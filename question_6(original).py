"""
Question #6 quadratic or linear relation?
James li
Dec. 9. 2020
This program asks a user if they want to see a table of either a quadratic function or a linear relation with values of their choosing.
The x and y values of the chosen relation is then calculated and formatted into a table of values, then displayed to the user.
"""

class QuadraticOrLinearInputError(Exception):

    pass

class PlayAgainInputError(Exception):

    pass

def quadratic():

    while True:
        try:
            print("For the Quadratic function: y=ax^2 + bx + c")
            a = float(input("Enter a number value for ‘a’: "))
            b = float(input("Enter a number value for ‘b’: "))
            c = float(input("Enter a number value for ‘c’: ")) 
            break
        except ValueError:
            print("That is not a number!")

    x = (-b/(2*a)) - 6
    print(f"{'x':>8}{'y':>9}")

    for i in range(11):
        x += 1
        print(f"{round(x,2):>10}{round(a*x**2+b*x+c,2):>9}")

def linear():

    while True:
        try:
            print("For the linear equation: 0 =ax + by + c")
            a = float(input("Enter a number value for 'a': "))
            b = float(input("Enter a number value for 'b': "))
            c = float(input("Enter a number value for 'c': "))
            break
        except ValueError:
            print("That is not a number!")

    print(f"{'x':>8}{'y':>9}")
    
    for x in range(-5,6):
        y = - (a*x + c) / b
        if y == -0:
            y == 0
        print(f"{round(x,2):>8}{round(y,2):>10}")

while True:
    while True: 
        try:
            quadratic_or_linear = input("Which relationship would you like to see a table of values of? \n1. quadratic \n2. linear \n")

            if quadratic_or_linear != "1" and quadratic_or_linear != "2":
                raise QuadraticOrLinearInputError
            break
        
        except QuadraticOrLinearInputError:
            print("Please enter 1 for a quadratic function and 2 for a linear relation")

    if quadratic_or_linear == "1":
        quadratic()
    elif quadratic_or_linear == "2":
        linear()

    while True:
        try:   
            play_again = input("Would you like to see another table of values of another relation? (Y/N) ")

            if play_again != "N" and play_again != "Y":
                raise PlayAgainInputError
            break
        except PlayAgainInputError:
            print("Please enter a 'Y' for play again and an 'N' to quit")
    if play_again == "N":
        print("Thank you, goodbye")
        break 
    elif play_again == "Y":
        continue    