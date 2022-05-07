
# 674. Longest Continuous Increasing Subsequence

from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        max_length: int = 1
        local_length: int = 1
        
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                local_length += 1
            else:
                max_length = max(max_length, local_length)
                local_length = 1
                
        return max(max_length, local_length)