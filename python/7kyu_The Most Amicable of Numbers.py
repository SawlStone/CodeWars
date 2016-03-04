def abundant_number(num):
    n = 1
    L = []
    while n < num:
        if num % n == 0:
            L.append(n)
        n += 1
    return sum(i for i in L)


def amicable_numbers(n1, n2):
    return True if abundant_number(n1) == n2 and abundant_number(n2) == n1 else False