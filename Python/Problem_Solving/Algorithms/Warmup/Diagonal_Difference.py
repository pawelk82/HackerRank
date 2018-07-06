#! /usr/bin/python3

#Given a square matrix, calculate the absolute difference between the sums of its diagonals. 

#Input Format

#The first line contains a single integer, n, the number of rows and columns in the matrix arr.
#Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].

#Output Format

#Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    i,a,b,l = 0, 0, 0, len(arr)-1
    while i != len(arr):
        a += arr[i][i]
        b += arr[i][l-i]
        i += 1    
    return (abs(a-b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
