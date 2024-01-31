def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_set = set(my_list)
    # Sum the unique integers in the set and return the result
    result = sum(unique_set)
    return result
