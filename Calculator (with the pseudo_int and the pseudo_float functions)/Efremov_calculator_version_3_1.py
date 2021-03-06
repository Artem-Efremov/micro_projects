"""

    Changes in version 3.1:
      - All cycles ware replaced by the recursive functions.
      - The program will start data processing when the script is opened as 
        self-dependent file. It allows to import functions from the script.
      - Added the variable '__all__'.
      - The principle of the function "pseudo_int" is based on the recursion.

"""


import operator


__all__ = ['pseudo_int', 'pseudo_float']


OPERATORS = { 
              '+': operator.add, '/': operator.truediv, 
              '*': operator.mul, '**': operator.pow, 
              '-': operator.sub, '%': operator.mod,
              '//': operator.floordiv
            }


def is_valid_number(string_num):
    if string_num:
        valid_chars = '0123456789+-.'
        is_only_valid_chars = all([i in valid_chars for i in string_num])
        is_single_spec_chars = all([string_num.count(i) <= 1 for i in '+-.'])
        is_leading_spec_chars = all([string_num.index(i) == 0 
                                     if i in string_num else True 
                                     for i in '+-'])
        return all([is_only_valid_chars,
                    is_single_spec_chars,
                    is_leading_spec_chars])
    return False


def pseudo_int(string_num, indexx=0):
    """ Convert the number from string to integer 
        type without built-in function int """
    if len(string_num) > 1:
        return (pseudo_int(string_num[:-1], indexx+1) + 
                (ord(string_num[-1]) - ord('0')) * 10**indexx)
    return (ord(string_num) - ord('0')) * 10**indexx


def pseudo_float(string_num):
    """ Convert the number from string to float 
        type without built-in function float """

    sign = {'+': 1, '-': -1}.get(string_num[0], 1)                  # Get unary operation

    if string_num[0] in '+-':
        string_num = string_num[1:]
    if string_num[0] == '.':
        string_num = '0' + string_num

    if '.' in string_num:
        int_part, fract_part = string_num.split('.')
        integer = pseudo_int(int_part)
        fraction = pseudo_int(fract_part)
        return integer + fraction / 10**len(fract_part)
    else:
        return pseudo_int(string_num)


def process_number():
    str_num = input('Enter the number: ')
    if is_valid_number(str_num):
        return pseudo_float(str_num)
    else:
        print("You entered an invalid number. Please, try again!")
        return process_number()


def process_operation():
    op = input('Enter the operation: ')
    if op in OPERATORS:
        return op, OPERATORS.get(op)
    else:
        print('You didn`n enter a valid operation. Please, try again!')
        return process_operation()   


def is_division_by_zero(func):
    number = process_number()
    if number == 0 and func.__name__ in ['truediv', 'floordiv', 'mod']:
        print('You are trying to divide by zero. ' +
              'Please, choose another number')
        return is_division_by_zero(func)
    return number


def finish():
    answer = input("Try again? (y/n)\n").lower()
    if answer not in ['y', 'n']:
        print('Please, enter a valid answer.')
        return finishing()
    return answer


def calculator(answer='y'):
    if answer == 'y':
        first_num = process_number()
        op, func = process_operation()
        second_num = is_division_by_zero(func)
        result = func(first_num, second_num)
        print(str(first_num), op, str(second_num), '=', result, sep=' ')
        return calculator(finish())



if __name__ == '__main__':
    calculator()
