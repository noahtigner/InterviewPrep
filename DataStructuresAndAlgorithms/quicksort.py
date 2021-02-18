def quicksort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)
            _quicksort(arr, low, partition_index-1)
            _quicksort(arr, partition_index, high)

    def partition(arr, low, high):
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
                swap(arr, low, high)
                low += 1
                high -= 1
        return low

    def swap(arr, low, high):
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp

    _quicksort(arr, 0, len(arr) - 1)
    return arr

arr = [1, 2, 3, 4, 5, 44, 55, 22, 1, 55, 7]
print(quicksort(arr))
