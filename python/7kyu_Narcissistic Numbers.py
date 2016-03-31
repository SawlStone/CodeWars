def is_narcissistic(i):
    return True if sum(int(n)**len(str(i)) for n in list(str(i))) == i else False