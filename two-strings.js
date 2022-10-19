// Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

// A string is represented by an array if the array elements concatenated in order forms the string.

 

// Example 1:

// Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
// Output: true
// Explanation:
// word1 represents string "ab" + "c" -> "abc"
// word2 represents string "a" + "bc" -> "abc"
// The strings are the same, so return true.
// Example 2:

// Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
// Output: false
// Example 3:

// Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
// Output: true

let word1 = ["ab", "c"]
let word2 = ["a", "bc"]

var arrayStringsAreEqual = function(word1, word2) {
    let combinedWord1 = []
    let combinedWord2 = []
    for (let i = 0; i < word1.length; i++) {
        combinedWord1 += word1[i]
    }
    for (let i = 0; i < word2.length; i++) {
        combinedWord2 += word2[i]
    }
    if (combinedWord1 === combinedWord2) {
        return true
    } else {
        return false
    }
};

console.log(arrayStringsAreEqual(word1, word2))

// var arrayStringsAreEqual = function(word1, word2) {
//     return word1.join('') === word2.join('')
// };

// console.log(word1.join(""))

