
# 24. Swap Nodes in Pairs

from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current: Optional[ListNode] = ListNode(0, head)
        temp: Optional[ListNode]

        head = head.next 
        while current.next and current.next.next:
            temp = current.next.next
            current.next.next = temp.next
            temp.next = current.next
            current.next = temp
            current = temp.next

        return head


head: Optional[ListNode] = Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
while head:
    print(head.val)
    head = head.next

