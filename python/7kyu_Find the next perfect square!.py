def find_next_square(sq):
    if sq < 0:
        return False
    else:
        import math
        tr = math.sqrt(sq)
        if tr == int(tr):
            res = sq + 2 * math.sqrt(sq) + 1
            return res
        else:
            return -1