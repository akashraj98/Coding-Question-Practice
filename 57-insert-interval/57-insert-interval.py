class Solution:
    def insert(self, n_intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = []
        flag = 1
        for interval in n_intervals:
            if newInterval[0]< interval[0] and flag:
                intervals.append(newInterval)
                flag = 0
            intervals.append(interval)
        if not n_intervals or flag ==1:
            intervals.append(newInterval)
        i= 1
        print(intervals)
        while i< len(intervals):
            if intervals[i][0]<= intervals[i-1][1]:
                # merge 
                a =min(intervals[i][0],intervals[i-1][0])
                b = max(intervals[i-1][1],intervals[i][1])
                intervals[i] = [a,b]
                intervals.pop(i-1)
            else:
                i+=1
        return intervals
