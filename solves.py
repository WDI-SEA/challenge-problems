'''
# 1 - Most efficient way to guess a random number in a range:
 You are given a range of values, and you must write an algorithm to guess a random number in the range in the most efficient way possible.
 After every time you guess, you're told if you're right, too high, or too low.
 '''
def binary_search(arr, target):
    # start with the lowest index for the search
    low = 0
    # start with the highest end of the range for our search
    high = len(arr) - 1

    # iterate through the array while lower index is still less than high index
    while low <= high:
        # find the mid index of the portion between low & high indices
        mid = low + (high - low) // 2
        # save guess to variable to check
        guess = arr[mid]

        # check guess against target
        if guess == target:
            return mid
        # if guess was too low, adjust lower bound to be higher than mid
        elif guess < target:
            low = mid + 1
        # if guess was too high, adjust higher bound to be lower than mid
        else:
            high = mid - 1
    
    # if we finished iterating without answer, it's not there
    return None


'''
# 2 - Write an algorithm to flatten a multi-dimensional array:
vec = [[1,2,3], [4,5,6], [7,8,9]] => [1,2,3,4,5,6,7,8,9]
'''
def two_d_flatten(arr):
    # start with new empty array
    # Outer loop to iterate through the outer array
        # inner loop to iterate through each ele in array
            # add each ele to empty array
    # return new array