
# 589. N-ary Tree Preorder Traversal

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result: List[int] = []
        stack: List['Node'] = [root]
        
        if not root:
            return result
        
        while True:
            
            if not stack:
                return result
            
            current = stack.pop()
            result.append(current.val)
            
            for child in reversed(current.children):
                if child:
                    stack.append(child)
                