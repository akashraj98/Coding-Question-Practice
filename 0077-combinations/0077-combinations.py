class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # find all subset of size 2
        def backtrack(nums,subset,res,k):
            if len(subset)>k:
                return
            if len(subset)==k:
                res.append(subset)
                return
            for i in range(len(nums)):
                backtrack(nums[i+1:],subset+[nums[i]],res,k)
        res = []
        nums = [i+1 for i in range(n)]
        backtrack(nums,[],res,k)
        return res