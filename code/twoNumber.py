###################################################################################################
#   Filename:       twoNumber.py
#   Description:    A simple hello world example. Just to show the process for python development.
#   Date:           07/02/2023
#   Author:         no0n00
###################################################################################################
        
def num_input():
    try:
        a = int(input("Please type your number: "))
        return a
    except ValueError:
        print("Inavlid Input")
        num_input()

num1 = num_input()
num2 = num_input()

#numerical print statements
print(num1, " + ", num2, " = ", float(num1 + num2))
print(num1, " - ", num2, " = ", float(num1 - num2))
print(num1, " * ", num2, " = ", float(num1 * num2))
print(num1, " / ", num2, " = ", float(num1 / num2))
print(num1, " % ", num2, " = ", float(num1 % num2))
print(num1, " ** ", num2, " = ", float(num1 ** num2))
print(num1, " // ", num2, " = ", float(num1 // num2))

#boolean print statements
print(num1, " == ", num2, " is ", num1 == num2)
print(num1, " != ", num2, " is ", num1 != num2)
print(num1, " > ", num2, " is ", num1 > num2)
print(num1, " < ", num2, " is ", num1 < num2)