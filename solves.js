/*  # 1
Most effecient way to guess a random number in a range:

You are given a range of values, and you must write an algorithm to guess a random number in the range in the most effecient way possible.

After every time you guess, you're told if you're right, too high, or too low.  */

const binarysearch = (arr, target) => {
    let iterations = 0
    // define some indices
    let low = 0
    let high = arr.length - 1
    
    while (low <= high) {
        iterations++
        let middle = Math.floor((low + high) / 2)
        // check if target is greater than arr at middle index
        if (arr[middle] === target) {
          return {index: middle, iterations: iterations}  
        } else if (arr[middle] < target) {
            // if true move window to right side
            low = middle + 1            
        } else { // move window to the left side
            high = middle - 1
        }
    }
    return {index: -1, iterations: iterations}
}

const arr = [1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

console.log("# 1. ", binarysearch(arr, 1))


/*  # 2
Write an algorithm to flatten a multi-dimensional array:    */

const flattener = (arr) => {
    let iterations = 0
    let newArr = []
    // outer loop to iterate through outer array
    for (let subArr of arr) {
        // inner loop to iterate through each element in subArr
        for (let ele of subArr) {
            // add each element to new array
            newArr.push(ele)
            iterations++
        }
    }
    return {newArr: newArr, iterations: iterations}
}

console.log("# 2. ", flattener([[1,2,3], [4,5,6], [7,8,9]]))