# An additive number is a string whose digits can form an additive sequence.

# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

# Given a string containing only digits, return true if it is an additive number or false otherwise.

# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

# Example 1:

# Input: "112358"
# Output: true
# Explanation: 
# The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

# Example 2:

# Input: "199100199"
# Output: true
# Explanation: 
# The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199




input = "45054104158"
def additive_num(input):
    nums = list(input)
    idx = 0
    first_one = int(nums[0]) + int(nums[1])
    first_two = int("".join(nums[0:2:])) + int(nums[2])
    first_three = int(nums[0]) + int("".join(nums[1:3:]))
    answer = 0
    if first_one == int(nums[2]):
        idx = 3
        answer = first_one
        prev = int(nums[1])
    elif first_two == int("".join(nums[3:3+len(str(first_two)):])):
        idx = 3+len(str(first_two))
        answer = first_two
        prev = int(nums[2])
        # print(f"second:{idx}")
    elif first_three == int("".join(nums[3:3+len(str(first_three)):])):
        idx = 3+len(str(first_three))
        answer = first_three
        prev = int("".join(nums[1:3:]))
        # print(f"third:{idx}")
    else:
        return False
    while idx < len(nums):
        new_answer = answer + prev
        if new_answer == int("".join(nums[idx:idx+len(str(new_answer)):])):
            idx = idx+len(str(new_answer))
            prev = answer
            answer = new_answer
        else:
            return False
    
    return True






print(additive_num(input))
    
    


