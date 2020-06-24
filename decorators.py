# Decorators are simply some wrappers on top of the function
# https://realpython.com/primer-on-python-decorators/

# Define the decorator
import functools

def do_twice(func):
    # Define the inner function
    def print_twice(*args,**kwargs):
        for index in range(2):
            func(*args,**kwargs)
    return print_twice

# call the decorator
@do_twice
def print_string(arg):
    print("kishore"+str(arg))
