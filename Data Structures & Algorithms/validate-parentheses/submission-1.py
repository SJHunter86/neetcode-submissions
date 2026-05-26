class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}": "{", "]": "[", ")":"("}
        stack = []
        # if its an opening bracket, append it to the stack
        # otherwise, pop stack or #, if top != brackets[bracket] return False
        # return not stack to assert it is empty
        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                top = stack.pop() if stack else "#"
                if brackets[bracket] != top:
                    return False
        return not stack