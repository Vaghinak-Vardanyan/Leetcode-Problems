
# 665. Non-decreasing Array

from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        length: int = len(nums)
        is_modified: bool = False
            
        for i in range(1, length):
            if nums[i] < nums[i - 1]:
                if is_modified:
                    return False
                
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                    
                is_modified = True
        
        return True