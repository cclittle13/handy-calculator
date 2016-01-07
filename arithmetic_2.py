# def add(num1, num2):
#     return num1 + num2

def add(list_of_inputs):
    # return num1 + num2

    final_sum = 0
    for num in list_of_inputs[1:]:
        final_sum += int(num)
        
    return final_sum


def subtract(list_of_inputs):
    # return num1 - num2

    final_sum = int(list_of_inputs[1])
    for num in list_of_inputs[2:]:
        final_sum -= int(num)

    return final_sum


def multiply(list_of_inputs):

    # return num1 * num2

    final_product = 1
    for num in list_of_inputs[1:]:
        final_product = final_product * int(num)
        
    return final_product


def divide(list_of_inputs):
    # Need to turn at least argument to float for division to
    # not be integer division

    #return float(num1) / float(num2) 
    
    final_product = float(list_of_inputs[1])
    for num in list_of_inputs[2:]:
        final_product =  float(final_product) / float(num)

    return final_product



def square(list_of_inputs):
    # Needs only one argument
    # return num1 * num1
    list_of_squares = []


    for num in list_of_inputs[1:]:
        square_of_num = int(num) * int(num)
        # print square_of_num,
        list_of_squares.append(str(square_of_num))

    string_of_squares = " ".join(list_of_squares)
    
    return string_of_squares    





def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return float(num1) ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
