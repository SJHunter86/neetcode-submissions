class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append((temp, i))

        return result