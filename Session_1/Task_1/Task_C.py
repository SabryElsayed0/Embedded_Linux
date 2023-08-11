#*********************************************************#
#****   Author : Sabry Elsayed        ********************#
#****   SWC:     Python->Embedded linux ******************#
#****   Date :        12/8/2023        ********************#
#****   Version : 1.00                ********************#
#*********************************************************#

#Write a python program to access environment variables.
# we import the os module, which provides functions to interact with the operating system. 
import os

# Access a specific environment variable
specific_variable = os.environ.get('SPECIFIC_VARIABLE')
print("Value of SPECIFIC_VARIABLE:", specific_variable)

# Access all environment variables
all_variables = os.environ
print("\nAll Environment Variables:")
for key, value in all_variables.items():
    print(f"{key}: {value}")
#################################################################