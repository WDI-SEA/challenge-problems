'''given an array and a total, return true if one or more consecutive numbers in the array sum up to that total'''

def consecutive_sum(arr, target):
    if len(arr) == 0:
        return false
    if len(arr) == 1 and arr[0] != target:
        return false
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[i]
            if (sum == target):
                return true
    return false
        