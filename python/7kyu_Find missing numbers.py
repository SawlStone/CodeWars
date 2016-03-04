def find_missing_numbers(arr):
    if arr == []: return []
    n, k = arr[0], arr[-1]
    rsl = []
    while n < k:
        n += 1
        rsl.append(n)
    res = []
    for i in rsl:
        if i not in arr:
            res.append(i)
    return res