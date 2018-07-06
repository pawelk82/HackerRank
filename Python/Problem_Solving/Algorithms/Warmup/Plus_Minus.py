#! /usr/bin/python3

#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
#Print the decimal value of each fraction on a new line.

#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
#though answers with absolute error of up to 10**-4 are acceptable.

#Input Format

#The first line contains an integer, n, denoting the size of the array.
#The second line contains n space-separated integers describing an array of numbers arr(a0,a1,a2,...,an-1).

#Output Format

#You must print the following 3 lines:

#   1. A decimal representing of the fraction of positive numbers in the array compared to its size.
#   2. A decimal representing of the fraction of negative numbers in the array compared to its size.
#   3. A decimal representing of the fraction of zeros in the array compared to its size.


import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr1 = [0,0,0]
    for i in arr:
        if i > 0:
            arr1[0] += 1
        elif i < 0:
            arr1[1] += 1
        elif i == 0:
            arr1[2] += 1
    for s in arr1: print ('%0.6f' % (s/n))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
