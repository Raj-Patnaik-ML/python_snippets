def insertion_sort(arr):
    new_arr = [0] * len(arr)
    for el in arr:
        el_idx = 0
        for itr_el in arr:
            if el > itr_el:
                el_idx += 1
        new_arr[el_idx] = el

    return new_arr


if __name__ == '__main__':
    arr = [2, 8, 1, 3, 4, 0, 5]
    print(arr)
    new_arr = insertion_sort(arr)
    print(new_arr)
