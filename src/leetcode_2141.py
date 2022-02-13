
# 2141. Maximum Running Time of N Computers

from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra: int = sum(batteries[:-n])
        batteries = batteries[-n:]

        prefix: int = 0
        for i, time in enumerate(batteries): 
            prefix += time
            if i + 1 < n and batteries[i + 1] * (i + 1) - prefix > extra:
                return (prefix + extra) // (i + 1)
                
        return (prefix + extra) // n


print(Solution().maxRunTime(2, [3, 3, 3]))