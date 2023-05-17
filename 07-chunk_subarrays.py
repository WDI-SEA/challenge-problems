'''
Directions: Given an array and chunk size, divide the array into many subarrays where each subarray is of length size

Examples:

chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
'''


def chunkify(list, chunk):
    # placeholder for new array
    new_list = []
    # placeholder sub array
    new_sublist = []
    # for loop that iterates over each item in array
    for i in range(len(list)):
        # if (i + 1) % chunk = 0,
        if (i+1) % chunk == 0: 
            # push current index into array
            new_sublist.append(list[i])
            # push subarray into placeholder array
            new_list.append(new_sublist)
            # start a new subarray
            new_sublist = []
        # else
        else:
            # push current index into array
            new_sublist.append(list[i])
    # if placeholder array[len(array)] != []
    if new_sublist != []:
        # push subarray into array
        new_list.append(new_sublist)
    # return array
    return(new_list)

print(chunkify([1, 2, 3, 4], 2))
print(chunkify([1, 2, 3, 4, 5], 2))
print(chunkify([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(chunkify([1, 2, 3, 4, 5], 4))
print(chunkify([1, 2, 3, 4, 5], 10))
