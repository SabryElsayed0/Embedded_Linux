#*********************************************************#
#****   Author : Sabry Elsayed        ********************#
#****   SWC:     Python->Embedded linux- ******************#
#****   Date :    12/8/2023            ********************#
#****   Version : 1.00                ********************#
#*********************************************************#


##Print the calendar of a given month and year

# we import the os module, which provides functions to interact with the Calender 
import calendar
#ask user to enter the year 
y = int(input("Input the year : "))
#ask user to enter the Month 
m = int(input("Input the month : "))
#finally print the calender for this month and year
print(calendar.month(y, m))

#####################################################