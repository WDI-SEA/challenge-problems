var getConcatenation = function(nums) {
 return nums.concat(nums)
    
};c



var getConcatenation = function(nums) {
    let len = nums.length;
    for(let i=0; i<len; i++){
        nums.push(nums[i]);
    }
    return nums;
};