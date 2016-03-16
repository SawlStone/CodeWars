# 1 = anane
# 2 = adak


def count_arara(n):
    if n == 2: return "adak"
    return "adak " * int(n/2-1) + "adak" if n % 2 == 0 else "adak" * int(n/2) + "anane"

print(count_arara(10))