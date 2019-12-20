# Simple python program to use shared library to call C functions using ctypes.

from ctypes import *

so_file = "/<absolute-path-to-project-directory>/hello.so"

my_functions = CDLL(so_file)

print (type(my_functions))

print (my_functions.square(10))
print (my_functions.square(5))

print ('Hello from python3')
