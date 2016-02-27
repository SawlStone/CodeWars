def is_monotone(heights):
    if not heights:
        return True
    for x in range(len(heights)):
        return True if len(heights) <= 1 or float(heights[x]) <= float(heights[x + 1]) else False