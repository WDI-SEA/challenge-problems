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
greedy(100)
