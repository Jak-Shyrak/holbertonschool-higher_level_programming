#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    if len(argv) - 1 == 1:
        print("1 argument:")
    else:
        print(len(argv) - 1, "arguments:")

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
