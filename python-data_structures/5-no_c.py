#!/usr/bin/python3
def no_c(my_string):
    new_string = ""

    # Iterate through each character in the input string
    for c in my_string:
        # Check if the current character is not 'c' or 'C'
        if c != 'c' and c != 'C':
            # If not 'c' or 'C', add it to the result string
            new_string += c

    # Return the final result string
    return new_string
