// Implement a method to perform basic string compression using the counts of repeated characters.
// For example, the string "aabcccccaaa" would become "a2b1c5a3".
// If the compressed string would not become smaller than the original string, 
// your method should return the original string.
// Assume only uppercase and lowercase letters (a-z).

// Simple
// time: O(n), space: O(n)
function  stringCompression1(string) {
	let cmp = "";
    let count = 1;
    let prev = string[0];
    for(let i = 1; i < string.length; i++) {
        if(string[i] === prev) {
            count++;
        }
        else {
            cmp += prev;
            cmp += count.toString();
            count = 1;
            if(cmp.length >= string.length) {
                return string;
            }
        }
        prev = string[i];
    }
    cmp += prev;
    cmp += count.toString();
    
    return cmp.length < string.length ? cmp : string;
}