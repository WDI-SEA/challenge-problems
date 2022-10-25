# 

# Given an amount of change, determine the minimum number of coins required to make that change       
# Examples:   # greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`   # greedy(5) --> 1 `(1 nickle)`

# amount  99
# divide as many quarters as possible if then remainder goes to the next coin
# - 3x 25 = 29
# divide as many dimes 
# 2x - 20 = 9
# divid as many nickels
# 1x - 5 = 4
# divid as many pennys
# 4s - 4 = 0

import math

def function(amount):
    q = 25
    d = 10
    n = 5
    p = 1
    amount = sum(q + d + n + p)
    math.floor(amount/q) = math.remainder
    math.remainder(amount/d) = math.remainder2
    math.remainder2(amount/n) = math.remainder3
    math.remainder3(amount/p) = math.remainder4
    
    quarters = math.remainder
    dimes = math.remainder2
    nickels = math.remainder3
    pennies = math.remainder4

print(function(amount))


 
##### --- solution bracket
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