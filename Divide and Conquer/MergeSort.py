def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    return sort(left_half, right_half)


def sort(arr1, arr2):
    p1 = 0
    p2 = 0
    merged_arr = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged_arr.append(arr1[p1])
            p1 += 1
        else:
            merged_arr.append(arr2[p2])
            p2 += 1

    while p1 < len(arr1):
        merged_arr.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        merged_arr.append(arr2[p2])
        p2 += 1

    return merged_arr


arr = [23, 12, 45, 34, 56]
sorted_arr = mergeSort(arr)
print(sorted_arr)
