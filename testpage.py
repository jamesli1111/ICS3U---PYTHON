
import matplotlib.pyplot as plt
from os import system, name

#Create function to clear screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
 
#Creates function that asks and returns values a, b, c
def ask_value():
    while True:
        try:
            print(f"For an equation in the form {equation}")
            a = float(input("Enter the value for a: "))
            b = float(input("Enter the value for b: "))
            c = float(input("Enter the value for c: "))
            break
        except ValueError:
            clear()
            print("Please enter a valid value!")
    print(" {:5} X Value: {:10} Y Value: ".format("", ""))
    return a, b, c

#Starts main loop for the program
playagain = "Y"
while playagain == "Y":
    x_list, y_list, x_list2, y_list2 = [], [], [], []
    clear()
 
    #Ask user which relation type they want
    while True:
        try:
            relation = int(input("Which table for a relation would you like to see? \n 1. Linear \n 2. Quadratic \n 3. Reciprocal \n "))
            if relation == 1 or relation == 2 or relation == 3:
                break
            print("Please type either 1 or 2 or 3!")
        except ValueError:
            clear()
            print("Please type a valid number!")
    clear()

    equation = ""
    equation_full = ""
    #For a linear function
    if relation == 1:
        equation = "ax + by + c = 0"
        #Asks and gets values for the equation from the user
        values = ask_value()
        equation_full = f"{values[0]}x + {values[1]}y + {values[2]} = 0"
        #Calculates y for x from -4 to 4
        for x in range(-4, 5):
            y = -(values[0]*x + values[2]) / values[1]
            #Prevents -0
            if y == 0:
                y = 0
            x_list.append(x)
            y_list.append(y)
            print(" {:12.2f} {:19.2f}".format(x, y))
 
    #For quadratic function
    elif relation == 2:
        equation = "y = ax^2 + bx + c"
        #Asks and gets values for the equation from the user
        values = ask_value()
        equation_full = f"y = {values[0]}x^2 + {values[1]}x + {values[2]}"
        #Calculates the x vertex so that it can be the center
        xvertex = -values[1] / (2*values[0])
        currentx = xvertex - 4
 
        #Calculates y for 4 x's to the right and left of x vertex
        while currentx < xvertex + 5:
            y = values[0]*currentx**2 + values[1]*currentx + values[2]
            print(" {:12.2f} {:19.2f}".format(currentx, y))
            currentx += 1

        #Calculates the points for the graph
        currentx = xvertex - 4
        while currentx < xvertex + 4:
            y = values[0]*currentx**2 + values[1]*currentx + values[2]
            x_list.append(currentx)
            y_list.append(y)
            currentx += 0.1

    #For reciprocal function
    elif relation == 3:
        equation = "y = a/x-b + c"

        #Asks and gets values for the equation from the user
        print("For an equation in the form y = a/x-b + c")
        values = ask_value()
        equation_full = f"y = {values[0]}/ x - {values[1]} + {values[2]}"
        #Gets the asymtote, and calculates the y coord for 4 units to the left and right of the asymtote
        currentx = values[1] - 4

        while currentx < values[1] + 5:

            #If the x is the asymtote, then just print 'Vertical asymtote'
            if currentx != values[1]:
                y = values[0]/(currentx - values[1]) + values[2]
                print(" {:12.2f} {:19.2f}".format(currentx, y))
            else:
                print(" {:12.2f} {:>25}".format(currentx, "Vertical Asymtote"))
            currentx += 1

        #Calculates the points for the graph
        currentx = values[1] - 4
        while currentx < values[1] + 5:
            if currentx != values[1]:
                y = values[0]/(currentx - values[1]) + values[2]
                if currentx < values[1]:
                    x_list.append(currentx)
                    y_list.append(y)
                elif currentx > values[1]:
                    x_list2.append(currentx)
                    y_list2.append(y)
            currentx = round(currentx + 0.1, 5)

    #Creates the graphs
    plt.title(f"Graph for the equation {equation_full}")          
    plt.plot(x_list2, y_list2, color = 'blue') 
    plt.plot(x_list, y_list, color = 'blue') 
    plt.show() 

    #Asks to play again
    while True:
        playagain = input("Do you want to try again? (Y/N) ")
        if playagain == "N" or playagain == "Y":
            break
        else:
            print("Please type either 'N' or 'Y'")