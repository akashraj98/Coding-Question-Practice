class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates,[],result,target)
        return result
    
    def dfs(self,nums,subset,result,target):
        if target == 0:
            result.append(subset)
        if target < 0:
            return
        for i in range(len(nums)):
            if nums[i]> target:
                break
            self.dfs(nums[i:],subset+[nums[i]],result,target-nums[i])