class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                top = stack.pop() if stack else "#"
                if brackets[bracket] != top:
                    return False
        
        return len(stack) == 0


