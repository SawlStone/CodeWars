
def reverse_fun(n):
    L = [i for i in n]
    res = []
    while len(L) > 0:
        res.append(L.pop(-1))
        if not L:
            break
        res.append(L.pop(0))

    return ''.join(res)
	
	
# Test.describe("reverse_fun example testcases")
# Test.it("should work for even length")
# Test.assert_equals(reverse_fun('012345'), '504132')

# Test.it("should work for odd length too")
# Test.assert_equals(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')