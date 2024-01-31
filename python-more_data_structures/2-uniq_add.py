def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_set = set()

    # Iterate through the list and add unique integers to the set
    for i in my_list:
        unique_set.add(i)

    # Sum the unique integers in the set and return the result
    result = sum(unique_set)
    return result
