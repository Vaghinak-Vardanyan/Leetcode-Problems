
# 1209. Remove All Adjacent Duplicates in String II

from typing import List, Tuple

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack: List[Tuple[int, int]] = []
            
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                stack.append((char, stack[-1][1] + 1))
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
                    
        return "".join([char for char, count in stack])
        