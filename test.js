// let word1 = ["ab", "c"]
// let word2 = ["a", "bc"]

// var arrayStringsAreEqual = function(word1, word2) {
//     let combinedWord1 = []
//     let combinedWord2 = []
//     for (let i = 0; i < word1.length; i++) {
//         combinedWord1 += word1[i]
//     }
//     for (let i = 0; i < word2.length; i++) {
//         combinedWord2 += word2[i]
//     }
//     if (combinedWord1 === combinedWord2) {
//         return true
//     } else {
//         return false
//     }
// };
// nums = [4,3,2,7,8,2,3,1]

// var findDuplicates = function(nums) {
    
//     let numbers = [];
//     let duplicates = [];
    
//     for(let i=0; i<nums.length; i++) {
//         let num = nums[i];
//         if(!numbers[num] ) {
//             numbers[num] = num;
//             console.log(numbers[num])
//         } else {
//             duplicates.push(num);
//         }
//     }
//     return duplicates;
// };

// console.log(findDuplicates(nums))

// Days of the Week Problem
// 30 % 7 

// const daysOfWeek = (days) => {
//     let day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
//     let amountOfDays = days % 7
//     let futureDay = day[i+amountOfDays]
//     return futureDay
// }
// console.log(daysOfWeek(day[1], 9))
function dayOfWeek(day, k) {
    const days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    ];
    const index = days.indexOf(day);
    return days[(index + k) % 7];
}

console.log(dayOfWeek("Monday", 24))