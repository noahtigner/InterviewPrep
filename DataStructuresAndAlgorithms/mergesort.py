def mergesort(arr):
    def _mergesort(helper, low, high):
        if low < high:
            middle = (low + high) // 2
            _mergesort(helper, low, middle)
            _mergesort(helper, middle + 1, high)
            merge(helper, low, middle, high)

    def merge(helper, low, middle, high):
        for i in range(low, high + 1):
            helper[i] = arr[i]

        left = low
        right = middle + 1
        curr = low

        # Iterate through helper array. Compare left and right half, copying back
        # the smaller element into the original array
        while left <= middle and right <= high:
            if helper[left] <= helper[right]:
                arr[curr] = helper[left]
                left += 1
            else:
                arr[curr] = helper[right]
                right += 1
            curr += 1
        # Copy the rest of the left side of the array into the original array
        remaining = middle - left
        for i in range(remaining + 1):
            arr[curr + i] = helper[left + i]

    helper = [0 for _ in range(len(arr))]
    _mergesort(helper, 0, len(arr) - 1)
    return arr

arr = [1, 2, 3, 4, 5, 44, 55, 22, 1, 55, 7]
print(mergesort(arr))

