class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1:
            return 0

        intervals.sort(key = lambda x : x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]

        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                start = intervals[i][0]
                end = intervals[i][1]
            elif intervals[i][1] <= end:
                start = intervals[i][0]
                end = intervals[i][1]
                ans += 1
            elif intervals[i][0] < end:
                ans += 1
        
        return ans


