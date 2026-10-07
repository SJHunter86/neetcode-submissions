# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = head
        node_to_remove = head
        sentinel.next = head

        for _ in range(n):
            curr = curr.next

        prev = sentinel
        while curr:
            curr = curr.next
            prev = prev.next
            node_to_remove = node_to_remove.next
        
        prev.next = node_to_remove.next
        node_to_remove.next = None

        return sentinel.next

"""
- move the first pointer forward n times
- start second pointer, move them together
- node removal
- return sentinel.next
"""