'''
Gets a radius value from the user, then calculates and displays the area and circumference of the radius entered
'''

import math

radius = int(input("Enter a radius value for your circle: "))

#displays and calculates the area of the circle by using math's pi variable
#displays and calculates the circumference of the circle using math's pi variable on the next line
print(f"The area of the circle is {round(radius**2*math.pi,1)} \nThe circumference of the circle is {round(2*math.pi*radius,1)}")



