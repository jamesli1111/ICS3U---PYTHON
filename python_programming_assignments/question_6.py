"""
This program asks a user if they want to see a table of either a quadratic function or a linear relation with values of their choosing.
The desired values of the chosen relation is then formatted into a table of values and then dsiplayed to the user.
"""

class InputError(Exception):

    pass

class PlayAgainInputError(Exception):

    pass

while True: 

    try:

        quadratic_or_linear = input("Which relationship would you like to see a table of values of? \n1. quadratic \n2. linear \n")

        if quadratic_or_linear != "1" or quadratic_or_linear != "2":
            raise InputError
        break
    
    #in case the user enters something other than '1' or '2', the program will not crash
    except InputError:

        print("Please enter 1 for a quadratic function and 2 for a linear relation")

    if quadratic_or_linear == "1":

        print("For the Quadratic function: y=ax^2 + bx + c")
        a = float(input("Enter a value for ‘a’: "))
        b = float(input("Enter a value for ‘b’: "))
        c = float(input("Enter a value for ‘c’: ")) 

        #makes sure that the table of values begins with negative domain values
        x = (-b/(2*a)) - 6

        print(f"{'x':>11}{'y':>9}")

        #rounds values of a quadratic function to one decimal place and formats numbers to the right by 12 and 9 spaces

        #formats the negative domain part of the table of values
        for i in range(6):
            x += 1
            print(f"{round(x,1):>12}{round(a*x**2+b*x+c,1):>9}")

        #formats positive domain part of the table of values
        for i in range(5):
            x += 1
            print(f"{round(x,1):>12}{round(a*x**2+b*x+c,1):>9}")


    elif quadratic_or_linear == "2":

        print("For the linear equation: y = mx + b")
        m = float(input("Enter a value for 'a': "))
        b = float(input("Enter a value for 'b': "))

        x = -6

        print(f"{'x':>11}{'y':>9}")

        #rounds values of a linear relation to one decimal place and formats numbers to the right by 12 and 9 spaces

        #formats negative domain part of table of values
        for i in range(5):
            x += 1
            print(f"{round(x,1):>12}{round(m*x+b,1):>9}")
    
        #formats positive domain part of table of values
        for i in range(6):
            x += 1
            print(f"{round(x,1):>12}{round(m*x+b,1):>9}")
            
    try:   

        play_again = input("Would you like to see another table of values of another relation? (Y/N) ")
        
        #makes sure that the program doesn't restart unless the user types 'Y' (yes)
        if play_again != "N" or play_again != "Y":
            raise PlayAgainInputError
        break

    except PlayAgainInputError:
        print("Please enter a 'Y' for play again and a 'N' to quit")
        
        if play_again == "N":
            print("Thank you, goodbye")
        break  