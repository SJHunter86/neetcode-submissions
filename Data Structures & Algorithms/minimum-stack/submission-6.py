class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = self.stack[-1][1] if self.stack else val
        self.stack.append((val, min(curr_min, val))) # O(1)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop() # O(1)

    def top(self) -> int:
        return self.stack[-1][0] # O(1)

    def getMin(self) -> int:
        return self.stack[-1][1]
