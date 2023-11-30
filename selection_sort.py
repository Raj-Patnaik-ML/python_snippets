def selection_sort(arr):
    for idx, el in enumerate(arr):
        min_el = el
        min_idx = idx
        for cmp_idx, cmp_el in enumerate(arr[idx:]):
            if cmp_el < min_el:
                min_el = cmp_el
                min_idx = cmp_idx

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]


if __name__ == '__main__':
    arr = [2, 4, 3, 0, 1]
    print(arr)
    selection_sort(arr)
    print(arr)
