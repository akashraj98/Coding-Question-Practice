class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res =0
        # prevend = intervals[0][1]
        # for start,end in intervals[1:]:
        #     if start >= prevend:
        #         prevend = end
        #     else:
        #         res+=1
        #         prevend = min(prevend,end)
        # return res
        i= 1
        while i< len(intervals):
            if intervals[i][0]< intervals[i-1][1]:
                # We need to merege here
                if intervals[i-1][1]< intervals[i][1]: # 
                # we pop the one whos endpt is greater
                # so that we ensure that this does not overlaps with anpther
                    intervals.pop(i)
                else:
                    intervals.pop(i-1)
                res+=1
            else:
                # just move ahead
                i+=1
        return res
