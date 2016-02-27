def unique_in_order(iterable):
    answer = []
    for i in iterable:
        if len(answer) < 1 or answer[-1] != i:
            answer.append(i)
    return answer