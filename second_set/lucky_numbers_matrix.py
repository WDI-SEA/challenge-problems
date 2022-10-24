# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

arr = [[3,6],[7,1],[5,2],[4,8]]

arr2 = [[3,7,8],[9,11,13],[15,16,17]]

arr3 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]

arr4 = [[7,8],[1,2]]


def lucky_numbers(matrix):
    smolNumRow = []
    testingList = []
    beegNumList = []

    for i in range(len(matrix)):
        smolNumRow.append(min(matrix[i]))
        

    for index in range(len(matrix[0])):
        testingList = []
        for i in range(len(matrix)):
            testingList.append(matrix[i].pop(0))
        beegNumList.append(max(testingList))

    for index in smolNumRow:
        for subIndex in beegNumList:
            if subIndex in smolNumRow:
                return [subIndex]
    
    return []

print(lucky_numbers(arr))
print(lucky_numbers(arr2))
print(lucky_numbers(arr3))
print(lucky_numbers(arr4))