#! /usr/bin/python3


#You are in-charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. 
#When she blows out the candles, she’ll only be able to blow out the tallest ones. 
#Your task is to find out how many candles she can successfully blow out.

#For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 3, 2, 1, 3, 
#she will be able to blow out 2 candles successfully, since the tallest candle is of height 3 and there are 2 such candles.

#Complete the function birthdayCakeCandles that takes your niece's age and an integer array containing height of each candle as input, 
#and return the number of candles she can successfully blow out.

#Input Format

#The first line contains a single integer, n, denoting the number of candles on the cake.
#The second line contains n space-separated integers, where each integer i describes the height of candle i.

#Output Format

#Print the number of candles that can be blown out on a new line.

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    a = max(ar)
    sv = [x for x in ar if x == a] #creates an array sv from all the maximal values of array ar
    return (len(sv))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
