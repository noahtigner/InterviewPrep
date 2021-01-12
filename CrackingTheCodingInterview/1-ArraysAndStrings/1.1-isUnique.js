// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?

// Simple
// time: O(n), space: O(n)
function isUnique1(string) {
	let seen = [];
    for(let i = 0; i < string.length; i++) {
        if(seen.includes(string[i])) {
            return false;
        } 
        else {  
            seen.push(string[i])
        }
    }
    return true;
}

// Alternative: no extra data structures
// time: O(n^2), space: O(1)
function isUnique2(string) {
	for(let i = 0; i < string.length; i++) {
        for(let j = i + 1; j < string.length; j++) {
            if(string[i] === string[j]) {
                return false;
            }
        }
    }
    return true;
}

// Alternative: better time, worse space
// time: O(nlogn), space: O(n)
function isUnique3(string) {
	let sorted = string.split('').sort().join('');
    let prev = sorted.charAt(0);
    for(let i = 1; i < sorted.length; i++) {
  	    if(prev === sorted.charAt(i)) {
    	    return false;
        }
        prev = sorted.charAt(i);
    }
    return true;
}

// Optimization
// time: O(n), space: O(1)
function isUnique4(string) {
	let chars = new Array(256).fill(0);
    for(let i = 0; i < string.length; i++) {
  	    if(chars[string[i].charCodeAt()] === 1) {
    	    return false;
        }
  	    chars[string[i].charCodeAt()]++;
    }
    return true;
}