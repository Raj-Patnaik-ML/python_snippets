def binary_search(arr, low, high, el):
    if low > high:
        return -1

    mid = (low + high) // 2

    if el == arr[mid]:
        return mid
    elif el < arr[mid]:
        return binary_search(arr, low, mid-1, el)
    else:
        return binary_search(arr, mid+1, high, el)


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, 4]
    find = 2
    print(arr)
    idx = binary_search(arr, 0, len(arr)-1, find)
    if idx == -1:
        print(f'Element {find} not found')
    else:
        print(f'Element {find} found at {idx}')
