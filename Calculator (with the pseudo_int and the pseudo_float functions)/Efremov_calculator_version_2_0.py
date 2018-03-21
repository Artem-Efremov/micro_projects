"""

    Changes in version 2.0:
      - Added the 'pseudo_int' function that convert the string number to int. 
        This function is based on the built-in 'ord' function.
      - Added an import of the 'operator' module.
      - Added the dictionary with the main arithmetic operators from the 
        'operator' module. The keys of the dict are the valid operators.

"""



import operator


def pseudo_int(string_num):
    """ Convert the number from string type to 
        integer type without built function int """
    int_num = 0
    reverse_string_num = string_num[::-1] # begin read the characters from the end of the string.
    for indexx in range(len(string_num)):
        digit = reverse_string_num[indexx]
        if ord('0') <= ord(digit) <= ord('9'):
            int_num += (ord(digit) - ord('0')) * 10**indexx # '2698' => 8 * 10**0 + 9 * 10**1 + 6 * 10**2 + 2 * 10**3 = 2698
        else:
            return None
    return int_num


while True:
    str_first_num = input('Enter the first integer number: ') # Get the first number
    first_num = pseudo_int(str_first_num)
    if first_num:
        break
    else:
        print("You didn`n enter an integer number. Please, try again!")


while True:
    op = input('Enter the operation: ') # Get the operation
    operators = {'+': operator.add, '/': operator.truediv, '*': operator.mul,
                 '**': operator.pow, '-': operator.sub, '%': operator.mod,
                 '//': operator.floordiv}
    if op in operators:
        func = operators.get(op)
        break
    else:
        print("You didn`n enter a valid operation. Please, try again!")


while True:
    str_second_num = input('Enter the second integer number: ') # Get the second number
    second_num = pseudo_int(str_second_num)
    if second_num is None:
        print("You didn`n enter an integer number. Please, try again!")
    elif second_num == 0 and op in ['/', '//', '%']:
        print('You are trying to divide by zero. Please, choose another number')
    else:
        break


result = func(first_num, second_num)


# Formatted represent of the result
print(str_first_num, op, str_second_num, '=', result, sep=' ')
