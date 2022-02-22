
# 169. Majority Element

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote, majority = 1, nums[0]

        for n in nums[1:]:
            if vote == 0:
                majority = n
            
            vote += (1 if majority == n else -1)

        return majority


print(Solution().majorityElement([2, 2, 1, 5, 1, 2, 2]))