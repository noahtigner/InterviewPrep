// The following code sums the digits in a number.
// What is the Big O time?

int sumDigits(int remaining) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// O(digits)
// the loop will occur for every digit in the number
// alternatively, O(log n), since n=10^digits, so digits = log n