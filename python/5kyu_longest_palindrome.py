def longest_palindrome(s):
    L = []
    for i in range(len(s)):
        for j in range(0, i):
            item = s[j:i + 1]
            if item == item[::-1]:
                L.append(item)
    if s == '': return 0
    return 1 if len(L) < 1 else max(len(i) for i in L)