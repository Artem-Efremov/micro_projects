"""

    Changes in version 3.0:
      - Added the support of float numbers.
      - Added the support of unary operators ('+' and '-').
      - Added zero-filling for numbers, that start with dot (e.g. '.0544').
      - Added the cycle for repeating of the program.

"""



import operator


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


def pseudo_int(string_num):
    """ Convert the number from string to integer 
        type without built-in function int """
    int_num = 0
    reversed_string_num = string_num[::-1]                          # begin read the characters from the end of the string.
    for indexx in range(len(string_num)):
        digit = reversed_string_num[indexx]
        int_num += (ord(digit) - ord('0')) * 10**indexx             # '2698' => 8 * 10**0 + 9 * 10**1 + 6 * 10**2 + 2 * 10**3 = 2698
    return int_num



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
        float_num = integer + fraction / 10**len(fract_part)
    else:
        integer = pseudo_int(string_num)
        float_num = integer * 1.0

    return float_num




answer = 'y'

while answer == 'y':

	# Get and process first number
    while True:
        str_first_num = input('Enter the first number: ')
        if not is_valid_number(str_first_num):
            print("You entered an invalid number. Please, try again!")
            continue
        first_num = pseudo_float(str_first_num)
        break


    # Get and process the operation
    while True:
        op = input('Enter the operation: ')
        operators = { 
                      '+': operator.add, '/': operator.truediv, 
                      '*': operator.mul, '**': operator.pow, 
                      '-': operator.sub, '%': operator.mod,
                      '//': operator.floordiv
                    }
        
        if op not in operators:
        	print('You didn`n enter a valid operation. Please, try again!')
        
        func = operators.get(op)
        break            


	# Get and process first number
    while True:
        str_second_num = input('Enter the second number: ')
        if not is_valid_number(str_first_num):
            print("You entered an invalid number. Please, try again!")
            continue
        second_num = pseudo_float(str_second_num)
        if second_num == 0 and op in ['/', '//', '%']:
            print('You are trying to divide by zero. ' +
                  'Please, choose another number')
        else:
            break


    result = func(first_num, second_num)


    # Formatted represent of the result
    print(str_first_num, op, str_second_num, '=', result, sep=' ')
    
    while True:
        answer = input("Try again? (y/n)\n").lower()
        if answer in ['y', 'n']:
            break
