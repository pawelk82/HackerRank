#! /usr/bin/python3

'''
Task

You are given a N X M integer array matrix with space 
separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of N and M.
The next N lines contains the space separated elements of M columns.

Output Format

First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4

Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]


'''

import numpy as np
arr = np.array([input().split() for _ in range(int(input().split()[0]))], int)
print (np.transpose(arr))
print (arr.flatten())
