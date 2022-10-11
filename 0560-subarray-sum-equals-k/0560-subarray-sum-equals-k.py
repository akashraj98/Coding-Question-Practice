class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         start = 0
#         end = 1
#         n = len(nums)
#         sm = nums[start]
#         while start< n:
#             while end< n and sm < k:
#                 sm+=nums[end]
#                 end+=1
#                 if sm == k:
#                     count+=1
                
#             sm-=nums[start]
#             start+=1

#         return count
                
        
                    
                
        res = 0
        prefixsum = 0
        d = {0:1}
        for num in nums:
            prefixsum +=num
            # diff = prefix-k
            if prefixsum-k in d:
                res += d[prefixsum-k]
            if prefixsum not in d:
                d[prefixsum] = 1
            else:
                d[prefixsum] = 1+ d[prefixsum]
        return res