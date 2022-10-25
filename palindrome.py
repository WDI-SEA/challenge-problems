import string


def palindrome(str):
    str = str.lower()
    str_list = list(str)
    str_list.reverse()
    # rev_str = str[::-1]
    rev_string = ''.join(str_list)

    if str == rev_string:
        return 'PALINDROME!'
    else:
        return "not this time"
 
print(palindrome(''))


