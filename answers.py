# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

# def reverse(word):
#     if len(word) == 0:
#         return word
#     else:
#         return reverse(word[1:]) + word[0]
  
  
# print(reverse('computer'))
# print(reverse(reverse("computer")))


    

# import sys

# def sum(coins, length, target):
    
#     # Create a base case that will stop the function
#     if(target == 0):
#         return 0
#     for i in range(0,length):
#         if(coins[i] <= target):
#            sub = sum(coins,length,target - coins[i])
#            if(sub != target and sub + 1 <  length):
#             sub = sub + 1
#     return sub

# coins = [25,25,25]
# length = len(coins)
# target = 40

# sum(coins,length, target)



# Direction:

# Given an amount of change, determine the minimum number of coins required to make that change

# Examples:
# greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
# greedy(5) --> 1 `(1 nickle)`


import math

def greedy(change):
    quarters = 25
    dime = 10
    nickle = 5
    penny = 1

    q = math.floor(change/quarters)
    change = (change - q * quarters)
    d = math.floor(change/dime)
    change = (change - d * dime)
    n = math.floor(change/nickle)
    change = (change - n * nickle)
    p = math.floor(change/penny)
    change = (change - n * penny)

    print(f'{q}: quarters, {d}: dimes, {n}: nickles, {p}: pennies')

# PSEUDOCODE
# 1. create variables for each value of cents
# 2. divide the by the highest cent and return a floor number, round down
# 3. subtract that value from the change
# 4. continue steps 2 - 4

# quarters = 25
# print(math.floor(65/quarters))
greedy(65)


# PART 2 QUESTIONS
# 1)
# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one
# digit, continue reducing in this way until a single-digit number is
# produced. The input will be a non-negative integer.


def digital root(n):
x = str(n)
r=0
while len(x) > 1:
r=0
for i in range (len(x)):
r = r + int(x[i])
X = str(r)
return r

    
#  2)
#  Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen == 0: 
            return -1
        left = [0 for i in range(numsLen)]
        right = [0 for i in range(numsLen)]
        right[numsLen - 1] = nums[numsLen - 1]
        for i in range(numsLen - 2, -1, -1):
            right[i] = right[i + 1] + nums[i]
        left[0] = nums[0]
        if right[0] == left[0]:
            return 0
        for i in range(1, numsLen):
            left[i] = left[i - 1] + nums[i]
            if left[i] == right[i]:
                return i
        return -1
        
