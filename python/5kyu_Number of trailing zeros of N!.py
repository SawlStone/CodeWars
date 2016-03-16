# a program that will calculate the number of trailing zeros 
# in a factorial of a given number.
# N! = 1 * 2 * 3 * 4 ... N

def zeros(n):
    sum = 0
    while n > 0:
        sum += n / 5
        n /= 5
    return sum
	
# zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
# that has 2 trailing zeros 4790016(00)