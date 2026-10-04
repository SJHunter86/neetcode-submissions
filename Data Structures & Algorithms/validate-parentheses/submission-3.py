class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for bracket in s:
            if bracket in "{[(":
                stack.append(bracket)
            else:
                top = stack.pop() if stack else "#"
                if brackets[bracket] != top:
                    return False
        
        return not stack

"""
- if you see an opener, push to a stack
- if you see a closer, pop from stack and compare it
- if you pop from an empty stack, return False
- if its a match, move on, otherwise return False
- if you finish with leftovers, its false
- if its an empty stack, its true
"""