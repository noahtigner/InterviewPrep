def quicksort(arr):
    # Average: O(nlogn)
    # Worst: O(n^2) in the case of bad pivots leading to one long branch
    # Space: O(1) in-place
    # Optimization: don't pass arr around internally

    def _quicksort(low, high):
        if low < high:
            partition_index = partition(low, high)
            _quicksort(low, partition_index-1)
            _quicksort(partition_index, high)

    def partition(low, high):
        pivot = arr[(high + low) // 2]
        while low <= high:
            # find element on left that should be on right
            while arr[low] < pivot:
                low += 1
            # find element on right that should be on left
            while arr[high] > pivot:
                high -= 1
            # swap elements, move left and right
            if low <= high:
                swap(low, high)
                low += 1
                high -= 1
        return low

    def swap(low, high):
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp

    _quicksort(0, len(arr) - 1)
    return arr

arr = [1, 2, 3, 4, 5, 44, 55, 22, 1, 55, 7]
print(quicksort(arr))
