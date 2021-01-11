// The following code computes the intersection (the number of elements in common) of two arrays.
// It assumes thait neither array has duplicates.
// It computes the intersection by sorting one array (array b) and then iterating through array a checking (via binary search)
// if each value is in b.
// What is its runtime?

int intersection(int[] a, int[] b) {
    mergesort(b);
    int intersect = 0;

    for(x : a) {
        if(binarySearch(b, x) >= 0) {
            intersect++;
        }
    }

    return intersect;
}

// O(blogb + alogb)
// mergesort : O(blogb)
// for x in a:
//  binarySearch : O(logb)
