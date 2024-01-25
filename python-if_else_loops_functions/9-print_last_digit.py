#!/usr/bin/python3
def print_last_digit(number):
    """
    Prints the last digit of a number

    Parameters:
    - number (int): Number whose the last digitmust be returned

    Returns:
    int: Value of the last digit

    """
    l_digit = abs(number) % 10
    print(l_digit, end='')
    return(l_digit)
