class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        last_end = intervals[0][1]
        removed = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < last_end:
                removed += 1
            else:
                last_end = curr[1]

        return removed