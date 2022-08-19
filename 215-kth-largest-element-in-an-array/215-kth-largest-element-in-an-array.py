import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsi = [-i for i in nums]
        heapq.heapify(numsi)
        for i in range(k-1):
            heapq.heappop(numsi)
        return -heapq.heappop(numsi)
        
            
        