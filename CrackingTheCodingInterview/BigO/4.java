// the following code performs integer division. Assume a and b are both positive.
// What is its runtime?

int div(int a, int b) {
    int count = 0;
    int sum = b;
    while(sum <= a) {
        sum += b;
        count++;
    }
    return count;
}

// O(a/b)
// div will loop as many times as (sum+b)<a, which corresponds to a/b