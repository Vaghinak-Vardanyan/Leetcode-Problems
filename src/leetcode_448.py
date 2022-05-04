
# 448. Find All Numbers Disappeared in an Array

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lookup_table: List[int] = [True] * len(nums)
            
        for number in nums:
            lookup_table[number - 1] = False
            
        return [index for index, not_found in enumerate(lookup_table, 1) if not_found]