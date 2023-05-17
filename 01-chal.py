# Most effecient way to guess a random number in a range:

# You are given a range of values, and you must write an algorithm to guess a random number in the range in the most effecient way possible.

# After every time you guess, you're told if you're right, too high, or too low.

def guess_number(low, high, is_too_high):
    while low <= high:
        mid = low + (high - low) // 2
        result = is_too_high(mid)
        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else: # result == 1
            low = mid + 1
    return None
