class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,subset,res):
            res.append(subset)
            for i in range(len(nums)):
                # this is impoetant 
                # we need to check duplicate with comparing with earlier 
                # or else it will mail
                if i>0 and nums[i]==nums[i-1]:
                    continue
                
                backtrack(nums[i+1:],subset+[nums[i]],res)
        res = []
        nums.sort()
        backtrack(nums,[],res)
        return res
        