# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

testArr1 = [2,3,1,3,2,4,6,9,2,19,23,7]
testArr2 = [2,1,4,3,9,6]

def relativeSortArray(arr1, arr2):
    inArr = []
    outArr = []

    dict = {}

    finalArr = []


    # splits items into separate arrays depending on whether they appear in
    for item in arr1:
        if item in arr2:
            inArr.append(item)
        else:
            outArr.append(item)


    for i in arr2:
        dict[i] = 0

    for item in inArr:
        for index in dict:
            if item == index:
                dict[item] += 1

    for index in dict:
        for i in range(dict[index]):
            finalArr.append(index)

    # print(finalArr)

    # sorts second array in ascending order
    outArr.sort()

    return [*finalArr, *outArr]


print(relativeSortArray(testArr1, testArr2))