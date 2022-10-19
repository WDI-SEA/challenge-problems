#!/bin/python3

import math
import os
import random
import re
import sys

#An English text needs to be encrypted using the following encryption scheme.
# First, the spaces are removed from the text. Let  be the length of this text.
# Then, characters are written into a grid, whose rows and columns have the following constraints:
# 
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    l = len(s)
    output =""
    # find the square root of the len(s)
    square_root = math.sqrt(l)
    # use math.floor() on that result to create the rows
    r = math.floor(square_root)+1
    # use math.ceil() on that to create colums
    col = math.ceil(square_root)
    # print(column)
    # as long as RxC >= len(s) -- print the itiration of (r[0] + c[0]) + (r[1] + c[0])
    # create grid
        # for el in range(0, l, r):
        # if el < l - (r-1):
        #    print (''.join(list(s[el:el+r])))
        # else:
        #     print (''.join(list(s[el:])))
    for el in range(col):
        k = el
        # itirate through all els of the col, r times for each col, (l times total) then print as a string
        for j in range(k, l, col): 
            # print(range(k, l, col))
            output += s[j]
        output += " "
    return output        
        
    

     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()