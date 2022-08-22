import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        i=0
        minheap = []
        f_res = []
        for row in mat:
            ones=sum(row)
            heapq.heappush(minheap,(ones,i) )
            # res.append((ones,i))  
            i+=1
        # print(minheap)
        for i in range(k):
            one,index=heapq.heappop(minheap)
            f_res.append(index)
        return f_res
        