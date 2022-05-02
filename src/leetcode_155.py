
# 155. Min Stack

from typing import List

class MinStack:

    def __init__(self):
        self.stack: List[int] = list()
        
        
    def push(self, val: int) -> None:
        element = {"val": val, "min": val}
        
        if self.stack:
            element["min"] = min(self.stack[-1]["min"], element["min"])     
            
        self.stack.append(element)
    
            
    def pop(self) -> None:
        self.stack.pop()
                 
                
    def top(self) -> int:
        return self.stack[-1]["val"]
        

    def getMin(self) -> int:
        return self.stack[-1]["min"]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()