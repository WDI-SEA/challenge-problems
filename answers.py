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



    

