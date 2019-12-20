***** Small project to call C functions from python program. *****

How to call C functions in python?

-> Simple C program - hello.c

c_python_test$ cat hello.c
#include <stdio.h>

int main (int argc, char **argv)
{
        printf ("Hello from C\n");

        return 0;
}

int square (int i)
{
        return i * i;
}


-> Compile hello.c to get executable hello
c_python_test$ cc -o hello hello.c

c_python_test$ ls -lrt hello
-rwxrwxr-x 1 wind wind 8328 Dec 20 13:13 hello

-> Run hello
c_python_test$ ./hello
Hello from C

-> Create Shared Object Library (hello.so) of hello.c program so that we can use it in hello.py program.

c_python_test$ cc -fPIC -shared -o hello.so hello.c

c_python_test$ ls -lrt hello.so
-rwxrwxr-x 1 wind wind 7928 Dec 20 13:17 hello.so


c_python_test$ file -b hello.so
ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=37b4f16d5ecc6b9214b290d2e25e6a62ecdccf38, not stripped

-----

-> Simple python3 program - hello.py
c_python_test$ cat hello.py
# Simple python program

from ctypes import *

so_file = "/<absolute-path>/hello.so"

my_functions = CDLL(so_file)

print (type(my_functions))

print (my_functions.square(10))
print (my_functions.square(5))

print ('Hello from python3')

c_python_test$

-> Run hello.py using python3
c_python_test$ python3 hello.py
<class 'ctypes.CDLL'>
100
25
Hello from python3
c_python_test$ 
