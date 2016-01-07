"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.

This version was pair programmed by cclittle13 and apao @ Hackbright.
"""

from arithmetic import *


# Your code goes here
def xtra_credit_eval(tokens):

    math_symbol = tokens[0]

    if math_symbol == "+":
        final = add(tokens)
    elif math_symbol == "-":
        final = subtract(tokens)
    elif math_symbol == "*":
        final = multiply(tokens)
    elif math_symbol == "/":
        final = divide(tokens)
    elif math_symbol == "square":
        final = square(tokens)
    elif math_symbol == "cube":
        final = cube(tokens)
    elif math_symbol == "pow":
        final = power(tokens)
    elif math_symbol == "mod":
        final = mod(tokens)

    print final 

# This is the final solution prior to Extra Credit.
# def evaluate_math_input(math_symbol,num1,num2):

#     # print "Welcome to our calculator!"

#     # user_math_input = raw_input("Type your math problem here:\n>> ")

#     # tokens = user_math_input.split(" ")

#     # if len(tokens) == 3:
#     #     math_symbol = tokens[0]
#     #     num1 = int(tokens[1])
#     #     num2 = int(tokens[2])
#     # else:
#     #     math_symbol = tokens[0]
#     #     num1 = int(tokens[1])

#     if math_symbol == "+":
#         final = add(num1,num2)
#     elif math_symbol == "-":
#         final = subtract(num1,num2)
#     elif math_symbol == "*":
#         final = multiply(num1,num2)
#     elif math_symbol == "/":
#         final = divide(num1,num2)
#     elif math_symbol == "square":
#         final = square(num1)
#     elif math_symbol == "cube":
#         final = cube(num1)
#     elif math_symbol == "pow":
#         final = power(num1,num2)
#     elif math_symbol == "mod":
#         final = mod(num1, num2)

#     print final 


# def handy_calculator():
#     """Use this to parse user input and call appropriate math operation."""

#     print "Welcome to our calculator!"
    
#     while True:
#         user_math_input = raw_input("Press 'q' to exit or type your math problem here:\n>> ")


#         if user_math_input == 'q':
#             break
#         else:
            
#             tokens = user_math_input.split(" ")
#             num2 = 0


#             # This is the final solution prior to Extra Credit.
#             # if len(tokens) == 3:
#             #     math_symbol = tokens[0]
#             #     num2 = int(tokens[2])
#             #     if math_symbol == 'pow':
#             #         num1 = float(tokens[1])
#             #     else:
#             #         num1 = int(tokens[1])
#             # else:
#             #     math_symbol = tokens[0]
#             #     num1 = int(tokens[1])
            
#             # evaluate_math_input(math_symbol, num1, num2)

#             continue

#handy_calculator()

def new_calculator():
    """Use this to parse user input and call appropriate math operation."""

    print "Welcome to our calculator!"
    
    while True:
        user_math_input = raw_input("Press 'q' to exit or type your math problem here:\n>> ")


        if user_math_input == 'q':
            break
        else:
            
            tokens = user_math_input.split(" ")
            # num2 = 0
            xtra_credit_eval(tokens)
            continue


new_calculator()
