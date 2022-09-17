
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(k):
            heappush(nums,heappop(nums)+1)
        res =1
        return reduce(lambda acc,n : acc*n%(10**9+7),nums)
        
            
        