class Node:
    def __init__(self, key: int, val: int, prev = None, next = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # used to keep track of nodes, must be updated
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        recent = self.cache[key]
        self.remove_node(recent)
        self.add_to_head(recent)
        return recent.val
        
    def remove_node(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node

        self.add_to_head(node)

        if len(self.cache) > self.capacity:
            node_to_remove = self.tail.prev
            self.remove_node(node_to_remove)
            del self.cache[node_to_remove.key]
            
        
