# Directions: Given a string, return a new string with the reversed order of characters
# Examples
# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'

my_string = 'zion'

def reverse(string): 
    reversed_string = ''
    for char in range(len(string)):
        reversed_string = string[char] + reversed_string
        # print(reversed_string)
    return reversed_string

print(reverse(my_string))