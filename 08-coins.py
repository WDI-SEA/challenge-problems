'''
Direction:

Given an amount of change, determine the minimum number of coins required to make that change

Examples:

greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
greedy(5) --> 1 `(1 nickle)`

'''

def greedy(change):
    coins = {
        25: 0,
        10: 0,
        5: 0,
        1: 0,
    }
    remainder = change
    for i in coins:
        coins[i] = int(remainder / i)
        remainder = remainder % i
    min_coins = coins[25] + coins[10] + coins[5] + coins[1]
    return f"{min_coins}: {coins[25]} quarters, {coins[10]} dimes, {coins[5]} nickels, {coins[1]} pennies"

print(greedy(65))