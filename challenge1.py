# https://leetcode.com/problems/root-equals-sum-of-children/
# You are given the root of a binary tree that consists of exactly 3 nodes: 
# the root, its left child, and its right child.

# Return True if the value of the root is equal 
# to the sum of the values of its two children, or false otherwise.

root = [5, 3, 4]


def TreeNode(string, mid = None, low = 0, high = None):
    sorted_root = sorted(string)
    high = sorted_root[len(sorted_root) - 1]
    low = sorted_root[low]
    mid = sorted_root[int(len(sorted_root)/2)]
    print(f'High: {high}')
    print(f'Low: {low}')
    print(f'Mid: {mid}')
    if high == mid + low:
        print(f'{high} = {mid} + {low}')
        return True
    else:
        print(f'{high} != {mid} + {low}')
        return False
#Find a way to sort the array from lowest to highest,
#Set the highest to the sum of the other numbers
# if the two numbers added equal the sum, return true -- otherwise false

print(TreeNode(root))