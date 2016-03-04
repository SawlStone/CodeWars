def abundant_number(num):
    n = 1
    L = []
    while n < num:
        if num % n == 0:
            L.append(n)
        n += 1
    return False if sum(i for i in L) < num else True