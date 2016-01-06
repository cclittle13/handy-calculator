"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def evaluate_math_input():

    print "Welcome to our calculator!"

    user_math_input = raw_input("Type your math problem here:\n>> ")

    tokens = user_math_input.split(" ")

    math_symbol = tokens[0]
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    if math_symbol == "+":
        final = add(num1,num2)
    elif math_symbol == "-":
        final = subtract(num1,num2)
    elif math_symbol == "*":
        final = multiply(num1,num2)
    elif math_symbol == "/":
        final = divide(num1,num2)

    print final 

evaluate_math_input()        

