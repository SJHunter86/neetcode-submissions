# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head

        while curr:
            nxt = curr.next # is now 1
            curr.next = prev
            prev = curr
            curr = nxt

        
        return prev


"""
             C
null <- 0    1 -> 2 -> 3 -> null
 P                N
"""