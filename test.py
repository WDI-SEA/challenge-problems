

# def judgeCircle(moves):
#     """
#     :type moves: str
#     :rtype: bool
#     """
#     upCount = 0
#     downCount = 0
#     rightCount = 0
#     leftCount = 0
#     for i in moves:
#         if i == "U":
#             upCount += 1
#         elif i == "D":
#             downCount += 1
#         elif i == "R":
#             rightCount += 1
#         elif i == "L":
#             leftCount +=1
#     return leftCount == rightCount and upCount == downCount



# print(judgeCircle("UD"))
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