# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split lists
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow is now the middle
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        list1, list2 = head, prev
        while list2:
            list1_next = list1.next
            list2_next = list2.next

            list1.next = list2
            list2.next = list1_next

            list1 = list1_next
            list2 = list2_next





"""
- given list is 0-indexed sorted
- find middle index? split the list
- reverse the second half (n-1, n-2, n-3)
- zip the lists?

2 4 6
8 10
2 8 4 10 6
"""