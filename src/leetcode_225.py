
# 225. Implement Stack using Queues

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()
        self.size = 0
    
    
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(self.size):
            self.queue.append(self.queue.popleft())
            
        self.size += 1

        
    def pop(self) -> int:
        assert not self.empty()
        self.size -= 1
        
        return self.queue.popleft()
 

    def top(self) -> int:
        assert not self.empty()
        return self.queue[0]

        
    def empty(self) -> bool:
        return self.size == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()