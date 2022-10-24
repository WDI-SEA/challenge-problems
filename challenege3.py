# take in a word or string, and reverse it

#PSUEDOCODE
# function that takes in a string, somehow maybe make it into an array
# and start printing from the end, until the index is 0

def reverse_string(string, index = None):
    list(string)
    index = len(string)
    if index == 0:
        return
    else:
        return string[index:0:-1] + string[0]
        


# print(reverse_string('string'))

def reverse(word):
    if len(word) == 0:
        return word
    else:
        print(word[0:])
        return reverse(word[1:]) + word[0]


print(reverse('string'))