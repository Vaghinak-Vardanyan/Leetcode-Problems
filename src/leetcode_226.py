
# 226. Invert Binary Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


class IterativeSolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        stack: List[int] = [root]
            
        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left
            
            if current.left:
                stack.append(current.left)
            
            if current.right:
                stack.append(current.right)
                
        return root
           