* Calculator

    Description:
        The script is based on work of three loops.

        The first two is same and take a number from the standard input as 
        a string (the loop repeats if the number isn`t valid).

        VALID STRING NUMBERS: The numbers that consist only from digits. 
        Any symbols like a punctuation, a whitespace or a letter are not 
        valid and break the loop.

        Third loop takes a symbol from the standard input as a string 
        (the loop repeats if the symbol of operator isn`t valid).

        VALID OPERATORS: + -  * ** / // %

    Changes in version 2.0:
      - Added the 'pseudo_int' function that convert the string number to int. 
        This function is based on the built-in 'ord' function.
      - Added an import of the 'operator' module.
      - Added the dictionary with the main arithmetic operators from the 
        'operator' module. The keys of the dict are the valid operators.

    Changes in version 3.0:
      - Added the support of float numbers.
      - Added the support of unary operators ('+' and '-').
      - Added zero-filling for numbers, that start with dot (e.g. '.0544').
      - Added the cycle for repeating of the program.

    Changes in version 3.1:
      - All cycles ware replaced by the recursive functions
      - The program will start data processing when the script is opened as 
        self-dependent file. It allows to import functions from the script.
      - Added the variable '__all__'
      - The principle of the function "pseudo_int" is based on the recursion

    Changes in version 3.2:
      - The functions from module operator were replaced by the lambda-functions.
