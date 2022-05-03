
# 204. Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        
        result: int = 0
        sieve: list[bool] = [True] * n 
        current_prime: int = 2
        
        
        while current_prime * current_prime < n:
            
            if sieve[current_prime]:
                result += 1
                for i in range(current_prime * current_prime, n, current_prime):
                    sieve[i] = False
            
            current_prime += 1
        
        for i in range(current_prime, n):
            if sieve[i]:
                result += 1
        
        return result