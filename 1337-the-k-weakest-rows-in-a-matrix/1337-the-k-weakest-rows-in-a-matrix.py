import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        i=0
        res = []
        f_res = []
        for row in mat:
            ones=sum(row)
            res.append((ones,i))  
            i+=1
        res.sort()
        for i in range(k):
            f_res.append(res[i][1])
        return f_res
        