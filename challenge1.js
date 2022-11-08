// # Leetcode- Medium

// # 17. Letter Combinations of a Phone Number

// # Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

// # A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

const prompt = require('prompt-sync')();

const input = prompt('numbers using digits from 2-9: ');

function phoneLetters (input) {
    let letters = {
        "2" : ["a", "b", "c"],
        "3" : ["d", "e", "f"],
        "4" : ["g", "h", "i"],
        "5" : ["j", "k", "l"],
        "6" : ["m", "n", "o"],
        "7" : ["p", "q", "r", "s"],
        "8" : ["t", "u", "v"],
        "9" : ["w", "x", "y", "z"]
    }

    if (input.length === 0) {
        return []
    }

    let comboArr = []
    const getLetters = [...input].forEach(digit => {
        letters[digit].forEach(letter => {
            comboArr.push(letter)
        })
    })

    const str = comboArr.join('')

    let combinations = (str) => {
        let output = []
        let index = 0
        while (index < str.length) {
            let char = str.charAt(index)
            let x;
            let arrTemp = [char]
            for (x in output) {
                arrTemp.push("" + output[x] + char)
                console.log(arrTemp)
            }
            output = output.concat(arrTemp)
            index++
        }

        // return console.log(output)
    }
    
    combinations(str)



}
phoneLetters(input)