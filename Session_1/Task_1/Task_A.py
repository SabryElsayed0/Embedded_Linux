#*********************************************************#
#****   Author : Sabry Elsayed        ********************#
#****   SWC:     Python->Embedded linux ******************#
#****   Date :        12/8/2023        ********************#
#****   Version : 1.00                ********************#
#*********************************************************#

#Write a Python program to count the number 4 in a given list

my_list = [1, 4, 2, 4, 7, 4, 9, 4]

count = sum(1 for num in my_list if num == 4)

print("Number of 4s in the list:", count)

###########################################################