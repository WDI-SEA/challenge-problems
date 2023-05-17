'''
Directions:
Given a string, return a new string with the reversed
order of characters

Examples

reverse('apple') === 'leppa'
reverse('hello') === 'olleh'
reverse('Greetings!') === '!sgniteerG'
'''

# def reverse(word):
#     new_string = ""
#     for i in word: 
#         new_string = i + new_string
#     return new_string

def reverse(string):
    return string[::-1]

print(reverse("hello"))