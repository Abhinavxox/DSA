def quickSort(arr):
    if len(arr) <= 1:
        return arr

    left = 0
    right = len(arr) - 1
    m = (left + right) // 2

    pivot = arr[m]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr = swap(arr, left, right)
            left += 1
            right -= 1

    left_part = quickSort(arr[:left])
    right_part = quickSort(arr[left:])

    return left_part + right_part


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


arr = [23, 12, 45, 34, 56]
sorted_arr = quickSort(arr)
print(sorted_arr)
