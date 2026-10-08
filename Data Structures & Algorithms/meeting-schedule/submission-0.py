"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda interval: interval.start)
        for i, interval in enumerate(intervals):
            if i == 0:
                continue
            if interval.start < intervals[i-1].end:
                return False
        
        return True