class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        newInterval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                newInterval = intervals[i]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res
