// There are two types of edits that can be performed on strings:
// insert a character, remove a character, or replace a character.
// Given two strings, write a function to check if they are one (or zero) edits away.

// Simple
// time: O(nlogn) space: O(n)
function oneAway1(a, b) {
    let diff = Math.abs(a.length - b.length);
    let min_length = Math.min(a.length, b.length);
    let edits = diff;
    
    if(edits > 1) {
        return false;
    }
    
    let a_srtd = a.split("").sort().join();	// O(nlogn)
    let b_srtd = b.split("").sort().join();
    for(let i = 0; i < min_length; i++) {
        if(a_srtd[i] !== b_srtd[i]) {
            edits++;
        }
    }
    return edits < 2;
}
  
// Optimization
// time: O(n), space: O(1)
function oneAway2(a, b) {
    let edits = 0;

    let as = new Array(256).fill(0);
    let bs = new Array(256).fill(0);
    for(let i = 0; i < a.length; i++) {
        as[a[i].charCodeAt()]++;
    }
    for(let i = 0; i < b.length; i++) {
        bs[b[i].charCodeAt()]++;
    }
    for(let i = 0; i < 256; i++) {
        if(as[i] !== bs[i]) {
            edits++;
        }
    }
    return edits < 2;
}