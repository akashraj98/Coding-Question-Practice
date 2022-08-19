import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        hp = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(hp,-matrix[i][j])
                if len(hp)>k:
                    heapq.heappop(hp)
        return -hp[0]
                
        