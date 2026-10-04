class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                second = stack.pop() if stack else 0
                first = stack.pop() if stack else 0
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
        
        return stack[0]