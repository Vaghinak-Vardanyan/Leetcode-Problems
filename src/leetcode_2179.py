
# 2179. Count Good Triplets in an Array

from typing import List
from typing import Optional

class FenwickTree:
    
    def __init__(self, n: int, fill: Optional[int] = None) -> None:
        self.length = n
        self.bit: List[int] = [0] * self.length
        if fill:
            for i in range(self.length):
                self.add(i, fill)


    def prefix_sum(self, right: int) -> int:
        result: int = 0
        while right >= 0:
            result += self.bit[right]
            right = (right & (right + 1)) - 1

        return result


    def query(self, left: int, right: int) -> int:
        if left > 0:
            return self.prefix_sum(right) - self.prefix_sum(left - 1)

        return self.prefix_sum(right)


    def add(self, index: int, delta: int) -> None:
        while index < self.length:
            self.bit[index] += delta
            index = index | (index + 1) 



class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        result: int = 0
        length: int = len(nums1)
        nums1_reversed: List[int] = [0] * length
        indices: List[int] = [0] * length

        for i, num in enumerate(nums1):
            nums1_reversed[num] = i

        for i, num in enumerate(nums2):
            indices[i] = nums1_reversed[nums2[i]]

        left_smallers: FenwickTree = FenwickTree(length)
        right_largers: FenwickTree = FenwickTree(length, 1)

        for i in indices:
            if 0 < i < length - 1:
                smaller_count = left_smallers.query(0, i - 1)
                right_count = right_largers.query(i + 1, length - 1)
                result += smaller_count * right_count  

            left_smallers.add(i, 1)
            right_largers.add(i, -1)

        return result


print(Solution().goodTriplets(nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]))