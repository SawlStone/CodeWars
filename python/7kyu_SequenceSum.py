def sum_of_n(n):
    result = []
    x = 0
    for i in range(abs(n) + 1):
        x += i if n >= 0 else -i
        result.append(x)
    return result