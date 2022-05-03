
# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        lookup_table: dict[int, bool] = dict()
        next_number: int
        
        while True:
            
            if n in lookup_table:
                return False
            
            lookup_table[n] = True
            next_number = 0
            
            while n:
                next_number += (n % 10) ** 2
                n //= 10
            
            n = next_number
            
            if n == 1:
                return True
                