def group_check(s):
    s_length = len(s) + 1

    while len(s) < s_length:
        s_length = len(s)
        s = s.replace('()', '').replace('{}', '').replace('[]', '')

    if len(s) <= 0 or s == "": return True
    return False