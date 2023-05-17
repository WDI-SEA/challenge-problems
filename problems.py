vec = [[1,2,3], [4,5,6], [7,8,9]]
def flatten (list):
    flattened = []
    for arr in list:
        for item in arr:
            flattened.append(item)
    return flattened
    
print(flatten(vec))


def palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

print(palindrome('abba'))  # Output: True
print(palindrome('hello'))  # Output: False



def most_used(word):
    most_common_char = max(word, key=word.count)
    return most_common_char

print(most_used('hello'))  # Output: 'l'




def array_split(arr, split):
    chunks = []
    while len(arr) > 0:
        chunks.append(arr[:split])
        arr = arr[split:]
    return chunks
    
    
print(array_split([1, 2, 3, 4], 2))  # Output: [[ 1, 2], [3, 4]]
print(array_split([1, 2, 3, 4, 5], 2))  # Output: [[ 1, 2], [3, 4], [5]]
print(array_split([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [[ 1, 2, 3], [4, 5, 6], [7, 8]]
print(array_split([1, 2, 3, 4, 5], 4))  # Output: [[ 1, 2, 3, 4], [5]]
print(array_split([1, 2, 3, 4, 5], 10))  # Output: [[ 1, 2, 3, 4, 5]]







    
import random 

def random_array(arr):
    random.shuffle(arr)
    return(arr)
    

my_arr = ['banana','orange','ketchup','lettuce']
print(random_array(my_arr))
        
        
