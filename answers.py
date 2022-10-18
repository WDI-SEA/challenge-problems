# Write a program that prints the day of the week given a number of days and weeks.

# Example: 30 days from Monday is Wednesday.

def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
  
  
print(reverse('computer'))
print(reverse(reverse("computer")))

import sys

def minCoins(coins, m, target):
 
    # base case
    if (target == 0):
        return 0
 
    # Initialize result
    
    res = sys.maxsize
     
    # Try every coin that has smaller value than target
    for i in range(0, m):
        if (coins[i] <= target):
            sub_res = minCoins(coins, m, target-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
 
    return res
 
coins = [9, 6, 5, 1]
m = len(coins)
target = 11

print(minCoins(coins,m,target))
    





    

