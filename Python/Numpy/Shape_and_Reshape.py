#! /usr/bin/python3

'''
shape

The shape tool gives a tuple of array dimensions and can be used to change 
the dimensions of an array.

Task

You are given a space separated list of nine integers. Your task is to convert this list 
into a 3X3 NumPy array.

Input Format

A single line of input containing 9 space separated integers.

Output Format

Print the 3X3 NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9

Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]

'''

import numpy as np
arr = [int(x) for x in input().split()]
arr = np.array(arr)
print (np.reshape(arr,(3,3)))
