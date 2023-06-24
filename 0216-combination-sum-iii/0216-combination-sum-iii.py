class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(nums,subset,res):
            if len(subset)==k and sum(subset)==n:
                res.append(subset)
                return

            for i in range(len(nums)):

                backtrack(nums[i+1:],subset+[nums[i]],res)
                
        nums = [i+1 for i in range(9)]
        result = []
        backtrack(nums,[],result)
        return result