// the following code computes a % b. What is its runtime?

int mod(int a, int b) {
    if(b <= 0) {
        return -1;  // error
    }
    int div = a / b;
    return a - div * b;
}

// O(1)
// constant time (no recursion or looping)