#*********************************************************#
#****   Author : Sabry Elsayed        ********************#
#****   SWC:     Python->Embedded linux ******************#
#****   Date :        12/8/2023        ********************#
#****   Version : 1.00                ********************#
#*********************************************************#

#Write a Python program which accepts the radius 
# of a circle from the user and compute the area.

import math

try:
    # Ask user Enter radius 
    radius = float(input("Enter the radius of the circle: "))
    #check if negtvive or positive and take action
    if radius > 0 :
        # Compute the area of the circle
        area = math.pi * (radius ** 2)
        # Print the area of the circle
        print("The area of the circle is:", area)
    else:
        print("Radius cannot be negative. Please enter a non-negative value.")
except:
    #if the raduis isnot number we will print this message
    print('The Radius is not a number')
   
        
