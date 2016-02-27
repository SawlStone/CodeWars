def namelist(names):
    names_list = [i['name'] for i in names]

    if len(names_list) <= 1: return ''.join(names_list)
    if len(names_list) == 2: return ' & '.join(names_list[-2:])
    return "".join(', '.join([n for n in names_list[:-2]]) + ", " + ' & '.join(names_list[-2:]))