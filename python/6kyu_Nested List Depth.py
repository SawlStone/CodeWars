def list_depth(l):
    result = []
    for i in l:
        if type(i) == list:
            result.append(list_depth(i))
    if len(result) > 0:
        return 1 + max(result)
    return 1


# A nested list is a list that apears as a value inside another list,
# [item, item, [item, item], item]
# in the above list, [item, item] is a nested list.



# list_depth([True])
# return 1

# list_depth([])
# return 1

# list_depth([2, "yes", [True, False]])
# return 2

# list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
# return 6

# list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
# return 2