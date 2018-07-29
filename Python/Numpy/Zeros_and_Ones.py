#! /usr/bin/python3

'''

Task

You are given the shape of the array in the form of space-separated integers, each integer 
representing the size of different dimensions, your task is to print an array of 
the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Output Format

First, print the array using the numpy.zeros tool and 
then print the array with the numpy.ones tool. 

Sample Input 0

3 3 3

Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]

'''

import numpy as np
arr = list(map(int, input().split()))
print (np.zeros((arr), dtype = np.int))
print (np.ones((arr), dtype = np.int))


