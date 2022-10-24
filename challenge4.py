# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

array = [1,'1','2',3,'4','6',5]

def numberPrint(array):
    newArray = []
    for i in range(0,len(array)):
        if type(array[i]) == str:
            newArray.append(int(array[i]))
        else:
            newArray.append(array[i])
    return newArray
print(f'SHOULD BE: [1, 1, 2, 3, 4, 6, 5] ANSWER:',numberPrint(array))