
# 703. Kth Largest Element in a Stream

from typing import List

class Heap:
    
    def __init__(self, nums: List[int]):
        self._capacity: int = len(nums)
        self._size: int = self._capacity
        self._array: List[int] = nums
    
        for i in range(self._size // 2 - 1, -1, -1):
            self._heapify_up_bottom(i)
    
    
    def getLength(self) -> int:
        return self._size
    
    
    def getMin(self) -> int:
        assert self._size > 0
        return self._array[0]
    
    
    def add(self, val: int):
        if self._size == self._capacity:
            self._array.append(val)
            self._capacity += 1
            self._size += 1
        else:
            self._size += 1
            self._array[self._size - 1] = val
            
        self._heapify_bottom_up(self._size - 1)
        
    
    def removeMin(self):
        assert self._size > 0
        self._array[0] = self._array[self._size - 1]
        self._size -= 1
        self._heapify_up_bottom(0)
    
    
    def _heapify_bottom_up(self, index):
        parent = (index - 1) // 2
        
        if index > 0 and self._array[parent] > self._array[index]:
            self._array[parent], self._array[index] = self._array[index], self._array[parent]
            self._heapify_bottom_up(parent)
    
    
    def _heapify_up_bottom(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        
        min_index: int = index
        
        if left < self._size and self._array[left] < self._array[min_index]:
            min_index = left
            
        if right < self._size and self._array[right] < self._array[min_index]:
            min_index = right
        
        if min_index != index:
            self._array[index], self._array[min_index] = self._array[min_index], self._array[index]
            self._heapify_up_bottom(min_index)
        

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k: int = k
        self._heap: int = Heap(nums)
        
            
    def add(self, val: int) -> int:
        self._heap.add(val)
        while self._heap.getLength() > self._k:
            self._heap.removeMin()
        
        return self._heap.getMin()
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)