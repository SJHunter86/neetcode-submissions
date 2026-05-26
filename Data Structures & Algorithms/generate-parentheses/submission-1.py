class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking
        stack = []
        result = []

        def backtrack(open_n, close_n):
            # base case
            if open_n == n == close_n:
                result.append(''.join(stack))
                return
            # add opening condition
            if open_n < n:
                stack.append('(')
                backtrack(open_n+1, close_n)
                stack.pop()
            # add closing condition
            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n+1)
                stack.pop()
        
        backtrack(0, 0)
        return result