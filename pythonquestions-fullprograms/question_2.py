'''
Gets a radius value from the user, then calculates and displays the area and circumference of the radius entered
'''

import math

radius = int(input("Enter a radius value for your circle: "))

#displays and calculates the area of the circle by using math's pi variable
print(f"The area of the circle is {round(radius*math.pi**2,1)}")

#displays and calculates the circumference of the circle using math's pi variable
print(f"The circumference of the circle is {round(2*math.pi*radius,1)}")


