# given a string return a a new string with reversed character
# reverse('apple') === 'leppa'
# reverse('hello') === 'olleh'
# reverse('Greetings!') === '!sgniteerG'

# using slice:



text = "apple"
print(text[::-1])


def reverse_for_loop(string):
    # set an empty array
    reveresed = " "
# loop through string
    for char in string:
        # set reverse to be the appends char in reverse 
        reveresed = char + reveresed
    return reveresed

reverse_for_loop("apple")

def reverse_while(string):
    # set empty string for reversed
    reversed = " "
    length = len(string)

    while length > 0:
        # reversed to the end of the string
        reversed += string[length -1]
        # decrement the length - cause if you don't you get an inifinite loop
        length = length -1
    return reversed

print(reverse_while("Hello!"))


# Implement a function unique_in_order that will take in an argument either a string or an array and return a list of elements without any elements with the same # values next to each other, but preserving the original order.
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(string):
    # need an array to store duplicates
    duplicates = " "
    # check len of the string
    # loop over string and check for duplicates
    # move duplicates to dup array
    # return array w/out duplicates
    for char in string:
        if char not in duplicates:
           duplicates = duplicates + char
    print(duplicates)            

unique_in_order('AAAABBBCCDAABBB')


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


string="abdndbwobf"
print(convert(string))
