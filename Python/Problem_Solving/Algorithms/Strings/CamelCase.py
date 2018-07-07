#! /usr/bin/python3

'''
Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following properties:

    It is a concatenation of one or more words consisting of English letters.
    All letters in the first word are lowercase.
    For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, print the number of words in s on a new line.

Input Format

A single line containing string s.

Output Format

Print the number of words in string s.
'''

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    words = 1
    for l in s:
        if l.isupper():
            words += 1
    return (words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()
