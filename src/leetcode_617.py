
# 617. Merge Two Binary Trees

from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        root1.val = root1.val + root2.val
        
        return root1


class IterativeSolution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        stack: List[Tuple(Optional[TreeNode], Optional[TreeNode])] = [(root1, root2)]
            
        while stack:
            current = stack.pop()
            
            if not current[1]:
                continue
            
            if not current[0].left:
                current[0].left = current[1].left
            else:
                stack.append((current[0].left, current[1].left))
                
            if not current[0].right:
                current[0].right = current[1].right
            else:
                stack.append((current[0].right, current[1].right))
            
            current[0].val += current[1].val
        
        return root1
                