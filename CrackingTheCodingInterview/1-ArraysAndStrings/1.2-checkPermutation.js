// Given two strings, write a method to decide if one is a permutation of the other

// Simple
// time: O(nlogn), space: O(n)
function checkPermutation1(a, b) {
	if(a.length !== b.length) {
        return false;
    }
    a_srtd = a.split('').sort().join();		// O(nlogn)
    b_srtd = b.split('').sort().join();
    for (let i = 0; i < a.length; i++) { // O(n)
        if (a_srtd[i] !== b_srtd[i]) {
            return false;
        }
    }
    return true;
}

// Optimization
// time: O(n), space: O(n)
function checkPermutation2(a, b) {
	if(a.length !== b.length) {
        return false;
    }
    a_hash = {}
    b_hash = {}
    for(let i = 0; i < a.length; i++) {
        if(a[i] in a_hash) {
            a_hash[a[i]]++;
        }
        else {
            a_hash[a[i]] = 0;
        }
        if(b[i] in b_hash) {
            b_hash[b[i]]++;
        }
        else {
            b_hash[b[i]] = 0;
        }
    }
    
    // compare objects: O(n)
    let a_keys = Object.keys(a_hash);
    let b_keys = Object.keys(b_hash);
    if(a_keys.length !== b_keys.length) {
        return false;
    }
    for(let key of a_keys) {
        if(a_hash[key] !== b_hash[key]) {
            return false;
        }
    }
    return true;
}