# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
nums = [2,2,111,4,4]
def singleNumber(nums):
    num = {}
    for i in nums:
        if i not in num:
            num[i]=1
        else:
            num[i]=i+1
    for i in num:
        if num[i] == 1:
            return i
        

print(singleNumber(nums))
