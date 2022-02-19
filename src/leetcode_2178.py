

from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2:
            return []

        if finalSum < 5:
            return [finalSum]

        result: List[int] = []
        current: int = 2
        current_sum: int = 0

        while current_sum < finalSum:
            result.append(current)
            current_sum += current
            current += 2

        if current_sum > finalSum:
            diff: int = current_sum - finalSum
            result.remove(diff)

        return result


print(Solution().maximumEvenSplit(28))