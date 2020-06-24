"""
Implement a Python code to print the output on the console and also
redirect to a text file(log)
"""


import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)
f = open("E:\\PythonPractice\\logging_test.txt", "w")
handler1 = logging.StreamHandler(f)
handler1.setLevel(logging.INFO)
root.addHandler(handler1)
