## Keep the change

# assign coins to their money values
# keep a running total the coins needed

def greedy(cents):
    # running totals of coins
    total_coins = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    # loop while theres still change
    while cents > 0:
        # if change - 25 is not negative
        if cents - 25 >= 0:
            # subtract 25 from change
            cents -= 25
            # and we can add a quarter
            total_coins += 1
            quarters +=1
        # else we can move onto dimes
        # same logic -- if change - a dime (10) is not negative
        elif cents - 10 >= 0:
            # subtract 10 from change
            cents -= 10
            # add a dime
            total_coins += 1
            dimes += 1
        elif cents - 5 >= 0:
            cents -= 5
            total_coins += 1
            nickles += 1
        elif cents - 1 >= 0:
            cents -= 1
            total_coins += 1
            pennies += 1
    # for nicer looking message
    msg_quarters = f"{quarters} quarters" if quarters else ""
    msg_dimes = f"{dimes} dimes" if dimes else ""
    msg_nickles = f"{nickles} nickles" if nickles else ""
    msg_pennies = f"{pennies} pennies" if pennies else ""
    print(f"Here's {total_coins} coins")
    print(msg_quarters, msg_dimes, msg_nickles, msg_pennies)

greedy(666)