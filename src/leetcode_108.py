
# 108. Convert Sorted Array to Binary Search Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        
        middle: int = (len(nums) - 1) // 2
        
        return TreeNode(nums[middle], self.sortedArrayToBST(nums[:middle]), self.sortedArrayToBST(nums[middle + 1:]))


