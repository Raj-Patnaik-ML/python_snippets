def quick_sort(arr, lo, hi):
    if lo >= hi:
        return

    pivot = arr[lo]
    i = lo - 1
    j = hi + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    quick_sort(arr, lo, j)
    quick_sort(arr, j + 1, hi)


if __name__ == '__main__':
    arr = [4, 7, 3, 3, 6, 4, 2, 0, 2, 2, 1]
    # arr = [1, 0, 1, 0, 1, 1, 0]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
