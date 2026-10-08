"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key=lambda interval: interval.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        max_rooms = 1

        for i in range(1, len(intervals)):
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            max_rooms = max(max_rooms, len(heap))
        
        return max_rooms
            