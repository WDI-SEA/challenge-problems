
'''Write a function that takes an array as a parameter and returns an array with the elements in a random order.'''
import random
def shuffle_array(arr):
    for i in range(len(arr)):
        index = random.randrange(i, len(arr))
        temp = arr[i]
        arr[i] = arr[index]
        arr[index] = temp
    
arr = [1, 2, 3, 4]
shuffle_array(arr)
print(arr)