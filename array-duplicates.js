// Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

// You must write an algorithm that runs in O(n) time and uses only constant extra space.

var findDuplicates = function(nums) {
    
    let numbers = [];
    let duplicates = [];
    
    for(let i=0; i<nums.length; i++) {
        let num = nums[i];
        if(!numbers[num] ) {
            numbers[num] = num;
        } else {
            duplicates.push(num);
        }
    }
    return duplicates;
};