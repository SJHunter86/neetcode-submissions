class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, idx = stack.pop()
                result[idx] = i - idx
            stack.append((temp, i))
        return result


# STACK
# [(38, 1)]

# RESULT
# [1, 4, 1, 2, 1, 0, 0]