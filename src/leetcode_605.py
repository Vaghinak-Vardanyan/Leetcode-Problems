
# 605. Can Place Flowers

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if self.isFreeAndIsolated(i, flowerbed):
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
    
        
    def isFreeAndIsolated(self, index, flowerbed: List[int]):
        if flowerbed[index]:
            return False
        
        if index > 0 and flowerbed[index - 1]:
            return False
        
        if index < len(flowerbed) - 1 and flowerbed[index + 1]:
            return False
        
        return True
            