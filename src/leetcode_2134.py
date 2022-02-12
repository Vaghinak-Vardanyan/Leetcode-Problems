
# 2134. Minimum Swaps to Group All 1's Together II

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length = len(nums)
        ones: int = sum(nums)
        ones_window_max: int = 0
        ones_window_current: int = 0
        nums_doubled = [nums[i % length] for i in range(2 * length)]

        for i in range(2 * length):
            if ones <= i and nums_doubled[i - ones]:
                ones_window_current -= 1
            
            if nums_doubled[i]:
                ones_window_current += 1
            
            ones_window_max = max(ones_window_max, ones_window_current)
        
        return ones - ones_window_max

print(Solution().minSwaps([0,1,0,1,1,0,0]))