// # Complete a method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

// # Examples
// # "the-stealth-warrior" gets converted to "theStealthWarrior"
// # "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

const prompt = require('prompt-sync')();

const str = prompt('String with - and/or _: ');

function camelCasing (str) {
    let arr = []
    // iterate and find -_
    for (i=0; i < str.length; i++) {
        if (str[i] === '-' || str[i] === '_') {
            if (str[i+1] === '-' || str[i+1] === '_') {
                continue
            } else if (i === str.length -1){
                continue
            } else {                
                let to_cap = str[i+1]
                let char = to_cap.toUpperCase()
                arr.push(char)
                i++
            }
            
        } else {
            arr.push(str[i])
        }
    }

    let output = arr.join("")
    console.log(output)
}

camelCasing(str)

