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
