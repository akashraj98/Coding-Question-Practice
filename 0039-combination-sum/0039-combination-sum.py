class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums,subset,target,res):
            if target==0:
                res.append(subset)
                return
            if target <0:
                return
            for i in range(len(nums)):
                if nums[i]>target:
                    continue
                backtrack(nums[i:],subset+[nums[i]],target-nums[i],res)
                
        res = []
        backtrack(candidates,[],target,res)
        return res