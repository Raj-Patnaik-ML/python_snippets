from functools import reduce, wraps, cmp_to_key

arr = [3, 2, 1, 0, -1, -2, 4, -3]
res = reduce(lambda a1, a2: a1 + a2, arr)
print(res)

res = sorted(arr, key=lambda x: x)
print(res)

res = filter(lambda x: x < 0, arr)
print(list(res))

res = map(lambda x: sum(x), list(zip(arr, arr)))
print(list(res))
res = map(lambda x, y: x + y, arr, arr)
print(list(res))
