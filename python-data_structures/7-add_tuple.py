#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two integers from each tuple or use 0 if not present
    a = tuple_a[:2] + (0, 0)
    b = tuple_b[:2] + (0, 0)
    
    # Calculate the sum of corresponding elements
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
