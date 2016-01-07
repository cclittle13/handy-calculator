# def add(num1, num2):
#     return num1 + num2

def add(list_of_inputs):
    final_sum = 0
    for num in list_of_inputs[1:]:
        final_sum += int(num)
        
    return final_sum


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return float(num1) ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
