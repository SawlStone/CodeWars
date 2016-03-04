def abundant_number(num):
    n = 1
    L = []
    while n < num:
        if num % n == 0:
            L.append(n)
        n += 1
    res = sum(i for i in L)
    if res < num:    return "deficient "
    elif res > num:  return "abundant "
    else:            return "perfect "


def amicable_numbers(n1, n2):
    def ab_num1(num):
        n = 1
        L = []
        while n < num:
            if num % n == 0:
                L.append(n)
            n += 1
        return sum(i for i in L)
    return "amicable" if ab_num1(n1) == n2 and ab_num1(n2) == n1 else "not amicable"


def deficiently_abundant_amicable_numbers(n1, n2):
    num1 = str(abundant_number(n1))
    num2 = str(abundant_number(n2))
    num3 = str(amicable_numbers(n1, n2))
    return num1 + num2 + num3