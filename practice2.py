# # reverse the array

# #define a function that reverses the array
# def ReverseArr(arr):
#     #make an empty array to store the elements in
#     Reverse = []
#     #create a for loop to itterate over the array use range , len -1, -1,-1
#     for _ in range(len(arr)-1, -1, -1):
#         #append the index inside of the empty array. 
#         Reverse.append(arr[_])
#     #return the reversed array
#     return Reverse

# arr = [1,2,3,4,5]
# print(ReverseArr(arr))

# define a function that reverses a given array
def reversed_Array(arr):
    #create a variable that stores a empty array
    reversed_A = []
    #use a for loop to iterate over the given array:
    for _ in range(len(arr)-1, -1, -1):

        #append the element inside of the empty array
        reversed_A.append(arr[_])
    #return the new array
    return reversed_A

arr = [9,8,7,6,5,4,3,2,1]
print(reversed_Array(arr))

