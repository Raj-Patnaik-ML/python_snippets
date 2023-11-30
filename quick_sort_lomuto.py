# def quick_sort(lst, l, h):
#     if l >= h:
#         return
#
#     pivot = lst[h]
#     curr_mid = l
#
#     for i in range(l, h):
#         if lst[i] < pivot:
#             lst[curr_mid], lst[i] = lst[i], lst[curr_mid]
#             curr_mid += 1
#     lst[curr_mid], lst[h] = lst[h], lst[curr_mid]
#
#     quick_sort(lst, l, curr_mid-1)
#     quick_sort(lst, curr_mid+1, h)
#
#
# if __name__ == '__main__':
#     arr = [1, 2]
#     print(arr)
#     quick_sort(arr, 0, len(arr) - 1)
#     print(arr)


def quick_sort(lst):
    if not lst:
        return lst

    pivot = lst[-1]

    left = list()
    right = list()

    for el in lst[:-1]:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    arr = [4, 7, 3, 2, 6, 4, 0, 3, 6, 1, 9]
    print(arr)
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
