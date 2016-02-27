# optimized solution

def presses(phrase):
    keypads_dict = [
        '1', 'ABC2', 'DEF3',
        'GHI4', 'JKL5', 'MNO6',
        'PQRS7', 'TUV8', 'WXYZ9',
        '*', ' 0', '#'
    ]

    return sum(1 + n.index(j) for n in keypads_dict for j in phrase.upper() if j in n)

# first solution

def presses(phrase):
    result = []
    keypads_dict = {
        tuple('1'): 1, tuple('ABC2'): 2, tuple('DEF3'): 3, tuple('GHI4'): 4,
        tuple('JKL5'): 5, tuple('MNO6'): 6, tuple('PQRS7'): 7, tuple('TUV8'): 8,
        tuple('WXYZ9'): 9, tuple('*'): 10, tuple(' 0'): 11, tuple('#'): 12
    }
    keypads_list = [i.upper() for i in phrase]
    for n in keypads_dict.keys():
        for i in keypads_list:
            if i in n:
                result.append(n.index(i) + 1)
    return sum(result)