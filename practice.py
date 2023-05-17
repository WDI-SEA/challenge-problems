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
