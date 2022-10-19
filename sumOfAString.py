# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

testArr = [1, '3', 2, '5']

def sum_of_a_string(arr):
    return sum(map(int, arr))

print(sum_of_a_string(testArr))