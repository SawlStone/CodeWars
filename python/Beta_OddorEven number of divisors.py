def oddity(n):
    results = set()
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            results.add(i)
            results.add(n / i)
    if len(results) % 2 == 0:
        return 'even'
    else:
        return 'odd'

"""
def oddity(n):
    div_list = [x for x in range(1, n // 2 + 1) if n % x == 0]
    if (len(div_list) + 1) % 2 == 0:
        return 'even'
    else:
        return 'odd'
"""