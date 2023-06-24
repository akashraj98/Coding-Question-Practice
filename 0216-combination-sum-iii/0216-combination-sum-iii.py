class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(nums,subset,res,target):
            if len(subset)==k and target==0:
                res.append(subset)
                return

            for i in range(len(nums)):
                if nums[i]>target:
                    break
                backtrack(nums[i+1:],subset+[nums[i]],res,target-nums[i])
                
        nums = [i+1 for i in range(9)]
        result = []
        backtrack(nums,[],result,n)
        return result