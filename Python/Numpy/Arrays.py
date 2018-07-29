#! /usr/bin/python3

#The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.

#To use the NumPy module, we need to import it using:

#import numpy

#Task

#You are given a space separated list of numbers.
#Your task is to print a reversed NumPy array with the element type float.

#Input Format

#A single line of input containing space separated numbers.

#Output Format

#Print the reverse NumPy array with type float.

import numpy

def arrays(arr):
    x=numpy.array(arr)
    x=numpy.asfarray(x,float)
    return numpy.flipud(x)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

