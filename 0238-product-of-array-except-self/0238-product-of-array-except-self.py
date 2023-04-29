class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1]
        prefix = [1,]
        prev = 1
        for i in range(len(nums)-1):
            prefix.append(prefix[i]*nums[i])

        for i in range(len(nums)-1,0,-1):
            suffix.append(prev*nums[i])
            prev = prev*nums[i]
        suffix = suffix[::-1]
        res = []
        for i in range(len(nums)):
            res.append(suffix[i]*prefix[i])
        return res