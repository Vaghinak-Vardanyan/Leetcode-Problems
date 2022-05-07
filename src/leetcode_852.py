
# 852. Peak Index in a Mountain Array

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        length: int = len(arr)
        low: int = 0
        high: int = length - 1
        index: int = 0
        
        while low < high:
            index = (high + low) // 2
            
            if index + 1 < length and arr[index] < arr[index + 1]:
                low = index + 1
            else:
                high = index
        
        return low
            