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

#this function asks for the user's values of their quadratic function, then makes a table of values
def quadratic():

    #Makes sure the user inputs a number for a, b, and c values
    while True:
        try:
            print("For the Quadratic function: y=ax^2 + bx + c")
            a = float(input("Enter a number value for ‘a’: "))
            b = float(input("Enter a number value for ‘b’: "))
            c = float(input("Enter a number value for ‘c’: ")) 
            break
        except ValueError:
            print("That is not a number!")

    #makes sure that the table of values begins with negative domain values
    x = (-b/(2*a)) - 6

    print(f"{'x':>11}{'y':>9}")

    #rounds values of a quadratic function to one decimal place and formats numbers to the right by 12 and 9 spaces

    #formats the negative domain part of the table of values
    for i in range(6):
        x += 1
        print(f"{round(x,2):>12}{round(a*x**2+b*x+c,2):>9}")

    #formats positive domain part of the table of values
    for i in range(5):
        x += 1
        print(f"{round(x,2):>12}{round(a*x**2+b*x+c,2):>9}")

#this function asks for the values of the user's linear relation, then makes a table of values 
def linear():

    #Makes sure the user inputs a number for a, b, and c values
    while True:
        try:
            print("For the linear equation: y = mx + b")
            m = float(input("Enter a number value for 'm': "))
            b = float(input("Enter a number value for 'b': "))
            break
        except ValueError:
            print("That is not a number!")

    #makes sure that the table of values begins with negative domain values   
    x = -6

    print(f"{'x':>11}{'y':>9}")

    #Does the same thing as thing as code lines, 38 through 45
    #formats negative domain part of table
    for i in range(5):
        x += 1
        print(f"{round(x,2):>12}{round(m*x+b,2):>9}")

    #formats positive domain part of table 
    for i in range(6):
        x += 1
        print(f"{round(x,2):>12}{round(m*x+b,2):>9}")

while True:
    while True: 
        try:
            quadratic_or_linear = input("Which relationship would you like to see a table of values of? \n1. quadratic \n2. linear \n")

            if quadratic_or_linear != "1" and quadratic_or_linear != "2":
                raise QuadraticOrLinearInputError
            break
        #makes sure that the user enters either "1" or "2"
        except QuadraticOrLinearInputError:
            print("Please enter 1 for a quadratic function and 2 for a linear relation")
    #the number '1' represents the user picking a quadratic function
    if quadratic_or_linear == "1":
        quadratic()
    #the number '2' represents the user picking a linear relation
    elif quadratic_or_linear == "2":
        linear()
    while True:
        try:   
            play_again = input("Would you like to see another table of values of another relation? (Y/N) ")

            #makes sure that the user types either "Y" or "N"
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