// the following code computes the product of a and b. What is its runtime?

int product(int a, int b) {
    int sum = 0;
    for(int i = 0; i < b; i++) {
        sum += a;
    }
    return sum;
}

// O(b)
// linear time because we iterate over b and do constant work each time