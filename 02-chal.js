// Directions:
// Given a string, return true if the string is a palindrome
// or false if it is not. Palindromes are strings that
// form the same word if it is reversed. Do include spaces
// and punctuation in determining if the string is a palindrome.

// Examples:

// ```
// palindrome("abba") === true
// palindrome("abcdefg") === false
// ```

function palindrome(str) {
  const reversed = str.split('').reverse().join('');
  return str === reversed;
}

console.log(palindrome("abba")); // Outputs: true
console.log(palindrome("abcdefg")); // Outputs: false
console.log(palindrome("A man, a plan, a canal: Panama")); // Outputs: false
