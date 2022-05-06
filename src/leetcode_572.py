
# 572. Subtree of Another Tree

from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if self.isIdentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isIdentical(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
    
        if not first and not second:
            return True
    
        if not first or not second:
            return False
    
        return first.val == second.val \
           and self.isIdentical(first.left, second.left) \
           and self.isIdentical(first.right, second.right)


class IterativeSolution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack: List[TreeNode] = [root]
            
        while stack:
            current = stack.pop()
            
            if current.val == subRoot.val:
                if self.isIdentical(current, subRoot):
                    return True
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        return False
        
    
    def isIdentical(self, first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        
        stack: List[Tuple(Optional[TreeNode], Optional[TreeNode])] = [(first, second)]
        
        while stack:
            current_first, current_second = stack.pop()
            
            if not current_first and not current_second:
                continue
            
            if not current_first or not current_second or current_first.val != current_second.val:
                return False
            
            stack.append((current_first.left, current_second.left))
            stack.append((current_first.right, current_second.right))
            
        return True
