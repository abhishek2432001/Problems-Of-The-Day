from math import floor, sqrt
from bisect import bisect

''' You are given a list of q queries and for every query, you are given an integer N.
  The task is to find how many numbers(less than or equal to N) have number of divisors exactly equal to 3.

Example 1:

Input:
q = 1
query[0] = 6
Output:
1
Explanation:
There is only one number 4 which has
exactly three divisors 1, 2 and 4 and
less than equal to 6.'''
def sieve(n):
        primes = [1] * (n + 1)
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = 0
            p += 1
        return primes
def threeDivisors(query, q):
	num = int(sqrt(max(query)))
	primes = sieve(num)
	primes = [i for i in range(len(primes)) if primes[i]][2:] # ignoring 0 and 1
	return [bisect(primes, sqrt(num)) for num in query]