
# 371. Sum of Two Integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFF
        max_value = 1000
        
        while b != 0:
            
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = carry << 1
        
        
        if a > max_value:
            a = ~(a ^ mask)
        
        return a