# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.


def solution(arr):
    num_arr = []
    for num in arr:
        num_arr.insert(0, int(num))
    return sum(num_arr)


arr = [0, '1', 3, '-7', -9, '12']
print(solution(arr))

