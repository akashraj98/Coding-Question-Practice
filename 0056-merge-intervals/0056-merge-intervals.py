class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i= 1         # we start from 1 since we are merging wiht prev intervals
        print(intervals)
        while i< len(intervals):
            if intervals[i][0]<= intervals[i-1][1]:
                i_c,j_c = intervals[i]
                i_p,j_p  = intervals[i-1]
                intervals[i] = [min(i_c,i_p),max(j_c,j_p)]
                # intervals[i] =[min(intervals[i][0],intervals[i-1][0]),max(intervals[i-1][1],intervals[i][1])]
                intervals.pop(i-1)
            else:
                i+=1
        return intervals
        