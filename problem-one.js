// did this problem on leetcode: https://leetcode.com/problems/valid-anagram/

// initial solution:

const isAnagram = function (s, t) {
    const sDictionary = {}
    const tDictionary = {}
    for (const letter of s) {
        if (!sDictionary[letter]) {
            sDictionary[letter] = 1
        } else {
            sDictionary[letter]++
        }
    }
    for (const letter of t) {
        if (!tDictionary[letter]) {
            tDictionary[letter] = 1
        } else {
            tDictionary[letter]++
        }
    }

    for (const letter of s) {
        if (sDictionary[letter] !== tDictionary[letter]) {
            return false
        }
    }

    for (const letter of t) {
        if (tDictionary[letter] !== sDictionary[letter]) {
            return false
        }
    }
    return true
}

// second attempt after looking at a hint:

const isAnagramB = function (s, t) {
    const dictionary = {}
    for (const letter of s) {
        if (!dictionary[letter]) {
            dictionary[letter] = 1
        } else {
            dictionary[letter]++
        }
    }
    for (const letter of t) {
        if (!dictionary[letter]) {
            return false
        } else {
            dictionary[letter]--
        }
    }

    for (const key in dictionary) {
        if (dictionary[key] !== 0) {
            return false
        }
    }

    return true
}
