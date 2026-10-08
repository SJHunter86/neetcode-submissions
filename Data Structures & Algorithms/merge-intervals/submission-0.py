class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= result[-1][1]: # overlap
                prev = result.pop()
                new_interval = [
                    min(prev[0], curr[0]),
                    max(prev[1], curr[1])
                ]
                result.append(new_interval)
            else:
                result.append(curr)
        
        return result

"""
- iterate through the intervals
- 
"""