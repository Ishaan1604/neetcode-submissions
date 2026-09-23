class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        newInterval = intervals[-1]
        overlap = 0
        for i in range(len(intervals) - 2, -1, -1):
            if intervals[i][1] > newInterval[0]:
                overlap += 1
            else:
                newInterval = intervals[i]
        
            
        return overlap