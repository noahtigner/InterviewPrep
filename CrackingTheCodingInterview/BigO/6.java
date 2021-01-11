// the following code computes the (integer) square root of a number.
// If the number is not a perfect square (ther is no int sqrt), then it returns -1.
// It does this by trying increasingly large numbers until it finds the right value (or is too high).
// What is its runtime?

int sqrt(int n) {
    for(guess = 1; guess * guess <= n; guess++) {
        if(guess * guess == n) {
            return guess;
        }
    }
    return -1;
}

// O(sqrt n)
// This will loop while guess^2<=n, or sqrt(n) times