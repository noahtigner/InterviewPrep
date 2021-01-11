// the following code computes the (integer) square root of a number.
// If the number is not a perfect square (there is no int square root), then it returns -1.
// It does this by successive guessing. If n is 100, it first guesses 50. Too high? Try something lower. Too low? Try something lower-halfway between 1 and 50.
// What is its runtime?

int sqrt(int n) {
    return sqrt_helper(n, 1, n);
}

int sqrt_helper(int n, int min, int max) {
    if(max < min) return -1; // no sqrt

    int guess = (min + max) / 2;
    if(guess * guess == n) {    // found it
        return guess;
    } else if(guess * guess < n) {  // too low
        return sqrt_helper(n, guess + 1, max);
    } else {    // too high
        return sqrt_helper(n, min, guess - 1);
    }
}

// O(log n)
// logarithmic because n shrinks in half with each call to sqrt_helper
// this is essentially binary search