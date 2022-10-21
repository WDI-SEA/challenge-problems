
def day_of_the_week(input_day, remainder, count):
    # array of days
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    #  base case
    
    # recursive case
    # theory -- any number that is divisible by 7 will return the same day of the week
    # therefore -- any remainder added to given day will result in the correct day of the week. (?)
    if remainder <= 0 or remainder < count:
        if remainder == 0:
            print(f'no remainder, {input_day}')
        elif remainder in range(0,5):
            print(f'remainder is {remainder}, so now figure out the hard part')
        return 0
    else:
        return day_of_the_week(remainder - count, count, 1) + 1
        

print(day_of_the_week('sunday', 14, 7))


def division(n, b, q = 1):
    """
    parameters : a et b (integers)
    returns: the remainder of a and b
    pre-requisites : q = 1
    """
    if n <= 0 or n < b:
        if n == 0:
            print("Your division has no remainder.")
        elif n in range(0,5):
            print("Your remainder is", n)
        return 0
    else:
        return division(n - b, b, q) + q

print(division(14,7))