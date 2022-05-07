
# 456. 132 Pattern

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        length: int = len(nums)
        
        if length < 3:
            return False
            
        minimums: List[int] = [0] * length
        stack: List[int] = []
        
        for i, num in enumerate(nums):
            if i == 0:
                minimums[i] = num
            else:
                minimums[i] = min(minimums[i - 1], num)
        
        
        for i in range(length - 1, 0, -1):
            
            while stack and stack[-1] <= minimums[i]:
                stack.pop()
            
            if not stack or nums[i] <= stack[-1]:
                stack.append(nums[i])
                continue
            
            return True
        
        return False