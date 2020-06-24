"""
Implement a function to print your name character by character using
a recursive function
"""

def print_name(string):
    if not string:
        return
    if string:
        chararray = list(string)
        print(chararray.pop(0))
        string = "".join(chararray)
    print_name(string)

