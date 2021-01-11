// the following code computes a^b. What is its runtime?

int power(int a, int b) {
    if(b < 0) {
        return 0; // error
    } else if(b == 0) {
        return 1;
    } else {
        return a * power(a, b - 1);
    }
}

// O(b)
// linear time because we will recursively call power b times and perform constant work each time