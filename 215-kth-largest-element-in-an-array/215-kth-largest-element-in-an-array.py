import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsi = []
        for i in nums:
            if len(numsi) <k:
                heapq.heappush(numsi,i)
            else:
                if numsi[0] < i:
                    heapq.heappush(numsi,i)
                    heapq.heappop(numsi)

        return(numsi[0])