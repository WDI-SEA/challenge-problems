# reverse the array

#define a function that reverses the array
def ReverseArr(arr):
    #make an empty array to store the elements in
    Reverse = []
    #create a for loop to itterate over the array use range , len -1, -1,-1
    for _ in range(len(arr)-1, -1, -1):
        #append the index inside of the empty array. 
        Reverse.append(arr[_])
    #return the reversed array
    return Reverse

arr = [1,2,3,4,5]
print(ReverseArr(arr))

