# Directions: Given a string, return true if the string is a palindrome or false if it is not. Palindromes are strings that form the same word if it is reversed. Do include spaces and punctuation in determining if the string is a palindrome.

# Examples:
# palindrome("abba") === true
# palindrome("abcdefg") === false

def palindromes(str):
    strList = list(str)
    strList.reverse()
    reversed_str = ''.join(strList)
    if str == '':
        print(f'Please try again and enter a word this time.')
    elif str == reversed_str:
        print(f'{str} is a palindrome')
    else:
        print(f'{str} reversed is {reversed_str} and is not a palindrome')


input = input('What potential palindrome would you like to check? \n')
palindromes(input)
