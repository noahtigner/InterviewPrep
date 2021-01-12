// Write a method to replace all spaces in a string with '%20'. 
// You may assume that the string has sufficientspace at the end to hold the additional characters,
// and that you are given the "true" length.

// Input: "Mr John Smith   ", 13
// Output: "Mr%20John%20Smith"

// Simple
// time: O(n), space: O(n)
function URLify(string, length) {
	let out = "";
    for(let i = 0; i < string.length; i++) {
        if(string[i] === ' ' && length > 0) {
            out += '%20';
            length = length - 1;
        }
        else if(length > 0) {
            out += string[i];
            length = length - 1;
        }
    }
    return out;
}