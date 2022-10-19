# DESCRIPTION:
# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    index = 0
    count_list = []
    test_list = list(set(seq))
    for num in test_list:
        count_list.insert(len(count_list), seq.count(num))
    for idx, num in enumerate(count_list):
        if num % 2 != 0:
            index = idx
    return test_list[index]    

# OR

def find_it(seq):
    for i in seq:
        if seq.count(i)%2==1:
            return i