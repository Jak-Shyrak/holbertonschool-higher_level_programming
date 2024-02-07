#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: . ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n")

    lines = text.split("\n")
    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i < len(lines) - 1:
            print("\n")
