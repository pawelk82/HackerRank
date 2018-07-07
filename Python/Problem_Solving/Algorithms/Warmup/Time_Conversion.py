#! /usr/bin/python3

#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
#Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

#Input Format

#A single string s containing a time in 12-hour clock format (i.e.:hh:mm:ssAM or hh:mm:ssPM), 
#where 01 <= hh <= 12 and 00 <= mm,ss <= 59.

#Output Format

#Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

import os
import sys

def timeConversion(s):
    n = 12
    if s[0:2] == "12" and "AM" in s:
        return ("00"+s[2:8])
    elif s[0:2] == "12" and "PM" in s or "AM" in s:
        return (s[0:8])
    elif "PM" in s:
        ho = n+int(s[0:2])
        return (str(ho)+s[2:8])
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
