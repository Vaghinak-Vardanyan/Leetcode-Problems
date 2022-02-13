
# 78. Subsets

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]

        for number in nums:    
            result.extend([subset + [number] for subset in result])
            
        return result
        

print(Solution().subsets([1,2,3]))