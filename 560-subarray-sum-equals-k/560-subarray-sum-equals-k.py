class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        res = 0
        prefixSum = {0:1}
        
        for n in nums:
            currSum+=n
            diff =  currSum - k
            res+= prefixSum.get(diff,0)
            prefixSum[currSum] = 1+ prefixSum.get(currSum,0)
            
        return res
    
#         count = 0
#         for i in range(len(nums)):
#             sum_n = 0
#             for j in range(i,len(nums)):
#                 sum_n+=nums[j]
#                 if sum_n == k:
#                     count+=1
#         return count
        