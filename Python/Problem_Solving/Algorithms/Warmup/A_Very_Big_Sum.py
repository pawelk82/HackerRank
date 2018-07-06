#! /usr/bin/python3

#Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

#Input Format

#The first line of the input consists of an integer n.
#The next line contains n space-separated integers contained in the array.

#Output Format

#Print the integer sum of the elements in the array.

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return (sum(int(i) for i in ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
