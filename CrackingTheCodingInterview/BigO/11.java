// The following code prints all strings of length k where the characters are in sorted order.
// It does this by generating all strings of length k and then checking if each is sorted.
// What is the runtime?

void printSortedStrings(int remaining) {
    printSortedStrings(remaining, "");
}

void printSortedStrings(int remaining, String prefix) {
    if(remaining == 0) {
        if(isInOrder(prefix)) {
            System.out.println(prefix);
        }
    } else {
        for(char c = 'a'; c <= 'z'; c++) {
            printSortedStrings(remaining - 1, prefix + c);
        }
    }
}

boolean isInOrder(String s) {
    boolean isInOrder = true;
    for(int i = 1; i < s.length(); i++) {
        int prev = ithLetter(s.charAt(i - 1));
        int curr = ithLetter(s.charAt(i));
        if(prev > curr) {
            return false;
        }
    }
    return true;
}

// O(kc^k)
// k = s.lenght()
// c = chars in alphabet (27)
// isInOrder() : O(k) to check if each string is sorted
// O(c^k) to generate each string