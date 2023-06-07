# #Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# #create a function that returns odd or even
# def odd_or_even(num):

#    if num <= 100:
#       if num % 2 == 0:
#          print('even')
#       else:
#          print('odd')
#    else:
#       print('out od range')
        

# odd_or_even(70)

# # ## ## Num 2

# # return a finction that always retuns hello world

# # define the function and pass taco
# def say_hello(taco):
#    if taco:
#    #define my logic which is to return "Hello, World"
#     return "Hello World!"


# print(say_hello("say it!"))

### # #### num3

# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.
   



# def count_occurrences(string_list, queries):
#     results = []
#     for query in queries:
#         count = 0
#         for string in string_list:
#             if query == string:
#                 count += 1
#         results.append(count)
#     return results

# string_list1 = ['a', 'a', 'b', 'ab', 'ab', 'ab']
# queries1 = ['ab', 'a']

# output1 = count_occurrences(string_list1, queries1)
# print(output1) 


#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#create a solution class
    #use a hash table to check if ints are duplicates
    #creating a ducplicate check that passes self and num and returns a bool
        #hash the value
            #for loop to itereate over each element and add it to the hash table
            #if value is inside of hash table return true.

class Solution:
    def duplicate_check(self, nums: list[int]) -> bool:
        hashset = set()
        for _ in nums:
            if _ in hashset:
                return True
            hashset.add(_)
        return False

solution = Solution()  
nums = [1,2,3,4,4,5,6,7]
result = solution.duplicate_check(nums)
print(result)




