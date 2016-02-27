def pattern(n):
    # Happy Coding ^_^
    res_list = ''.join([str(i) for i in reversed(range(n + 1)) if i > 0])
    result = ''
    for i in range(1, n + 1):
        result += '\n' if len(result) > 0 else ''
        result += res_list
        if len(str(i)) == 1:
            res_list = res_list[:-1]
        else:
            res_list = res_list[:-2]
    return result