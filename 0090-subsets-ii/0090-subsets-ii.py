class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(subset,i,res):
            if i>=len(nums):
                res.append(subset)
                return
            
            dfs(subset+[nums[i]],i+1,res)
            while i+1<len(nums) and nums[i]== nums[i+1]:
                i = i+1
            dfs(subset,i+1,res)
        dfs([],0,res)
        return res
            