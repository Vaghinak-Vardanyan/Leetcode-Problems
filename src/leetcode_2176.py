
# 2176. Count Equal and Divisible Pairs in an Array

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        result: int = 0
        length: int = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j] and i * j % k == 0:
                    result += 1

        return result


