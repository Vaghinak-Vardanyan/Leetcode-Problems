
# 1675. Minimize Deviation in Array

from typing import List 
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maximum: int = -1
        minimum: int = 1000000000

        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] *= 2

            maximum = max(maximum, nums[i])
            minimum = min(minimum, nums[i])
            nums[i] = -nums[i]
        
        heapq.heapify(nums)

        difference: int = maximum - minimum

        while nums[0] % 2 == 0:

            top = -heapq.heappop(nums)
            difference = min(top - minimum, difference)
            top //= 2
            minimum = min(top, minimum)
            heapq.heappush(nums, -top)

        return min(difference, -nums[0] - minimum)


print(Solution().minimumDeviation([4,1,5,20,3]))
print(Solution().minimumDeviation([1,2,3,4]))
