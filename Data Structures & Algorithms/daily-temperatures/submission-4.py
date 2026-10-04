class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temp:
                    prev_temp, prev_idx = stack.pop()
                    result[prev_idx] = i - prev_idx
            stack.append((temp, i))

        return result
                    

"""
- index of the temperature is the temp that day
- need result = []
- result[i] is "number of days after the ith day before a warmer temperature appears on a future day"
    - reword that
- if no day in the future has a warmer temperature for the ith day, then its 0


[30,38,30,36,35,40,28] - input
[1, 4, 1, 2, 1, 0, 0] - result
- 0 - there was 1 day until it was warmer than 30
- 1 - there was 4 days after 38 until it was warmer
- 2 - 1 day after 30 before it was warmer

- need a look-back, so the index needs to be stored with the temperature?
- if its warmer, append temp with its index, update a count with every pop
- need to graph how that works

[1,4,1,2,1,0,0]
stack
[(38, 1)]

(30, 0) - append - no prior stack
(38, 1) - warmer
    - pop[1] = 0 <-- result index
    - curr = 1 <-- current index
    - 1 - 0 = 1 <-- width between them
    - result[0] = 1
    - append
(30, 2) - not warmer, append
(36, 3) - warmer
    - pop[1] = 2
    - curr = 3
    - 3 - 2 = 1
    - result[2] = 1
    - append
(35, 4) - not warmer, append
(40, 5) - warmer
    - pop[1] = 4
    - curr = 5
    - 5 - 4 = 1
    - result[4] = 1
    - pop[1] = 3
    - curr = 5
    - 5 - 3 = 2
    - result[3] = 2
    - pop[1] = 1
    - curr = 5
    - 5 - 1 = 4
    - result[1] = 4
(28, 6) - not warmer, append
"""