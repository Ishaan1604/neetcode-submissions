"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x.start)
        rooms = [intervals[0].end]
        max_rooms = 1
        
        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i].start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
            max_rooms = max(max_rooms, len(rooms))

        return max_rooms
