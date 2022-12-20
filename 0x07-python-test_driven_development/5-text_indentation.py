#!/usr/bin/python3
"""Text indentations"""


def text_indentation(text):
    """Prints a text with 2 new lines
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.

    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    leng = len(text)
    for i in range(leng):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print("\n")
        else:
            print(text[i], end="")
