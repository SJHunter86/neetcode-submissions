"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}

        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            node_map[curr] = new_node
            curr = curr.next
        
        # Now have a map
        curr = head
        while curr:
            copy = node_map[curr]
            copy.next = node_map.get(curr.next)
            copy.random = node_map.get(curr.random)
            curr = curr.next
        
        return node_map.get(head)