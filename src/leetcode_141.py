
# 141. Linked List Cycle

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False
        
        first: Optional[ListNode] = head
        second: Optional[ListNode] = head
        
        while True:
            if not second or not second.next or not second.next.next:
                return False
            
            first = first.next
            second = second.next.next
            
            if first == second:
                return True