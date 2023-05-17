'''
Directions:
Given a string, return true if the string is a palindrome
or false if it is not. Palindromes are strings that
form the same word if it is reversed. Do include spaces
and punctuation in determining if the string is a palindrome.

Examples:

palindrome("abba") === true
palindrome("abcdefg") === false

'''

# def palindrome(string):
#     for i in range(len(string)):
#         end = int(len(string) - i) - 1
#         if string[i] != string[end]:
#             return False
#     return True

def palindrome(string):
    return string == string[::-1]

print(palindrome("tacocat"))
print(palindrome("racecar"))
print(palindrome("abcdefg"))