# square sum . take the sq  of each of the num and add them together

from re import I
import string


def add_square(nums):
    list = []
    # square each num - num* num
    for num in nums:
        sq_num = num * num
        list.append(sq_num)
    # add that num square to square
    total = sum(list)
    return total



# print(add_square([1, 2, 3]))

def squared_sum(nums):
    return sum(num * num for num in nums)



# take a string and convert to camel case convert_to_camel
string = "convert_to_camel"

def to_camel_case(string):
# remove underscore
    new_string = string.replace("_", " ").replace("-", " ") 
# change to an array
    new_string = new_string.split()
    print(new_string)  
#convert that letter to caps
    return new_string[0] + "".join(i.capitalize() for i in new_string[1:])

print(to_camel_case(string))


def camel_case_convert(string):
    strang = string.replace('-', ' ').replace('_', ' ')
    strang = strang.split()
    print(strang)
    if len(string) == 0:
        return string
    print(strang[0])
    return strang[0] + ''.join(i.capitalize() for i in strang[1:])

# print(camel_case_convert("the_stealth_warrior"))