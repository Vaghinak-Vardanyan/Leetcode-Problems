
# 136. Single Number

from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda accumulator, current: accumulator ^ current, nums, 0)


print(Solution().singleNumber([4,1,2,1,2]))