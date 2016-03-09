def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if not num % i: return False
    return True

prime = memoize(is_prime)

class Primes:
    @staticmethod
    def first(n):
        if n < 6:
            primes = [2, 3, 5, 7, 11]
            return primes[:n]
        primes = [2]
        no_primes = 1
        test_num = 3
        while no_primes < n:
            if prime(test_num):
                primes.append(test_num)
                no_primes += 1
            test_num += 2

        return primes
