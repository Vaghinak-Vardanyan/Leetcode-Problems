
# 239. Sliding Window Maximum

from typing import List
from collections import deque

class maxQueue(object):
    def __init__(self):
        self._queue: deque = deque()
        self.added_count: int = 0
        self.remove_count: int = 0    
    
    def maximum(self) -> int:
        return self._queue[0][0]
    
    def push(self, val: int):
        while self._queue and self._queue[-1][0] < val:
            self._queue.pop()
        self._queue.append((val, self.added_count))
        self.added_count += 1
    
    def pop(self):
        if self._queue and self._queue[0][1] == self.remove_count:
            self._queue.popleft()
        self.remove_count += 1
    

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs: List[int] = list() 
        queue: maxQueue = maxQueue()

        for i in range(k):
            queue.push(nums[i])

        maxs.append(queue.maximum())
        for i in range(k, len(nums)):
            queue.pop()
            queue.push(nums[i])
            maxs.append(queue.maximum())

        return maxs