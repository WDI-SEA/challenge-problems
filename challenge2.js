// # From Git-repo

// # Direction:
// # Given an amount of change, determine the minimum number of coins required to make that change
// # Examples:

// # greedy(65) --> 4 `(2 quarters, 1 dime, 1 nickle)`
// # greedy(5) --> 1 `(1 nickle)`

const prompt = require('prompt-sync')();

const change = prompt('Amount of change: ');

function coinsNeeded (change) {
    let quarters;
    let dimes;
    let nickles;
    let pennies
    // get divisision and remainder to keep going down
    quarters = Math.floor(change/25)
    change = change - (quarters * 25)

    dimes = Math.floor(change/10)
    change = change - (dimes * 10)

    nickles = Math.floor(change/5)
    change = change - (nickles * 5)

    pennies = change

    let msg1 = quarters ? `${quarters} quarters` : ''
    let msg2 = dimes ? `${dimes} dimes` : ''
    let msg3 = nickles ? `${nickles} nickles` : ''
    let msg4 = pennies ? `${pennies} pennies` : ''

    console.log(msg1, msg2, msg3, msg4)


}

coinsNeeded(change)