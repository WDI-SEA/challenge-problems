'''
We define a magic square to be an nXn matrix of distinct positive integers from 1  to n^2  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a 3x3 matrix s of integers in the inclusive range [1,9] . We can convert any digit a to any other digit b in the range [1,9] at cost of [a-b] . Given s, convert it into a magic square at minimal cost. 

Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range [1,9].

https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    s = sum(s, [])  # flaten s

    #  All possible magic squares of 3x3 order
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]
    
    
    costs = []  # this variable will contain all possible costs

    for magic_square in magic_squares:
        costs.append(sum([abs(magic_square[i] - s[i]) for i in range(9)]))

    return min(costs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
