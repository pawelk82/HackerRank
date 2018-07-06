#! /usr/bin/python3

#Given an array of integers, find the sum of its elements.

#Input Format

#The first line contains an integer, n, denoting the size of the array.
#The second line contains n space-separated integers representing the array's elements.

#Output Format

#Print the sum of the array's elements as a single integer. 


import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return (sum(int(i) for i in ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
