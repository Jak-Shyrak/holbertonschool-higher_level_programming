#!/usr/bin/python3
import sys


def add_arguments(arguments):
    result = sum(int(arg) for arg in arguments)
    return result


if __name__ == "__main__":
    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Check if there are any arguments
    if not arguments:
        print("No arguments provided.")
    else:
        # Add the arguments and print the result
        result = add_arguments(arguments)
        print("Result:", result)
