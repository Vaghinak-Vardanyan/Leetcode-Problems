
# 2177. Find Three Consecutive Integers That Sum to a Given Number

from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        remainder: int = num % 3
        quotient: int = num // 3
        if remainder == 0:
            return [quotient - 1, quotient, quotient + 1]

        return []


print(Solution().sumOfThree(5871158))