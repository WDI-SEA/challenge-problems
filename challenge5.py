# Write a function that takes an array as a parameter and returns an array with the elements in a random order.
import random, math
arr = [1,2,3,4,5,6,7,8,9]

def randomize(arr, x=None):
    # take in array, randomly index
    # after using each index, make the array smaller until there is none left (for loop?)
    newArray = []
    array = arr
    x=len(array)
    if x == 0:
        return newArray
    while x > 0:
        y = random.randrange(x)
        newArray.append(array[y])
        del array[y]
        x=len(array)
        # array[y:y]
        # randomize(array,x)
    return newArray
    

print(randomize(arr))

# x=len(arr)
# y = random.randrange(x)
# # print(x,y)
# arr.pop(y)
# print(arr)