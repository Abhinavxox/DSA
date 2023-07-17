def binarySearch(arr, s, e, Number):
    if s > e:
        return False

    m = (s + e) // 2

    if arr[m] == Number:
        return True
    elif arr[m] < Number:
        return binarySearch(arr, m + 1, e, Number)
    else:
        return binarySearch(arr, s, m - 1, Number)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Number = 11
print(binarySearch(arr, 0, len(arr) - 1, Number))
