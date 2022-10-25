# Medium

# from collections import defaultdict

# # Input:
# strs = ["eat","tea","tan","ate","nat","bat"]    
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# GEEKFORGEEKS
# temp = defaultdict(list)
# for ele in strs:
#     temp[str(sorted(ele))].append(ele)
# res = list(temp.values())

# print(str(res))

#####################################################
#####################################################

# Easy

# Input:
list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

mergedlist = []

mergedlist.extend(list1)
mergedlist.extend(list2)
mergedlist.sort()

print(mergedlist)

# joinedlist = list1 + list2
# joinedlist.sort()
# print(joinedlist)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.root = self.val
        if TreeNode == 0:
            return print('nothing here')
        return:
            print(f'[{self.root.left}, {self.root.right}, {self.root.value}])
                  
list