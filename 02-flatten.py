'''
Write an algorithm to flatten a multi-dimensional array:

vec = [[1,2,3], [4,5,6], [7,8,9]]
=> [1,2,3,4,5,6,7,8,9]
'''

def flatten(list):
    i = 1
    while i < len(list):
        for j in list[i]:
            list[0].append(j)
        i += 1
    return list[0]

print(flatten([[1,2,3], [4,5,6], [7,8,9], [10,11], [12, 13, 14] ]))