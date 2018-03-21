"""
Description:
    The script is based on work of three loops.
    
    The first two is same and take a number from the standard input as a string 
    (the loop repeats if the number isn`t valid).

    VALID STRING NUMBERS: The numbers that consist only from digits. Any symbols 
    like punctuations, whitespaces or letters are not valid and break the loop.
    
    Third loop takes a symbol from the standard input as a string (the loop 
    repeats if the symbol of operator isn`t valid).
    
    VALID OPERATORS: + -  * ** / // %
"""


while True:
    str_first_num = input('Enter the first integer number: ') # Get the first number
    
    is_digit = True 
    first_num = 0
    ind = 0
    
    # Convert the first number from string type to integer type without function int
    while ind < len(str_first_num):
        digit = str_first_num[::-1][ind] # begin from the end of string
        if ord('0') <= ord(digit) <= ord('9'):
            first_num += (ord(digit) - ord('0')) * 10**ind # '2698' => 8 * 10**0 + 9 * 10**1 + 6 * 10**2 + 2 * 10**3 = 2698
            ind += 1
        else:
            is_digit = False
            break

    # Verify 
    if is_digit:
        break
    else:
        print("You didn`n enter an integer number. Please, try again!")




while True:
    str_second_num = input('Enter the second integer number: ') # Get the second number
    
    is_digit = True
    second_num = 0
    ind = 0
    
    # Convert the first number from string type to integer type without function int
    while ind < len(str_second_num):
        digit = str_second_num[::-1][ind]
        if ord('0') <= ord(digit) <= ord('9'):
            second_num += (ord(digit) - ord('0')) * 10**ind # '2698' => 8 * 10**0 + 9 * 10**1 + 6 * 10**2 + 2 * 10**3 = 2698
            ind += 1
        else:
            is_digit = False
            break

    # Verify 
    if is_digit:
        break
    else:
        print("You didn`n enter an integer number. Please, try again!")




while True:
    op = input('Enter the operation: ') # Get the operation

    # Try to get the result
    if op == '+':
        result = first_num + second_num
    elif op == '-':
        result = first_num - second_num
    elif op == '*':
        result = first_num * second_num
    elif op == '**':
        result = first_num ** second_num
    elif op == '/':
        result = first_num / second_num
    elif op == '%':
        result = first_num % second_num
    elif op == '//':
        result = first_num // second_num
    else:
        print("You didn`n enter a valid operation. Please, try again!")
        continue
    break

# Formatted represent of the result
print(str_first_num, op, str_second_num, '=', result, sep=' ')
