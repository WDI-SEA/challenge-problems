https://dev.to/seanpgallivan/solution-running-sum-of-1d-array-34na

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


	nums = [1,2,3,4]
    output = [1,3,6,10]

    Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


    nums = [1,1,1,1,1]
    output = 	[1,2,3,4,5]

JavaScript
    var runningSum = function(nums) {
    let ans = new Array(nums.length)
    ans[0] = nums[0]
    for (let i = 1; i < nums.length; i++)
        ans[i] = ans[i-1] + nums[i]
    return ans
};

Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] + nums[i]
        return ans