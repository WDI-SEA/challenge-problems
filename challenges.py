# PALINDROME TEST

string = input('Enter a string: >')
def reverse_string(string):
    new_string = ''
    index = len(string)
    while index:
        index -=1
        new_string += string[index]
    return new_string

# print(reverse_string(string))

def palindrome_test(string):
    if reverse_string(string) == string:
        return True
    else:
        return False

print(palindrome_test(string))



# HIGHEST AND LOWEST

def highest_lowest(nums):
    if nums:
        nums = nums.split(' ')
        high_num = nums[0]
        low_num = nums[0]
        for num in nums:
            if int(num) > int(high_num):
                high_num = num
            if int(num) < int(low_num):
                low_num = num
        return f'high: {high_num} low {low_num}'

print(highest_lowest('1 5 6 9 100'))






