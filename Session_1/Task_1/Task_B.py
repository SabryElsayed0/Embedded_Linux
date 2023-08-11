###################################################################

#Write a Python program to test whether a passed letter is a vowel or not.
input_letter = input("Enter a letter: ")

#*********************************************************#
#****   Author : Sabry Elsayed        ********************#
#****   SWC:     Python->Embedded linux ******************#
#****   Date :        12/8/2023        ********************#
#****   Version : 1.00                ********************#
#*********************************************************#
#Write a Python program to test whether a passed letter 
# is a vowel or not.


vowels = ['a', 'e', 'i', 'o', 'u']
if input_letter.lower() in vowels:
    print("The letter is a vowel.")
else:
    print("The letter is not a vowel.")
 #########################################################
    
