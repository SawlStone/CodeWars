def is_square(n):
    if n < 0:
        return False
    else:
        import math
        sq = math.sqrt(n)
        if sq == int(sq):
            return True
        else: 
            return False