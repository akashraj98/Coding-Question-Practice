class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows ==2:
            return res
        for _ in range(numRows-2):
            last = res[-1]
            new_Array = []
            for i in range(len(last)-1):
                new_Array.append(last[i]+last[i+1])
            new_Array = [1]+new_Array+[1]
            res.append(new_Array)
        return res
            
            
        