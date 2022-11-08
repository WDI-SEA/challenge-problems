# From Git-repo

# Direction:
# Given an amount of change, determine the minimum number of coins required to make that change
# Examples:

# greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
# greedy(5) --> 1 `(1 nickle)`

change = int(input("How much change do you need? \n"))

def change_calc(change, quarters=0, dimes=0, nickles=0, pennies=0):
    # base case
    if change == 0:
        return print(f"Output: {quarters+dimes+nickles+pennies} : {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies")

    if change >= 25:
        result = divmod(change, 25)
        quarters += result[0]
        change = result[1]
        change_calc(change, quarters, dimes, nickles, pennies)
    
    elif change >= 10:
        result = divmod(change, 10)
        dimes += result[0]
        change = result[1]
        change_calc(change, quarters, dimes, nickles, pennies) 
    
    elif change >= 5:
        result = divmod(change, 5)
        nickles += result[0]
        change = result[1]
        change_calc(change, quarters, dimes, nickles, pennies) 
    
    else:
        pennies += change
        change = 0
        change_calc(change, quarters, dimes, nickles, pennies)          

# change_calc(change)

def coin_calc(change, qtrs=0, dimes=0, nickles=0, pennies=0):
    if change >= 25:
        qtrs = change // 25
        mod = change % 25
        if mod == 0:
            return print(qtrs)
        else:
            coin_calc(mod, qtrs, dimes, nickles, pennies)
    
    elif change >= 10:
        dimes = change // 10
        mod = change % 10
        if mod == 0:
            return print(qtrs + dimes)
        else:
            coin_calc(mod, qtrs, dimes, nickles, pennies)
    
    else:
        nickles = change // 5
        mod = change % 5
        pennies = mod
        return print(qtrs + dimes + nickles + pennies)

coin_calc(change)
    


    



