# Direction:
# Given an amount of change, determine the minimum number of coins required to make that change
# Examples:
# greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
# greedy(5) --> 1 `(1 nickle)`

def greedy(change, coin = 0):
    # quarter = 25
    # dime = 10
    # nickle = 5
    # penny = 1
    coins = {
        '1': {
            'quarter': 25 },
        'dime': 10,
        'nickle': 5,
        'penny': 1        
    }
    # coins = [25, 10, 5, 1]
    print(coins[coin])
    # change_printout = []
    # # base case
    # if change == 0:
    #     return change_printout
    # function
    
    # if change / coins[coin]
    # recursive case
    
greedy(25, 1)