#! /usr/bin/python3

'''
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, 
awarding points on a scale from 1 to 100 for three categories: problem clarity, 
originality, and difficulty.

We define the rating for Alice's challenge to be the triplet A = (a[0], a[1], a[2]), and 
the rating for Bob's challenge to be the triplet B = (b[0], b[1], b[2]).

Your task is to find their comparison points by comparing a[0] with b[0],a[1] with b[1], and a[2] with b[2].

    If a[i] > b[i], then Alice is awarded 1 point.
    If a[i] < b[i], then Bob is awarded 1 point.
    If a[i] = b[i] , then neither person receives a point.

Comparison points is the total points a person earned.

Given A and B, can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains 3 space-separated integers, a[0], a[1], and a[2], describing the respective values in triplet A.
The second line contains 3 space-separated integers, b[0], b[1], and b[2], describing the respective values in triplet B.

Output Format

Return an array of two integers denoting the respective comparison points earned by Alice and Bob.
'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    alice, bob = 0, 0
    for i in range(0,len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return (alice, bob)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = solve(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
