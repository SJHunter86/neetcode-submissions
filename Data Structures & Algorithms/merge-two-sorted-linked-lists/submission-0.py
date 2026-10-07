# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        
        result = ListNode()
        curr = result

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        
        remaining = list1 if list1 else list2
        curr.next = remaining

        return result.next
"""
head 5 6 7
head
head 1 2 3 4 -> list 1 | 1 2 3 4 5 6 7

- while both lists .next is not None
- compare current node values
    - if same or tie, append from list 1
    - else list 2
- after the while loop, 1 list remains
    - determine which list still has nodes
    - just point to it, its already sorted

"""