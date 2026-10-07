# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def build_integer(node: Optional[ListNode]) -> int:
            mult = 1
            result = 0
            while node:
                result += node.val * mult
                mult *= 10
                node = node.next
            return result
        
        def build_linked_list(x: int) -> Optional[ListNode]:
            if x == 0:
                return ListNode(0)
            sentinel = ListNode(-1, None)
            curr = sentinel
            while x > 0:
                new_node = ListNode(x%10, None)
                x = x // 10
                curr.next = new_node
                curr = curr.next
            
            return sentinel.next

        total = build_integer(l1) + build_integer(l2)
        return build_linked_list(total)