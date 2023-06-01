"""
2d array w 2 values
make a 1d array with all values in 2d array
new_array=[]
array=[[1,2,3],[4,5,6],[7,8,9]]
result= [1,2,3,4,.....]
"""

#define a function that prints a new array of the values of nested array into new_array
def solution(array):
    #create a variable of empty array to insert in
    new_array= []

    # use a for loop to iterate over the nested array -- identify the indexes 
    for item in array:
        for value in item:
            print(value)
        # then iterate over those to find the values
            new_array.append(value)
    print(new_array)

   

        #insert what is returned inside the result array.
 


array=[[1,2,3],[4,5,6],[7,8,9]]
solution(array)
