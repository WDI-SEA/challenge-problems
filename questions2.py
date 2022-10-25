
# EASY

# class Solution:
# def moveZeroes(self, nums) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     prev = 0
#     for i in range(0, len(nums)):
#         if nums[i] != 0 and nums[prev] == 0:
#             nums[prev], nums[i] = nums[i], nums[prev]
#         if nums[prev] != 0:
#             prev += 1
#     return print(nums)

# nums = [0,1,0,3,12]
# print(moveZeroes(nums))

# # Link: https://leetcode.com/problems/move-zeroes/


########################################################
########################################################

#EASY 
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
#         word1 = ''.join(word1)
#         word2 = ''.join(word2)
#         if word1 == word2:
#             return True
#         else:
#             return False

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]

# Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

# EASY 
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res, stack = [], [(root, False)]
#         while stack:
#             node, visited = stack.pop()  # the last element
#             if node:
#                 if visited:
#                     res.append(node.val)
#                 else:  # inorder: left -> root -> right
#                     stack.append((node.right, False))
#                     stack.append((node, True))
#                     stack.append((node.left, False))
#         return res

# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/