
# 189. Rotate Array

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        left: int = 0
        right: int = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left = 0
        right = k - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left = k
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            

nums: List[int] = [1,2,3,4,5,6,7]
k: int = 3
Solution().rotate(nums, 3)
print(nums)
