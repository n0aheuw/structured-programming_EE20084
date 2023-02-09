###################################################################################################
#   Filename:       leapYear.py
#   Description:    A simple hello world example. Just to show the process for python development.
#   Date:           07/02/2023
#   Author:         no0n00
###################################################################################################

try:
    year = int(input("Enter a year: "))

    if ((year % 4) == 0):
        if ((year % 100) == 0) & ((year % 400) == 0):
            print("Leap Year")
        elif ((year % 100) != 0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")

except ValueError:
    print("VALUE ERROR: Invalid Input")
