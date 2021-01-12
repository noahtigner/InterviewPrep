// Given a string, write a function to check if its a permutation of a palindrome.
// A palindrom is a word or phrase that is the same forwards as backwards.
// A permutation is a rearrangement of letters.
// The palindrom does not need to be limited to just dictionary words.
// You can ignore casing and non-letter characters

// We know:
// - must have even number of all characters,
// - except for (possibly) one
// - ignore whitespace & special characters

// Simple
// time: O(n), space: O(n)
function palindromePermutation1(string) {
	let counts = {};
    for(let i = 0; i < string.length; i++) {
        if(string[i] in counts) {
            counts[string[i]]++;
        }
        else {
            counts[string[i]] = 1;
        }
    }
    let odds = 0;
    for(let key of Object.keys(counts)) {
        if(key !== ' ' & counts[key] % 2 == 1) {
            if(odds === 1) {
                return false;
            }
        odds++;
        }
    }
    return true;
}

// Optimization
// time: O(n), space: O(1)
function palindromePermutation2(string) {
	let counts = new Array(26).fill(0);
	for(let i = 0; i < string.length; i++) {
        let lower = string[i].toLowerCase().charCodeAt() - 97;
        if(lower >= 0 & lower < 26) {
            counts[lower]++;
        }
    }
    let odds = 0;
    for(let j = 0; j < 26; j++) {
        if(counts[j] % 2 === 1) {
            odds++;
        }
    }
    return odds <= 1; 
}