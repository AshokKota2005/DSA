import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 0
        primes = [1] * n
        for i in range(2,math.ceil(math.sqrt(n))+1):
            if primes[i] == 1:
                for j in range(i*i,n,i):
                    primes[j] = 0
        primes[0] = 0
        primes[1] = 0 
        return primes.count(1)

        