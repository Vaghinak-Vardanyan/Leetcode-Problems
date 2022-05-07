
# 669. Trim a Binary Search Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if high < root.val:
            return self.trimBST(root.left, low, high)
        
        if low > root.val:
            return self.trimBST(root.right, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root


class IterativeSolution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        while root and (high < root.val or low > root.val):
            if high < root.val:
                root = root.left
            else:
                root = root.right
                
        if not root:
            return None
        
        current: Optional[TreeNode] = root
        while current.left:
            if low <= current.left.val:
                current = current.left
            else:
                current.left = current.left.right
                
        current = root
        while current.right:
            if current.right.val <= high:
                current = current.right
            else:
                current.right = current.right.left
                
        return root